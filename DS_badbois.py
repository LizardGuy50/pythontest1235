import random, pygame

def run_enemy_ai(framecount,AI_mode,AI_pos,mapdata,night,leftdoor,rightdoor,cfr_low,cfr_high,fleerooms,ability_lurk_here,rage):
    approach_sound = pygame.mixer.Sound('audio_data/walking_towards.wav')
    flee_left_sound = pygame.mixer.Sound('audio_data/flee.wav')
    flee_right_sound = pygame.mixer.Sound('audio_data/flee.wav')
    gameover = False
    #put if statment here
    for i in range (int(len(AI_mode)/3)):
        #print("UwU")
        if (AI_pos[i*3+2] < 3 and ability_lurk_here[i]) or framecount < 100: #stuns the enemies for the first 100 frames (1.4 - 4 seconds depending on hardware)
            can_move = False
        else:
            can_move = True
        if framecount%AI_mode[i*3+2] == 0 and night >= random.randint(0,7) and can_move: #the later sections allow the AI to move more frequently and consistently
            #print("OwO")
            #print("Nyaaa")
            startpoint = AI_pos[i*3+2]
            #move
            if startpoint == 0:
                print("navigation fuckup")
                break
            exit1 = mapdata[startpoint*5+1]
            exit2 = mapdata[startpoint*5+2]
            exit3 = mapdata[startpoint*5+3]
            exit4 = mapdata[startpoint*5+4]
            navigableareas = []
            if exit1 != 999 and exit1 != 777:
                navigableareas.append(mapdata[startpoint*5+1])
            if exit2 != 999 and exit2 != 777:
                navigableareas.append(mapdata[startpoint*5+2])
            if exit3 != 999 and exit3 != 777:
                navigableareas.append(mapdata[startpoint*5+3])
            if exit4 != 999 and exit4 != 777:
                navigableareas.append(mapdata[startpoint*5+4])
            if AI_mode[i*3+1] == 0:   #charge mode
                navigableareas.sort()
                use_entry = 0
            else:                   #wander mode
                use_entry = random.randint(0,int(len(navigableareas)-1))
            if navigableareas[use_entry] < 3:
                #play sound here or something
                #pygame.mixer.music.load('audio_data/walking_towards.wav')
                #pygame.mixer.music.play(1)
                pygame.mixer.Sound.play(approach_sound)
                #print("sound not included :)")
            if navigableareas[use_entry] == 0:
                #print("Haiiiii ^-^")
                #check if doors are closed
                if navigableareas[use_entry] == exit4: #attacking left door
                    if leftdoor: #attack fails
                        navigableareas[use_entry] = AI_pos[i*3+1] #reset to start point
                        AI_pos[i*3+1] = flee_location(AI_pos,i,fleerooms)
                        print("attack failed!")
                        #pygame.mixer.music.load('audio_data/walking_away_left.wav')
                        #pygame.mixer.music.play(1)
                        pygame.mixer.Sound.play(flee_left_sound)
                        rage[i]-= 200
                    else:
                        gameover = True
                        print("gameover")
                if navigableareas[use_entry] == exit2: #attacking right door
                    if rightdoor: #attack fails
                        navigableareas[use_entry] = AI_pos[i*3+1]
                        AI_pos[i*3+1] = flee_location(AI_pos,i,fleerooms)
                        print("attack failed!")
                        #pygame.mixer.music.load('audio_data/walking_away_right.wav')
                        #pygame.mixer.music.play(1)
                        pygame.mixer.Sound.play(flee_right_sound)
                        rage[i]-= 200
                    else:
                        gameover = True
                        print("gameover")
            AI_pos[i*3+2] = navigableareas[use_entry]
        else:
            #dont move
            pass
    return AI_pos,gameover,rage

def decide(fleerooms,AI_mode,rage,cfr_low,cfr_high,activate_ability):
    #changes AI_mode[n*3+1] to one of the valid options
    #0:charge,1:wander
    #if rage < 0: set rage to 100 + flee (might change later)
    #if 0 < rage < cfr_low: switch to wander mode
    #if cfr_low < rage < cfr_high : toggle mode on func call
    #if cfr_high < rage < 1000: switch to charge mode
    #if rage > 1000: activate ability + set rage to cfr_low
    for i in range (int(len(rage)-1)):
        #loop through all the enemies and update them
        if rage[i] < 0:
            rage[i] = 100
        if rage[i] > 0 and rage[i] < cfr_low:
            #set the mode to wander
            AI_mode[i*3+1] = 1
        if rage[i] > cfr_low and rage[i] < cfr_high:
            #toggle the mode
            if AI_mode[i*3+1] == 1:
                AI_mode[i*3+1] = 0
            else:
                AI_mode[i*3+1] = 1
        if rage[i] > cfr_high:
            #set the mode to charge
            AI_mode[i*3+1] = 0
        if rage[i] > 1000:
            #activate the ability
            rage[i] = cfr_low
            activate_ability[i] = True
    return AI_mode, rage, activate_ability

def force_rage_up(rage, quarthour):
    #increaces the rage of all AI enemies
    for i in range (int(len(rage))):
        rage[i] += quarthour*50 #need to balance
    return rage

def abilities(ability_ID,enemy_ID,activate_ability,ability_camera_invis,ability_rapid_move,ability_lurk_here,ability_flee_now,ability_random_tp):
    #the abilities are things like: be invis to cameras, rapid move, wait in the room ajacent to player room, instaflee, random tp e.t.c.
    #add this once the current version of the game is winnable (these abilities will make the AI harder)
    #still a work in progress, this will not work in its current form
    id_assemble = []
    if ability_ID == 1 and activate_ability[enemy_ID]:
        ability_camera_invis[enemy_ID] = True
        #if true, dont render in camera view unless in room ID of 1 or 2 until next two quarthour count
    if ability_ID == 2 and activate_ability[enemy_ID]:
        ability_rapid_move[enemy_ID] = True
        #if true, half the required countdown until the next quarthour count
    if ability_ID == 3 and activate_ability[enemy_ID]:
        ability_lurk_here[enemy_ID] = True
        #if true, when in room ID of 1 or 2, wait until the next quarthour count
    if ability_ID == 4 and activate_ability[enemy_ID]:
        ability_flee_now[enemy_ID] = True
        #if true, flee
    if ability_ID == 5 and activate_ability[enemy_ID]:
        ability_random_tp[enemy_ID] = True
        #if true, go to any room with an ID greater than 5 (avoids the AI winning via BS)
    activate_ability[enemy_ID] = False
    #pick a new ability
    ability_ID = random.randint(1,5)
    return ability_camera_invis, ability_rapid_move, ability_lurk_here, ability_flee_now, ability_random_tp, ability_ID

def flee_location(AI_pos,i,fleerooms):
    AI_pos[i*3+1] = fleerooms[random.randint(0,int(len(fleerooms)-1))]
    return AI_pos[i*3+1]

def flee_now(AI_pos,AI_ID,fleerooms):
    AI_pos[AI_ID*3+1] = flee_location(AI_pos,AI_ID,fleerooms)

def random_tp():
    #tp specified enemy to a random room
    pass

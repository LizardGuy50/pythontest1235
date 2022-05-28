#modules
import pygame, time, random                             #libaries
import DS_mapgen, DS_load, DS_badbois, DS_cinematic     #classes
#welcome to the haunted spacearia :)
pygame.init()

valid_flee_locations = []

#readsavefile for relevent data
display_width = 1250
display_height = 900

night_reached,seen_opening_cutscene,ngplus,display_width,display_height = DS_load.load_save("savedata.txt") 

#colour shortcuts
black = (0,0,0)
grey = (150,150,150)
white = (255,255,255)
red = (150,0,0)
green = (0,150,0)
blue = (0,0,150)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)

#functions
#screen text
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text, largeText, black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    return

def mainmenu_misctext(text,colour,centre_h,centre_v):
    menu_text = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, menu_text, colour)
    TextRect.center = ((centre_h),(centre_v))
    gameDisplay.blit(TextSurf, TextRect)
    return

#screens
def mainmenu(display_width,display_height,night_reached,ngplus):
    mm_frame_count = 0
    button_ID = 0
    button_ID_last = 0
    intro = True
    use_background = random.randint(0,3)
    glitchy_frames = 0
    glitch_sound = pygame.mixer.Sound('audio_data/MMG.wav')
    boop = pygame.mixer.Sound('audio_data/boop.wav')
    total_swapped = 0
    while intro:
        hover = 0
        button_ID_last = button_ID
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        #background graphics
        glitch_background = random.randint(1,100)
        if glitch_background > 98:
            glitchy_frames = random.randint(3,9)
        if glitchy_frames > 0:
            use_background = random.randint(0,3)
            glitchy_frames -= 1
            pygame.mixer.Sound.play(glitch_sound)
            vertical_randomness = random.randint(-100,100)
            gameDisplay.blit((main_menu_background[use_background]),(random.randint(-100,100),vertical_randomness))
        else:
            vertical_randomness = random.randint(-5,5)
            gameDisplay.blit((main_menu_background[use_background]),(random.randint(-5,5),vertical_randomness))

        mm_frame_count += 1        
        largeText = pygame.font.Font('freesansbold.ttf',115)
        menu_text = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("Darkspace Survival", largeText, red)
        TextRect.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #menu text
        mainmenu_misctext("New Game",green,350,275)
        mainmenu_misctext("Continue",green,340,375)
        mainmenu_misctext("Quit",red,310,675)
        if ngplus:
            mainmenu_misctext("Nightmare",green,350,475)
            mainmenu_misctext("Custom Level",green,375,575)
        else:
            mainmenu_misctext("Locked",grey,325,475)
            mainmenu_misctext("Locked",grey,325,575)
       
        #new game
        if 150+300 > mouse[0] > 150 and 250+50 > mouse[1] > 250:
            pygame.draw.rect(gameDisplay, bright_green,(150,250,100,50))
            mainmenu_misctext("New Game",bright_green,350,275)
            button_ID = 1
            hover += 1
            if click[0] == 1:
                intro = False
                return 1, False
        else:
            pygame.draw.rect(gameDisplay, green,(150,250,100,50))
            hover -= 1

        #continue
        if 150+300 > mouse[0] > 150 and 350+50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, bright_green,(150,350,100,50))
            mainmenu_misctext("Continue",bright_green,340,375)
            button_ID = 2
            hover += 1
            if click[0] == 1:
                intro = False
                return night_reached, False
        else:
            pygame.draw.rect(gameDisplay, green,(150,350,100,50))
            hover -= 1

        #special game modes
        if ngplus:
            #nightmare (will use night value of 6+)
            if (150+300 > mouse[0] > 150 and 450+50 > mouse[1] > 450) and ngplus == 1:
                pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
                mainmenu_misctext("Nightmare",bright_green,350,475)
                button_ID = 3
                hover += 1
                if click[0] == 1:
                    intro = False
                    return 6, False
            else:
                pygame.draw.rect(gameDisplay, green,(150,450,100,50))
                hover -= 1

            #custom level load (use file: customlevel.txt)
            if (150+300 > mouse[0] > 150 and 550+50 > mouse[1] > 550) and ngplus == 1:
                pygame.draw.rect(gameDisplay, bright_green,(150,550,100,50))
                mainmenu_misctext("Custom Level",bright_green,375,575)
                button_ID = 4
                hover += 1
                if click[0] == 1:
                    intro = False
                    return 0, False
            else:
                pygame.draw.rect(gameDisplay, green,(150,550,100,50))
                hover -= 1
        else:
            pygame.draw.rect(gameDisplay, grey,(150,450,100,50))
            pygame.draw.rect(gameDisplay, grey,(150,550,100,50))


        #quit
        if 150+300 > mouse[0] > 150 and 650+50 > mouse[1] > 650:
            pygame.draw.rect(gameDisplay, bright_red,(150,650,100,50))
            mainmenu_misctext("Quit",bright_red,310,675)
            button_ID = 5
            hover += 1
            if click[0] == 1:
                intro = False
                mainmenu_active = False
                savefile = open("savedata.txt", "w")
                savedatawrite=(str(display_width)+","+str(display_height)+","+str(night_reached)+","+str(ngplus))
                savefile.write(savedatawrite)
                savefile.close()
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red,(150,650,100,50))
            hover -= 1

        #wipe data
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    print("save data wiped")
                    savefile = open("savedata.txt", "w")
                    savefile.write("1250,900,1,0")
                    savefile.close()
                    night_reached = 1
                    ngplus = 0
        
        smallText = pygame.font.Font("freesansbold.ttf",20)
        if ngplus == 1:
            mainmenu_misctext("Bonus Content Unlocked",red,1000,160)
        textSurf, textRect = text_objects("Hold DEL to clear save", smallText, white)
        textRect.center = (1000,800)
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)
        #hover = 3: not hovering,5: hovering
        if hover == 3: #this doesnt work properly for some reason
            button_ID = 0
        if button_ID_last != button_ID:
            pygame.mixer.Sound.play(boop)
    return

def super_generator_control(map_size,roomnumber,lookedat):
    # run all of the map gen code and return the map
    generate = True
    while generate:
        try:
            while generate:
                mapdata = [0,999,1,999,2,1,777,999,777,0,2,777,0,777,999] #should always have 2 t junctions next to the player
                testlist = []
                for i in range (roomnumber):
                    tmp = i+1
                    for j in range (int(len(mapdata)/5)):
                        if True:
                            mapgrid,lookedat = DS_mapgen.populate_map_grid(mapgrid,mapdata,map_size,j,lookedat)
                        else:
                            pass
                    mapdata = DS_mapgen.create_room(mapdata,False,False,mapgrid,map_size) #create room function
                    mapgrid,mapdata = DS_mapgen.check_map_grid(mapdata,mapgrid,map_size,i)

                for j in range (int(len(mapdata)/5)):
                    if True:   
                        mapgrid,lookedat = DS_mapgen.populate_map_grid(mapgrid,mapdata,map_size,j,lookedat)
                for i in range (len(mapgrid)):
                    if mapgrid[i] == 888:
                        pass
                    else:
                        testlist.append(mapgrid[i])
                euclidscore = len(testlist)
                if night > 7:
                    score_required = 0.95 - ((night-5)*0.05) #avoids some instability in nightmare mode :)
                else:
                    score_required = 0.96
                if euclidscore > (roomnumber * score_required):
                    generate = False
                    print("Generation complete: " + str(euclidscore) + "/" + str(roomnumber))
                else:
                    mapgrid = DS_mapgen.define_map_grid(map_size)
                    mapdata = [0,999,777,999,777]
                    testlist = []
        except:
            #print("it broke again!")
            mapgrid = DS_mapgen.define_map_grid(map_size)
            mapdata = [0,999,777,999,777]
            testlist = []
        else:
            generate = False
    return mapdata,mapgrid

def levelloader(mapgrid,lookedat):
    #load the custom level (this was awful to work out and write in, might make a tool at some point)
    #an entire A4 page was used
    #will make this read from a .txt file at some point
    mapdata = [0,999,1,999,2,1,3,999,4,0,2,6,0,5,999,3,7,8,1,999,4,1,9,10,999,5,2,999,11,12,6,14,999,2,13,7,15,999,3,999,8,999,21,999,3,9,999,16,999,4,10,4,999,999,999,11,5,999,999,999,12,999,5,999,17,13,999,6,999,22,14,18,999,6,999,15,999,999,7,999,16,19,25,999,9,17,20,12,999,26,18,999,999,14,999,19,21,999,16,999,20,22,999,17,999,21,23,999,19,8,22,24,13,20,999,23,999,999,21,999,24,999,999,22,999,25,999,999,999,16,26,999,17,999,999]
    mapdata,temparray = DS_load.load_map()
    #print(mapdata)
    for j in range (int(len(mapdata)/5)):
        mapgrid,lookedat = DS_mapgen.populate_map_grid(mapgrid,mapdata,map_size,j,lookedat)
    night = 5
    night = int(temparray[0])
    #print(mapgrid)
    return night,mapdata,mapgrid

def time_calculation(gamewin, rage, quarthour):
    if framecount%1000 == 0:
        quarthour += 1
        rage = DS_badbois.force_rage_up(rage,quarthour)

    if quarthour == 20:
        gamewin = True
    return gamewin, rage, quarthour

def time_display(quarthour,power,white):
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(str(20-quarthour) + " Time Remaining", smallText, white)
    textRect.center = (1100,50)#( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    if power > 0:
        textSurf, textRect = text_objects(str(power) + "% System Power", smallText, white)
    else:
        textSurf, textRect = text_objects("SYSTEM FALIURE", smallText, white)
    textRect.center = (1100,75)#( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    return

#code setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Darkspace survival')
clock = pygame.time.Clock()
crashed = False
smallText = pygame.font.Font("freesansbold.ttf",20)
print("game load in progress")
gameDisplay.fill(green)
LSBG = pygame.image.load("image_data/LBG.png")
gameDisplay.blit(LSBG,(0,0))
message_display("LOADING")
textSurf, textRect = text_objects("LOADING: cameras", smallText, white)
textRect.center = (1000,800)
gameDisplay.blit(textSurf, textRect)
pygame.display.update()
#images (image_data/<animation name>/_)
#cameras cant comress much bc of the use of named images
cameras = [pygame.image.load("image_data/cameras/cam_0_door_closed.png")]               #0
cameras.append(pygame.image.load("image_data/cameras/cam_0_door_open.png"))
cameras.append(pygame.image.load("image_data/cameras/corridor_clear_s.png"))
cameras.append(pygame.image.load("image_data/cameras/corridor_enemy_s.png"))
cameras.append(pygame.image.load("image_data/cameras/junction_clear_s.png"))
cameras.append(pygame.image.load("image_data/cameras/junction_enemy_s.png"))        #5
cameras.append(pygame.image.load("image_data/cameras/corner_clear_s.png"))
cameras.append(pygame.image.load("image_data/cameras/corner_clear_s.png"))
cameras.append(pygame.image.load("image_data/cameras/vent_clear_s.png"))
cameras.append(pygame.image.load("image_data/cameras/vent_enemy_s.png"))
cameras.append(pygame.image.load("image_data/cameras/room_clear_s.png"))   #10
cameras.append(pygame.image.load("image_data/cameras/room_enemy_s.png"))

gameDisplay.blit(LSBG,(0,0))
message_display("LOADING")
textSurf, textRect = text_objects("LOADING: main menu graphics", smallText, white)
textRect.center = (1000,800)
gameDisplay.blit(textSurf, textRect)
pygame.display.update()

#mainmenu background
main_menu_background = [pygame.image.load("image_data/main_menu/MM1.png")]
main_menu_background.append(pygame.image.load("image_data/main_menu/MM2.png"))
main_menu_background.append(pygame.image.load("image_data/main_menu/MM3.png"))
main_menu_background.append(pygame.image.load("image_data/main_menu/MM4.png"))

gameDisplay.blit(LSBG,(0,0))
message_display("LOADING")
textSurf, textRect = text_objects("LOADING: jumpscare animation", smallText, white)
textRect.center = (1000,800)
gameDisplay.blit(textSurf, textRect)
pygame.display.update()

jumpscare = DS_load.load_image_seq("image_data/jumpscare",30,".png")

gameDisplay.blit(LSBG,(0,0))
message_display("LOADING")
textSurf, textRect = text_objects("LOADING: game win animation", smallText, white)
textRect.center = (1000,800)
gameDisplay.blit(textSurf, textRect)
pygame.display.update()

phase_win = DS_load.load_image_seq("image_data/phase_complete",100,".png")

gameDisplay.blit(LSBG,(0,0))
message_display("LOADING")
textSurf, textRect = text_objects("LOADING: misc animations", smallText, white)
textRect.center = (1000,800)
gameDisplay.blit(textSurf, textRect)
pygame.display.update()

cam_onoff_leftdoor = DS_load.load_image_seq("image_data/cam_onoff_leftdoor_2",21,".png")
cam_onoff_rightdoor = DS_load.load_image_seq("image_data/cam_onoff_rightdoor_2",21,".png")
cam_onoff_nodoor = DS_load.load_image_seq("image_data/cam_onoff_nodoor_2",21,".png")
cam_onoff_bothdoor = DS_load.load_image_seq("image_data/cam_onoff_bothdoor_2",21,".png")

gameDisplay.blit(LSBG,(0,0))
message_display("LOADING")
textSurf, textRect = text_objects("LOADING: audio", smallText, white)
textRect.center = (1000,800)
gameDisplay.blit(textSurf, textRect)
pygame.display.update()

#sound loading
ability_trig_sound = pygame.mixer.Sound('audio_data/Rolling_Thunder.mp3')
map_nav_sound = pygame.mixer.Sound('audio_data/boop.wav')
map_task_sound = pygame.mixer.Sound('audio_data/high_boop.wav')
alarm_sound = pygame.mixer.Sound('audio_data/alarm base.wav')
power_down_sound = pygame.mixer.Sound('audio_data/no_power.mp3')

#loop
mainmenu_active = True
startnight = False
cameraview = False
gameover = False
camup = False
camdown = False
gamewin = False
leftdoor = False
rightdoor = False
dot_flash = True
sparepower = 10
powerup = False
#######################
framerate_display = False
#######################
custommode = False
#######################
pygame.key.set_repeat(200)
pygame.mixer.set_num_channels(16)
while not crashed:
    frametime = time.time()

    if mainmenu_active:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('audio_data/DSS_mainmenu_music.mp3')
        pygame.mixer.music.play(100)
        night,mainmenu_active = mainmenu(display_width,display_height,night_reached,ngplus)
        startnight = True
        #pygame.mixer.music.stop()

    if startnight:
        custommode = False
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        if night == 0:
            nightname = "Custom level"
            custommode = True
            night = 1
        elif night == 1:
            nightname = "Repair Main Reactor"
            night_reached = night
        elif night == 2:
            nightname = "Reset Life Support"
            night_reached = night
        elif night == 3:
            nightname = "Restart Main Computer"
            night_reached = night
        elif night == 4:
            nightname = "Send Distress Signal"
            night_reached = night
        elif night == 5:
            nightname = "Survive The Monsters"
            night_reached = night
        else:
            nightname = "Nightmare (" + str(night-5) + ")"
            #night = 125
        for i in range(120):
            gameDisplay.fill(white)
            tmpmsg = (nightname)
            message_display(tmpmsg)
            pygame.display.update()
            clock.tick(60)
        startnight = False
        #generate map
        map_size = 21 #size of the layout grid, keep as large as possible to avoid odd behaviour
        mapgrid = DS_mapgen.define_map_grid(map_size)
        generate = True
        lookedat = ""
        testlist = []
        roomnumber = (night*10+5)
        #phase: 1:15 2:25 3:35 4:45 5:55 nightmare: 65
        if custommode:
            night,mapdata,mapgrid = levelloader(mapgrid,lookedat)
        else:
            mapdata,mapgrid = super_generator_control(map_size,roomnumber,lookedat)
        
        #end of generation code
        tmpint = night
        if tmpint > 6:
            tmpint = 4
        framecount = 0 #used to check if an AI should move yet
        leftdoor = False
        rightdoor = False
        cameraview = False
        cam_num = 0 #reset the camera number to the bridge cam
        #initiate AI
        rage = [random.randint(0,1000)] #how confident the AI is
        cfr_low = 500-(night*20)
        cfr_high = 500-(night*5)
        #spawn
        AI_pos = [0,0,0] #reset to 1 if more had been added
        AI_mode = [0,0,0]
        ability_camera_invis = [False]
        ability_rapid_move = [False]
        ability_lurk_here = [False]
        ability_flee_now = [False]
        ability_random_tp = [False]
        activate_ability = [False]
        chosen_ability = [0]
        for i in range (tmpint):
            AI_pos.append(i*3+1)
            AI_pos.append(0)
            AI_pos.append(0)
            AI_mode.append(i*3+1)
            AI_mode.append(0)
            AI_mode.append(0)
            rage.append(random.randint(0,1000))
            ability_camera_invis.append(False) #almost% done
            ability_rapid_move.append(False) #wip (need to balence movement speed before adding)
            ability_lurk_here.append(False) #almost done
            ability_flee_now.append(False) #almost done
            ability_random_tp.append(False) #wip (may not include this one)
            activate_ability.append(False) #toggles the ability activation
            chosen_ability.append(0)
        #set to starting positions
        for i in range (int(len(AI_pos)/3)):
            #i*3+0: ID, i*3+1: start pos, i*3+2: current pos
            fleerooms = DS_mapgen.find_all_flee_rooms(mapdata)
            AI_pos[i*3+1] = fleerooms[random.randint(0,len(fleerooms)-1)] #pick one of the last 5 rooms to generate
            AI_pos[i*3+2] = AI_pos[i*3+1] #set position to startpoint
        #assign speed values (number of frames needed before moving)
        for i in range (int(len(AI_mode)/3)):
            #i*3+0: ID, i*3+1: mode, i*3+2: speed
            
            AI_mode[i*3+2] = random.randint((6-(tmpint/2))*40+10,(6-(tmpint/2))*50+40)
            if AI_mode[i*3+2] < 1:
                AI_mode[i*3+2] = 1
            #phase1: 110 > 150 frames, phase5: 30 > 70 frames, nightmare: 10 > 50 frames
            #phase1: 2.3 > 3 seconds, phase5: 1 > 1.6 seconds, nightmare: 0.6 > 1.3 seconds @15fps (need to update this bit after removing a pile of print commands)
            #the values still need balancing / testing
        #randomly assign AI modes
        for i in range (int(len(AI_mode)/3)):
            AI_mode[i*3+1] = random.randint(0,1) #assign a mode to each AI (make wander mode less common until the mode switch is added)
        print(AI_pos)
        print(AI_mode)
        #print(fleerooms)

        #set render point for camera pointer
        lookpos = 0
        for x in range (map_size):
            for y in range (map_size):
                tmp = mapgrid[x*map_size+y]
                if tmp == 0:
                    lookpos = x*map_size+y
        lookpos += 1
        quarthour = 1
        power = 100
        task = 50
        task_cam = random.randint(0,len(mapdata)/5-1) # any camera that is avaliable
        pygame.mixer.music.stop()
        if night < 6:
            pygame.mixer.music.load('audio_data/AMB_3.wav')
        else:
            pygame.mixer.music.load('audio_data/Wolf Mother - Loopop.mp3')
        pygame.mixer.music.play(100) #play temp ambience
        if sparepower > 20:
            power=90 #you did well, this level is harder (less power)
        if sparepower < 5:
            quarthour=3 #you did poorly, this level will be easier (less time)
        startstop = True
        
    #Enemy AI control start (testing version)
    
    #select mode (will add later)
    AI_mode,rage,activate_ability = DS_badbois.decide(fleerooms,AI_mode,rage,cfr_low,cfr_high,activate_ability)
    #move enemies
    AI_pos,gameover,rage = DS_badbois.run_enemy_ai(framecount,AI_mode,AI_pos,mapdata,night,leftdoor,rightdoor,cfr_low,cfr_high,fleerooms,ability_lurk_here,rage)
    #check if any abilities need to be made active
    for i in range (len(activate_ability)):
        if activate_ability[i]:
            ability_ID = chosen_ability[i]
            ability_camera_invis,ability_rapid_move,ability_lurk_here,ability_flee_now,ability_random_tp,ability_ID = DS_badbois.abilities(ability_ID,i,activate_ability,ability_camera_invis,ability_rapid_move,ability_lurk_here,ability_flee_now,ability_random_tp)
            chosen_ability[i] = ability_ID
            pygame.mixer.Sound.play(ability_trig_sound)#tells the player that an ability has been activated
    #Enemy AI control end

    #camera background stuff
    if not cameraview:
        #show command bridge
        gameDisplay.fill(red)
        if leftdoor and not rightdoor:
            gameDisplay.blit((cam_onoff_leftdoor[20]),(0,0))
            #pygame.display.update()
        if rightdoor and not leftdoor:
            gameDisplay.blit((cam_onoff_rightdoor[20]),(0,0))
            #pygame.display.update()
        if leftdoor and rightdoor:
            gameDisplay.blit((cam_onoff_bothdoor[20]),(0,0))
            #pygame.display.update()
        if not leftdoor and not rightdoor:
            gameDisplay.blit((cam_onoff_nodoor[20]),(0,0))
            #pygame.display.update()

    if camup:
        camup = False
        cameraview = False
        #play animation
        if leftdoor and not rightdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_leftdoor,True,framecount,display_width,display_height)
        if rightdoor and not leftdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_rightdoor,True,framecount,display_width,display_height)
        if leftdoor and rightdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_bothdoor,True,framecount,display_width,display_height)
        if not leftdoor and not rightdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_nodoor,True,framecount,display_width,display_height)

    if camdown:
        camdown = False
        cameraview = True
        #play animation
        if leftdoor and not rightdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_leftdoor,False,framecount,display_width,display_height)
        if rightdoor and not leftdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_rightdoor,False,framecount,display_width,display_height)
        if leftdoor and rightdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_bothdoor,False,framecount,display_width,display_height)
        if not leftdoor and not rightdoor:
            framecount = DS_cinematic.cam_flipper(cam_onoff_nodoor,False,framecount,display_width,display_height)
    #cam stuff end

    #camera nav code (movement validation)
    #print(cam_num)
    if mapdata[cam_num*5+1] != 999 and mapdata[cam_num*5+1] != 777:
        E1 = True
    else:
        E1 = False
    if mapdata[cam_num*5+2] != 999 and mapdata[cam_num*5+2] != 777:
        E2 = True
    else:
        E2 = False
    if mapdata[cam_num*5+3] != 999 and mapdata[cam_num*5+3] != 777:
        E3 = True
    else:
        E3 = False
    if mapdata[cam_num*5+4] != 999 and mapdata[cam_num*5+4] != 777:
        E4 = True
    else:
        E4 = False
    #camera nav controls handled later

    if cameraview:
        #show cameras
        gameDisplay.fill(green)
        if leftdoor and not rightdoor:
            gameDisplay.blit((cam_onoff_leftdoor[0]),(0,0))
        if rightdoor and not leftdoor:
            gameDisplay.blit((cam_onoff_rightdoor[0]),(0,0))
        if leftdoor and rightdoor:
            gameDisplay.blit((cam_onoff_bothdoor[0]),(0,0))
        if not leftdoor and not rightdoor:
            gameDisplay.blit((cam_onoff_nodoor[0]),(0,0))
        pygame.draw.rect(gameDisplay, bright_green,(50,700,600,150))


        #draw map on screen #map is 21*21 in size
        #area starts @ 700px from left & 200px from top
        #area is 500px wide & 650px tall
        drawfrom = [680,200,680] #h,v,h reset
        drawsize = [25,25]
        drawdot = [10,10,5,5] #h,v offset,h,v size
        map_assemble_str = [""]
        count = 0
        for x in range (map_size):
            drawfrom[0] = drawfrom[2]
            for y in range (map_size):
                count +=1
                tmp = mapgrid[x*map_size+y]
                if tmp == 888:
                    strtmp = "--"   #display bright_green
                    pygame.draw.rect(gameDisplay, bright_green,(drawfrom[0],drawfrom[1],drawsize[0],drawsize[1]))
                elif tmp == 777:
                    strtmp = "??"   #display bright_green
                    pygame.draw.rect(gameDisplay, bright_green,(drawfrom[0],drawfrom[1],drawsize[0],drawsize[1]))
                else:
                    strtmp = "0" + str(tmp) #display green
                    pygame.draw.rect(gameDisplay, green,(drawfrom[0],drawfrom[1],drawsize[0],drawsize[1]))

                if tmp == task_cam:
                    pygame.draw.rect(gameDisplay, black,(drawfrom[0],drawfrom[1],drawsize[0],drawsize[1]))
                
                if tmp == 0:
                    pygame.draw.rect(gameDisplay, white,(drawfrom[0],drawfrom[1],drawsize[0],drawsize[1]))

                if count == lookpos:
                    pygame.draw.rect(gameDisplay, black,(drawfrom[0] + drawdot[0]-2,drawfrom[1] + drawdot[1]-2,drawdot[2]+4,drawdot[3]+4))
                    if dot_flash:
                        pygame.draw.rect(gameDisplay, bright_red,(drawfrom[0] + drawdot[0],drawfrom[1] + drawdot[1],drawdot[2],drawdot[3]))
                    else:
                        pygame.draw.rect(gameDisplay, red,(drawfrom[0] + drawdot[0],drawfrom[1] + drawdot[1],drawdot[2],drawdot[3]))
                    draw_h = drawfrom[0]
                    draw_v = drawfrom[1]
                    
                map_assemble_str.append(strtmp)
                drawfrom[0] += drawsize[0]
            map_assemble_str.pop(0)
            drawfrom[1] += drawsize[1]
            map_assemble_str = [""]

        #check position of enemies
        for i in range (int(len(AI_pos)/3)):
            if AI_pos[i*3+2] == cam_num and not ( ability_camera_invis[i] and cam_num > 2): #if the enemy is in the same room as the camera <and not> the ability is active and the enemy is next to the player
                enemy_on_camera = True

        #read camera data
        exit1 = mapdata[cam_num*5+1]
        exit2 = mapdata[cam_num*5+2]
        exit3 = mapdata[cam_num*5+3]
        exit4 = mapdata[cam_num*5+4]
        exittotal = 0
        exitcount = 0
        exitstring = ["","","","","",""]
        pygame.draw.rect(gameDisplay, bright_red,(draw_h,draw_v+20,5,5))
        pygame.draw.rect(gameDisplay, bright_red,(draw_h,draw_v,5,5))
        pygame.draw.rect(gameDisplay, bright_red,(draw_h+20,draw_v+20,5,5))
        pygame.draw.rect(gameDisplay, bright_red,(draw_h+20,draw_v,5,5))
        if exit1 != 999 and exit1 != 777:
            exittotal += 1
            exitcount += 1
            exitstring[0] = "\/: " + str(exit1) + " "
        else:
            exitstring[0] = ""
            pygame.draw.rect(gameDisplay, bright_red,(draw_h,draw_v+20,25,5))
        if exit2 != 999 and exit2 != 777:
            exittotal += 2
            exitcount += 1
            exitstring[1] = "<: " + str(exit2) + " "
        else:
            exitstring[1] = ""
            pygame.draw.rect(gameDisplay, bright_red,(draw_h,draw_v,5,25))
        if exit3 != 999 and exit3 != 777:
            exittotal += 3
            exitcount += 1
            exitstring[2] = "/\: " + str(exit3) + " "
        else:
            exitstring[2] = ""
            pygame.draw.rect(gameDisplay, bright_red,(draw_h,draw_v,25,5))
        if exit4 != 999 and exit4 != 777:
            exittotal += 4
            exitcount += 1
            exitstring[3] = ">: " + str(exit4) + " "
        else:
            exitstring[3] = ""
            pygame.draw.rect(gameDisplay, bright_red,(draw_h+20,draw_v,5,25))
        doornum = exitcount
        if doornum == 4:
            exitstring[4] = "Large Room "
            if enemy_on_camera:
                gameDisplay.blit(cameras[11],(50,200))
            else:
                gameDisplay.blit(cameras[10],(50,200))
        if doornum == 3:
            exitstring[4] = "Corridor "
            if enemy_on_camera:
                gameDisplay.blit(cameras[5],(50,200))
            else:
                gameDisplay.blit(cameras[4],(50,200))
        if doornum == 2:
            if (exittotal%2)==0:
                if cam_num != 0:
                    exitstring[4] = "Corridor "
                    if enemy_on_camera:
                        gameDisplay.blit(cameras[3],(50,200))
                    else:
                        gameDisplay.blit(cameras[2],(50,200))
                else:
                    if rightdoor:
                        gameDisplay.blit(cameras[0],(50,200))
                    else:
                        gameDisplay.blit(cameras[1],(50,200))
                    exitstring[4] = "Control Room "
            else:
                exitstring[4] = "Corridor "
                if enemy_on_camera:
                    gameDisplay.blit(cameras[7],(50,200))
                else:
                    gameDisplay.blit(cameras[6],(50,200))
        if doornum == 1:
            exitstring[4] = "Air Vent "
            if enemy_on_camera:
                gameDisplay.blit(cameras[9],(50,200))
            else:
                gameDisplay.blit(cameras[8],(50,200))
        enemy_on_camera = False
        #output hints in where the camera can move to
        
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(exitstring[0] + exitstring[1] + exitstring[2] + exitstring[3] + exitstring[4] + "( CAM: " + str(cam_num) + " )", smallText, black)
        textRect.center = (900,750)#( (150+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        #task bar
        #100h,800v draw position
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Switch to CAM " + str(task_cam) + " and hold CTRL to complete the task", smallText, black)
        textRect.center = (350,715)
        gameDisplay.blit(textSurf, textRect)
        task_bar_draw = [100,725]
        #100 10px segments
        for i in range (100):
            #draw background
            pygame.draw.rect(gameDisplay, black,(task_bar_draw[0],task_bar_draw[1],5,100))
            task_bar_draw[0] += 5
        task_bar_draw[0] = 100
        for i in range (task):
            #draw taskbar
            if i < 30:
                pygame.draw.rect(gameDisplay, red,(task_bar_draw[0],task_bar_draw[1],5,100))
            elif i > 50:
                if dot_flash:
                    pygame.draw.rect(gameDisplay, blue,(task_bar_draw[0],task_bar_draw[1],5,100))
                else:
                    pygame.draw.rect(gameDisplay, bright_blue,(task_bar_draw[0],task_bar_draw[1],5,100))
            else:
                pygame.draw.rect(gameDisplay, green,(task_bar_draw[0],task_bar_draw[1],5,100))
            task_bar_draw[0] += 5
        #end

    #time calculation
    gamewin, rage, quarthour = time_calculation(gamewin, rage, quarthour)
    if framecount%2000 == 0: #every 2 time advances, deactivate abilities
        #set all abilities to false
        for i in range(len(activate_ability)):
            ability_camera_invis[i] = False
            ability_rapid_move[i] = False
            ability_lurk_here[i] = False
            ability_flee_now[i] = False
            ability_random_tp[i] = False

    #display time countdown
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(str(20-quarthour) + " Time Remaining", smallText, white)
    textRect.center = (1100,50)#( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    if power > 0:
        textSurf, textRect = text_objects(str(power) + "% System Power", smallText, white)
    else:
        textSurf, textRect = text_objects("SYSTEM FALIURE", smallText, white)
    textRect.center = (1100,75)#( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    #power calculation
    usage = 0
    if cameraview:
        usage+=1
    if leftdoor:
        usage+=1
    if rightdoor:
        usage+=1
    if framecount%(280-(usage*25)-(night*2)) == 0: #usage/depletion: 1/300, 2/250, 3/200 (1 less frame per night)
        power -= 1
    if framecount%(500) == 0 and powerup:
        power += random.randint(0,1)
    textSurf, textRect = text_objects("Usage: " + str(usage), smallText, white)
    textRect.center = (1100,100)#( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    if power < 1:
        leftdoor = False
        rightdoor = False
        if True: #change this to startstop
            pygame.mixer.Sound.play(power_down_sound)
            startstop = False
        if cameraview:
            camup = True

    #task code
    if night > 6:
        tmpint = 6
    if framecount%(100-(tmpint*10)) == 0:
        task-=1
    if task == 0:
        power = 0
    if task < 30 and not cameraview:
        textSurf, textRect = text_objects("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", smallText, bright_red)
        textRect.center = (0,850)
        gameDisplay.blit(textSurf, textRect)
        if not low_power_level:
            low_power_level = True
            pygame.mixer.Sound.play(alarm_sound)
    if task > 30:
        low_power_level = False
    if task > 50:
        powerup = True
    else:
        powerup = False
        
    #dot flash
    if framecount%5 == 0:
        dot_flash = not dot_flash
        
    #game over code
    if gameover:
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.mixer.music.load('audio_data/jumpscare_1_test.wav')
        pygame.mixer.music.play(1)
        mainmenu_active = True
        gameover = False
        #play animation
        if cameraview:
            for i in range (5):
                gameDisplay.blit((jumpscare[i]),(0,0))
                pygame.display.update()
        for i in range (25):
            gameDisplay.blit((jumpscare[i+5]),(0,0))
            pygame.display.update()
        print("game over :)")
        pygame.mixer.stop()

    if gamewin:
        #play song :)
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.mixer.music.load('audio_data/Sci Fi Vortex.mp3')
        pygame.mixer.music.play(1)
        #show level complete screen
        gamewin = False
        sparepower = power
        if night != 5 and not custommode:
            startnight = True
            night += 1
            for i in range (99):
                gameDisplay.blit((phase_win[i]),(0,0))
                pygame.display.update()
        else:
            mainmenu_active = True
            for i in range (99):
                gameDisplay.blit((phase_win[i]),(0,0))
                pygame.display.update()
            if night == 5 and not custommode:
                #unlocked nightmare mode
                for i in range(60):
                    gameDisplay.fill(red)
                    tmpmsg = ("Unlocked Nightmare Mode")
                    message_display(tmpmsg)
                    pygame.display.update()
                    clock.tick(60)
                #unlocked custom level mode
                for i in range(60):
                    gameDisplay.fill(red)
                    tmpmsg = ("Unlocked Custom Level")
                    message_display(tmpmsg)
                    pygame.display.update()
                    clock.tick(60)
                night_reached = 6
                ngplus = 1
        if night > 5:
             #night += 1
             night_reached = 6
        pygame.mixer.stop()

    #keyboard input    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_COMMA:
                #task -=1
                pass
            if (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL) and task < 100 and cam_num == task_cam:
                task += 5
                if task > 100:
                    task = 100
                pygame.mixer.Sound.play(map_task_sound)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                #cam toggle
                if cameraview:
                    camup = True
                if not cameraview and power > 0:
                    camdown = True
            if event.key == pygame.K_q and power > 0:
                #left door
                leftdoor = not leftdoor
            if event.key == pygame.K_e and power > 0:
                #right door
                rightdoor = not rightdoor
            #camera controls
            if event.key == pygame.K_s and E1 and cameraview and power > 0:
                cam_num = mapdata[cam_num*5+1]
                lookpos += map_size
                pygame.mixer.Sound.play(map_nav_sound)
            if event.key == pygame.K_a and E2 and cameraview and power > 0:
                cam_num = mapdata[cam_num*5+2]
                lookpos -= 1
                pygame.mixer.Sound.play(map_nav_sound)
            if event.key == pygame.K_w and E3 and cameraview and power > 0:
                cam_num = mapdata[cam_num*5+3]
                lookpos -= map_size
                pygame.mixer.Sound.play(map_nav_sound)
            if event.key == pygame.K_d and E4 and cameraview and power > 0:
                cam_num = mapdata[cam_num*5+4]
                lookpos += 1
                pygame.mixer.Sound.play(map_nav_sound)
            #cheat to get to the end of the night, its not so simple anymore
            if event.key == pygame.K_END and framerate_display and cam_num == 10 and not cameraview:
                gamewin = True
            #return to menu cheat
            if event.key == pygame.K_ESCAPE:
                mainmenu_active = True
                pygame.mixer.stop()
            """#power offline cheat
            if event.key == pygame.K_i:
                power = 0
            #power reset cheat
            if event.key == pygame.K_l:
                power = 100"""
            #show framerate
            if event.key == pygame.K_k:
                framerate_display = not framerate_display
    frametime = time.time() - frametime #how long since the start of the loop
    frametime = round(frametime, 4) #removing usless junk
    framerate = round(1/frametime,1) #calculate the framerate
    if framerate_display:
        if framerate > 55:
            pygame.draw.rect(gameDisplay, bright_green,(0,400,2000,100))
        else:
            pygame.draw.rect(gameDisplay, bright_red,(0,400,2000,100))
        message_display(str(frametime) + "SPF, " + str(framerate) + "FPS") #at the time of making this comment: 40 - 60 FPS is normal
    framecount +=1
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()

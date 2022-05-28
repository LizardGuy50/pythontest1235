import pygame
def load_save(savename):
    try:
        savedataread = open("savedata.txt")
        savedatatext = savedataread.read()
        print("save data:")
        print(savedatatext)
        savedata = savedatatext.split(",")
        print(savedata)
        display_width = int(savedata[0])
        display_height = int(savedata[1])
        night_reached = int(savedata[2])
        ngplus = int(savedata[3])
        savedataread.close()
    except:
        print("no savefile found")
        seen_opening_cutscene = False
        night_reached=1
        ngplus=0
    else:
        print("savefile loaded")
        seen_opening_cutscene = True
        #data format: (scr sze (w), (h)),night,ng+
    return night_reached,seen_opening_cutscene,ngplus,display_width,display_height

def load_map():
    try:
        savedataread = open("custommap.txt")
        savedatatext = savedataread.read()
        print("map:")
        print(savedatatext)
        savedata = savedatatext.split(",")
        print(savedata)
        maplayout = int(savedata)
        savedataread.close()
        savedataread = open("custommapdata.txt")
        savedatatext = savedataread.read()
        print("map data:")
        print(savedatatext)
        savedata = savedatatext.split(",")
        print(savedata)
        mapdata = int(savedata)
        savedataread.close()
    except:
        print("no map found")
        maplayout = [0,999,1,999,2,1,3,999,4,0,2,6,0,5,999,3,7,8,1,999,4,1,9,10,999,5,2,999,11,12,6,14,999,2,13,7,15,999,3,999,8,999,21,999,3,9,999,16,999,4,10,4,999,999,999,11,5,999,999,999,12,999,5,999,17,13,999,6,999,22,14,18,999,6,999,15,999,999,7,999,16,19,25,999,9,17,20,12,999,26,18,999,999,14,999,19,21,999,16,999,20,22,999,17,999,21,23,999,19,8,22,24,13,20,999,23,999,999,21,999,24,999,999,22,999,25,999,999,999,16,26,999,17,999,999]
        mapdata = [4]
    else:
        print("map loaded")
    return maplayout,mapdata

def load_image_seq(file_path,seq_len,file_type):
    #file_path stores the start of the file path ('image_data/<sequence name>/')
    #seq_len stores the number of images in the sequence (int)
    #file_type stores the file type ('.png')
    img_seq = []
    for i in range (seq_len):
        num = i + 1
        if num <10:
            tmpstr = "00"
        elif num < 100:
            tmpstr = "0"
        else:
            tmpstr = ""
        img_assemble = file_path + "/0" + tmpstr + str(num) + file_type
        img_seq.append(pygame.image.load(img_assemble))
    return img_seq

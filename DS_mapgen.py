#modules
import pygame, time, random
def create_room(mapdata,addtactic,fleeroom,mapgrid,mapsize): #array,bool,bool,array,int
    go = True
    count = 0
    temparray = [0]
    openarray = [777,999,999,999,999,999] #777 is avaliable, 999 is not avaliable
    while go:
        try:
            ID = mapdata[(count*5)]
        except:
            #print("map array empty")
            go = False
        else:
            ID = mapdata[(count*5)]
            exit1 = mapdata[(count*5)+1]
            exit2 = mapdata[(count*5)+2]
            exit3 = mapdata[(count*5)+3]
            exit4 = mapdata[(count*5)+4]
            if exit1 == 777:
                temparray.append(1)
            if exit2 == 777:
                temparray.append(2)
            if exit3 == 777:
                temparray.append(3)
            if exit4 == 777:
                temparray.append(4)
            if len(temparray) == 1:
                count+=1
            else:
                #room has at least 1 slot avaliable
                temparray.pop(0)
                useexit = temparray[random.randint(0,len(temparray)-1)]
                #generate an ID
                newID = (int(len(mapdata)/5))
                mapdata[int(count*5)+useexit] = newID
                #assemble the new room
                if addtactic:
                    #add a tactic to the room
                    pass
                else:
                    #add a marker for no tactic added
                    pass
                if fleeroom:
                    #add a marker that this is a flee room
                    pass
                else:
                    #add a marker for no flee room
                    pass
                #generate new room perameters
                if useexit == 3:
                    newexit1 = ID
                    newexit2 = openarray[random.randint(0,5)]
                    newexit3 = openarray[random.randint(0,1)]
                    newexit4 = openarray[random.randint(0,5)]
                    #check if any possible exits conflict with other rooms
                if useexit == 4:
                    newexit2 = ID
                    newexit1 = openarray[random.randint(0,5)]
                    newexit3 = openarray[random.randint(0,5)]
                    newexit4 = openarray[random.randint(0,1)]
                    #check if any possible exits conflict with other rooms
                if useexit == 1:
                    newexit3 = ID
                    newexit2 = openarray[random.randint(0,5)]
                    newexit1 = openarray[random.randint(0,1)]
                    newexit4 = openarray[random.randint(0,5)]
                    #check if any possible exits conflict with other rooms
                if useexit == 2:
                    newexit4 = ID
                    newexit2 = openarray[random.randint(0,1)]
                    newexit3 = openarray[random.randint(0,5)]
                    newexit1 = openarray[random.randint(0,5)]
                    #check if any possible exits conflict with other rooms
                #populate all relevent exits
                #assemble the room and add it to the map
                newroom = [newID,newexit1,newexit2,newexit3,newexit4]
                for i in range (5):
                    mapdata.append(newroom[i])
                go = False
                return mapdata

def define_map_grid(size): #size is the square dimentions (must be odd)
    mapgrid = [888]
    halfofsize = int((size+1)/2-1)
    fullsize = size*size
    for i in range (fullsize-1):
        mapgrid.append(888)
    mapgrid[int(size*((size-1)/2)+halfofsize)] = 0
    return mapgrid


def populate_map_grid(mapgrid,mapdata,map_size,roomID,lookedat): #need to modify the roomID at some point
    #mapgrid contains all of the rooms arranged
    #mapdata contains the room details
    #mapsize holds the 'mapgrid' size
    #find the list entry marked as the roomID
    #use the mapdata to populate it
    ####################
    #find the starting point
    pos = 0
    lookfor = roomID
    for i in range (len(mapgrid)):
        pos = i
        if mapgrid[i] == lookfor:
            break
        else:
            pass
    if pos == (len(mapgrid)-1):
        #not found the data
        return mapgrid, lookedat
    #get relevent data from mapdata
    exit1 = mapdata[roomID*5+1]
    exit2 = mapdata[roomID*5+2]
    exit3 = mapdata[roomID*5+3]
    exit4 = mapdata[roomID*5+4]
    #add data to the grid
    #description            exit number
    #pos -1 is left         (2)
    #pos +1 is right        (4)
    #pos -map_size is up    (3)
    #pos +map_size is down  (1)
    if exit1 != 999 and exit1 != 777:
        mapgrid[pos+map_size] = exit1
        #print("added room on E1 (D)")
    if exit2 != 999 and exit2 != 777:
        mapgrid[pos-1] = exit2
        #print("added room on E2 (L)")
    if exit3 != 999 and exit3 != 777:
        mapgrid[pos-map_size] = exit3
        #print("added room on E3 (U)")
    if exit4 != 999 and exit4 != 777:
        mapgrid[pos+1] = exit4
        #print("added room on E4 (R)")
    #just for displaying the mapgrid
    map_assemble = [0]  
    return mapgrid,lookedat

def check_map_grid(mapdata,mapgrid,map_size,roomID):
    #go to the room ID
    #look at the space that it is trying to connect to
    #if the tile exists and has an entrance facing the current tile,
    #link the tiles
    #if the tile exists and does not have an entrance facing current tile,
    #set exit to unavaliable
    #print(mapgrid)
    #print(roomID)
    lookfor = roomID
    tmp = 0
    for i in range (int(len(mapgrid))):
        if mapgrid[i] == lookfor:
            tmp = i
            break
        else:
            pass
    if tmp == (len(mapgrid)-1):
        return mapgrid, mapdata
    #check if there are any unused exits that point towards another tile
    exit1 = mapdata[roomID*5+1]     #(D)
    exit2 = mapdata[roomID*5+2]     #(L)
    exit3 = mapdata[roomID*5+3]     #(U)
    exit4 = mapdata[roomID*5+4]     #(R)
    #check if there are any tiles in the way
    tile1 = mapgrid[tmp+map_size]   #(D)
    tile2 = mapgrid[tmp-1]          #(L)
    tile3 = mapgrid[tmp-map_size]   #(U)
    tile4 = mapgrid[tmp+1]          #(R)
    #compare the exit and tile contents
    #if exitN == 777 (blank) and tileN != 888 then exitN = 999 (invalid)
    if exit1 == 777 and tile1 != 888:
        exit1 = 999
    if exit2 == 777 and tile2 != 888:
        exit2 = 999
    if exit3 == 777 and tile3 != 888:
        exit3 = 999
    if exit4 == 777 and tile4 != 888:
        exit4 = 999
    #write back to mapdata
    mapdata[roomID*5+1] = exit1
    mapdata[roomID*5+2] = exit2
    mapdata[roomID*5+3] = exit3
    mapdata[roomID*5+4] = exit4
    return mapgrid, mapdata

def check_if_room_fully_used(mapdata,roomID):
    #checks the mapdata array
    #if there are no avaliable exits return True else return False
    exit1 = mapdata[roomID*5+1]
    exit2 = mapdata[roomID*5+2]
    exit3 = mapdata[roomID*5+3]
    exit4 = mapdata[roomID*5+4]
    if exit1 != 0 and exit2 != 0 and exit3 != 0 and exit4 != 0:
        return True
    else:
        return False

def find_all_flee_rooms(mapdata):
    #populate the flee room list
    fleerooms = []
    for i in range (int(len(mapdata)/5)):
        exittotal = 0
        exit1 = mapdata[i*5+1]
        exit2 = mapdata[i*5+2]
        exit3 = mapdata[i*5+3]
        exit4 = mapdata[i*5+4]
        """
        print()
        print(i)
        print(exit1)
        print(exit2)
        print(exit3)
        print(exit4)
        """
        if exit1 == 999:
            exittotal += 1
        if exit1 == 777:
            exittotal += 1
            
        if exit2 == 999:
            exittotal += 1
        if exit2 == 777:
            exittotal += 1
            
        if exit3 == 999:
            exittotal += 1
        if exit3 == 777:
            exittotal += 1
            
        if exit4 == 999:
            exittotal += 1
        if exit4 == 777:
            exittotal += 1
            
        #print(str(i) + " " + str(exittotal))
        if exittotal == 3:
            fleerooms.append(i) #if the tile is a small room, set it as a fleeroom
    print(fleerooms)
    return fleerooms

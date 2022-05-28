how to play a 5 nights style game made in 5 days:

install pygame (REQUIRED):
LINUX: python3 -m pip install -U pygame --user
WINDOWS: py -m pip install -U pygame --user
https://www.pygame.org/wiki/GettingStarted

!!!IMPORTANT!!!
IF SOME FOLDERS ARE ZIPPED:
Unzip "audio_data" and "image_data" before playing, 
they are zipped to get past the upload file count maximum
IF THERE IS NO "image_data" FOLDER:
create one and put all of the folder except for "audio_data" inside it

Due to the way that python files are compiled and run, the game will load slowly the first time it is run

Recommended that this game is run on a computer with good single thread performance
No GPU minimum specs other than being able to show graphics in a 1250 x 900 px window

Features:
-generated map (size is determined by the game progress)
-generated enemies (including pathfinding to the player)
-conbination of FNaF 1/2 gameplay elements:
	-distraction task
	-doors
	-limited power (drains based on usage)
	-camera system

#######################
HOW TO PLAY:
#######################
MAIN:
Q: left door
E: right door
SPACE: camera toggle
WASD: camera navigation
CTRL: complete task
ESC: main menu
#######################
DEBUG:
K: FPS display
there is still a cheat to skip level but it wont be listed here
#######################
NIGHTMARE MODE
play the game with higher difficulty levels
CUSTOM MODE
specify a map to play and a difficulty, loads from 2 .txt files if avaliable (custommap.txt & custommapdata.txt)
#######################
Made in PyGame with visuals rendered in Blender
#######################
Excluding the modules used (random, pygame & time) all code is origional to this game
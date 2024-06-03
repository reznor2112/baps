#setup global
import time #used for pauses
import os #used for cls
cmdClearScreen = "clear" #clear or cls
debug = True
#TRYING LATER currentRoom = objRoom1

#setup room as class (should all objects exist in same class???) 
#https://w3schools.com/python/python_classes.asp
if debug == True : 
    print ("Setting up room objects")

class classRoom:
    def _init_(self, name, desc):
        self.name = name
        self.desc = desc

objRoom1 = classRoom("Bedroom","Stuff in it")
objRoom2 = classRoom("Landing","Stairs leading down")

if debug == True :
    print ("Printing objRoom1 and 2 name and desc")
    print (objRoom1.name + " " + objRoom1.desc)
    print (objRoom2.name + " " + objRoom2.desc)
#objRoom1.name = "The Main Bedroom"
#objRoom1.desc = "There is a bed and a window. Out of the window is a cool 80s camper and a Tesla!!"

#main
currentRoom = objRoom1 #hardcoding start room
print ("Hi! Starting in 2 seconds")
time.sleep(2)
os.system(cmdClearScreen)
# call roombit
if debug == True: 
    print ("Starting Room bit")
print ("You are in " +currentRoom.name+ ".")
# call object bit
print ("You can see ")
#call direction bit
print ("You can go ")
#call prompt bit

#end
exit()

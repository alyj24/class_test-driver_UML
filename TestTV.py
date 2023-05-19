'''continuation of the program to test the class'''

# import the TV from the module created
from class_TV import TV

# construct the test driver
def TestTV():
    # create two objects from class TV
    # tv1 objects (channel is 30, volume is 3)
    tv1 = TV(30, 3)
    tv1.turnOn()
    # tv2 objects (channel is 3, volume is 2)
    tv2 = TV(3, 2)
    tv2.turnOn()
# recognize the command and print the output
# run the program
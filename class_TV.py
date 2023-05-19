print("Assignment 6".center(42, "="))
print("\033[95m=" * 42)
print("\033[94mCMPE-103-MODULE-4-INTRODUCTION-TO-OBJECT-ORIENTED-PROGRAMMING")
print("\033[95m=" * 42)

# create a python code that have a class named "TV" and a Test Driver program named
# "TestTV" that will create two objects from class 'TV' and will produce the given outputs.

# pseudocode
# create a class and named as it is intructed
class TV:
    '''A python code whereas class and object are used, and UML Class Diagram is practiced.'''
    # define attributes and set default methods
    channel_tv = 1
    volume_tv = 1
    on_tv = False

    # implement constructor
    def __init__(self, channel_tv, volume_tv):
    self.channel = channel_tv
    self.volume = volume_tv

# establish the methods for tv
    # turn on the tv (none)
    def turnOn(self):
        self.on_tv = True
    # turn off the tv (none)
    def turnOff(self):
        self.on_tv = False
    # returns the channel of the tv (int)
    def getChannel(self):
        return self.channel
    # sets a new channel for the tv (none)
    # there is 1  to 120 selection
    def setChannel(self, channel):
        if self.on_tv and 1 <= channel <= 120:
            self.channel = channel
    # gets the volume level of the tv (int)
    def getVolume(self):
        return self.volume
    # sets a new volume level of the tv (none)
    # there is 1 to 7 range
    def setVolume(self, volume):
        if self.on_tv and 1 <= volume <= 7:
            self.volume = volume
    # increase the channel number by 1 (none)
    def channelUp(self):
        if self.on_tv and self.channel < 120:
            self.channel += 1
    # decrease the channel number by 2 (none)
    def channelDown(self):
        if self.on_tv and self.channel > 1:
            self.channel -= 1
    # increase the volume level by 1 (none)
    def volumeUp(self):
        if self.on_tv and self.volume < 7:
            self.volume += 1
    # decrease the volume level by 1 (none)
    def volumeDown(self):
        if self.on_tv and self.volume > 1:
            self.volume -= 1
# end
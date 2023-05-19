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
# end
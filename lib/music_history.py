
# {{PROBLEM}} Class Design Recipe

# Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

# As a user
# So that i can keep track of my music listening 
# I want to add tracks I've listened to and see a list of them


## 2. Design the interface 

class MusicListeningHistory():

    # music listening history - class 

    def __init__(self):
        self.musictracker = []

    # Side effects: 
        #  we store the music that the user gives as input 
        
    def addtotracker(self, songsadded):
        self.musictracker.append(songsadded)
        # print(musictracker)
        # Parameters:
            # songsadded - string 

        # Side Effects: 
            # takes what music is given as input and adds it to the list 

    def musiclist(self):
        return musictracker





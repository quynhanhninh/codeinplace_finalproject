# ----------------------------------------------
# This program randomizes song(s) to suggest to its user. 
# Song database includes 3 key categories of Emotion, Genre, and Occasion, with respective sub-categories. 
#
# Author: Ninh Quynh Anh 
# Email: anh.ninh.190008@student.fulbright.edu.vn 
# ----------------------------------------------

import random

# Here are the playlists to recommend music; the first 3 are dictionaries with key-values pairs of sub-categories and corresponding songs; the last playlist includes all the songs for random mode
emotion = {"happy":["Mr. Blue Sky - Electric Light Orchestra", "New Light - John Mayer", "Party In The U.S.A - Miley Cyrus", "Mariposa - Peach Tree Rascals", "Best Day of My Life - American Authors"], "sad":["Summertime Sadness - Lana Del Rey", "Slow Dancing In The Dark - Joji", "Before You Go - Lewis Capaldi", "The Night We Met - Lord Huron", "Stone Cold - Demi Lovato"], "bad biatch":["good 4 u - Olivia Rodrigo", "Better Than Revenge - Taylor Swift", "Fuck You - Lily Allen", "Sorry Not Sorry - Demi Lovato", "Primadona - MARINA"]}
genre = {"US-UK Pop":["Shape of You - Ed Sheeran", "Starboy - The Weekend", "Sucker - Jonas Brothers", "FRIENDS - Marshmallow, Anne-Marie", "Still Into You - Paramore"], "Kpop":["I Got A Boy - Girls' Generation", "Fire - BTS", "Psycho - Red Velvet", "Power - EXO", "BANG BANG BANG - BIGBANG"], "Vpop":["Muộn rồi mà sao còn - Sơn Tùng M-TP", "Trốn Tìm - Đen", "Gác Lại Âu Lo - Da LAB, Miu Lê", "Nàng Thơ - Hoàng Dũng", "Tình Bạn Diệu Kỳ - Ricky Star, AMEE"]}
occasion = {"birthday":["Birthday - Katy Perry", "Birthday - Anne-Marie", "BIRTHDAY - SOMI", "Any song - ZICO", "Khúc hát mừng sinh nhật - Phan Đình Tùng"], "love anniversary":["Best Of You - Andy Grammer, Elle King", "LOVE - AILEE, CHEN", "You & Me - James TW", "Electric Love - BØRNS", "Dance To This - Troye Sivan, Ariana Grande"], "road trip":["Summer - Calvin Harris", "YOUTH - Troye Sivan", "Riptide - Vance Joy", "Shut Up and Dance - WALK UP THE MOON", "I'm on Top of The World - The World's Cause"]}
random_list = ["Mr. Blue Sky - Electric Light Orchestra", "New Light - John Mayer", "Party In The U.S.A - Miley Cyrus", "Mariposa - Peach Tree Rascals", "Best Day of My Life - American Authors", "Summertime Sadness - Lana Del Rey", "Slow Dancing In The Dark - Joji", "Before You Go - Lewis Capaldi", "The Night We Met - Lord Huron", "Stone Cold - Demi Lovato", "good 4 u - Olivia Rodrigo", "Better Than Revenge - Taylor Swift", "Fuck You - Lily Allen", "Sorry Not Sorry - Demi Lovato", "Primadona - MARINA", "Shape of You - Ed Sheeran", "Starboy - The Weekend", "Sucker - Jonas Brothers", "FRIENDS - Marshmallow, Anne-Marie", "Still Into You - Paramore", "I Got A Boy - Girls' Generation", "Fire - BTS", "Psycho - Red Velvet", "Power - EXO", "BANG BANG BANG - BIGBANG", "Muộn rồi mà sao còn - Sơn Tùng M-TP", "Trốn Tìm - Đen", "Gác Lại Âu Lo - Da LAB, Miu Lê", "Nàng Thơ - Hoàng Dũng", "Tình Bạn Diệu Kỳ - Ricky Star, AMEE", "Birthday - Katy Perry", "Birthday - Anne-Marie", "BIRTHDAY - SOMI", "Any song - ZICO", "Khúc hát mừng sinh nhật - Phan Đình Tùng", "Best Of You - Andy Grammer, Elle King", "LOVE - AILEE, CHEN", "You & Me - James TW", "Electric Love - BØRNS", "Dance To This - Troye Sivan, Ariana Grande", "Summer - Calvin Harris", "YOUTH - Troye Sivan", "Riptide - Vance Joy", "Shut Up and Dance - WALK UP THE MOON", "I'm on Top of The World - The World's Cause"]

def main():
    '''Receive input from user to generate songs'''
    while True:
    # Introduce the program and ask user how many songs they want
        print("Welcome to the music recommender tool!")
        num_song = int(input("(Enter 0 stop) Number of songs to receive (1, 2, or 3): "))
        if num_song == 0:
            break
        if num_song > 3:
            print("Number must be from 1 to 3. Please try again!") # redo if user chooses more than 3

    # Ask user to choose from 4 modes: emotion, genre, occasion, and random
        mode = int(input("There are 4 modes of song recommendation: 1 - Emotion, 2 - Genre, 3 - Occasion, 4 - Random. Enter number of your choice: "))
        if mode == 0 or mode > 4: # Check for error in user's input
            print("Number must be from 1 to 3. Please try again!")
            print("")
            break
        else:
            print("")
            random_song(mode, num_song)
            print("")
            print("")

def random_song(mode, num_song):
    '''
    A method to select song from chosen mode 

    Parameter 
    --------
    mode: int 
        The category of songs' type in numerical type
    num_song: int 
        The number of song to which users want to listen
    '''
    if mode == 4: # User chooses random mode
        track = [] # To keep track of randomized number
        print("Please enjoy the music:")
        for i in range(num_song):
            num_rand = random.randint(0, len(random_list) - 1) # Randomize a number within the list's length
            while num_rand in track: # To make sure not duplicating any number (or song) when randomizing
                num_rand = random.randint(0, len(random_list) - 1) # Randomize a new number
            track.append(num_rand) # Add the randomized number to the tracking list
            print(random_list[num_rand]) # Print song name whose index being the randomized number from the playlist of all songs

    # User chooses one of the other 3 modes, with sub-categories to choose from:
    elif mode == 1:
        mode = emotion # Call out dictionary 'Emotion' with key-value pairs being sub-categories and corresponding songs
        sub_choice = input('There are "happy", "sad", and "bad biatch" songs. Enter one category: ') # Ask user to choose a specific sub-category
        random_sub_list(mode, num_song, sub_choice)
    elif mode == 2: # Similar to mode 1
        mode = genre
        sub_choice = input('There are "US-UK Pop", "Kpop", and "Vpop" songs. Enter one category: ')
        random_sub_list(mode, num_song, sub_choice)
    else: # Similar to mode 1 and 2
        mode = occasion
        sub_choice = input('There are "birthday", "love anniversary", and "road trip" songs. Enter one category: ')
        random_sub_list(mode, num_song, sub_choice)

def random_sub_list(mode, num_song, sub_choice):
    '''
    A helper method to choose music randomly in the sub-catergory list  

    Parameter 
    --------
    mode: int 
        The category of songs' type in numerical type
    num_song: int 
        The number of song to which users want to listen
    sub_choice: str 
        The subcategory of songs' type
    '''
    track = [] # To keep track of randomized number
    sub_list = mode[sub_choice] # Access the value in the dictionary (earlier assigned as mode) with sub-category being the key, then assign the value into a new list to later randomize its items/songs
    print("Please enjoy music from " + sub_choice + " playlist:")
    for i in range(num_song):
        num_rand = random.randint(0, len(sub_list) - 1) # Randomize a number within the list's length
        while num_rand in track: # To make sure not duplicating any number (or song) when randomizing
            num_rand = random.randint(0, len(sub_list) - 1)
        track.append(num_rand)
        print(sub_list[num_rand]) # Print song name whose index being the randomized number from the respective list

if __name__ == '__main__':
    main()

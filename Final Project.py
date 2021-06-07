""" This program randomizes song(s) to suggest to its user. Songs are categorized into lists of emotion, genre, and occasion. """

import random

# Here are the playlists to recommend music
emotion = {"happy":["Mr. Blue Sky - Electric Light Orchestra", "New Light - John Mayer", "Party In The U.S.A - Miley Cyrus", "Mariposa - Peach Tree Rascals", "Best Day of My Life - American Authors"], "sad":["Summertime Sadness - Lana Del Rey", "Slow Dancing In The Dark - Joji", "Before You Go - Lewis Capaldi", "The Night We Met - Lord Huron", "Stone Cold - Demi Lovato"], "bad biatch":["good 4 u - Olivia Rodrigo", "Better Than Revenge - Taylor Swift", "Fuck You - Lily Allen", "Sorry Not Sorry - Demi Lovato", "Primadona - MARINA"]}
genre = {"US-UK Pop":["Shape of You - Ed Sheeran", "Starboy - The Weekend", "Sucker - Jonas Brothers", "FRIENDS - Marshmallow, Anne-Marie", "Still Into You - Paramore"], "Kpop":["I Got A Boy - Girls' Generation", "Fire - BTS", "Psycho - Red Velvet", "Power - EXO", "BANG BANG BANG - BIGBANG"], "Vpop":["Muộn rồi mà sao còn - Sơn Tùng M-TP", "Trốn Tìm - Đen", "Gác Lại Âu Lo - Da LAB, Miu Lê", "Nàng Thơ - Hoàng Dũng", "Tình Bạn Diệu Kỳ - Ricky Star, AMEE"]}
occasion = {"birthday":["Birthday - Katy Perry", "Birthday - Anne-Marie", "BIRTHDAY - SOMI", "Any song - ZICO", "Khúc hát mừng sinh nhật - Phan Đình Tùng"], "love anniversary":["Best Of You - Andy Grammer, Elle King", "LOVE - AILEE, CHEN", "You & Me - James TW", "Electric Love - BØRNS", "Dance To This - Troye Sivan, Ariana Grande"], "road trip":["Summer - Calvin Harris", "YOUTH - Troye Sivan", "Riptide - Vance Joy", "Shut Up and Dance - WALK UP THE MOON", "I'm on Top of The World - The World's Cause"]}
random_list = ["Mr. Blue Sky - Electric Light Orchestra", "New Light - John Mayer", "Party In The U.S.A - Miley Cyrus", "Mariposa - Peach Tree Rascals", "Best Day of My Life - American Authors", "Summertime Sadness - Lana Del Rey", "Slow Dancing In The Dark - Joji", "Before You Go - Lewis Capaldi", "The Night We Met - Lord Huron", "Stone Cold - Demi Lovato", "good 4 u - Olivia Rodrigo", "Better Than Revenge - Taylor Swift", "Fuck You - Lily Allen", "Sorry Not Sorry - Demi Lovato", "Primadona - MARINA", "Shape of You - Ed Sheeran", "Starboy - The Weekend", "Sucker - Jonas Brothers", "FRIENDS - Marshmallow, Anne-Marie", "Still Into You - Paramore", "I Got A Boy - Girls' Generation", "Fire - BTS", "Psycho - Red Velvet", "Power - EXO", "BANG BANG BANG - BIGBANG", "Muộn rồi mà sao còn - Sơn Tùng M-TP", "Trốn Tìm - Đen", "Gác Lại Âu Lo - Da LAB, Miu Lê", "Nàng Thơ - Hoàng Dũng", "Tình Bạn Diệu Kỳ - Ricky Star, AMEE", "Birthday - Katy Perry", "Birthday - Anne-Marie", "BIRTHDAY - SOMI", "Any song - ZICO", "Khúc hát mừng sinh nhật - Phan Đình Tùng", "Best Of You - Andy Grammer, Elle King", "LOVE - AILEE, CHEN", "You & Me - James TW", "Electric Love - BØRNS", "Dance To This - Troye Sivan, Ariana Grande", "Summer - Calvin Harris", "YOUTH - Troye Sivan", "Riptide - Vance Joy", "Shut Up and Dance - WALK UP THE MOON", "I'm on Top of The World - The World's Cause"]

def main():
    while True:
    # Introduce program and ask user how many songs they want
        print("Welcome to the music recommender tool!")
        num_song = int(input("(Enter 0 stop) Number of songs to receive (1, 2, or 3): "))
        if num_song == 0:
            break
        if num_song > 3:
            print("Number must be from 1 to 3. Please try again!") # redo if user chooses more than 3

    # Ask user to choose from 4 modes: emotion, genre, occasion, and random
        mode = int(input("There are 4 modes of song recommendation: 1 - Emotion, 2 - Genre, 3 - Occasion, 4 - Random. Enter number of your choice: "))
        if mode == 0 or mode > 4:
            print("Number must be from 1 to 3. Please try again!")
            print("")
            break
        else:
            print("")
            random_song(mode, num_song)
            print("")
            print("")

def random_song(mode, num_song):
    if mode == 4: # Random mode
        track = []
        print("Please enjoy the music:")
        for i in range(num_song):
            num_rand = random.randint(0, len(random_list) - 1)
            while num_rand in track: # To eliminate repeated number
                num_rand = random.randint(0, len(random_list) - 1)
            track.append(num_rand)
            print(random_list[num_rand])

    # Here are for the other 3 modes with sub-categories to choose from:
    elif mode == 1:
        mode = emotion
        sub_choice = input('There are "happy", "sad", and "bad biatch" songs. Enter one category: ')
        random_sub_list(mode, num_song, sub_choice)
    elif mode == 2:
        mode = genre
        sub_choice = input('There are "US-UK Pop", "Kpop", and "Vpop" songs. Enter one category: ')
        random_sub_list(mode, num_song, sub_choice)
    else:
        mode = occasion
        sub_choice = input('There are "birthday", "love anniversary", and "road trip" songs. Enter one category: ')
        random_sub_list(mode, num_song, sub_choice)

def random_sub_list(mode, num_song, sub_choice):
    track = []
    sub_list = mode[sub_choice]
    print("Please enjoy music from " + sub_choice + " playlist:")
    for i in range(num_song):
        num_rand = random.randint(0, len(sub_list) - 1)
        while num_rand in track:
            num_rand = random.randint(0, len(sub_list) - 1)
        track.append(num_rand)
        print(sub_list[num_rand])

if __name__ == '__main__':
    main()

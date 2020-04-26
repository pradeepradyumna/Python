from tkinter import *
import pygame
import os

window = Tk()
window.title("Music Player")
window.geometry("310x90")

pygame.mixer.init()

lblSong = Label(window, text='Your music', font="times 20")
lblSong.grid(row=1, column=1)

n = 0


def PlaySong(songname):
    try:
        pygame.mixer.music.load(str(songname))
        pygame.mixer.music.play(0)
        lblSong['text'] = str(songname)
        print("playing" + str(songname))
    except Exception as ex:
        print(ex)


def btnPlay_click(songname):
    global n
    global currentsongname
    n = n + 1
    if n == 1:
        print("play")
        currentsongname = songname
        PlaySong(songname)

    elif (n % 2) == 0:
        if currentsongname != songs_listbox.get():
            n = 0
            PlaySong(songs_listbox.get())
        else:
            print("paused")
            pygame.mixer.music.pause()

    elif (n % 2) != 0:
        if currentsongname != songs_listbox.get():
            n = 0
            PlaySong(songs_listbox.get())
        else:
            print("unpaused")
            pygame.mixer.music.unpause()


btnPlay = Button(window, text='Play/ Pause', width=20, command=lambda: btnPlay_click(songs_listbox.get()))
btnPlay.grid(row=6, column=1)

songs = os.listdir()
songs_listbox = StringVar(window)

songs_listbox.set("Pick a song")

menu = OptionMenu(window, songs_listbox, *songs)
menu.grid(row=6, column=6)

window.mainloop()

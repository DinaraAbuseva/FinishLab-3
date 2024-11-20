import tkinter as tk
from pygame import mixer
from key_generate import key


window = tk.Tk()
window.title("Keygen")
file_png = tk.PhotoImage(file = "./Hitman.png")
bg = tk.Label(image = file_png)

mixer.init()
mixer.music.load("music.mp3")


def play():
    if button_mus["text"] == "Play!":
        button_mus["text"] = "Pause"
        mixer.music.play()
    else:
        button_mus["text"] = "Play!"
        mixer.music.pause()


button_mus = tk.Button(window, text = "Play!",command = play)
button_mus.place(in_ = bg, relx = 0, rely = 0, 
                 anchor = "nw", 
                 width = 80, height = 40)

for_key = tk.Label(window, text="Key will be here!")
for_key.place(in_ = bg, relx = 0.5, rely = 0.7, 
                 anchor = "s", width = 100, height = 50)


def end():
    for_key.config(text=key)


button_gen = tk.Button(window, text = "Generate!", command = end)


def animation(i,j):
    if i < 500:
        if j < 300:
            button_gen.place(x = i,y = j)
            button_gen.after(50,lambda: animation(i,j))
            j += 1
        i += 2


animation(0,0)

bg.pack(fill = "both", expand = "YES")



window.mainloop()


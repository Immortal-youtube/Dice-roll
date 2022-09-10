from tkinter import *
import random 
import os

def reroll2():
    text1 = random.randint(1,6)
    result.config(text=text1)
    
window = Tk()
print(os.path.join(os.path.dirname(__file__),"dice.png"))
result = Label(window ,font=("Ariel",200),foreground="cyan",background="black")
result.pack(anchor='center')

reroll = Button(window,text="re roll",font=("Ariel",30),foreground="Blue",background="Black",command=reroll2)
reroll.pack(anchor='s')
photo = PhotoImage(file = os.path.join(os.path.dirname(__file__),"dices.png"))
window.iconphoto(False,photo)



window.mainloop()
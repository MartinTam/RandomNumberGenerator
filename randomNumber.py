from tkinter import *
import random

root = Tk()
root.geometry('500x500')
root.title('Random Number Generator')
# ---------------------------------------------------------------

# Title frame
titleFrame = LabelFrame(root, padx = 400, pady = 100).pack()
title = Label(titleFrame, text = 'Random Number Generator', font = ('Comicsans', 20), padx = 20, pady = 20).pack()



# ---------------------------------------------------------------
root.mainloop()





#number = random.randint(9,9)
#number = random.uniform(10, 1)

#print(number)
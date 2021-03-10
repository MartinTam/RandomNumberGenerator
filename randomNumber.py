from tkinter import *
import random

root = Tk()
root.geometry('450x500')
root.title('Random Number Generator')
# ---------------------------------------------------------------

MOVE = 30

# Title
title = Label(root, text = 'Random Number Generator', font = ('Comicsans', 20), padx = MOVE, pady = MOVE).grid(row = 0, column = 1, columnspan = 4)

# Type of number
chooseType = StringVar()
chooseType.set('Integer')
Radiobutton(root, text = 'Integer', variable = chooseType, value = 'Integer', padx = MOVE).grid(row = 1, column = 1, columnspan = 2)
Radiobutton(root, text = 'Floating point', variable = chooseType, value = 'Floating point', padx = MOVE).grid(row = 2, column = 1, columnspan = 2)

# Values
startTitle = Label(root, text = 'From:' ).grid(row = 3, column = 1, padx = MOVE, pady = (MOVE, 0))
endTitle = Label(root, text = 'To:' ).grid(row = 3, column = 2, padx = MOVE, pady = (MOVE, 0))

startValue = Entry(root, width = 20)
endValue = Entry(root, width = 20)

startValue.grid(row = 4, column = 1, padx = MOVE, pady = (0, MOVE) )
endValue.grid(row = 4, column = 2, padx = MOVE, pady = (0, MOVE) )

# Generate random number

showRandomNumber = Label(root, padx = MOVE, pady = MOVE)  # For destroying the last generate number in the background

def randomNumber():
    global showRandomNumber
    showRandomNumber.destroy()

    if chooseType.get() == 'Integer':
        number = random.randint( int( startValue.get() ), int( endValue.get() ) )
        showRandomNumber = Label(root, text = number, padx = MOVE, pady = MOVE)
        showRandomNumber.grid(row = 6, column = 1, columnspan = 2)

    
    elif chooseType.get() == 'Floating point':
        number = random.uniform( float( startValue.get() ), float( endValue.get() ) )
        showRandomNumber = Label(root, text = number, padx = MOVE, pady = MOVE)
        showRandomNumber.grid(row = 6, column = 1, columnspan = 2)


# Generate button
generate = Button(root, text = 'Generate', command = randomNumber).grid(row = 5, column = 1, columnspan = 2, padx = MOVE, pady = (0, MOVE) )


# ---------------------------------------------------------------
root.mainloop()
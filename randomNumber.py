from tkinter import *
import random

root = Tk()
root.geometry('800x500')
root.title('Random Number Generator')
# ---------------------------------------------------------------

# Title
title = Label(root, text = 'Random Number Generator', font = ('Comicsans', 20)).grid(row = 0, column = 0)

# Type of number
chooseType = StringVar()
chooseType.set('Integer')
Radiobutton(root, text = 'Integer', variable = chooseType, value = 'Integer').grid(row = 1, column = 0)
Radiobutton(root, text = 'Floating point', variable = chooseType, value = 'Floating point').grid(row = 2, column = 0)

# Values
startTitle = Label(root, text = 'From:').grid(row = 3, column = 0)
endTitle = Label(root, text = 'To:').grid(row = 3, column = 1)

startValue = Entry(root, width = 20)
endValue = Entry(root, width = 20)

startValue.grid(row = 4, column = 0)
endValue.grid(row = 4, column = 1)

# Generate random number

showRandomNumber = Label(root)  # For destroying the last generate number

def randomNumber():
    global showRandomNumber
    showRandomNumber.destroy()

    if chooseType.get() == 'Integer':
        number = random.randint( int( startValue.get() ), int( endValue.get() ) )
        showRandomNumber = Label(root, text = number)
        showRandomNumber.grid(row = 6, column = 0)

    
    elif chooseType.get() == 'Floating point':
        number = random.uniform( float( startValue.get() ), float( endValue.get() ) )
        showRandomNumber = Label(root, text = number)
        showRandomNumber.grid(row = 6, column = 0)


    #showRandomNumber.grid_forget()

# Generate button
generate = Button(root, text = 'Generate', command = randomNumber).grid(row = 5, column = 0, columnspan = 2)


# ---------------------------------------------------------------
root.mainloop()





#number = random.randint(9,9)
#number = random.uniform(10, 1)

#print(number)
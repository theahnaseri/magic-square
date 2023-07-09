from main import fillMagicSquare
from termcolor import *
from time import *
from tkinter import *
from tkinter import messagebox

# inherianceing from Tk module and initializing the Tk class for creating object
class App(Tk):
    def __init__(self):
        # Initial
        Tk.__init__(self)
        self.title("Magic Square Solver")
        self.iconbitmap(default=f'{__file__}\\..\\magic_square.ico')
        self.geometry('520x715')
        self.resizable(width=False, height=False)

        # Status Frame
        self.statusFrame = LabelFrame(self, text='Status')
        self.statusFrame.place(x=8, y=5, width=505, height=175)

        self.welcomeLabel = Label(self.statusFrame,text="~•~ Welcome To Magic Square Solver ~•~", font=("Tahoma",15))
        self.welcomeLabel.pack(pady=8)

        self.inputLabel = Label(self.statusFrame,text="Set the Magic Square size", font=("Tahoma",12))
        self.inputLabel.pack(pady=2)

        self.inputSpinbox = Spinbox(self.statusFrame, from_=1, to=10, width=20, font=('Helvetica', 12, 'bold'))
        self.inputSpinbox.pack(pady=2)

        self.displayButton = Button(self.statusFrame, text="Display", font=("Tahoma",12), command=self.display)
        self.displayButton.pack(pady=8)

        # Square Frame
        self.squareFrame = LabelFrame(self, text='Square')
        self.squareFrame.place(x=8, y=185, width=505, height=520)
        

    def display(self):
        self.squareFrame.destroy()
        self.squareFrame = LabelFrame(self, text='Square')
        self.squareFrame.place(x=8, y=185, width=505, height=520)

        size = int(self.inputSpinbox.get())
        if size == 2:
            messagebox.showinfo("Attention", "There is no magic square of size 2")
            return
        magicSquare = fillMagicSquare(size)

        # Loop through the matrix and create labels for each value
        for i in range(len(magicSquare)):
            for j in range(len(magicSquare[i])):
                # Create a label with the cell value
                cell_text = str(magicSquare[i][j])
                cell_label = Label(self.squareFrame, text=cell_text, font=("Arial", 14), width=4, height=2, bd=2, relief="solid")
                
                # Position the label in the grid
                cell_label.grid(row=i, column=j)

# creating the object of app for tk main window
if __name__ == "__main__":
    app = App()
    app.mainloop()
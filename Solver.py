from tkinter import *
from tkinter import messagebox
class Sudoku:

    def __init__(self, board):
        #Before we start solving the problem we have to validate whether the solution can be obtained or not
        flag=True    #By the end of the validation of the flag is true then we get the solution ,else no
        self.duplicate=[]   #A duplicate of the original list is made to make the validation
        for i in range(9):
            self.duplicate+=[['','','','','','','','','']]
        for i in range(9):
            for j in range(9):
                self.duplicate[i][j]=board[i][j]
        # We iterate over each block and check whether it is valid or not
        for i in range(9):
            for j in range(9):
                if not (self.isValid(i,j,self.duplicate)):  #If atleast one block is not satisfying the rule then we make flag as false
                    flag=False
        if flag:
            #After validation we start solving using the backtracking method
            self.backtrack(board)
        else:
            #If the solution can not be obtained then we just throw an error message
            messagebox.showinfo('Error','The following Grid does not obey the Suduko rules')




    #Is valid is the fuction used to check whether a particular block in the board is obeying the sudoku rules or not
    def isValid(self,x, y, b):
        if(b[x][y]==''):
            return True
        tmp = b[x][y];
        b[x][y] = 'D'
        for i in range(9):
            if b[i][y] == tmp : return False
        for i in range(9):
            if b[x][i] == tmp : return False
        for i in range(3):
            for j in range(3):
                if b[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp: return False
        b[x][y] = tmp
        return True
    #we check all the possibilities and see if the current possibility is giving the solution
    # Thats the general idea of this algorithm
    def backtrack(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '':
                    for k in '123456789': #A block can have any value in the range of 1 to 9
                        board[i][j] = k
                        if self.isValid(i, j, board) and self.backtrack(board): #This is the condition that a value in the block must satisfy
                            return True
                        board[i][j] = ''
                    return False
        return True

#Window class is purely for the GUI
# where we create the Sudoku board GUI
class window:
    def __init__(self, toplevel):

        toplevel.resizable(width = False, height = False)
        toplevel.title('Final')

        font = ('Arial', 18)


        #We create 9 frames and each frame is nothing but one row in the board
        self.fr = Frame(toplevel)

        self.fr.pack(ipady = 0, padx = 0)
        self.fr1 = Frame(toplevel)

        self.fr1.pack(ipady = 0, padx = 0)
        self.fr2 = Frame(toplevel)

        self.fr2.pack(ipady = 0, padx = 0)
        self.fr3 = Frame(toplevel)

        self.fr3.pack(ipady = 0, padx = 0)
        self.fr4 = Frame(toplevel)

        self.fr4.pack(ipady = 0, padx = 0)
        self.fr5 = Frame(toplevel)

        self.fr5.pack(ipady = 0, padx = 0)
        self.fr6 = Frame(toplevel)

        self.fr6.pack(ipady = 0, padx = 0)
        self.fr7 = Frame(toplevel)

        self.fr7.pack(ipady = 0, padx = 0)
        self.fr8 = Frame(toplevel)

        self.fr8.pack(ipady = 0, padx = 0)
        self.fr9 = Frame(toplevel)

        self.fr9.pack(ipady = 1, padx = 1)

        #__board are the text fields/entries in the GUI
        self.__board = []
        for i in range(1,10):
            self.__board += [[0,0,0,0,0,0,0,0,0]]

        variable = self.fr
        #px,py denote the position where the component has to be placed in the frame
        px = 0
        py = 0
        # ' i ' denotes which row are we currently in,so depending on the i value we select the frame
        for i in range(0,9):
            for j in range(0,9):

                if i == 0:
                    variable = self.fr
                if i == 1:
                    variable = self.fr1
                if i == 2:
                    variable = self.fr2
                if i == 3:
                    variable = self.fr3
                if i == 4:
                    variable = self.fr4
                if i == 5:
                    variable = self.fr5
                if i == 6:
                    variable = self.fr6
                if i == 7:
                    variable = self.fr7
                if i == 8:
                    variable = self.fr8

                color = 'white'  # Background color of each entry
                f_color='black'  #Foreground color of each entry

                #The below 3 conditions are to identify which 3x3 grid it is
                if j in [3,4,5] and i in [0,1,2,6,7,8]:
                    color = 'black'
                    f_color= 'white'
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    color = 'black'
                    f_color = 'white'
                else:
                    color = 'white'
                    f_color = 'black'
                #We create entries and assign its configurations depending upon the i and j values
                self.__board[i][j] = Entry(variable, width = 2, font = font,fg=f_color, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = f_color,
                                          textvar = bd[i][j])
                self.__board[i][j].pack(side = LEFT, padx = px, pady = py)



        #Button to get the solution
        self.btn1 = Button(self.fr9, text = 'Solve', fg = 'blue', font = ('Arial', 13), command = self.solve)
        self.btn1.pack(side = LEFT)

        #Button to reset the grid to original state
        self.btn2 = Button(self.fr9, text = 'Reset', fg = 'red', font = ('Arial', 13), command = self.reset)
        self.btn2.pack(side = RIGHT)

    def solve(self):
        #To identify which blocks are the non changable ones we change their color to Orange
        def recolor(self):
            for i in range(9):
                for j in range(9):
                    if bd[i][j].get() != '':
                        self.__board[i][j].configure(bg='orange')
        #Correct method is to remove the invalid entries
        self.correct()
        recolor(self)
        #We take the information from the entries and convert them into a 2 dimensional list
        for i in range(9):
            for j in range(9):
                board[i][j]=bd[i][j].get()
        #We get the solution in the form of a list
        o=Sudoku(board)
        #We assign each value of the entry with the respective value in the list
        for i in range(9):
            for j in range(9):
                bd[i][j].set(board[i][j])


    def correct(self):
        for i in range(9):
            for j in range(9):
                if bd[i][j].get() == '':
                    continue
                #If the size of the string is more than 1 or it is not digit we just make it as empty
                if len(bd[i][j].get()) > 1 or bd[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    bd[i][j].set('')

    def reset(self):
        #Make all the entries empty and change the colors back to normal
        for i in range(9):
            for j in range(9):
                bd[i][j].set('')
                if j in [3,4,5] and i in [0,1,2,6,7,8]:
                    self.__board[i][j].configure(bg='black')
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    self.__board[i][j].configure(bg='black')
                else:
                    self.__board[i][j].configure(bg='white')


#The window on which all the components are placed
game=Tk()
board=[]
for i in range(1,10):
    board += [[0,0,0,0,0,0,0,0,0]]
bd = []
for i in range(1,10):
    bd += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        bd[i][j] = StringVar(game)
a=window(game)
game.mainloop()
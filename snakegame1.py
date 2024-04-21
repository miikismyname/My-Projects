from tkinter import *
from math import floor,ceil
from random import choice

score = 0
labellist = []
alist = []
snakebody = []
allist = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), 
(10, 10), (10, 11), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)}
newway = 'E'
oldway = ''
forgotten = False
gameover = False
destroyed = False
movemade = False



def gameon():
    global oldway
    global newway
    global forgotten
    global labellist
    global snakebody
    global apple
    global gameover
    global gameoverframe
    global score
    global movemade
    global allist
    global destroyed

    if gameover != True:

        if newway == 'E':
            if oldway != 'W':
                newrow = int(snake_head.grid_info()['row'])
                newcolumn = int(snake_head.grid_info()['column'])
                if newcolumn+1 == 12:
                    snake_head.grid_forget()
                    snake_head.grid(row=newrow,column=0)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=newrow,column=0,sticky=E)
                else:
                    snake_head.grid_forget()
                    snake_head.grid(row=newrow,column=newcolumn+1)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=newrow,column=newcolumn+1,sticky=E)
                for i in snakebody:
                    if snakebody.index(i) != 0:
                        if (newcolumn - int(i.grid_info()['column'])) > 0:
                            if newcolumn!=11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn+1,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=11,row = newrow)
                        elif (newcolumn - int(i.grid_info()['column'])) < 0:
                            if newcolumn == 0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=0,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn-1,row = newrow)
                        elif (newrow - int(i.grid_info()['row'])) > 0:
                            if newrow != 11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow+1)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 11)
                        else:
                            if newrow ==0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 0)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow-1)

                oldway = 'E'
            else:
                newway = 'E'
        elif newway == 'N':
            if oldway != 'S':
                newrow = int(snake_head.grid_info()['row'])
                newcolumn = int(snake_head.grid_info()['column'])
                if newrow == 0:
                    snake_head.grid_forget()
                    snake_head.grid(row=11,column=newcolumn)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=11,column=newcolumn,sticky=N)
                else:
                    snake_head.grid_forget()
                    snake_head.grid(row=newrow-1,column=newcolumn)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=newrow-1,column=newcolumn,sticky=N)
                for i in snakebody:
                    if snakebody.index(i) != 0:
                        if (newcolumn - int(i.grid_info()['column'])) > 0:
                            if newcolumn!=11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn+1,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=11,row = newrow)
                        elif (newcolumn - int(i.grid_info()['column'])) < 0:
                            if newcolumn == 0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=0,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn-1,row = newrow)
                        elif (newrow - int(i.grid_info()['row'])) > 0:
                            if newrow != 11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow+1)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 11)
                        else:
                            if newrow ==0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 0)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow-1)
                oldway = 'N'
            else:
                newway = 'S'
        elif newway == 'W':
            if oldway != 'E':    
                newrow = int(snake_head.grid_info()['row'])
                newcolumn = int(snake_head.grid_info()['column'])
                if newcolumn == 0:
                    snake_head.grid_forget()
                    snake_head.grid(row=newrow,column=11)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=newrow,column=11,sticky=W)
                else:
                    snake_head.grid_forget()
                    snake_head.grid(row=newrow,column=newcolumn-1)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=newrow,column=newcolumn-1,sticky=W)
                for i in snakebody:
                    if snakebody.index(i) != 0:
                        if (newcolumn - int(i.grid_info()['column'])) > 0:
                            if newcolumn!=11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn+1,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=11,row = newrow)
                        elif (newcolumn - int(i.grid_info()['column'])) < 0:
                            if newcolumn == 0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=0,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn-1,row = newrow)
                        elif (newrow - int(i.grid_info()['row'])) > 0:
                            if newrow != 11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow+1)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 11)
                        else:
                            if newrow ==0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 0)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow-1)
                oldway = 'W'
            else:
                newway = 'E'
        else:
            if oldway != 'N':
                newrow = int(snake_head.grid_info()['row'])
                newcolumn = int(snake_head.grid_info()['column'])
                if newrow == 11:
                    snake_head.grid_forget()
                    snake_head.grid(row=0,column=newcolumn)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=0,column=newcolumn,sticky=S)
                else:
                    snake_head.grid_forget()
                    snake_head.grid(row=newrow+1,column=newcolumn)
                    snake_eye.grid_forget()
                    snake_eye.grid(row=newrow+1,column=newcolumn,sticky=S)
                for i in snakebody:
                    if snakebody.index(i) != 0:
                        if (newcolumn - int(i.grid_info()['column'])) > 0:
                            if newcolumn!=11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn+1,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=11,row = newrow)
                        elif (newcolumn - int(i.grid_info()['column'])) < 0:
                            if newcolumn == 0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=0,row = newrow)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn-1,row = newrow)
                        elif (newrow - int(i.grid_info()['row'])) > 0:
                            if newrow != 11:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow+1)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 11)
                        else:
                            if newrow ==0:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = 0)
                            else:
                                newrow = int(i.grid_info()['row'])
                                newcolumn =  int(i.grid_info()['column'])
                                i.grid_forget()
                                i.grid(column=newcolumn,row = newrow-1)
                oldway = 'S'
            else:
                newway = 'N'
        movemade = True
        
        if snake_head.grid_info()['row'] == apple.grid_info()['row'] and snake_head.grid_info()['column'] == apple.grid_info()['column']:
            score +=1
            scorelbl.config(text=str(score))
            snake_body = Label(root, text='',bg='dark green',width=6,height=3,border=5,relief=RAISED)
            if newway == 'W':
                if snakebody[-1].grid_info()['column'] !=11:
                    snake_body.grid(row=snakebody[-1].grid_info()['row'],column=snakebody[-1].grid_info()['column']+1)
                else:
                    snake_body.grid(row=snakebody[-1].grid_info()['row'],column=0)
                snakebody.append(snake_body)
            elif newway == 'E':
                if snakebody[-1].grid_info()['column'] !=0:
                    snake_body.grid(row=snakebody[-1].grid_info()['row'],column=snakebody[-1].grid_info()['column']-1)
                else:
                    snake_body.grid(row=snakebody[-1].grid_info()['row'],column=11)
                snakebody.append(snake_body)
            elif newway == 'N':
                if snakebody[-1].grid_info()['row'] !=11:
                    snake_body.grid(row=snakebody[-1].grid_info()['row']+1,column=snakebody[-1].grid_info()['column'])
                else:
                    snake_body.grid(row=0,column=snakebody[-1].grid_info()['column'])
                snakebody.append(snake_body)
            elif newway == 'S':
                if snakebody[-1].grid_info()['row'] !=0:
                    snake_body.grid(row=snakebody[-1].grid_info()['row']-1,column=snakebody[-1].grid_info()['column'])
                else:
                    snake_body.grid(row=11,column=snakebody[-1].grid_info()['column'])
                snakebody.append(snake_body)
            allist = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), 
(10, 10), (10, 11), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)}
            for i in snakebody:
                snaketuple =  (int(i.grid_info()['row']),int(i.grid_info()['column']))
                allist.discard(snaketuple)
            apple.grid_forget()
            chc = choice(list(allist))
            roww = chc[0]
            columnn = chc[1]
            apple.grid(row=roww,column=columnn)
        for i in snakebody:
            if destroyed != True:
                if snakebody.index(i) != 0:
                    if snake_head.grid_info()['row'] == i.grid_info()['row'] and snake_head.grid_info()['column'] == i.grid_info()['column']:
                        gameover = True
                        for i in labellist:
                            i.destroy()
                        for i in snakebody:
                            i.destroy()
                        destroyed = True
                        labellist = []
                        snakebody = []
                        scorelbl.destroy()
                        snake_eye.destroy()
                        apple.destroy()
                        
                        gameoverframe = Frame(root,bg='black')
                        gameoverframe.pack(expand=1,fill=BOTH)
                        root.geometry('810x864')
                        for i in range(9):
                            for j in range(9):
                                if j%2 == 0 and i%2 == 0:
                                    bg_ = '#001840'
                                elif j%2 == 1 and i%2 == 1:
                                    bg_ = '#001840'
                                else: 
                                    bg_ = 'black'
                                labeldot = Label(gameoverframe,text='',bg=f'{bg_}',width=12,height=6,relief=FLAT)
                                alist.append(labeldot)
                        for i in alist:
                            i.grid(row=floor(alist.index(i)/9),column = alist.index(i)%9)
                        root.update()
                        window_width = startinterfaceframe.winfo_width()
                        window_height = startinterfaceframe.winfo_height()
                        screen_width = startinterfaceframe.winfo_screenwidth()
                        screen_height = startinterfaceframe.winfo_screenheight()

                        x = int((screen_width/2) - (window_width/2))
                        y = int((screen_height/2) - (window_height/2))

                        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
                        gameoverlbl = Label(gameoverframe,text='GAME OVER',font=('Bahnschrift SemiLight Condensed',100),bg='black',fg='White',relief=GROOVE,border=5,width=10,height=1)
                        gameoverlbl.place(relx=0.5,rely=0.3,anchor=CENTER)
                        
                        restartbtn = Button(gameoverframe,text='Restart',font=('Bahnschrift SemiBold',40),bg='navy',fg='white',relief=RIDGE,border=4,activebackground='navy',activeforeground='white',command=restart)

                        restartbtn.place(relx=0.3,rely=0.665,anchor=CENTER)

                        mainmenubtn = Button(gameoverframe,text='Main Menu',font=('Bahnschrift SemiBold',40),bg='navy',fg='white',relief=RIDGE,border=4,activebackground='navy',activeforeground='white',command=mainmenu)

                        mainmenubtn.place(relx=0.7,rely=0.665,anchor=CENTER)

                        gameoverframe.update()
                        restartbtn.config(width=ceil(mainmenubtn.winfo_width()/38.25))
    
        root.after(100,gameon)

def waychanger(event):
    global newway
    global movemade
    if event.keysym == 'W' or event.keysym == 'w' or event.keysym == 'Up':
        if movemade == True:
            oldway = newway
            newway = 'N'
            if oldway == newway:
                newway = 'S'
    elif event.keysym == 'A' or event.keysym == 'a' or event.keysym == 'Left':
        if movemade == True:
            oldway = newway
            newway = 'W'
            if oldway == newway:
                newway = 'E'
    elif event.keysym == 'S' or event.keysym == 's' or event.keysym == 'Down':
        if movemade == True:
            oldway = newway
            newway = 'S'
            if oldway == newway:
                newway = 'N'
    else:
        if movemade == True:
            oldway = newway
            newway = 'E'
            if oldway == newway:
                newway = 'W'


root = Tk()
root.resizable(False,False)
root.title('Snake')

def mainmenu():
    global forgotten
    gameoverframe.forget()
    startinterfaceframe.pack(expand=1,fill=BOTH)
    forgotten = False

def restart():
    gameoverframe.forget()
    game()

def startinterface():
    global startinterfaceframe
        

    startinterfaceframe = Frame(root,bg='black')

    startinterfaceframe.pack(expand=1,fill=BOTH)




    snakelbl = Label(startinterfaceframe,text='SNAKE',font=('Bahnschrift SemiLight Condensed',100),bg='light green',fg='WHite',relief=RIDGE,border=10,width=8,height=1)

    snakelbl.place(relx=0.5,rely=0.2,anchor=CENTER)

    playbtn = Button(startinterfaceframe,text='Start',font=('Bahnschrift SemiBold',50),bg='light green',fg='white',relief=RIDGE,border=20,activebackground='light green',activeforeground='white',width=7,command=game)

    playbtn.place(relx=0.5,rely=0.665,anchor=CENTER)



    startinterfaceframe.update()


    for i in range(9):
        for j in range(9):
            if j%2 == 0 and i%2 == 0:
                bg_ = 'dark gray'
            elif j%2 == 1 and i%2 == 1:
                bg_ = 'dark gray'
            else: 
                bg_ = 'gray'
            labeldot = Label(startinterfaceframe,text='',bg=f'{bg_}',width=12,height=6,relief=FLAT)
            alist.append(labeldot)
    for i in alist:
        i.grid(row=floor(alist.index(i)/9),column = alist.index(i)%9)

        

    playbtn.lift()
    snakelbl.lift()

def game():
    global forgotten
    global snake_body0
    global snake_body1
    global snake_eye
    global snake_head
    global snakebody
    global apple
    global gameover
    global score
    global scorelbl
    global movemade
    global destroyed
    global newway

    score = 0
    newway = 'E'
    movemade = False


    if forgotten != True:
        startinterfaceframe.pack_forget()
        forgotten == True
    root.geometry('744x792')
    root.update()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    for i in range(12):
        for j in range(12):
            if j%2 == 0 and i%2 == 0:
                bg_ = 'gray'
            elif j%2 == 1 and i%2 == 1:
                bg_ = 'gray'
            else: 
                bg_ = 'light gray'
            labeldot = Label(root,text='',bg=f'{bg_}',width=8,height=4,relief=FLAT)
            labellist.append(labeldot)
    for i in labellist:
        i.grid(row=floor(labellist.index(i)/12),column = labellist.index(i)%12)
    apple = Label(root,text='',bg='red',width=2,height=1,border=8,relief=RAISED)
    root.update()
    chc = choice(list(allist))
    roww = chc[0]
    columnn = chc[1]
    apple.grid(row=roww,column=columnn)

    scorelbl = Label(root,text=str(score),bg='light gray',font=('Agency fb',18))
    scorelbl.grid(row=0,column=11)
    
    apple.lift()

    #creating the snake
    snake_head = Label(root, text='',bg='dark green',width=6,height=3,border=5,relief=RAISED)
    snake_body0 = Label(root, text='',bg='dark green',width=6,height=3,border=5,relief=RAISED)
    snake_body1 = Label(root, text='',bg='dark green',width=6,height=3,border=5,relief=RAISED)
        
    snake_eye = Label(root,text = '',bg = 'black',width=1,height=1)
    snake_eye.grid(row=2,column=4,sticky=E)
    
    snake_body1.grid(row=2,column=2)
    snake_body0.grid(row=2,column=3)
    snake_head.grid(row=2,column=4)

    snakebody.append(snake_head)
    snakebody.append(snake_body0)
    snakebody.append(snake_body1)
    
    destroyed = False
    gameover = False
    root.after(100,gameon())


startinterface()

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


root.bind('<Left>',waychanger)
root.bind('<Right>',waychanger) 
root.bind('<w>',waychanger)
root.bind('<a>',waychanger)
root.bind('<s>',waychanger)
root.bind('<d>',waychanger)
root.bind('<W>',waychanger)
root.bind('<A>',waychanger)
root.bind('<S>',waychanger)
root.bind('<D>',waychanger)
root.bind('<Up>',waychanger)
root.bind('<Down>',waychanger)

root.mainloop()



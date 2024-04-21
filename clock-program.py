from tkinter import * 
from time import *


def checkerk():
    global checksaat
    checksaat = False
    kmb.config(state='disabled',relief=SUNKEN,background='dark gray')
    ysa.config(state=NORMAL,relief=SOLID,background='light gray')
    #ssb.config(state=NORMAL,relief=SOLID,background='light gray')
    openkronometre()


def checkers():
    global checksaat
    global checkkronometre
    if checkkronometre == True:
        kronometreframe.place_forget()
    checkkronometre = False
    checksaat = True
    ysa.config(state='disabled',relief=SUNKEN,background='dark gray')
    kmb.config(state=NORMAL,relief=SOLID,background='light gray')
    #ssb.config(state=NORMAL,relief=SOLID,background='light gray')
    ysupdate()
    for j in turlabel:
        j.place_forget()

def openkronometre():
    global sayaç
    global checkkronometre
    global labelindex
    checkkronometre = True
    sayaç = f'{saat}:{dakika}.{saniye}'
    sl.config(text=sayaç)
    if slon == False:
        sl.place(anchor=CENTER,relx=0.5,rely=0.45)
        slon == True
    
    kronometreframe.place(relx=0.48,rely=0.63,anchor=CENTER)
    kronometreframe.lift()
    if turindexler != []:
        for i in turlabel:
            a = turlabel.index(i)
            if a >= 9 and a < 18:
                relyt = 0.7
                relyt += (a - 9) * 0.035
                i.place(relx=0.44599,rely=relyt,anchor=CENTER)
            elif a >= 18 and a <27:    
                relyt = 0.7
                relyt += (a - 18) * 0.035
                i.place(relx=0.53599,rely=relyt,anchor=CENTER)
            elif a >= 27:
                relyt = 0.7
                relyt += (a - 27) * 0.035
                i.place(relx=0.62599,rely=relyt,anchor=CENTER)
            else:
                relyt = 0.7
                relyt += a * 0.035
                i.place(relx=0.35599,rely=relyt,anchor=CENTER)



def ysupdate():
    global datenow
    global timenow
    if checksaat == True:
        datenow = strftime('%d.%m.%Y')
        if strftime('%m')[0] == '0':
            month = strftime('%m')[1]
            datenow = strftime(f'%d.{month}.%Y')
        timenow = strftime('%H:%M:%S')
        sl.config(text=timenow)
        if slon == False:
            sl.place(anchor=CENTER,relx=0.5,rely=0.45)
            slon == True
        datel.config(text=datenow)
        window.after(1000,ysupdate)
    

def kronometrestart():
    global kronometreaktif
    global stop
    global resetpacked
    start.pack_forget()
    reset.pack(side=RIGHT,padx=10)
    resetpacked = True
    stop = Button(kronometreframe,
               text='Durdur', font = ('Bahnschrift SemiLight SemiCondensed',30),bg='light gray',command=kronometredurdur)
    stop.pack(side=LEFT,padx=10)
    kronometreaktif = True
    kronometreupdate()


    
def kronometreupdate():
    global sayaç
    global saniye
    global saat
    global dakika
    global kronometreaktif
    global kronometrecalisiyor 
    sleep(1)   
    if kronometreaktif == True:
        saniye = str(1 + int(saniye))
        if int(saniye) < 10:
            saniye = f'0{saniye}'
        if saniye == '60':
            dakika = str(1 + int(dakika))
            if int(dakika) < 10:
                dakika = f'0{dakika}'
            saniye = '00'
            if dakika == 60:
                saat = str(1 + int(saat))
                dakika = '00'
        sayaç = f'{saat}:{dakika}.{saniye}'
        sl.config(text=sayaç)
        if slon == False:
            sl.place(anchor=CENTER,relx=0.5,rely=0.45)
            slon == True
        window.after(1000,kronometreupdater)
        kronometrecalisiyor = True
    else:
        kronometreaktif = False

def kronometreupdater():
    global sayaç
    global saniye
    global saat
    global dakika
    global kronometreaktif
    global kronometrecalisiyor   
    if kronometreaktif == True:
        saniye = str(1 + int(saniye))
        if int(saniye) < 10:
            saniye = f'0{saniye}'
        if saniye == '60':
            dakika = str(1 + int(dakika))
            if int(dakika) < 10:
                dakika = f'0{dakika}'
            saniye = '00'
            if dakika == 60:
                saat = str(1 + int(saat))
                dakika = '00'
        sayaç = f'{saat}:{dakika}.{saniye}'
        if checksaat == False:
            sl.config(text=sayaç)
        if slon == False:
            sl.place(anchor=CENTER,relx=0.5,rely=0.45)
            slon == True
        window.after(1000,kronometreupdater)

def kronometredurdur():
    global kronometreaktif
    kronometreaktif = False
    stop.pack_forget()
    start.config(text='Devam et')
    start.pack(side=LEFT,padx=10)
    
def turolustur():
    global turlar
    global turindex
    global relyt
    global labelindex
    global turlabel
    global reset
    global resetpacked
    turlar.append(sayaç)
    labelindex = turindex
    if resetpacked == False:
        reset.pack(side=RIGHT,padx=10)
        resetpacked = True
    if turindex >= 9 and turindex < 18:
        relyt = 0.7
        relyt += (turindex - 9) * 0.035
        labelindex =Label(window,text = f'{turindex+1}. {turlar[turindex]}',
          bg='dark gray',font=('agency fb',18))
        labelindex.place(relx=0.44599,rely=relyt,anchor=CENTER)
    elif turindex >= 18 and turindex <27:    
        relyt = 0.7
        relyt += (turindex - 18) * 0.035
        labelindex =Label(window,text = f'{turindex+1}. {turlar[turindex]}',
          bg='dark gray',font=('agency fb',18))
        labelindex.place(relx=0.53599,rely=relyt,anchor=CENTER)
    elif turindex >= 27:
        relyt = 0.7
        relyt += (turindex - 27) * 0.035
        labelindex =Label(window,text = f'{turindex+1}. {turlar[turindex]}',
          bg='dark gray',font=('agency fb',18))
        labelindex.place(relx=0.62599,rely=relyt,anchor=CENTER)
        if turindex >= 35:
            tur.config(state=DISABLED,bg='dark gray',relief=GROOVE)
    else:
        relyt = 0.7
        relyt += turindex * 0.035
        labelindex = Label(window,text = f'{turindex+1}. {turlar[turindex]}',
            bg='dark gray',font=('agency fb',18))
        labelindex.place(relx=0.35599,rely=relyt,anchor=CENTER)
    turlabel.append(labelindex)
    turindexler.append(turindex)
    turindex +=1


def sifirla():
    global saniye
    global dakika
    global saat
    global turlar
    global turindex
    global relyt
    global checkkronometre
    global kronometrecalisiyor
    global sayaç
    global sl
    global labelindex
    global turlabel
    global kronometreaktif
    global reset
    global resetpacked
    global stop
    turlar = []
    relyt = 0.7
    saniye = '00'
    dakika = '00'
    saat = '0'
    checkkronometre = False
    kronometrecalisiyor = False
    sayaç = f'{saat}:{dakika}.{saniye}'
    sl.config(text=sayaç)
    if slon == False:
        sl.place(anchor=CENTER,relx=0.5,rely=0.45)
        slon == True
    for j in turlabel:
        j.place_forget()
    turlabel = []
    if turindex >= 35:
        tur.config(state='normal',bg='light gray',relief=RAISED)
    turindex = 0
    kronometreaktif = False
    try:stop.pack_forget() 
    except:pass
    start.config(text='Başlat')
    start.pack(side=LEFT,padx=10)
    reset.pack_forget()
    resetpacked = False
"""    
def sdsecici():
    global slon
    global saatdilimleri
    global checksaat
    checksaat = False
    sl.place_forget()
    kronometreframe.place_forget()
    slon = False
    kmb.config(state=NORMAL,relief=SOLID,background='light gray')
    ysa.config(state=NORMAL,relief=SOLID,background='light gray')
    ssb.config(state=DISABLED,relief=SUNKEN,background='dark gray')
    for i in saatdilimleri:
        sdl = str(i)+'label'
        sdl = Button(window,text=f'GMT {sdl}')
        dilimlabel.append(sdl)
    for j in turlabel:
        j.place_forget()
"""


turlar = []
turlabel = []
turindex = 0
turindexler = []
relyt = 0.7
resetpacked = False
saniye = '00'
dakika = '00'
saat = '0'
checkkronometre = False
kronometrecalisiyor = False
saatdilimleri = [-12,-11,-10,-9,-8,-7,6,-5,4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
dilimlabel = []
slon = True

datenow = strftime('%d.%m.%Y')
if strftime('%m')[0] == '0':
    month = strftime('%m')[1]
    datenow = strftime(f'%d.{month}.%Y')
timenow = strftime('%H:%M:%S')


window = Tk()

photo = PhotoImage(file='clock.png')

window.title('Saat')
window.iconphoto(False,photo)
window.geometry('1920x1080')
window.config(background='dark gray')
window.state('zoomed')

frame = Frame(window,bg='dark gray')
frame.pack(anchor=NW,pady=10)

ysa = Button(frame,
            text='Yerel Saat',font= ('agency fb',23),bg='light gray',relief=SOLID
            ,activebackground='dark gray',command=checkers)

kmb = Button(frame,
             text='Kronometre', font= ('agency fb',23),bg='light gray',relief=SOLID
            ,activebackground='dark gray',command=checkerk)
"""
ssb = Button(frame,
             text='Saat Dilimi Seçme', font= ('agency fb',23),bg='light gray',relief=SOLID
            ,activebackground='dark gray',command=sdsecici)
"""

ysa.pack(side=LEFT,padx=10)
kmb.pack(side=LEFT)
#ssb.pack(side=LEFT,padx=10)

kronometreframe = Frame(window, bg = 'dark gray')

start = Button(kronometreframe,
               text='Başlat', font = ('Bahnschrift SemiLight SemiCondensed',30),bg='light gray',command=kronometrestart)

tur = Button(kronometreframe,
             text='Tur',font = ('Bahnschrift SemiLight SemiCondensed',30),bg='light gray',command=turolustur)

reset = Button(kronometreframe,
               text='Sıfırla', font = ('Bahnschrift SemiLight SemiCondensed',30),bg='light gray',command=sifirla)




start.pack(side=LEFT,padx=10)
tur.pack(side=RIGHT,padx=10,ipadx=16)


sl = Label(window,
               text=timenow, font= ('Tw Cen MT',178),bg = 'dark gray',fg = '#0047AB',width=0,pady=5)

datel = Label(window,
               text=datenow, font= ('agency fb',45),bg = 'dark gray', fg ='#0060AB',width=0)


sl.place(anchor=CENTER,relx=0.5,rely=0.45)
datel.place(x=1275,y=970,anchor=SE)


ysa.config(state='disabled',relief=SUNKEN,background='dark gray')
checkers()

window.mainloop()
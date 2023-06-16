import tkinter as tk
import itertools
import random

w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

evilboat=[]
goodboat=[]
spots=[]

def visBoat(occupied):
    bord=[]
    prnt = ''

    for j in range(0,10):
        for i in range(0,10):
            pnt='.'
            for k in occupied:
                if k[0]==i and k[1]==j:
                    pnt = 'x'
            prnt = ''.join((prnt,pnt))
        prnt = ''.join((prnt,'\n'))
    print(prnt)

    pirt = prnt.split('\n')


    for k in range(10):
        for (i,j) in itertools.zip_longest(pirt[k],range(len(pirt[k]))):
            if i=='.':
                bord.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#0000bb'))
            if i=='x':
                bord.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#808080'))
            else:
                pass

def vilBoat(occupied):
    global spots
    bord=[]
    prnt = ''

    for j in range(0,10):
        for i in range(0,10):
            pnt='.'
            for k in occupied:
                if k[0]==i and k[1]==j:
                    pnt = 'x'
            prnt = ''.join((prnt,pnt))
        prnt = ''.join((prnt,'\n'))
    print(prnt)

    pirt = prnt.split('\n')
    spots = pirt


    for k in range(10):
        for (i,j) in itertools.zip_longest(pirt[k],range(len(pirt[k]))):
            if i=='.':
                bord.append(c.create_rectangle(400+j*31,0+k*31,431+j*31,31+k*31,fill='#0000bb'))
            if i=='x':
                bord.append(c.create_rectangle(400+j*31,0+k*31,431+j*31,31+k*31,fill='#808080'))
            else:
                pass

def check(list0,allCor):

    for i in list0:
        for x in i:
            if x==10 or x==-1:
                return True
        if i in allCor:
            return True
    return False

def cordcheck(coordinate):
    cord=[]

    try:
        if coordinate[0] == 'A' or coordinate[0] == 'a':
            cord.append(0)
        if coordinate[0] == 'B' or coordinate[0] == 'b':
            cord.append(1)
        if coordinate[0] == 'C' or coordinate[0] == 'c':
            cord.append(2)
        if coordinate[0] == 'D' or coordinate[0] == 'd':
            cord.append(3)
        if coordinate[0] == 'E' or coordinate[0] == 'e':
            cord.append(4)
        if coordinate[0] == 'F' or coordinate[0] == 'f':
            cord.append(5)
        if coordinate[0] == 'G' or coordinate[0] == 'g':
            cord.append(6)
        if coordinate[0] == 'H' or coordinate[0] == 'h':
            cord.append(7)
        if coordinate[0] == 'I' or coordinate[0] == 'i':
            cord.append(8)
        if coordinate[0] == 'J' or coordinate[0] == 'j':
            cord.append(9)

        coordinate = coordinate.replace(' ', '')

        if coordinate[1]=='1':
            try:
                if coordinate[2]=='0':
                    cord.append(9)
            except:
                cord.append(0)
        else:
            cord.append(int(coordinate[1])-1)
        return True
    except:
        return False

def convert(coordinate,direction):
    cords = []
    cord = []

    if coordinate[0] == 'A' or coordinate[0] == 'a':
        cord.append(0)
    if coordinate[0] == 'B' or coordinate[0] == 'b':
        cord.append(1)
    if coordinate[0] == 'C' or coordinate[0] == 'c':
        cord.append(2)
    if coordinate[0] == 'D' or coordinate[0] == 'd':
        cord.append(3)
    if coordinate[0] == 'E' or coordinate[0] == 'e':
        cord.append(4)
    if coordinate[0] == 'F' or coordinate[0] == 'f':
        cord.append(5)
    if coordinate[0] == 'G' or coordinate[0] == 'g':
        cord.append(6)
    if coordinate[0] == 'H' or coordinate[0] == 'h':
        cord.append(7)
    if coordinate[0] == 'I' or coordinate[0] == 'i':
        cord.append(8)
    if coordinate[0] == 'J' or coordinate[0] == 'j':
        cord.append(9)

    coordinate = coordinate.replace(' ', '')

    if coordinate[1]=='1':
        try:
            if coordinate[2]=='0':
                cord.append(9)
        except:
            cord.append(0)
    else:
        cord.append(int(coordinate[1])-1)

    if direction == 'up' or direction == 'down':
        for i in range(5):
            cords.append([cord[0],cord[1]+i])
    if direction == 'right' or direction == 'left':
        for i in range(5):
            cords.append([cord[0]+i,cord[1]])

    return cords

def attackLoc(coordinate):
    cord = []

    if coordinate[0] == 'A' or coordinate[0] == 'a':
        cord.append(0)
    if coordinate[0] == 'B' or coordinate[0] == 'b':
        cord.append(1)
    if coordinate[0] == 'C' or coordinate[0] == 'c':
        cord.append(2)
    if coordinate[0] == 'D' or coordinate[0] == 'd':
        cord.append(3)
    if coordinate[0] == 'E' or coordinate[0] == 'e':
        cord.append(4)
    if coordinate[0] == 'F' or coordinate[0] == 'f':
        cord.append(5)
    if coordinate[0] == 'G' or coordinate[0] == 'g':
        cord.append(6)
    if coordinate[0] == 'H' or coordinate[0] == 'h':
        cord.append(7)
    if coordinate[0] == 'I' or coordinate[0] == 'i':
        cord.append(8)
    if coordinate[0] == 'J' or coordinate[0] == 'j':
        cord.append(9)

    coordinate = coordinate.replace(' ', '')

    if coordinate[1]=='1':
        try:
            if coordinate[2]=='0':
                cord.append(9)
        except:
            cord.append(0)
    else:
        cord.append(int(coordinate[1])-1)

    return cord

def enemy():
    global evilboat
    for i in range(5):
        while True:
            let=['a','b','c','d','e','f','g','h','i','j']
            randlet=random.choice(let)
            randnum=random.randint(0,9)
            randdir=random.randint(0,1)
            if i == 0:
                j=3
            if i == 1 or i == 2:
                j=2
            if i == 3:
                j=1
            if i == 4:
                j=0
            if randdir==0:
                dir='up'
            if randdir==1:
                dir='right'
            randcord=f'{randlet}{randnum}'
            eneLoc=convert(randcord,dir)
            eneShip = eneLoc[: len(eneLoc) - j]
            if check(eneShip,evilboat)==False:
                break
        evilboat.extend(eneShip)
        vilBoat([])

def allie():
    global goodboat
    for i in range(5):
        while True:
            if i == 0:
                j=3
            if i == 1 or i == 2:
                j=2
            if i == 3:
                j=1
            if i == 4:
                j=0
            allDir = input(f'boat{5-j} Direciton: ')
            allLoc = input(f'boat{5-j} First Coord: ')
            if allDir == 'up' or allDir == 'down' or allDir == 'right' or allDir == 'left':
                pass
            else:
                continue
            if cordcheck(allLoc) == False:
                continue
            alliLoc=convert(allLoc,allDir)
            allShip = alliLoc[: len(alliLoc) - j]
            if check(allShip,goodboat)==False:
                break
        goodboat.extend(allShip)
        visBoat(goodboat)

def kiling():
    a=0
    while True:
        atk=input('attack cord: ')
        boom=(spots[(attackLoc(atk))[1]])[(attackLoc(atk))[0]]
        if boom =='x':
            print('hit')
            a+=1
            c.create_rectangle(400+(attackLoc(atk))[0]*31,0+(attackLoc(atk))[1]*31,431+(attackLoc(atk))[0]*31,31+(attackLoc(atk))[1]*31,fill='#bb0000')
        if boom =='.':
            print('miss')
            c.create_rectangle(400+(attackLoc(atk))[0]*31,0+(attackLoc(atk))[1]*31,431+(attackLoc(atk))[0]*31,31+(attackLoc(atk))[1]*31,fill='#ffffff')
        if a==17:
            print('you win')
            break

visBoat([])
vilBoat([])
allie()
enemy()
kiling()

w.mainloop()
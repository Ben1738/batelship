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

visBoat([])
allie()
enemy()
'''while True:
    a=False
    tugDir = input('Tugboat(2) Direciton: ')
    tugLoc = input('Tugboat(2) First Coord: ')
    tugLocCon = convert(tugLoc,tugDir)
    tugBoat = tugLocCon[: len(tugLocCon) - 3]
    if check(tugBoat,[])==False:
        break
print(str(tugBoat))
visBoat(tugBoat)
while True:
    a=False
    sumDir = input('Sumbarine(3) Direciton: ')
    sumLoc = input('Sumbarine(3) First Coord: ')
    sumLocCon = convert(sumLoc,sumDir)
    sumBoat = sumLocCon[: len(sumLocCon) - 2]
    if check(sumBoat,tugBoat)==False:
        break
print(str(sumBoat))
tugBoat.extend(sumBoat)
visBoat(tugBoat)
while True:
    a=False
    desDir = input('Destroyer(3) Direciton: ')
    desLoc = input('Destroyer(3) First Coord: ')
    desLocCon = convert(desLoc,desDir)
    desBoat = desLocCon[: len(desLocCon) - 2]
    if check(desBoat,tugBoat)==False:
        break
print(str(desBoat))
tugBoat.extend(desBoat)
visBoat(tugBoat)
while True:
    a=False
    carDir = input('Carrier(4) Direciton: ')
    carLoc = input('Carrier(4) First Coord: ')
    carLocCon = convert(carLoc,carDir)
    carBoat = carLocCon[: len(carLocCon) - 1]
    if check(carBoat,tugBoat)==False:
        break
print(str(carBoat))
tugBoat.extend(carBoat)
visBoat(tugBoat)
while True:
    a=False
    batDir = input('Battleship(4) Direciton: ')
    batLoc = input('Battleship(4) First Coord: ')
    batLocCon = convert(batLoc,batDir)
    batBoat = batLocCon[: len(batLocCon)]
    if check(batBoat,tugBoat)==False:
        break
print(str(batBoat))
tugBoat.extend(batBoat)
visBoat(tugBoat)'''


w.mainloop()
import tkinter as tk
import itertools

w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

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

def check(list0):

    for i in list0:
        for x in i:
            if x==10 or x==-1:
                return True
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
            cords.append([cord[0]+i,cord[1]])
    if direction == 'right' or direction == 'left':
        for i in range(5):
            cords.append([cord[0],cord[1]+i])

    return cords
visBoat([])
while True:
    a=False
    tugDir = input('Tugboat(2) Direciton: ')
    tugLoc = input('Tugboat(2) First Coord: ')
    tugLocCon = convert(tugLoc,tugDir)
    tugBoat = tugLocCon[: len(tugLocCon) - 3]
    if check(tugBoat)==False:
        break
print(str(tugBoat))
visBoat(tugBoat)
while True:
    a=False
    sumDir = input('Sumbarine(3) Direciton: ')
    sumLoc = input('Sumbarine(3) First Coord: ')
    sumLocCon = convert(sumLoc,sumDir)
    sumBoat = sumLocCon[: len(sumLocCon) - 2]
    if check(sumBoat)==False:
        break
print(str(sumBoat))
tugBoat.extend(sumBoat)
visBoat(tugBoat)


w.mainloop()
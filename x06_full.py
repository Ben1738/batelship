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
spoots=[]

tugg=[]
subg=[]
desg=[]
carg=[]
batg=[]
allg = []
tugb=[]
subb=[]
desb=[]
carb=[]
batb=[]
allb=[]

def visBoat(occupied):
    global spoots
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
    spoots=pirt


    for k in range(10):
        for (i,j) in itertools.zip_longest(pirt[k],range(len(pirt[k]))):
            if i=='.':
                bord.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#0000bb'))
            if i=='x':
                bord.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#800080'))
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
                bord.append(c.create_rectangle(400+j*31,0+k*31,431+j*31,31+k*31,fill='#0000bb'))
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
    global tugb
    global subb
    global desb
    global carb
    global batb
    global allb
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
        if i == 0:
            tugb.append(eneLoc)
        if i == 1:
            subb.append(eneLoc)
        if i == 2:
            desb.append(eneLoc)
        if i == 3:
            carb.append(eneLoc)
        if i == 4:
            batb.append(eneLoc)
        allb = tugb,subb,desb,carb,batb

        evilboat.extend(eneShip)
        vilBoat(evilboat)

def allie():
    global goodboat
    global tugg
    global subg
    global desg
    global carg
    global batg
    global allg
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
        if i == 0:
            tugg.append(alliLoc)
        if i == 1:
            subg.append(alliLoc)
        if i == 2:
            desg.append(alliLoc)
        if i == 3:
            carg.append(alliLoc)
        if i == 4:
            batg.append(alliLoc)
        allg = tugg,subg,desg,carg,batg
        goodboat.extend(allShip)
        visBoat(goodboat)

def sunk(hit,alls):
    if hit in alls[0][0]:
        return 't'
    if hit in alls[1][0]:
        return 's'
    if hit in alls[2][0]:
        return 'd'
    if hit in alls[3][0]:
        return 'c'
    if hit in alls[4][0]:
        return 'b'

def sinky(who,tug,sub,des,car,bat):
    if tug == 2:
        print(f'{who} tugboat sunk')
    if sub == 3:
        print(f'{who} submairne sunk')
    if des == 3:
        print(f'{who} destroiyer sunk')
    if car == 4:
        print(f'{who} carrier sunk')
    if bat == 5:
        print(f'{who} battleship sunk')
    return


def kiling():
    global allg
    global allb
    repeat=[]
    a=0
    b=0
    tugc=0
    subc=0
    desc=0
    carc=0
    batc=0
    tugs=0
    subs=0
    dess=0
    cars=0
    bats=0
    while True:
        atk=input('attack cord: ')
        if cordcheck(atk) == False:
            continue
        try:
            boom=(spots[(attackLoc(atk))[1]])[(attackLoc(atk))[0]]
        except:
            continue
        if boom =='x':
            print('you hit')
            a+=1
            goodhit = [(attackLoc(atk))[0],(attackLoc(atk))[1]]
            c.create_rectangle(400+(attackLoc(atk))[0]*31,0+(attackLoc(atk))[1]*31,431+(attackLoc(atk))[0]*31,31+(attackLoc(atk))[1]*31,fill='#bb0000')
            if sunk(goodhit,allb) == 't':
                tugs+=1
            if sunk(goodhit,allb) == 's':
                subs+=1
            if sunk(goodhit,allb) == 'd':
                dess+=1
            if sunk(goodhit,allb) == 'c':
                cars+=1
            if sunk(goodhit,allb) == 'b':
                bats+=1
            sinky('enemy',tugs,subs,dess,cars,bats)
        if boom =='.':
            print('you miss')
            c.create_rectangle(400+(attackLoc(atk))[0]*31,0+(attackLoc(atk))[1]*31,431+(attackLoc(atk))[0]*31,31+(attackLoc(atk))[1]*31,fill='#ffffff')
        
        while True:
            randx=random.randint(0,9)
            randy=random.randint(0,9)
            bam=(spoots[randy])[randx]
            if [randx,randy] in repeat:
                continue
            repeat.append([randx,randy])
            break
        if bam =='x':
            print('enemy hit')
            b+=1
            badhit = [randx,randy]
            c.create_rectangle(0+randx*31,0+randy*31,31+randx*31,31+randy*31,fill='#bb0000')
            if sunk(badhit,allg) == 't':
                tugc+=1
            if sunk(badhit,allg) == 's':
                subc+=1
            if sunk(badhit,allg) == 'd':
                desc+=1
            if sunk(badhit,allg) == 'c':
                carc+=1
            if sunk(badhit,allg) == 'b':
                batc+=1
            sinky('your',tugc,subc,desc,carc,batc)
        if bam =='.':
            print('enemy miss')
            c.create_rectangle(0+randx*31,0+randy*31,31+randx*31,31+randy*31,fill='#ffffff')
        


        if b==17:
            print('you lose')
            break
        if a==17:
            print('you win')
            break

visBoat([])
vilBoat([])
allie()
enemy()
kiling()

w.mainloop()
import tkinter as tk
import itertools    

w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

bord=[]
occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]
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

w.mainloop()
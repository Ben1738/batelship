import tkinter as tk

w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

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

    return cords

tugDir = input('Tugboat(2) Direciton: ')
tugLoc = input('Tugboat(2) First Coord: ')
tugLocCon = convert(tugLoc,tugDir)
print(str(tugLocCon))


w.mainloop()
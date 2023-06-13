#!python3

'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''

def create(dir,x,y):
  '''
  You will need to specify what information you need as inputs, but the output should be a list
  Add whatever code you need for each of your different ships to specify what coordinates it
  occupies and/or whether it is vertical/horizontal
  '''
  output = [
    { "name" : "Tugboat", "size" : 2, "direction" : dir , "starting coordinate" : [x,y] },
    { "name" : "Sumbarine", "size" : 3, "direction" : dir , "coordinates" : [x,y] },
    { "name" : "Destroyer", "size" : 3, "direction" : dir , "coordinates" : [x,y] },
    { "name" : "Carrier", "size" : 4, "direction" : dir , "coordinates" : [x,y] },
    { "name" : "Battelship", "size" : 5, "direction" : dir , "coordinates" : [x,y] }
    ]
  return output

print(create("up",1,2))
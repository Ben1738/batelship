#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """
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


if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  

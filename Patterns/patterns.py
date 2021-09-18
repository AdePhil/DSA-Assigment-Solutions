
'''
Questions: 
https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/edit/main/assignments/9-patterns.md
'''

def pattern1(n):
  print("\npattern 1 \n")
  for row in range(0, n):
    for col in range(0, n):
      print("*", end =" ")
    print()
  

def pattern2(n):
  print("\npattern 2 \n")
  for row in range(0, n):
    for col in range(0, row + 1):
      print("*", end =" ")
    print()

def pattern3(n):
  print("\npattern 3 \n")
  for row in range(0, n):
    for col in range(0, n - row):
      print("*", end =" ")
    print()

def pattern4(n):
  print("\npattern 4 \n")
  for row in range(0, n):
    for col in range(0, row + 1):
      print(col + 1, end =" ")
    print()

def pattern5(n):
  print("\npattern 5 \n")
  for row in range(0, 2 * n):
    colLength = row + 1 if row < n else n - (row - n)
    for col in range(0, colLength):
      print("*", end =" ")
    print()

def pattern6(n):
  print("\npattern 6 \n")
  for row in range(0, n):
    # spaces
    for s in range(0, n-row + 1):
      print(" ",end =" ")
    for col in range(0, row + 1):
      print("*", end =" ")
    print()

def pattern7(n):
  print("\npattern 7 \n")
  for row in range(0, n):
    # spaces
    for s in range(0, row):
      print(" ",end =" ")
    for col in range(0, n - row):
      print("*", end =" ")
    print()

def pattern8(n):
  print("\npattern 8 \n")
  for row in range(0, n):
    # spaces
    for s in range(0, n - row + 1):
      print(" ",end =" ")
    for col in range(0, 2 * row + 1):
      print("*", end =" ")
    print()


def pattern9(n):
  print("\npattern 9 \n")
  for row in range(0, n):
    # spaces
    for s in range(0, row):
      print(" ",end =" ")
    colLength =  2 * (n - row)  -  1
    for col in range(0, colLength):
      print("*", end =" ")
    print()


def pattern10(n):
  print("\npattern 10 \n")
  for row in range(0, n):
    # spaces
    for s in range(0, n - row - 1):
      print(" ",end =" ")
    for col in range(0, row + 1):
      print(" * ", end =" ")
    print()

def pattern11(n):
  print("\npattern 11 \n")
  for row in range(0, n):
    # spaces
    for s in range(0, row):
      print(" ",end =" ")
    for col in range(0, n - row):
      print(" * ", end =" ")
    print()

def pattern12(n):
  print("\npattern 12 \n")
  for row in range(0,  2 * n):
    # spaces
    spacesLength = row if row < n else n - (row - n) - 1
    for s in range(0, spacesLength):
      print(" ",end =" ")
    colLength = n - row if row < n else (row - n) + 1
    for col in range(0, colLength):
      print(" * ", end =" ")
    print()


def pattern13(n):
  print("\npattern 12 \n")
  for row in range(0,  2 * n):
    # spaces
    for s in range(0, n - row):
      print(" ",end =" ")
    colLength = n - row if row < n else (row - n) + 1
    for col in range(0, colLength):
      print(" * ", end =" ")
    print()


def pattern17(n):
  print("\npattern 17 \n")
  for row in range(0,  2 * n):
    # spaces
    spaceLength = n - row if row < n else row - n + 2
    for s in range(0, spaceLength):
      print(" ",end =" ")
    colLength = row if row < n else n - (row - n + 2);
    for col in range(colLength, -1, -1):
      print(col + 1, end =" ")
    for col in range(2, colLength + 2):
      print(col, end =" ")
    print()

def pattern20(n):
  print("\npattern 20 \n")
  for row in range(0, n):
    colLength = n
    for col in range(0, colLength):
      string = '*'
      if not (row == 0 or row == n-1) and not (col == 0 or col == colLength - 1):
        string = ' '
      print(string, end='')
    print()

def pattern21(n):
  print("\npattern 21 \n")
  lastEnd, length = -1, 1
  for row in range(0, n):
    for col in range(lastEnd + 1, length):
      print(col + 1, end =" ")
    lastEnd = col
    length = lastEnd + 1 + row + 2
    print()

def pattern22(n):
  print("\npattern 22 \n")
  lastValue = 1
  for row in range(0, n):
    lastValue =  1 if row % 2 == 0 else 0
    for col in range(0, row + 1):
      print(lastValue, ' ', end='')
      lastValue = 1 if lastValue == 0 else 0
    print()

pattern1(5)
pattern2(5)
pattern3(5)
pattern4(5)
pattern5(5)
pattern6(5)
pattern7(5)
pattern8(5)
pattern9(5)
pattern10(5)
pattern11(5)
pattern12(5)
pattern17(5)
pattern20(5)
pattern21(5)
pattern22(5)
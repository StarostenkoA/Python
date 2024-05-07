SPACE = ' '
STRAR = '*'

rows = int(input("Enter num rows (3-20):"))
spaces = rows-1
stars = 1

for i in range(rows):
    print(
        (SPACE*spaces) +
        (STRAR*stars) +
        (SPACE*spaces)
    )
    stars += 2
    spaces -= 1

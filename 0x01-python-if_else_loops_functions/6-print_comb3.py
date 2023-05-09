#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i != j and not (i == 0 and j == 1):
            if i == 0:
                print("{:d}{:d}, ".format(i, j), end='')
            else:
                print("{:02d}, ".format(int(str(i)+str(j))), end='')
print("99\n", end='')

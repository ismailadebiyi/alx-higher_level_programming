#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i == 8):
            if(i < j):
                print(f"{i}{j}")
        elif (i < j):
            print(f"{i}{j},", end=" ")

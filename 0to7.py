# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for i in range(0,51):
    if (i-1) >= 7:
        break
    print(i,end=" ")

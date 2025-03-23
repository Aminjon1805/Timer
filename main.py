import time
import winsound

print("*********************")
print("*    T I M E R      *")
print("*********************")

set_time = int(input("Set time: "))

for i in range(set_time, 0, -1):
    second = i % 60
    minute = int(i / 60) % 60
    hour = int(i / 3600)




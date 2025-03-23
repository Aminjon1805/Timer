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

    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("\nTIME's UP")
for i in range(0, 10):
    winsound.Beep(1000, 500)



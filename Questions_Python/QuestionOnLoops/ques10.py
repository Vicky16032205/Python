import time

sec = 1
for i in range(1, 6):
    print("Time slept : ",sec,"sec")
    time.sleep(sec)
    sec *= 2
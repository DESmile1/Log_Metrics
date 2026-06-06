import time
import random

levels = ["INFO", "WARN", "ERROR"]
while True:
    with open("app.log", "a") as f:
        level = random.choice(levels)
        f.write(f"{time.ctime()} [{level}] System event occured\n")
        f.flush()
    time.sleep(1)
import os
from time import sleep

# Variables
storage = []


def Clear():
    os.system('cls')


def input_user():
    username = ""
    while not username:
        temp = input(" [+] Enter your gmail username (Before the @): ")
        if "@" in temp:
            Clear()
            print(" [+] Error! Please, just enter the part before the @")
            sleep(1.5)
        else:
            Clear()

            username = temp
    return username


def mix_up(obj, init_pos):
    global storage
    temp = ""
    for i in range(init_pos, len(obj)):
        temp = obj[:i] + "." + obj[i:]
        if temp not in storage:
            if ".." not in temp:
                storage.append(temp)
                mix_up(temp, init_pos+2)
    return storage


target = input_user().replace(".", "")
mix_up(target, 1)
file = open('gmail.txt', 'w')
for i in storage:
    temp = str(i) + "@gmail.com"
    file.write(temp)
    file.write("\n")
    print(temp)


Clear()
print(" [+] Now you have LOTS of gmail's for the same user. Enjoy!")
sleep(2)

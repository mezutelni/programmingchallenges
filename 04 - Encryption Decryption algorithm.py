from random import randint
import os
def generate_key():
    x=""
    isfile = os.path.isfile("key.txt") #checking path to file, return True, if file exist

    if (isfile!= True):
        open("key.txt","w").close()

    key_file = open("key.txt", "r+")
    if (key_file.read() != ""):
        key_file.seek(0)
        return key_file.read()

    elif (key_file.read() == ""):
        for i in range (1,128):
            x = x+str(randint(0,9))

    key_file.write(x)
    key_file.seek(0)
    return key_file.read()

key = int(generate_key())

print("1. Encrypt \n2. Decrypt \n3. I have decrypt/encrypt key \n4. Show me my key \n5. Delete my key")
action = str(input("What do you want to do?: "))
if action == "3":
    key = int(input("Give me your key(must be an int!): "))
    action = str(input("What do you want to do now?: "))
if (action.lower() in ("1","encrypt")):
    string = input("What is message you want to encrypt?: ")
    encrypted = []
    for i in range(0,len(string)):
        if string[i] == " ":
            x = -15
        else:
            x = ord(string[i])/key
        encrypted.append(x)
    print("Your encrypted message is: ")
    print(*encrypted)
elif (action.lower() in ("2","decrypt")):
    string = input("What is message you wan to decrypt?: ")
    string = string.split()
    decrypted = []
    for i in range(0, len(string)):
        if int(float(string[i])) == -15:
            decrypted.append(" ")
        else:
            x = int(round(float(string[i]) * key)) #I'm multiplaying crypted float with key, then rounding it to full int(because, sometimes, it gives something like 118.999999 which should be 119) and then, im chaning it to char
            if (x%1==0):
                decrypted.append(chr(x))
            else:
                print("I think, you may have wrong decrypt key!")
                break
    if len(decrypted) == len(string):
        print("Your decrypted message is: ")
        print(*decrypted)
elif (action.lower() in ("4","show")):
    print("Your key is: %s" %(key))
elif action.lower() in ("5","delete"):
    open("key.txt", "w").write("")


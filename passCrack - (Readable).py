# Required For The Exit Message That Lets The User Know Their Password Has Been Found
import sys
# Required for md5!!
import hashlib
# Global Vars:
stringPass = ""
# Functions:
def intro():
    print("Welcome to Password Crack!!!\n\n In this application, you will type a password into the console and Python will return an MD5 Hash of that password. Go ahead and copy that and then when Python asks you for the MD5 Hash, go ahead and Paste that into the console. ")
    print("Your md5 Hash is:", str(hashlib.md5(input("\n\nType your Password here: ").encode()).hexdigest()))
    main()
# Main Function That Uses Brute-Force To Guess and Check MD5 Hashes Created by Python in order!
def main():
    inputMD5Hash = input("Paste your MD5 Hash here: ")
    print("Your MD5 Hash is: ", inputMD5Hash)
    listOfCharacters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+,./;'[]\\<>?:\"{}|`~ ")
    for i in range(95):
        global stringPass
        stringPass = listOfCharacters[i]
        if hashlib.md5(stringPass.encode()).hexdigest() == inputMD5Hash:
            success()
        else:
            print(stringPass, "didn't seem to be your password!!")
        
        stringPass = listOfCharacters[i]
        for j in range(95):
            currentStringPass = stringPass + listOfCharacters[j]
            if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                stringPass = currentStringPass
                success()
            else:
                print(currentStringPass, "didn't seem to be your password!!")
            for k in range(95):
                currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k]
                if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                    stringPass = currentStringPass
                    success()
                else:
                    print(currentStringPass, "didn't seem to be your password!!")
                for l in range(95):
                    currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k] + listOfCharacters[l]
                    if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                        stringPass = currentStringPass
                        success()
                    else:
                        print(currentStringPass, "didn't seem to be your password!!")
                    for m in range(95):
                        currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k] + listOfCharacters[l] + listOfCharacters[m]
                        if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                            stringPass = currentStringPass
                            success()
                        else:
                            print(currentStringPass, "didn't seem to be your password!!")
                        for n in range(95):
                            currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k] + listOfCharacters[l] + listOfCharacters[m] + listOfCharacters[n]
                            if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                                stringPass = currentStringPass
                                success()
                            else:
                                print(currentStringPass, "didn't seem to be your password!!")
                            for o in range(95):
                                currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k] + listOfCharacters[l] + listOfCharacters[m] + listOfCharacters[n] + listOfCharacters[o]
                                if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                                    stringPass = currentStringPass
                                    success()
                                else:
                                    print(currentStringPass, "didn't seem to be your password!!")
                                for p in range(95):
                                    currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k] + listOfCharacters[l] + listOfCharacters[m] + listOfCharacters[n] + listOfCharacters[o] + listOfCharacters[p]
                                    if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                                        stringPass = currentStringPass
                                        success()
                                    else:
                                        print(currentStringPass, "didn't seem to be your password!!")
                                    for q in range(95):
                                        currentStringPass = stringPass + listOfCharacters[j] + listOfCharacters[k] + listOfCharacters[l] + listOfCharacters[m] + listOfCharacters[n] + listOfCharacters[o] + listOfCharacters[p] + listOfCharacters[q]
                                        if hashlib.md5(currentStringPass.encode()).hexdigest() == inputMD5Hash:
                                            stringPass = currentStringPass
                                            success()
                                        else:
                                            print(currentStringPass, "didn't seem to be your password!!")

# Function To Be Called If A Match Is Found
def success():
    # Simple Exit Program With Message That Says Password Was Found!
    sys.exit("\n\n\n\n\n\n\n\n\n\n\n\n\nPython found your password to be \"" + stringPass + "\"!!!")

# Initiate Program
intro()
# Required For The Exit Message That Lets The User Know Their Password Has Been Found
import sys
# Required for md5!!
import hashlib
# Global Vars:
a = ""
# Functions:
def intro():
    print("Welcome to Password Crack!!!\n\n In this application, you will type a password into the console and Python will return an MD5 Hash of that password. Go ahead and copy that and then when Python asks you for the MD5 Hash, go ahead and Paste that into the console. ")
    print("Your md5 Hash is:", str(hashlib.md5(input("\n\nType your Password here: ").encode()).hexdigest()))
    main()
# Main Function That Uses Brute-Force To Guess and Check MD5 Hashes Created by Python in order!
def main():
    b = input("Paste your MD5 Hash here: ")
    print("Your MD5 Hash is: ", b)
    c = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+,./;'[]\\<>?:\"{}|`~ ")
    for i in range(95):
        global a
        a = c[i]
        if hashlib.md5(a.encode()).hexdigest() == b:
            success()
        else:
            print(a, "didn't seem to be your password!!")
        
        a = c[i]
        for j in range(95):
            cA = a + c[j]
            if hashlib.md5(cA.encode()).hexdigest() == b:
                a = cA
                success()
            else:
                print(cA, "didn't seem to be your password!!")
            for k in range(95):
                cA = a + c[j] + c[k]
                if hashlib.md5(cA.encode()).hexdigest() == b:
                    a = cA
                    success()
                else:
                    print(cA, "didn't seem to be your password!!")
                for l in range(95):
                    cA = a + c[j] + c[k] + c[l]
                    if hashlib.md5(cA.encode()).hexdigest() == b:
                        a = cA
                        success()
                    else:
                        print(cA, "didn't seem to be your password!!")
                    for m in range(95):
                        cA = a + c[j] + c[k] + c[l] + c[m]
                        if hashlib.md5(cA.encode()).hexdigest() == b:
                            a = cA
                            success()
                        else:
                            print(cA, "didn't seem to be your password!!")
                        for n in range(95):
                            cA = a + c[j] + c[k] + c[l] + c[m] + c[n]
                            if hashlib.md5(cA.encode()).hexdigest() == b:
                                a = cA
                                success()
                            else:
                                print(cA, "didn't seem to be your password!!")
                            for o in range(95):
                                cA = a + c[j] + c[k] + c[l] + c[m] + c[n] + c[o]
                                if hashlib.md5(cA.encode()).hexdigest() == b:
                                    a = cA
                                    success()
                                else:
                                    print(cA, "didn't seem to be your password!!")
                                for p in range(95):
                                    cA = a + c[j] + c[k] + c[l] + c[m] + c[n] + c[o] + c[p]
                                    if hashlib.md5(cA.encode()).hexdigest() == b:
                                        a = cA
                                        success()
                                    else:
                                        print(cA, "didn't seem to be your password!!")
                                    for q in range(95):
                                        cA = a + c[j] + c[k] + c[l] + c[m] + c[n] + c[o] + c[p] + c[q]
                                        if hashlib.md5(cA.encode()).hexdigest() == b:
                                            a = cA
                                            success()
                                        else:
                                            print(cA, "didn't seem to be your password!!")

# Function To Be Called If A Match Is Found
def success():
    # Simple Exit Program With Message That Says Password Was Found!
    sys.exit("Python found your password to be \"" + a + "\"!!!")

# Initiate Program
intro()
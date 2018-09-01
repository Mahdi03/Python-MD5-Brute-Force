def a():
    global inputMD5Hash
    listOfCharacters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+,./;'[]\\<>?:\"{}|`~ ")
    for i in range(1):
        global stringPass
        stringPass = listOfCharacters[0]
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
a()
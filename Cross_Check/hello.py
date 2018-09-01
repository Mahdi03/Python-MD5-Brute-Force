listOfCharacters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&()-=_+,./;'[]\\<>?:\"{}|`~ ")
importString = ""
importString2 = "import"
execFileString = ""
for i in range(len(listOfCharacters)):
    if listOfCharacters[i].istitle() == True:
        filename = "bruteForce_cap" + listOfCharacters[i] + ".py"
    elif listOfCharacters[i] == "#":
        filename = "bruteForce_hash.py"
    elif listOfCharacters[i] == "!":
        filename = "bruteForce_exc.py"
    elif listOfCharacters[i] == "*":
        filename = "bruteForce_ast.py"
    elif listOfCharacters[i] == "\\":
        filename = "bruteForce_bs.py"
    elif listOfCharacters[i] == "/":
        filename = "bruteForce_fs.py"
    elif listOfCharacters[i] == "<":
        filename = "bruteForce_&lt;.py"
    elif listOfCharacters[i] == ">":
        filename = "bruteForce_&gt;.py"
    elif listOfCharacters[i] == ":":
        filename = "bruteForce_sc.py"
    elif listOfCharacters[i] == "?":
        filename = "bruteForce_qm.py"
    elif listOfCharacters[i] == "\"":
        filename = "bruteForce_qtd.py"
    elif listOfCharacters[i] == "|":
        filename = "bruteForce_strlne.py"
    elif listOfCharacters[i] == " ":
        filename = "bruteForce_space.py"
    else:
        filename = "bruteForce_" + listOfCharacters[i] + ".py"
    tempPyFile = open(filename, "w+")
    tempPyFile.close()
    print(filename, "created successfully!\n")
    importString += "import Cross-Check\\\\" + filename.replace(".py", "") + "\n"
    importString2 += " Cross-Check\\" + filename.replace(".py", "") + ","
    execFileString += "exec(open("+ "\"Cross-Check\\" + filename +"\", \"r\").read())\n"
print(importString)
print()
print(importString2)
print()
print(execFileString)

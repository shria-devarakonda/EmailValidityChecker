import re
regex_pattern = r"^[a-z][a-z0-9\.\_\-]*@[a-z]*\.[a-z]{1,3}$"
for i in range(int(input())):
    email = input()
    #email = email[1:-1]
    #print(email)
    a = bool(re.match(regex_pattern, email, re.I))
    if a == True:
        print("AWESOME GOOD MAIL ID")
        print(email)
        with open("validmails.txt", "+a") as f:
            f.write(email)
            f.write("\n")
    else:
        print("THATS A BAD MAIL ID MAN NAH")
        pass
    #print(name)
    #print(email)

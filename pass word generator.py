import random
import string
n =int(input("enter the lenght of the of the pass word needed:"))
print('''Choose the charaters set for  the pass word from these :
      1.Digits
      2.Letters
      3.Special Charaters
      4.Exit''' )
charactersList=" "
while(True):
    choice=int(input("pick a number"))
    if(choice==1):
        charactersList=charactersList+string.ascii_letters
    elif(choice==2):
        charactersList=charactersList+string.digits
    elif(choice==3):
        charactersList=charactersList+string.punctuation
    elif(choice==4):
        break
    else:
        print("please click the valid choice")
password=[]
for i in range (n) :
    randomchar=random.choice(charactersList)
    password.append(randomchar)
print("the random pass word is:"+"".join(password))


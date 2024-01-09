#Write a program to store roll and name of n students of a class.Display roll
#of all those students whose name in entered only in capital letters
D={}
def show(D):
    for i in D:
        if i.isupper():
            print(D[i])

#Main
s=int(input("Enter size: "))
for i in range(0,s,1):
    roll=int(input("Enter Roll No.: "))
    name=input("Enter name: ")
    D[name]=roll
show(D)

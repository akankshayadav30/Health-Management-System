def getdate():
    import datetime
    return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food: "))
        if(c==1):
            value=input("type here\n")
            with open("akanksha-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("akanksha-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food: "))
        if (c == 1):
            value = input("type here\n")
            with open("piyush-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("piyush-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food: "))
        if (c == 1):
            value = input("type here\n")
            with open("rohit-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohit-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(akanksha),2(piyush),3(rohit): ")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food: "))
        if(c==1):
            with open("akanksha-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("akanksha-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food: "))
        if (c == 1):
            with open("piyush-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("piyush-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food: "))
        if (c == 1):
            with open("rohit-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohit-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (akanksha,piyush,rohit): ")
print("HEALTH MANAGEMENT SYSTEM")
a=int(input("Press 1 for log the value and 2 for retrieve: "))

if a==1:
    b = int(input("Press 1 for akanksha 2 for piyush 3 for rohit: "))
    take(b)
else:
    b = int(input("Press 1 for akanksha 2 for piyush 3 for rohit: "))
    retrieve(b)
    
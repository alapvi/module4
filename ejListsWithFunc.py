
theList = []
def showMenu():
    print("Menu")
    print("1.- Add number")
    print("2.- Add number in a position")
    print("3.- Show the length")
    print("4.- Delete the last number")
    print("5.- Delete a number in the list")
    print("6.- Count number")
    print("7.- Positions of a number")
    print("8.- Show the list ")
    print("9.- Exit")
    option = int(input("Choose an option:"))
    return option
def addNumber():
    num = int(input("Input a number"))
    theList.append(num)

while True:
    option = showMenu()
    if option == 1:
        addNumber()
    elif option == 2:
        num = int(input("Input a number"))
        pos = int(input("Input the position"))
        if pos <= len(theList):
            theList.insert(pos,num)
        else:
            print("The index is out!!!")
    elif option == 3:
        print("The length of the list is ",len(theList))
    elif option == 4:
        if len(theList) > 0:
            print("The last element is ",theList.pop())    
    elif option == 5:
        pos = int(input("Input the position"))
        if pos <= len(theList):
            print("Deleting the element ",theList.pop(pos))
    elif option == 6:
        num = int(input("Input a number"))
        print("The ocurrences of the number ",num, " is ", theList.count())
    elif option == 7:
        num = int(input("Input a number"))
        pos=0
        for elem in range(0,theList.count(num)):
            index = theList.index(num,pos)
            print(index,end=" ")
            pos = index + 1
        print()
        """index = 1
        for elem in theList:
            if elem == num:
                print(index, end = " ")
            index += 1
        print()   
        """

    elif option == 8:
        for elem in theList:
            print(elem,end=" ")
        print()
    elif option == 9:
        break


    

    
    
    
    
    
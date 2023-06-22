while True:
    match = False
    userinput = input("?: ")
    f1= open("data.txt","r")
    data = list(eval(f1.read()))
    for pair in range(0,len(data)):
        for questions in range(0, len(data[pair][0])):
            print()
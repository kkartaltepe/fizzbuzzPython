def fizzbuzz(start, end):
    for x in range(start, end+1):
        if(x%5==0 and x%3==0):
            print("fizzbuzz")
        elif(x%5==0):
            print("fizz")
        elif(x%3==0):
            print("buzz")
        else:
            print(" {} ".format(x))

fizzbuzz(1, 100)

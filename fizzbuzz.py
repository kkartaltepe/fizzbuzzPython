def fizzbuzz(start, end):
    for x in range(start, end+1):
        if(x%5==0 and x%3==0):
            print("FizzBuzz")
        elif(x%3==0):
            print("Fizz")
        elif(x%5==0):
            print("Buzz")
        else:
            print(x)

fizzbuzz(1, 100)

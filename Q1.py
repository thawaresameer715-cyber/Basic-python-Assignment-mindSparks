#1. Write a function using a while loop to print even numbers from 1 to 20.

def even_no():
    i=1
    print("Even numbers are from 1 to 20= ")
    while i <= 20:
        if i%2==0:
            print(i, end=" ")
        i+=1

even_no()

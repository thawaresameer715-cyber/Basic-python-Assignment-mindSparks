#2. Use if-elif-else to classify a number as positive, negative, or zero; test in a for loop over a list

lst= [3,4,-7,2,-4,1,0,6,5]

for i in lst:
    if i==0:
        print(i," is Zero")
    elif i>0:
        print(i," is positive")
    else:
        print(i," is negative")

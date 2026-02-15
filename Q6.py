#6. Use nested for loops and if to print a multiplication table (1-10) as a list of tuples.

lst=[]
tup=()
for i in range(1,11):
    for j in range(1,11):
        lst.append((f"{i}x{j}= ",i*j))  

print(lst)
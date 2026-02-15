#8. Function to reverse a list using a for loop and slicing; compare with tuples (immutable)

lst= [-1,3,4,-7,2,-4,1,0,6,5]

# reversing list usinf slicing
rev_lst1= lst[::-1]
print(rev_lst1)

# reversing list usinf for-loop
New_lst=[]
for i in range(len(lst)-1,-1,-1):
    New_lst.append(lst[i])
print(New_lst)
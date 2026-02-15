# Create a list of 10 numbers, loop to find and print the maximum using only conditionals (no max()).

lst= [-1,3,4,-7,2,-4,1,0,6,5]

max_val= lst[0]
for i in range(len(lst)):
    if lst[i]>max_val:
        max_val=lst[i]
print(max_val)

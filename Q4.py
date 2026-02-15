#4. Define a tuple of fruits; use a for loop to print those starting with 'A' or 'B'.

tup=("Muskmelon","Apple", "Orange", "Banana", "Kivi", "Mango","berry", "Watermelon")

for i in tup:
    if i[0] in "abAB":
        print(i)
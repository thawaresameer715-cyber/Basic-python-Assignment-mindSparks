#7. Create a dictionary of {name: age}; loop to print adults (>=18) using items().

dict= { "Aarav": 24, "Meera": 31, "Kabir": 27, "Ishita": 12, "Rohan": 35, "Anaya": 29, "Vivaan": 9, "Sara": 33, "Arjun": 26, "Diya": 28}

for name, age in dict.items():
    if age>=18:
        print("adults (>=18)= ", name, age)

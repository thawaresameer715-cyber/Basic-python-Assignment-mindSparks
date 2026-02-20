#Generate 20 random nums (1-100), use sets for uniques, dict for frequency, print most common with conditional.

import random

# Generate 20 random numbers
raw_numbers = [random.randint(1, 100) for _ in range(20)]

# Use a set to identify all unique numbers present
unique_numbers = set(raw_numbers)

# Use a dictionary to count the frequency of each number
frequency = {}
for num in raw_numbers:
    frequency[num] = frequency.get(num, 0) + 1

# Find the most common number
most_common_num = None
highest_count = 0

for num, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_common_num = num

# Print results
print(f"Generated List: {raw_numbers}")
print(f"Unique Numbers ({len(unique_numbers)}): {unique_numbers}")
print(f"Frequency Map: {frequency}")

if highest_count > 1:
    print(f"\nMost Common: {most_common_num} (appeared {highest_count} times)")
else:
    print("\nAll numbers appeared only once.")
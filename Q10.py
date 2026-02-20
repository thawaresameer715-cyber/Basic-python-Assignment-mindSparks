#10. Merge two sets of numbers; use intersection and union, print differences with loop.
set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")

print("\nDifferences:")
for num in union_set:
    if num not in intersection_set:
        print(num)
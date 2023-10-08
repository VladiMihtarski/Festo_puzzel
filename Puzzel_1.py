import os
print("Current working directory:", os.getcwd())

with open(r'01_keymaker_ordered.txt', 'r') as file:
    keys = file.read().splitlines()


def is_ordered(key):
    return list(key) == sorted(key)

ordered_key = None
for key in keys:
    if is_ordered(key):
        ordered_key = key
        break

if ordered_key:
    print("Sorted key is", ordered_key)
else:
    print("there dosent have sorted key")

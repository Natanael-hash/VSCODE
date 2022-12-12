programming_class = {"java": 12, 'python': 10, "javascript": 7, "C": 11}

print(programming_class.items())
sorted_items = sorted(programming_class.items(), key=lambda item: item[1])
print(sorted_items)
sorted_programming_class = {k:v for k, v in sorted_items}
print(sorted_programming_class)
sorted_items = sorted(programming_class.items(), key=lambda item: item[0])
print(sorted_items)
sorted_programming_class = {k:v for k, v in sorted_items}
print(sorted_programming_class)

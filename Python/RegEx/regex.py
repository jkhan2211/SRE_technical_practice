import re

file = open("regex_sum_2090793.txt", "r")
content = file.read()
num_in_file = re.findall("[0-9]+", content)
print(num_in_file)

total = 0
# using loop
for i in range(0, len(num_in_file)):
    num_in_file[i] = int(num_in_file[i])
    total = total + num_in_file[i]

print("total-",total)

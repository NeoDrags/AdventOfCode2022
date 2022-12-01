sum = max = 0

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

lines.append('')

for line in lines:
    if line != '':
        sum += int(line)
    else:
        if max < sum:
            max = sum
        sum = 0

print(max)

x = []
Sum = 0

with open ("input.txt", "r") as f:
    lines = f.read().splitlines()

lines.append('')

for line in lines:
    if line != '':
        Sum += int(line)
    else:
        x.append(Sum)
        Sum = 0

x.sort()
print(sum(x[-3:]))

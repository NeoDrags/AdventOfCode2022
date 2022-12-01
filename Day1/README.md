# Day 1 - Part 1
## Question
Find the most calories carried by an elf
## Code
  ```py
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
  ```
## Output
  ```
  69693
  ```
# Day 1 - Part 2
## Question
Find the sum of the most calories carried by 3 elves
## Code
  ```py
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
  ```
## Output
```
200945
```

#!/usr/bin/python3

with open("input.txt", "r") as f:
  line = f.readline().strip().split()
  cols, width, spaces = [int(x) for x in line]

  x = f.read().split()

  output = []
  buf = ""
  for word in x:
    if len(word) + len(buf) + 1 > width:
      output.append(buf)
      buf = ""
    buf = (buf + " " + word).strip()

  lines = int(len(output) / cols)

  columns = [[]]

  counter = 0
  for i in range(0, len(output)):
    if counter > lines:
      columns.append([])
      counter = 0
    columns[-1].append(output[i])
    counter += 1

  row = 0

  output = ""
  for i in range(0, lines):
    for col in range(0, cols):
      output += columns[col][i].ljust(width) + (" " * spaces)
    output += "\n"
  print(output)
  

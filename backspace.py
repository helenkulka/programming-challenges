import sys

for line in sys.stdin:
  line = line.rstrip()
  chars = list(line)
  intended = []
  
  for i, char in enumerate(chars):
    if char == '<':
    #remove last element from our stack if we've seen a backspace
      if i != 0:
        intended.pop()
    else:
     #otherwise, append it
      intended.append(char)

  print(('').join(intended))
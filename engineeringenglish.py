import sys

seen = []
output_lines = []
lines = []

lines = sys.stdin.readlines()

for line in lines:
    line = line.rstrip()
    output_line = []
    for word in line.split():
        #check if lowercase word in our seen array, if it is replace with '.'
        if word.lower() in seen:
            output_line.append('.')
        #otherwise append it
        else:
            output_line.append(word)
            seen.append(word.lower())
    output_lines.append(output_line)

for l in output_lines:
    print(' '.join(l))


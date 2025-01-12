import sys
lines = []
while True:
    try:
        # Attempt to read a line
        row = input().strip()
        # If the line is empty, break out of the loop (optional)
        if not row:
            break

        # Convert each piece to int and append
        lines.append([int(x) for x in row.split()])
    except EOFError:
        break  # Stop if we reach end of file


problems = lines[0][0]
if problems == 0:
    print(0)
    sys.exit()


lines = lines[1:]
total = 0
for line in lines:
    if sum(line) >= 2:
        total += 1

print(total)


import sys

data = sys.stdin.read()
lines = data.split("\n")
endval = len(lines)
if lines[len(lines)-1].strip() == '' :
    endval = endval - 1
check = endval
while check >= 0:
    check = check - 1
    line = lines[check]
    if line.startswith("<p>") :
        j = check
        while j < endval:
            print lines[j]
            j = j + 1
        endval = check

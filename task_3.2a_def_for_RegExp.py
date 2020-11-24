import sys
import re

# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r"cat", line)) > 1:
#         print(line)

# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\bcat\b", line):
#         print(line)

# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"z...z", line):
#         print(line)

# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\\", line):
#         print(line)

# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\b(\w+)\1\b", line):
#         print(line)

# for line in sys.stdin:
#     line = line.rstrip()
#     newline = re.sub(r"human", r"computer", line)
#     print(newline)

# for line in sys.stdin:
#     line = line.rstrip()
#     newline = re.sub(r"\b[aA]+\b", r"argh", line, 1)
#     print(newline)

# for line in sys.stdin:
#     line = line.rstrip()
#     newline = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
#     print(newline)

for line in sys.stdin:
    line = line.rstrip()
    newline = re.sub(r"(\w)\1*", r"\1", line)
    print(newline)

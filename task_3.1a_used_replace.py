str = input()
old = input()
new = input()
count = 0
while(str.find(old) != -1):
    str = str.replace(old, new)
    count = count + 1
    if count > 1000:
        count = "Impossible"
        break
print(count)

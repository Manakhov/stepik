s = input()
t = input()
point = s.find(t)
count = 0
while(point != -1):
    point = s.find(t, point + 1)
    count = count + 1
print(count)

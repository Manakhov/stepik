objects = [1, 2, 1, 2, 3]
list_obj = []
ans = 0
for obj in objects:
    if obj not in list_obj:
        list_obj.append(obj)
        ans += 1
print(ans)
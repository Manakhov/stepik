objects = [1, 2, 1, 2, 3]
list_obj = []
ans = 1
for obj in objects:
    i = False
    for obj_comp in list_obj:
        if obj is obj_comp:
            ans += 1
            i = True
            break
    if i:
        continue
    else:
        list_obj.append(obj)
print(ans)

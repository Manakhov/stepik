def comparison(list_obj, obj_comp):
    for obj in list_obj:
        if obj_comp is obj:
            return True
    return False


objects = [1, 2, 1, 2, 3]
list_obj = []
ans = 1
for obj in objects:
    if comparison(list_obj, obj):
        ans += 1
    else:
        list_obj.append(obj)
print(ans)

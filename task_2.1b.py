dict = {}


def check_children(class_value, class_key):
    if class_value in dict[class_key]:
        return True
    else:
        for dic in dict[class_key]:
            if check_children(class_value, dic):
                return True
    return False


n = int(input())
for i in range(n):
    class_desc = input().split()
    dict[class_desc[0]] = []
    for cla in class_desc:
        if cla != class_desc[0] and cla != ':':
            dict[class_desc[0]].append(cla)
n = int(input())
dict['Errors'] = []
for i in range(n):
    error_name = input()
    for dic in dict['Errors']:
        if check_children(dic, error_name):
            print(error_name)
            break
    dict['Errors'].append(error_name)

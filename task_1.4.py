dict = {'global': []}


def create(request):
    dict[request[1]] = [request[2]]


def add(request):
    dict[request[1]].append(request[2])


def get(request_1, request_2):
    if request_2 in dict.get(request_1):
        return request_1
    elif request_1 == 'global':
        return None
    else:
        return get(dict.get(request_1)[0], request_2)


print("Введите кол-во запросов")
n = int(input())
print("Введите", n, "запроса(ов)")
for i in range(n):
    request = input().split()
    if request[0] == 'create':
        create(request)
    elif request[0] == 'add':
        add(request)
    elif request[0] == 'get':
        print(get(request[1], request[2]))

# add(['add', 'global', 'a'])
# create(['create', 'foo', 'global'])
# add(['add', 'foo', 'b'])
# print(get('foo', 'a'))
# print(get('foo', 'c'))
# create(['create', 'bar', 'foo'])
# add(['add', 'bar', 'a'])
# print(get('bar', 'a'))
# print(get('bar', 'b'))

print(dict)


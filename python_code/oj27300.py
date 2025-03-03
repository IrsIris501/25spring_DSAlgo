n=int(input())
model_list=[]
def value(x):
    if x[-1]=='B':
        return float(x[:-1:])*1000
    else:
        return float(x[:-1:])

for _ in range(n):
    flag=False
    model_name, para=input().split('-')
    for i in range(len(model_list)):
        if model_list[i][0]==model_name:
            model_list[i][1].append(para)
            flag=True
            break
    if not flag:
        model_list.append((model_name, [para]))

model_list.sort(key=lambda x:x[0])
for i in range(len(model_list)):
    print(model_list[i][0]+': ', end='')
    print(*sorted(model_list[i][1], key=lambda x:value(x)), sep=', ')


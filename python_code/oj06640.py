n=int(input())
inverted_dict=dict()
word_set=set()
for i in range(1, n+1):
    input_string=input()
    this_file=set()
    for j in range(len(input_string)):
        if input_string[j]==' ':
            c=int(input_string[0:j])
            s=input_string[j::].split()
            break
    for j in s:
        if j in word_set and j not in this_file:
            inverted_dict[j].append(i)
            this_file.add(j)
        elif j not in word_set:
            word_set.add(j)
            inverted_dict[j]=[i]
            this_file.add(j)



m=int(input())
for i in range(m):
    s=input()
    if s in word_set:
        print(*inverted_dict[s])
    else:
        print('NOT FOUND')



n,m = int(input()),int(input())
first_List = m * [int(i) for i in range(1, n + 1)]
second_List = [' ']
three_List = []
cnt = 0
while second_List[-1] != 1:
    second_List.clear()
    for j in range(cnt, m + cnt):
        second_List.append(first_List[j])
        cnt += 1
    two_List_copy = second_List.copy()
    three_List.append(two_List_copy)
    cnt -= 1
for k in range(len(three_List)):
    print(three_List[k][0], end='')

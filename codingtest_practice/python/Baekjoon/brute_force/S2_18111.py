N, M, B = map(int, input().split())
num_dict = {i:0 for i in range(257)}
num_set = set()
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        num_dict[lst[j]] += 1
        num_set.add(lst[j])
# 최소 시간
minT = 1e9
num_lst = sorted(list(num_set))
# 땅 높이
h = 0
# 블럭 개수
Blocks = B
result = 1
for i in range(min(num_lst), max(num_lst)+1):
    t_cnt = 0
    for j in range(len(num_lst)-1, -1, -1):
        if num_lst[j] == i and result:
            continue
        elif num_lst[j] > i and result:
            t_cnt += num_dict[num_lst[j]] * (num_lst[j] - i) * 2
            Blocks += num_dict[num_lst[j]] * (num_lst[j] - i)

        elif num_lst[j] < i and result:
            if Blocks >= num_dict[num_lst[j]] * (i - num_lst[j]):
                t_cnt += num_dict[num_lst[j]] * (i - num_lst[j])
                Blocks -= num_dict[num_lst[j]] * (i - num_lst[j])
            else:
                result = 0
    if t_cnt != 0 and result == 1:
        if minT >= t_cnt:
            minT = t_cnt
            if h < i:
                h = i

    Blocks = B
    result = 1

if len(num_lst) == 1:
    print(0, num_lst[0])
else:
    print(minT, h)



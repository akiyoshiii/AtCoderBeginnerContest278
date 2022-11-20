#N 長さ, K 操作数
N, K = map(int, input().split())
li = list(map(int, input().split())) #A1-An
#li[0], ... li[N-1]

j = 0


# 1, 2, ... k　回

while j < K :
    for i in range(0, N-1):
        li[(i)] = li[(i+1)]
#li[0] -> li[1]
#li[1] -> li[2]
#li[N-1] -> li[N]
    li [N-1] = 0
    j += 1
    



li_str = list(map(str,li))
answer = ' '.join(li_str)
print(answer)

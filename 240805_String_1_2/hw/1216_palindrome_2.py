T = 10
N = 100

for _ in range(T):
    tc = int(input())
    arr = [list(input()) for _ in range(N)]

'''
<생각 정리>
arr = ['A', 'B', 'B', 'A', 'C', 'C', 'A', 'B', 'A']
N = len(arr)
v_list = ['A', 'B', 'C']
idx_list = [] # A, B, C의 인덱스를 [], [], []로 받을 바깥 리스트

for x in v_list:
    temp_list = [] # A, B, C의 인덱스를 담을 리스트
    for i in range(N):
        if arr[i] == x:
            temp_list.append(i)
    idx_list.append(temp_list)
'''
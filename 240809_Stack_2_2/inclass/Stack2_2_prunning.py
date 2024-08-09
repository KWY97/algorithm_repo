# 백트래킹 활용해 부분 집합 만드는 함수

# def f(i, K): # bit[i]를 결정하는 함수
#     ### 여기 이해가 안댐
#     if i == K: # 모든 원소에 대해 결정하면
#         for j in range(K):
#             if bit[j] != 0:
#                 print(a[j], end = ' ')
#         print() # 부분 집합을 한 행에 표시
#     ###
#     else:
#         bit[i] = 1
#         f(i+1, K)
#         bit[i] = 0
#         f(i+1, K)
#
# N = 3
# a = [1, 2, 3] # 주어진 원소의 집합
# bit = [0] * N
# f(0, N) # N개의 원소에 대해 부분집합을 만드는 함수


# 부분 집합의 합
# N = 3
# a = [1, 2, 3] # 주어진 원소의 집합
# bit = [0] * N

# def ff(i, K): # bit[i]를 결정하는 함수
#     if i == K: # 모든 원소에 대해 결정하면
#         s = 0
#         for j in range(K):
#             if bit[j]: # bit[j]가 0이 아니면
#                 print(a[j], end = ' ')
#                 s += a[j]
#         print(' :', s) # 부분 집합을 한 행에 표시
#     else:
#         # bit[i] = 1
#         # f(i+1, K)
#         # bit[i] = 0
#         # f(i+1, K)
#
#         # 위의 4줄을 간략히 한 것
#         for j in [1, 0]:
#             bit[i] = j
#             ff(i+1, K)
#
# ff(0, N) # N개의 원소에 대해 부분집합을 만들고 합을 보여주는 함수
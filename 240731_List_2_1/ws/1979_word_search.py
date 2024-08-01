T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # 행 기준으로 확인
    for i in range(N):
        row_count = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_count += 1
            else: # arr[i][j]이 0일 때
                if row_count == K:
                    count += 1
                row_count = 0
        if row_count == K:  # 끝 났을 시 마지막 셀까지 검사
            count += 1

    # 열 기준으로 확인
    for j in range(N):
        col_count = 0
        for i in range(N):
            if arr[i][j] == 1:
                col_count += 1
            else: # arr[j][i]가 0일 때
                if col_count == K:
                    count += 1
                col_count = 0
        if col_count == K:  # 끝 났을 시 마지막 셀까지 검사
            count += 1

    print(f'#{tc} {count}')


# 내 코드 다시 해보기
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     row_ans = 0
#     col_ans = 0
#     for i in range(N):  # 행을 기준으로 확인
#         row_count = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 row_count += 1
#                 if row_count == K:
#                     # 뒤쪽 검증
#                     if j < N-1: # arr[i][j] 뒤에 숫자가 있다면
#                         if arr[i][j+1] == 0: # 뒷 숫자가 0이라면
#                             row_ans = row_count
#                             row_count = 0
#                         elif arr[i][j+1] == 1: # 뒷 숫자가 1이라면
#                             row_count = 0
#                     elif j >= N-1: # arr[i][j]가 마지막 이거나 뒤 숫자가 없다면
#                         row_ans = row_count
#                         row_count = 0
#                     # 앞쪽 검증
#                     if j - K <= 0:  # arr[i][j-K]가 없거나 처음이라면
#                         row_ans = row_count
#                     elif j - K > 0: # arr[i][j-K]가 있다면
#                         if arr[i][j-K] == 0: # 앞 숫자가 0이라면
#                             row_ans = row_count
#                             row_count = 0
#                         elif arr[i][j-K] == 1: # 앞 숫자가 1이라면
#                             row_count = 0
#
#     for j in range(N):  # 열을 기준으로 확인
#         col_count = 0
#         for i in range(N):
#             if arr[j][i] == 1:
#                 col_count += 1
#             if col_count == K:
#                 # 뒤쪽 검증
#                 if j < N - 1:  # arr[j][i] 뒤에 숫자가 있다면
#                     if arr[i][j + 1] == 0:  # 뒷 숫자가 0이라면
#                         col_ans = col_count
#                         col_count = 0
#                     elif arr[i][j + 1] == 1: # 뒷 숫자가 1이라면
#                         col_count = 0
#                 elif j >= N - 1:  # arr[j][i]가 마지막 이거나 뒤 숫자가 없다면
#                     col_ans = col_count
#                     col_count = 0
#                 # 앞쪽 검증
#                 if i - K <= 0:  # arr[j][i-K]가 없거나 처음이라면
#                     col_ans = col_count
#                 elif i - K > 0:  # arr[j][i-K]가 있다면
#                     if arr[j][i - K] == 0:  # 앞 숫자가 0이라면
#                         col_ans = col_count
#                         col_count = 0
#                     elif arr[j][i - K] == 1:  # 앞 숫자가 1이라면
#                         col_count = 0
#
#     print(f'#{tc} {row_ans + col_ans}')
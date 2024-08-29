def find_row(arr, N):
    for i in range(N):
        if '1' in arr[i]:
            return i

def find_col(row, M):
    for j in range(M-1, -1, -1):
        if arr[row][j] == '1':
            return j

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    my_password = []

    password = {
        '1011000': 0,
        '1001100': 1,
        '1100100': 2,
        '1011110': 3,
        '1100010': 4,
        '1000110': 5,
        '1111010': 6,
        '1101110': 7,
        '1110110': 8,
        '1101000': 9
    }
    row = int(find_row(arr, N))
    col = int(find_col(row, M))

    for code_start in range(col, col - 56, -7): #암호 시작 인덱스가 나옴
        print(code_start)





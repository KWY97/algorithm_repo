def search_start():
    for i in range(size):
        for j in range(size):
            if arr[i][j] == '2':
                return i, j

def find_road():


dxy =
size = 16

for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(size)]
    sx, sy = search_start()

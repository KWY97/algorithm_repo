def enque(item):
    global rear
    rear = (rear + 1) % (N+1)
    c_queue[rear] = item

def deque():
    global front
    front = (front + 1) % (N+1)
    return c_queue[front]

def isFull():
    return (rear + 1) % (N+1) == front

def isEmpty():
    return front == rear

def Qpeek():
    return c_queue[(front + 1) % (N+1)]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    c_queue = [0] * (N + 1)
    rear = front = 0

    # N개의 화덕에 M번까지의 피자를 조건에 맞추어 넣는 방법이 필요




    cnt = 0
    while cnt != M-1:
        if isFull(): # 포화상태라면
            check = Qpeek() # 출구에 있는 피자를 확인
            if check // 2 == 0: # 치즈가 다 녹았다면
                deque() # 뺀다
                cnt += 1
                # enque 못넣은 피자
            else: # 치즈 안녹았으면
                deque() # 출구에서 빼고
                check //= 2 # 치즈 양 줄이고
                enque(check) # 다시 넣어준다


# 덱 써서 할까 고민해보기
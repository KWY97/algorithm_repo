T = int(input()) # 노선 수

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charging_station = list(map(int, input().split())) # M개의 충전소 위치
    charge_cnt = 0 # 충전 횟수
    current = 0 # 현재 위치

    while current + K < N:
        for move in range(K, 0, -1): # 갈 수 있는 거리에서 가장 먼 충전소를 우선으로 가기 위해 범위를 역순으로
            if current + move in charging_station:
                current += move # 현재 위치 변경
                charge_cnt += 1 # 충전 횟수 추가
                break # for문을 종료
        else: # for문의 조건을 만족하지 못했을 시
            charge_cnt = 0
            break # while문을 종료
    print(f'#{tc} {charge_cnt}')
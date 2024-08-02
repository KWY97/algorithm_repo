T = int(input()) # 노선 수

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charging_station = list(map(int, input().split())) # M개의 충전소 위치
    charge_cnt = 0 # 충전 횟수
    current = 0 # 현재 위치

    while current < N:
        if current + K in charging_station:
            current += K
            charge_cnt += 1

        for i in range(M): # 충전수 개수
            if current > charging_station[i]:
                current = charging_station[i]
                charge_cnt += 1


    print(f'#{tc} {charge_cnt}')



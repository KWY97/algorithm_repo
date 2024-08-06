import pprint

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


# 지영누나 아이디어
# 함수로 열을 기준으로 아래부터 저장하고 슬라이싱해서 다시 저장해도 되고
# 0으로 배열 채워놓고 그냥 값 넣어도 댄다
# 출력양식 join할 때 인트는 join안되니까 입력을 아예 문자열로 받음




# d, l, n이 첫글자로 왔을 땐 뒤에 글자 확인

alpha_dic = {'č': 'c=', 'ć': 'c-', 'dž': 'dz=', 'đ': 'd-', 'lj': 'lj', 'nj': 'nj', 'š': 's=', 'ž': 'z='}
word = input()
N = len(word)

for i in range(N):
    # 단어가 d, l, n인 경우 뒤를 확인 해야함.
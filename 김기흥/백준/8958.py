T = int(input())
Score = []
for i in range(T): Score.append(input())
for i in Score:
    start_index = 0                     # X가 마지막으로 나온 지점 + 1의 index를 저장함
    total = 0                           # 한 케이스의 점수
    if 'X' not in i:
        total = int(len(i)*(len(i)+1)/2)
        print(total)
        continue

    for j in range(len(i)):
        if i[j] == 'X':                 # X가 나왔다면 O의 연속이 끊겼으므로
            n =  j - start_index        # 여태까지 나온 O의 점수만큼 계산해줌
            total+=int((n+1)*n/2)
            start_index = j+1           # 계산 후에는 X가 나온 인덱스 + 1부터 다시 검사 시작
    
    if i[len(i)-1] != 'X':
        n =  len(i) - start_index
        total += int((n+1)*n/2)
    print(total)
 

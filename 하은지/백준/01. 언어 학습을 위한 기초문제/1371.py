# sys.stdin.read() 함수 : 줄 수 대신 텍스트를 한 번에 입력받을 수 있음.
import sys
input = sys.stdin.read


# 입력받은 문자열의 공백과 개행문자를 제거함.
s = input().replace("\n","").replace(" ","")


# 카운트를 위해 알파벳 갯수만큼의 빈리스트를 생성함.
c = [0] * 26


# 전체 문자열에서 문자를 하나씩 뽑아서 변수 i에 차례대로 바인딩 해줌.
for i in s:
    c[ord(i)-97]+=1
    
# 리스트의 값 중 가장 큰 값을 변수 maxx에 바인딩해줌.
maxx = max(c)

# 가장 큰 값(maxx)과 값이 같은 리스트의 인덱스 값을 찾아서 새로운 빈리스트인 r에 넣어줌.
# 이때 빈리스트 r에는 해당 알파벳이 들어감.
r = []
for i in range(len(c)):
    if c[i] == maxx:
        r.append(chr(i+97))     

# 출력 
print(*r, sep = "")

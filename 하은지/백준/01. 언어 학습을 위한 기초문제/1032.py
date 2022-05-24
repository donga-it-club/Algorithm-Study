# [0] 변수 선언부 
import sys
T        = int(sys.stdin.readline().replace("\n", ""))
string_1 = ''
string_2 = ''
temp     = [] 

# [1] 연산 및 출력 
for i in range(T):
    user = sys.stdin.readline().replace("\n", "")
    
    if ( i == 0 ):
        string_1 = user 

    else:
        string_2 = user

        if (string_1 == string_2):
            pass
        
        else:
            for j in range(len(string_1)):
                if (string_1[j] == string_2[j]):
                    temp.append(string_1[j])
                else:
                    temp.append("?")

            string_1 = ''.join(temp)
            temp     = [] 

print(string_1)

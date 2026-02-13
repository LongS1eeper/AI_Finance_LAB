# 풀이

def solution(n, w, num):
    answer = 0
    
    while (num <= n):
        answer += 1
        if (num % (w*2) > w):
            num = num + (2 * (2*w - num % (2*w)) + 1)
        elif num % w == 0:
            num = num + 1
        else: 
            num = num + (2 * (w - num % w) + 1)
        
    return answer


# 해설

def solution(n, w, num):
    m1 = num%(w*2)
    m2 = ((w*2+1) - m1)%(w*2)
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))
def solution(n):
    pibo = [0, 1]
    for i in range(1,n):
        pibo.append(pibo[-2]+pibo[-1])
    
    return pibo[-1] % 1234567
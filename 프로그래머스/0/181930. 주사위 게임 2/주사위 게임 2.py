def solution(a, b, c):
    answer = 0
    sum = a + b + c
    sum_sqr = a**2 + b**2 + c**2
    sum_cub = a**3 + b**3 + c**3

    if a == b == c:
        answer = sum * sum_sqr * sum_cub

    elif a == b or b == c or a == c:
        answer = sum * sum_sqr

    else:    
        answer = sum
    return answer
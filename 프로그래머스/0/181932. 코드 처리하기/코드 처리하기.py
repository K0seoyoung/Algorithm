def solution(code):
    mode = False
    ret = ''
    for idx, i in enumerate(code):
        if i == "1":
            mode = not(mode)
        else:
            condition = idx % 2 == 0
            
            if mode and not(condition):
                ret += i
                continue
            if not(mode) and condition:
                ret += i
                continue
            
    if ret == '': 
        ret = "EMPTY"
    return ret
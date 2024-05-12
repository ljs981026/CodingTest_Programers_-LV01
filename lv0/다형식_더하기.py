def solution(polynomial):
    p_term = polynomial.split(' + ')
    f_term = 0
    c_term = 0
    for p in p_term:
        if 'x' in p:
            if p == 'x':
                p = '1x'
            f_term += int(p.replace('x',''))
        else:
            c_term += int(p)
    if f_term == 0:
        return str(c_term)
    elif c_term == 0:
        if f_term == 1:
            return "x"
        else:
            return str(f_term) + "x"
    else:
        if f_term == 1:
            return 'x + '+str(c_term)
        else:
            return str(f_term)+'x + '+str(c_term)

print(solution("3x + 7 + x"))
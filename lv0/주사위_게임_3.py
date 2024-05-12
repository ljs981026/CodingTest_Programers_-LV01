def solution(a, b, c, d):
    dice = [a,b,c,d]
    Dup = list(set(dice))
    if len(Dup) == 1:
        return 1111 * Dup[0]
    elif len(Dup) == 2:
        for item in dice:
            if dice.count(item) == 3:
                p = item
                q = [x for x in dice if x != p][0]
                return (10 * p + q)**2
            elif dice.count(item) == 2:
                p = item
                q = [x for x in Dup if x != p][0]
                return (p + q)*(abs(p-q))
    elif len(Dup) == 3:
        for item in dice:
            if dice.count(item) == 2:
                qr = [x for x in Dup if x != item]
                return qr[0] * qr[1]
    return min(dice)

print(solution(6,3,3,6))
def solution(order):
    answer = 0
    menu = {'americano': 4500, 'cafelatte': 5000, 'anything': 4500}
    for o in order:
        for m in menu:
            if m in o:
                answer += menu[m]
    return answer

print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
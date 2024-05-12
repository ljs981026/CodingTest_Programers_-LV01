import re
def solution(babbling):
    answer = 0
    for bab in babbling:
        if re.match(r"^(aya|ye|woo|ma)+$", bab):
            answer += 1
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
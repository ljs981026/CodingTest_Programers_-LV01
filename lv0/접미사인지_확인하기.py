def solution(my_string, is_suffix):
    if my_string.endswith(is_suffix) and len(is_suffix) <= len(my_string):
        return 1
    return 0

print(solution("banana", "ana"))
my_string = "banana"
is_prefix = "ban"

def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix) and len(is_prefix) <= len(my_string):
        return 1
    return 0

print(solution(my_string, is_prefix))


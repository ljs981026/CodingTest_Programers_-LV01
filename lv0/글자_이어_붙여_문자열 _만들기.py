def solution(my_string, index_list):
    return ''.join(my_string[i] for i in index_list)

print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
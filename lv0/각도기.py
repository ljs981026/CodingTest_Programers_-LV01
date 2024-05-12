angle_list = ((89,1),(90,2),(179,3),(180,4))
solution = lambda angle : [item[1] for item in angle_list if item[0] >= angle][0]

print(solution(70))
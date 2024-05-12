win_rsp = {'2': '0', '0': '5', '5': '2'}

solution = lambda r : ''.join([win_rsp[i] for i in r])

print(solution("205"))
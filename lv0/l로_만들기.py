solution = lambda ms : ''.join([x if x > 'l' else 'l' for x in ms])

print(solution("abcdevwxyz"))
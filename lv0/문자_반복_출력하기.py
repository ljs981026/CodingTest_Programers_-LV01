solution = lambda my_str, n : ''.join(list(map(lambda x : x*n, my_str))) 

print(solution("hello", 3))
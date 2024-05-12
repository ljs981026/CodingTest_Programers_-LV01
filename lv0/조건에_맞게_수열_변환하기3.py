solution = lambda arr, k : [i+k if k % 2 == 0 else i*k for i in arr]

print(solution([1, 2, 3, 100, 99, 98], 3))
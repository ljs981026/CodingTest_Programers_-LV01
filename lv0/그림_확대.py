def solution(picture, k):
    answer = []
    for pixel in picture:
        n_pixel = ''
        for p in pixel:
            n_pixel += (p * k)
        for i in range(k):            
            answer.append(n_pixel)
    return answer

print(solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."],	2))
from collections import Counter
solution = lambda sa : max(dict(Counter([len(i) for i in sa])).values())

print(solution(["a","bc","d","efg","hi"]))
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.
# 입출력 예
# 입력 #1

# aBcDeFg
# 출력 #1

# AbCdEfG

str = input()
answer = ''
for i in str:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)



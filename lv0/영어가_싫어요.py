def solution(numbers):
    answer = ''
    test = ''
    num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    for n in numbers:
        test += n
        if test in num_dict:
            answer += num_dict[test]
            test = ''    
    return int(answer)

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

print(solution("onefourzerosixseven"))
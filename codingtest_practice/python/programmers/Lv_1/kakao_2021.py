def solution(s):
    num_dicts = {"zero":"0",
                "one":"1",
                "two":"2",
                "three":"3",
                "four":"4",
                "five":"5",
                "six":"6",
                "seven":"7",
                "eight":"8",
                "nine":"9"}

    for num in num_dicts.keys():
        if num in s:
            s = s.replace(num, num_dicts[num])
    return int(s)

print(solution("one4seveneight"))
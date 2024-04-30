"""
S, D, T => 1제곱, 2제곱, 3제곱
* = 스타상, 해당 점수와 바로 전에 얻은 점수를 2배로
# = 아차상, 해당 점수 마이너스

스타상, 아차상은 중첩 가능, 존재하지 않을 수도 있음.
"""

def solution(dartResult):
    SDT_dict = {"S": 1, "D": 2, "T": 3}
    ans = []
    res = ""
    for char in dartResult:
        if char.isdigit():
            res += char
        else:
            if char in SDT_dict:
                res = int(res) ** SDT_dict[char]
                ans.append(res)
                res = ""
            elif char == "*":
                if len(ans) >= 2:
                    ans[-1] *= 2
                    ans[-2] *= 2
                else:
                    ans[-1] *= 2
            elif char == "#":
                ans[-1] *= -1
    return ans


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))


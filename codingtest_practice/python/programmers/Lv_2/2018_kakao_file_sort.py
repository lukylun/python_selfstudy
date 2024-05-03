"""
파일명은 공백, 마침표, "-"로만 이루어져 있음
영문자로 시작
숫자 하나이상 포함

HEAD - NUMBER - TAIL의 세 부분으로 파일명 구성
HEAD는 한 글자 이상의 문자
NUMBER 1자리에서 5자리 숫자 앞에 0이 올 수 있음
TAIL 없을 수도 있음, 숫자가 있을 수도 있음

조건
1) HEAD 부분 기준으로 사전순으로 정렬, 대소문자 구분하지 않음
2) HEAD가 같으면 NUMBER 숫자 순으로 정렬 ex) 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬, 앞의 숫자 0은 무시
3) HEAD와 NUMBER가 같으면 원래 입력에 주어진 순서를 유지
"""

def solution(files):
    answer = []
    combo = []
    for file in files:
        head = ''
        num = ''
        tail = ''

        for idx in range(len(file)):
            if not file[idx].isdigit() and not len(num):
                head += file[idx]
            elif file[idx].isdigit() and len(num) < 5:
                num += file[idx]
            elif file[idx].isdigit() and len(num) >= 5:
                tail += file[idx:]
                break
            elif len(num) and not file[idx].isdigit():
                tail += file[idx:]
                break
        combo.append([head, num, tail])

    combo = sorted(combo, key=lambda x: (x[0].lower(), int(x[1])))
    for comb in combo:
        ans = ''.join(comb)
        answer.append(ans)
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
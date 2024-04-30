"""
id 조건
1) 3자 이상 15자 이하
2) 아이디는 알파벳 소문자, 숫자, -, _, . 만 사용가능
3) .는 처음과 끝에 사용할 수 없음.

7단계 순차적 처리 과정
1) 모든 대문자를 소문자로 치환
2) 알파벳 소문자, 숫자, -, _, . 말고 다 제외
3) .가 2번 이상 연속된 부분을 하나로 치환
4) .가 처음이나 끝에 위치한다면 제거
5) 빈 문자열이라면 new_id "a" 대입
6) new_id 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외하고 다 제거 후 .가 끝이면 .도 제거
7) new_id 길이가 2자 이하라면 길이가 3이 될 때까지 new_id의 마지막 문자를 new_id에 더한다
"""

def solution(new_id):
    answer = ''

    # step 1
    new_id = new_id.lower()

    # step 2
    for i in new_id:
        if i in "~!@#$%^&*()=+[{]}:?,<>/":
            new_id = new_id.replace(i, "")

    # step 3
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    # step 4
    new_id = new_id.strip('.')

    # step 5
    if new_id == "":
        new_id = "a"

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')
    # step 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
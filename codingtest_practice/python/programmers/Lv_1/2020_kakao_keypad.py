"""
왼손 엄지는 *에서
오른손 엄지는 #에서 시작

규칙
1. 상하좌우 4가지 방향 이동, 1칸은 거리 1
2. 1,4,7는 왼손 엄지
3. 3,6,9는 오른손 엄지
4. 2,5,8,0은 현재위치에서 더 가까운 엄지손가락 사용
5. 거리가 같으면 오른손잡이는 오른 엄지손가락, 왼손잡이는 왼 엄지손가락 사용

순서대로 누를 번호 배열 numbers
왼손잡이, 오른손잡이 구분 hand
왼손으로 눌렀는지 오른손으로 눌렀는지 문자열 형태로 return
"""

def solution(numbers, hand):
    keypad = {1: (0, 0),
              2: (0, 1),
              3: (0, 2),
              4: (1, 0),
              5: (1, 1),
              6: (1, 2),
              7: (2, 0),
              8: (2, 1),
              9: (2, 2),
              0: (3, 1),
              "*": (3, 0),
              "#": (3, 2)}
    answer = ''

    left_now = 3, 0
    right_now = 3, 2
    for number in numbers:
        if number in (1, 4, 7):
            answer += "L"
            left_now = keypad[number]
        elif number in (3, 6, 9):
            answer += "R"
            right_now = keypad[number]
        else:
            r, c = keypad[number]
            left_dis = abs(r - left_now[0]) + abs(c - left_now[1])
            right_dis = abs(r - right_now[0]) + abs(c - right_now[1])
            if left_dis < right_dis:
                answer += "L"
                left_now = keypad[number]
            elif left_dis > right_dis:
                answer += "R"
                right_now = keypad[number]
            else:
                if hand == "left":
                    answer += "L"
                    left_now = keypad[number]
                else:
                    answer += "R"
                    right_now = keypad[number]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
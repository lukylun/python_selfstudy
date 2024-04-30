"""
전체 학생의 수 n
체육복 도난당한 학생 배열 lost
여벌의 체육복 학생들의 번호 배열 reserve
순서가 보장 누가 책임? 정렬 안 해도 되나?
"""

def solution(n, lost, reserve):
    # 자기 체육복 잃어버리고 여분 있는 학생 제거 => 자기가 입어야하니까
    lost_pop = [i for i in lost if i not in reserve]
    reserve_pop = [i for i in reserve if i not in lost]

    for i in reserve_pop:
        if i-1 in lost_pop:
            lost_pop.remove(i-1)

        elif i+1 in lost_pop:
            lost_pop.remove(i+1)

    return n - len(lost_pop)

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
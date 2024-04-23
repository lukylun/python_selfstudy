# 산술기하평균은 모두 같은 값일 때 최대임
# (a+b)/2 >= root(ab)
def solution(n, s):
    answer = []
    # n이 s보다 크면 존재하지 않음
    if n > s:
        return [-1]
    # 일단 s를 n으로 나눈 몫을 리스트에 n개를 담는다
    answer = [s // n for _ in range(n)]
    # 나머지가 0이면 그대로 출력
    if s % n == 0:
        return answer
    # 나머지가 0이 아니면 변수에 +1씩 더해준다
    for i in range(s % n):
        answer[i] += 1
    # 정렬해서 값 반환하면 끝.
    return answer.sort()
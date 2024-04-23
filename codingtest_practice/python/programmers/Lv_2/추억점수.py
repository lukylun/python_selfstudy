def solution(name, yearning, photos):
    answer = []
    grade = {}
    for idx in range(max(len(name), len(yearning))):
        grade[name[idx]] = yearning[idx]
    
    
    for photo in photos:
        cnt = 0
        for p in photo:
            if p in grade.keys():
                cnt += grade[p]
        answer.append(cnt)
    return answer
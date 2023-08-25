from collections import deque
def solution(begin, target, words):
    # target이 words에 없으면 0을 리턴  
    if target not in words:
        return 0
    
    # deque 생성
    q = deque()
    # q에 시작단어와 cnt를 담아
    q.append((begin, 0))
    
    # bfs 돌려
    while q:
        # q에서 하나 꺼내고
        word, cnt = q.popleft()
        # 방문배열 생성
        # 알파벳이 몇 개가 맞는지 카운팅 하기 위해
        visited = [0] * len(words)
        
        # word가 target 이면 탈출
        if word == target:
            break
        
        # 알파벳 하나씩 비교해서 visited에 카운팅
        for i in range(len(words)):
            for j in range(len(words[i])):
                if word[j] == words[i][j]:
                    visited[i] += 1
        
        # visited 하나씩 확인하면서
        # begin의 길이보다 1만큼 작은 것만 q에 담고
        # 해당 단어를 두 번 검색 못하도록 cnt를 str으로 바꿔서
        # 해당 단어를 초기화 시킴.
        for i in range(len(visited)):
            if visited[i] == len(begin) - 1:
                q.append((words[i], cnt + 1))
                words[i] = str(cnt)
            
    return cnt
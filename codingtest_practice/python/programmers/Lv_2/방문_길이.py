def solution(dirs):
    d = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)    
    }
    answer = 0
    visited = set()
    r, c = 0, 0

    for dir in dirs:
        dr, dc = d[dir]
        nr, nc = r + dr, c + dc
        go = (r, c, nr, nc)
        back = (nr, nc, r, c)
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            r, c = nr, nc
            if go not in visited:
                visited.add(go)
                visited.add(back)
    
    print(visited)
    print(len(visited)//2)

    return answer

print(solution('ULURRDLLU'))
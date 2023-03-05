dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

T=int(input())
for tc in range(1, T+1):
    answer="NO"
    n=int(input())
    box=[list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if box[i][j] == "o":
                for d in range(8):
                    ans=0
                    for nn in range(1,n+1):
                        if 0<=i+dx[d]*nn<n and 0<=j+dy[d]*nn<n:
                            if box[i+dx[d]*nn][j+dy[d]*nn]=="o":
                                ans+=1
                            else:
                                ans=0
                                break
                        if ans>=4:
                            answer="YES"
    print(f'#{tc} {answer}')
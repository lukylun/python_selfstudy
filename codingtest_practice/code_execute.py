for _ in range(10):
    tc = int(input())
    passwords = list(map(int, input().split()))
    nums = [x for x in range(1, 6)]

    front = 0
    i = 0
    while passwords[front] > 0:        
        passwords[front] -= nums[i]
        
        if passwords[front] <= 0:
            passwords[front] = 0
            break
        
        # front, i 값을 1씩 증가
        front = (front + 1) % 8
        i = (i + 1) % 5
    
    # passwords의 0값의 index
    idx = passwords.index(0)
    print(f'{tc} {" ".join(map(str, passwords[idx + 1:]))} {" ".join(map(str,(passwords[:idx + 1])))}')

    
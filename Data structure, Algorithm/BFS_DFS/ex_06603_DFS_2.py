def dfs(cnt, idx, candi):
    global numbers
    if cnt == 6:
        print(candi)
        return
    for i in range(idx, len(numbers)):
        if cnt == 0:
            new_candi = str(numbers[i])
        else:
            new_candi = candi + " " + str(numbers[i])
        dfs(cnt+1, i+1,new_candi)

while True:
    l = list(map(int,input().split()))
    n = l[0]
    if n == 0:
        break
    numbers = l[1:]
    dfs(0,0,"")
    print()
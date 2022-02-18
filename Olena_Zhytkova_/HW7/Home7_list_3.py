import random
N,M=6,8
matrix=[[random.randrange(1,100)for y in range(M)]for x in range(N)]

for im in range(N):
    print(*matrix[im])

maximum=-0
for j in range(M):
    minimum=100
    for i in range(N):
        if matrix[i][j]<minimum:
            minimum=matrix[i][j]
    if minimum>maximum:
        maximum=minimum 
print(f'The maximum element among the minimum elements:{maximum:4}')               



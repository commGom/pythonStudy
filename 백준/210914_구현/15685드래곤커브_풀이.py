# x,y,d,g 
# 출발지점 x,y, 시작방향, 세대
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
# 0 : (1,0) 1 : (0,-1) 2 : (-1,0) 3 : (0,1)

N = int(input())
map_list = [[0]*101 for _ in range(101)]

dirs = {0:(1,0), 1:(0,-1), 2: (-1,0), 3: (0,1)}

# d=시작방향 / g=세대
for _ in range(N):
    x, y, d, g = map(int, input().split())


    curve_list = [d]

    for _ in range(g):
        curve_list += [(i+1)%4 for i in curve_list[::-1]]

    map_list[y][x] = 1
    for curve in curve_list:
        x = x+dirs[curve][0]
        y = y+dirs[curve][1]
        print(x,y,map_list[y][x])
        map_list[y][x] = 1
        print(x,y,map_list[y][x])
    print(map_list)
cnt = 0
for i in range(100):
    for j in range(100):
        if map_list[i][j] and map_list[i][j+1] and map_list[i+1][j] and map_list[i+1][j+1]:
            cnt += 1
print(cnt)
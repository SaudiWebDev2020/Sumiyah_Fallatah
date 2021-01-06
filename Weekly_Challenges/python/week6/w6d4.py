# FloodFill
# ------------------------------------------------------------------------------------------------------------
# top is [-x,y]
# left is [x,-y] 
# right is [x,+y]
# bottom is [+x,y]

canvas2D = [
    [3,2,3,4,3],
    [2,3,3,4,0],
    [7,3,3,5,3],
    [6,5,3,4,1],
    [1,2,3,3,3]
]

def flood_fill(map,startXY,new_color):
    x = startXY[0]
    y = startXY[1]
    start_value = map[x][y]
    # print('f', map[y][x])
    if map[x][y] == start_value:
        map[x-1][y] = new_color
        map[x][y-1] = new_color
        map[x][1+y] = new_color
        map[1+x][y] = new_color
        return flood_fill(map,startXY,new_color)

print(flood_fill(canvas2D,[2,2],1))

canvas2D_result = [
    [3,2,1,4,3],
    [2,1,1,4,0],
    [7,1,1,5,3],
    [6,5,1,4,1],
    [1,2,1,1,1]
]
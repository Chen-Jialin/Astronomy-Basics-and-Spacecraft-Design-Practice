#Magician
# 开始前需手动设定：分棋子为两栈，一栈置于右士处，自下而上依次为，一士、二炮、五兵/卒，另一栈置于左士处，自下而上依次为一士、将/帅、二车、二马、二相/象，机械臂置于右栈顶呈张开状态
h = 10# 棋子厚度
# 棋子坐标
coordinates = [[0,0],# 将/帅
    [0,-30],# 士
    [0,30],
    [0,-60],# 相/象
    [0,60],
    [0,-90],# 马
    [0,90],
    [0,-120],# 车
    [0,120],
    [57,-90],# 炮
    [57,90],
    [85.5,0],# 兵/卒
    [85.5,-60],
    [85.5,60],
    [85.5,-120],
    [85.5,120]]
rightCoordinate = coordinates[1]
leftCoordinate = coordinates[2]
rightStack = [[85.5,0],# 兵/卒
    [85.5,-60],
    [85.5,60],
    [85.5,-120],
    [85.5,120],
    [57,-90],# 炮
    [57,90]]
leftStack = [[0,-60],# 相/象
    [0,60],
    [0,-90],# 马
    [0,90],
    [0,-120],# 车
    [0,120],
    [0,0]]# 将/帅

# 放置右栈棋子
for n in range(len(rightStack)):
    # 移至指定高度
    dType.SetPTPCmd(api, 7, 0, 0, - n * h, 0, 1)
    dType.dSleep(2000)

    # 抓取棋子
    dType.SetEndEffectorGripper(api, 1, 1)
    dType.dSleep(1000)
    dType.SetEndEffectorGripper(api, 0, 0)

    # 移至指定坐标
    dType.SetPTPCmd(api, 7, 0, 0, h + n * h, 0, 1)# 抬升
    dType.SetPTPCmd(api, 7, rightStack[n][0] - rightCoordinate[0], 0, 0, 0, 1)# x方向平移
    dType.SetPTPCmd(api, 7, 0, rightStack[n][1] - rightCoordinate[1], 0, 0, 1)# y方向平移
    dType.SetPTPCmd(api, 7, 0, 0, - h - len(rightStack) * h, 0, 1)# 下放
    dType.dSleep(8000)

    # 释放棋子
    dType.SetEndEffectorGripper(api, 1, 0)
    dType.dSleep(1000)
    dType.SetEndEffectorGripper(api, 0, 0)

    # 机械臂归位
    dType.SetPTPCmd(api, 7, 0, 0, h + len(rightStack) * h, 0, 1)# 抬升
    dType.SetPTPCmd(api, 7, 0, - (rightStack[n][1] - rightCoordinate[1]), 0, 0, 1)# y方向平移
    dType.SetPTPCmd(api, 7, - (rightStack[n][0] - rightCoordinate[0]), 0, 0, 0, 1)# x方向平移
    dType.SetPTPCmd(api, 7, 0, 0, - h, 0, 1)# 下放
    dType.dSleep(6000)

# 移至左栈
dType.SetPTPCmd(api, 7, 0, 60, 0, 0, 1)
dType.dSleep(1000)

# 放置左栈棋子
for n in range(len(leftStack)):
    # 移至指定高度
    dType.SetPTPCmd(api, 7, 0, 0, - n * h, 0, 1)
    dType.dSleep(2000)

    # 抓取棋子
    dType.SetEndEffectorGripper(api, 1, 1)
    dType.dSleep(1000)
    dType.SetEndEffectorGripper(api, 0, 0)

    # 移至指定坐标
    dType.SetPTPCmd(api, 7, 0, 0, h + n * h, 0, 1)# 抬升
    # dType.SetPTPCmd(api, 7, leftStack[n][0] - leftCoordinate[0], 0, 0, 0, 1)# x方向平移
    dType.SetPTPCmd(api, 7, 0, leftStack[n][1] - leftCoordinate[1], 0, 0, 1)# y方向平移
    dType.SetPTPCmd(api, 7, 0, 0, - h - len(leftStack) * h, 0, 1)# 下放
    dType.dSleep(8000)

    # 释放棋子
    dType.SetEndEffectorGripper(api, 1, 0)
    dType.dSleep(1000)
    dType.SetEndEffectorGripper(api, 0, 0)

    # 机械臂归位
    dType.SetPTPCmd(api, 7, 0, 0, h + len(leftStack) * h, 0, 1)# 抬升
    dType.SetPTPCmd(api, 7, 0, - (leftStack[n][1] - leftCoordinate[1]), 0, 0, 1)# y方向平移
    # dType.SetPTPCmd(api, 7, - (leftStack[n][0] - leftCoordinate[0]), 0, 0, 0, 1)# x方向平移
    dType.SetPTPCmd(api, 7, 0, 0, - h, 0, 1)# 下放
    dType.dSleep(6000)
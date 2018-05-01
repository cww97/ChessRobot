# Document for Dobot

## 文件说明

- `DobotDll/`: dobot公司给的dll，64位的dll
- `DobotControl`, 官方给的demo，先留着吧
- `main.py` main嘛，你懂的嘛，工作在这里
- `README.md`: 本文件，为了让大家看代码不过与难受，后面都讲的这页代码

## 全局变量说明

- `CON_STR`: 连接dobot的时候可能的返回状态
- `api`: 看名字就知道了哈，调用dll
- `relay_point`: 中继节点，有时候不能直接move过去，先到一个中继节点
- `origin_point`: 原点，摄像机不会排到，方面到大部分位置
- `board`: Board类，也就是棋盘
- `chess`: ChessArea类，对应棋子区

## 全局方法说明

- `connect()`: 连接dobot，返回连接状态
- `move(p)`: 移动到p点， p为一个长度为3的list，分别对应xyz坐标
- `set_chess(x, y)`: 对外接口，在(x, y)落子
- `move_around()`: 没事走两圈，溜溜，我也不知道这个方法有什么用，说不定说明时候就删了
- `__main__`: 单元测试的时候用的，喔

## Board类说明

类内的变量有棋盘的规格(9*9)、尺寸(cm)，单位长宽

- `location(self, x, y)`: 讲xy坐标变成实际机械臂要到的xyz坐标
- `down_chess(self, x, y)`: 讲落子指令丢进队列

## ChessArea类说明

// 困了，待续

## api 说明
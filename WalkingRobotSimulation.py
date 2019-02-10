class Solution:
    def robotSim(self, commands: 'List[int]', obstacles: 'List[List[int]]') -> 'int':
        dx,dy = [0,1,0,-1],[1,0,-1,0]
        obstacleSet = obstacleSet = set(map(tuple, obstacles))
        x = y = res = di = 0
        for cmd in commands:
            if cmd == -2:
                di = (di-1)%4
            elif cmd == -1:
                di = (di+1)%4
            else:
                for k in range(cmd):
                    if (x+dx[di],y+dy[di]) not in obstacleSet:
                        x = x+dx[di]
                        y = y+dy[di]
                        res = max(res,x**2+y**2)
        return res

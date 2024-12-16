class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offs = [(1, 2), (2, 1), (2, -1), (1, -2),
                (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        oq = deque([(0, 0, 0)])
        od = {(0, 0): 0}
        tq = deque([(x, y, 0)])
        td = {(x, y): 0}
        while True:
            ox, oy, os = oq.popleft()
            if (ox, oy) in td:
                return os + td[(ox, oy)]
            tx, ty, ts = tq.popleft()
            if (tx, ty) in od:
                return ts + od[(tx, ty)]
            for dx, dy in offs:
                nx, ny = ox + dx, oy + dy
                #double origin and dest pass
                if (nx, ny) not in od:
                    oq.append((nx, ny, os + 1))
                    od[(nx, ny)] = os + 1
                mx, my = tx + dx, ty + dy
                if (mx, my) not in td:
                    tq.append((mx, my, ts + 1))
                    td[(mx, my)] = ts + 1

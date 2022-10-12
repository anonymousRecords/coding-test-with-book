ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
if ax == bx:
    dx = cx
elif ax != bx:
    if ax == cx:
        dx = bx
    elif bx == cx:
        dx = ax
if ay == by:
    dy = cy
elif ay != by:
    if ay == cy:
        dy = by
    elif by == cy:
        dy = ay
print(dx, dy)
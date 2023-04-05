import math

def orientation(p, q, r):
    """ 3 점 p, q, r이 반시계 방향인지 시계 방향인지, 또는 일직선 상에 있는지 확인합니다."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # 일직선
    elif val > 0:
        return 1  # 시계 방향
    else:
        return 2  # 반시계 방향

def convex_hull(points):
    """주어진 점들의 Convex Hull을 찾습니다."""
    n = len(points)
    # 1. 가장 왼쪽 아래에 있는 점을 찾습니다.
    leftmost = points[0]
    for i in range(1, n):
        if points[i][0] < leftmost[0] or (points[i][0] == leftmost[0] and points[i][1] < leftmost[1]):
            leftmost = points[i]

    hull = []  # Convex Hull을 저장할 리스트
    p = leftmost  # 현재 점
    q = None  # 이전에 방문한 점
    while True:
        hull.append(p)
        q = points[0]
        for i in range(1, n):
            if q == p or orientation(p, q, points[i]) == 1 or (orientation(p, q, points[i]) == 0 and
                                                               (points[i][0] - p[0]) ** 2 + (points[i][1] - p[1]) ** 2 >
                                                               (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2):
                q = points[i]
        p = q
        if p == leftmost:
            break

    return hull

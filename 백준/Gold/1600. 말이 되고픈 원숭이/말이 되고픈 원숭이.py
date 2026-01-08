from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]


hourse = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
monkey = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def bfs():
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = 1

    q = deque()
    q.append((0, 0, K, 0))
    
    while q:
        x, y, k, move = q.popleft()
        
        # 목표 지점 도달
        if (x, y) == (H-1, W-1):
            return move

        # 말처럼 이동 K가 1이상
        if k:
            for i, j in hourse:
                nx = x + i
                ny = y + j

                if 0 <= nx < H and 0 <= ny < W:
                    if board[nx][ny] == 0 and visited[nx][ny][k-1] == 0:
                        visited[nx][ny][k-1] = 1
                        q.append((nx, ny, k-1, move+1))

        for i, j in monkey:
            nx = x + i
            ny = y + j

            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = 1
                    q.append((nx, ny, k, move+1))
            
    return -1

print(bfs())
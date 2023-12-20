import heapq
import numpy as np
from time import perf_counter

# 강화 학습을 위한 Q-learning 함수
def heuristic(a, b):
    return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])

def q_learning_update(q_values, state, next_state, reward, alpha, gamma):
    current_q = q_values[state]
    max_next_q = np.max(q_values[next_state])
    updated_q = current_q + alpha * (reward + gamma * max_next_q - current_q)
    q_values[state] = updated_q

def astar_with_q_learning(array, start, goal, alpha, gamma, episodes):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    q_values = {state: 0 for state in np.ndindex(array.shape)}

    for episode in range(episodes):
        current_state = start

        while open_set:
            current_cost, current_node = heapq.heappop(open_set)

            if current_node == goal:
                break

            for i, j in neighbors:
                neighbor = current_node[0] + i, current_node[1] + j
                new_cost = cost_so_far[current_node] + array[current_node]  # Use current_node instead of neighbor

                if 0 <= neighbor[0] < array.shape[0] and 0 <= neighbor[1] < array.shape[1]:
                    if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost + heuristic(goal, neighbor)
                        heapq.heappush(open_set, (priority, neighbor))
                        came_from[neighbor] = current_node

            next_state = current_node
            reward = -array[current_node]  # Inverse of the weighted cost
            q_learning_update(q_values, current_state, next_state, reward, alpha, gamma)

            current_state = next_state

    # 최종 경로 찾기
    path = [(0, 0)]
    while current_node in came_from:
        path.append(current_node)
        current_node = came_from[current_node]

    return path[::-1]

def astar_with_rl(array, start, goal, alpha, gamma, episodes):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    # 초기 Q-values 설정
    q_values = {(i, j): 0 for i in range(len(array)) for j in range(len(array[0]))}

    for episode in range(episodes):
        current_state = start

        while open_set:
            current_cost, current_node = heapq.heappop(open_set)

            if current_node == goal:
                break

            for i, j in neighbors:
                neighbor = current_node[0] + i, current_node[1] + j
                new_cost = cost_so_far[current_node] + 1

                if 0 <= neighbor[0] < len(array) and 0 <= neighbor[1] < len(array[0]) and array[neighbor[0]][neighbor[1]] == 0:
                    if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost + heuristic(goal, neighbor)
                        heapq.heappush(open_set, (priority, neighbor))
                        came_from[neighbor] = current_node

            # Q-learning 업데이트
            next_state = current_node
            reward = -heuristic(goal, next_state)  # 휴리스틱 역의 값 사용
            q_learning_update(q_values, current_state, next_state, reward, alpha, gamma)

            current_state = next_state

    # 최종 경로 찾기
    path = [(0, 0)]
    while current_node in came_from:
        path.append(current_node)
        current_node = came_from[current_node]

    return path[::-1]



# 메이즈 생성기
def generate_smooth_maze(rows, columns, density=0.5, generations=5):
    while True:
        maze = np.zeros((rows, columns), dtype=int)

        # Randomly initialize cells with walls
        for i in range(rows):
            for j in range(columns):
                maze[i][j] = 1 if np.random.rand() < density else 0

        # Cellular automaton rule for maze generation
        for _ in range(generations):
            new_maze = np.copy(maze)
            for i in range(1, rows-1):
                for j in range(1, columns-1):
                    neighbors = maze[i-1:i+2, j-1:j+2]
                    wall_count = np.sum(neighbors)
                    if wall_count >= 6:  # Adjust this threshold for thickness
                        new_maze[i][j] = 1
                    elif wall_count <= 3:
                        new_maze[i][j] = 0
            maze = new_maze

        # Ensure the start and end points are clear
        maze[0][0] = maze[rows-1][columns-1] = 0

        # Check if the start and end points are connected
        if is_connected(maze, (0, 0), (rows-1, columns-1)):
            return maze

# Helper function to check if two points are connected in the maze
def is_connected(maze, start, end):
    visited = set()

    def dfs(x, y):
        if (x, y) == end:
            return True
        visited.add((x, y))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                if dfs(nx, ny):
                    return True
        return False

    return dfs(*start)

# Example: Generate a 10x10 smooth maze with higher connectivity probability
rows, columns = 15, 15
maze = generate_smooth_maze(rows, columns, density=0.5, generations=5)
np.set_printoptions(precision=1, suppress=False)
originmaze = maze+0



start = (0, 0)
goal = (4, 4)

alpha = 0.1  # 학습률
gamma = 0.9  # 감가율
episodes = 100  # 에피소드 수

t = perf_counter()
result = astar_with_q_learning(maze, start, goal, alpha, gamma, episodes)
origin_res = astar_with_rl(originmaze, start, goal, alpha, gamma, episodes)
print(perf_counter()-t)

def mazeres(maze):
    maze_res = np.minimum(maze+np.random.random((15, 15))*0.5, 1)
    result = astar_with_q_learning(maze_res, start, goal, alpha, gamma, episodes)
    for i in result:
        maze_res[i[0], i[1]] += 2
    return maze_res

for i in origin_res:
    originmaze[i[0], i[1]] += 2
print(originmaze)


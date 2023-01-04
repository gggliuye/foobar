
def in_range(coordinate, height, width):
    return coordinate[0] < height and coordinate[0] >= 0 and coordinate[1] < width and coordinate[1] >= 0

def dijkstra(distances, frontier, height, width):
    movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while len(frontier) > 0:
        # extend frontier
        nexts = []
        for ele in frontier:
            ele_dist = distances[ele[0]][ele[1]]
            for move in movements:
                next = [ele[0] + move[0], ele[1] + move[1]]
                if in_range(next, height, width) and distances[next[0]][next[1]] == 100000:
                    if not next in nexts:
                        nexts.append(next)
                    # update distances
                    new_distance = ele_dist + 1
                    if new_distance < distances[next[0]][next[1]]:
                        distances[next[0]][next[1]] = new_distance
        # end of while
        frontier = nexts
    return distances


def in_range(coordinate, height, width):
    return coordinate[0] < height and coordinate[0] >= 0 and coordinate[1] < width and coordinate[1] >= 0

def dijkstra(distances, frontier, height, width):
    movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while len(frontier) > 0:
        # extend frontier
        nexts = []
        for ele in frontier:
            ele_dist = distances[ele[0]][ele[1]]
            for move in movements:
                next = [ele[0] + move[0], ele[1] + move[1]]
                if in_range(next, height, width) and distances[next[0]][next[1]] == 100000:
                    if not next in nexts:
                        nexts.append(next)
                    # update distances
                    new_distance = ele_dist + 1
                    if new_distance < distances[next[0]][next[1]]:
                        distances[next[0]][next[1]] = new_distance
        # end of while
        frontier = nexts
    return distances


def find_max_jump(distance_M, height, width):
    movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    max_jump = 0
    from_to = [-1, -1]
    # the two ends must locate in the shortest path
    for i in range(height):
        for j in range(width):
            ele = [i, j]
            dist_ele = distance_M[i][j]
            if dist_ele < 0 or dist_ele == 100000:
                continue
            for move in movements:
                next = [ele[0] + move[0], ele[1] + move[1]]
                if not in_range(next, height, width):
                    continue
                if distance_M[next[0]][next[1]] > 0 :
                    # not a wall
                    continue
                next_2 = [ele[0] + 2 * move[0], ele[1] + 2 * move[1]]
                if not in_range(next_2, height, width):
                    continue

                next_2_dist = distance_M[next_2[0]][next_2[1]]
                if next_2_dist == 100000 or next_2_dist < 0:
                    continue

                jump = next_2_dist - dist_ele - 2
                if jump > max_jump:
                    max_jump = jump
                    from_to = [next_2_dist, dist_ele]
    return max_jump, from_to


def solution_wrong(M):
    # make 1 (walls) to be -1 to indicate unavailable
    # make 1 (walls) to be inf to indicate not arrived yet
    height = len(M)
    width = len(M[0])
    for i in range(height):
        for j in range(width):
            if M[i][j] == 1:
                M[i][j] = -1
            else:
                # since length/width are max 20
                # 100000 is large enough
                M[i][j] = 100000
    M[0][0] = 1

    # start from the beginning point
    distance_M = dijkstra(M, [[0, 0]], height, width)
    if distance_M[-1][-1] == 100000:
        distance_M[-1][-1] = 10000
        distance_M = dijkstra(M, [[height - 1, width - 1]], height, width)

    current_length = distance_M[-1][-1]

    # find the place to break the wall
    max_jump, from_to = find_max_jump(distance_M, height, width)
    if max_jump < 1:
        return current_length

    if from_to[0] >= 10000:
        return from_to[0] - 10000 + 2 + from_to[1]

    return current_length - max_jump


def solution(M):
    # make 1 (walls) to be -1 to indicate unavailable
    # make 1 (walls) to be inf to indicate not arrived yet
    height = len(M)
    width = len(M[0])
    walls = []
    for i in range(height):
        for j in range(width):
            if M[i][j] == 1:
                M[i][j] = -1
                walls.append([i, j]);
            else:
                # since length/width are max 20
                # 100000 is large enough
                M[i][j] = 100000
    M[0][0] = 1

    # check for all the cases
    min_length = 100000
    for wall in walls:
        M_tmp = M[:]
        # reset the distance map
        for i in range(height):
            for j in range(width):
                if M_tmp[i][j] != -1:
                    M_tmp[i][j] = 100000
        M_tmp[wall[0]][wall[1]] = 100000
        M_tmp[0][0] = 1

        M_tmp = dijkstra(M_tmp, [[0, 0]], height, width)
        if M_tmp[-1][-1] < min_length:
            min_length = M_tmp[-1][-1]
        M_tmp[wall[0]][wall[1]] = -1

    return min_length



def test(M):
    res = solution(M)
    print(res)

test([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
test([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 0, 0]])

test([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
test([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

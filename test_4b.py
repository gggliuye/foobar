
class PathElement:
    def __init__(self, current, previous, flow, undo = False):
        self.current = current
        self.previous = previous
        self.flow = flow
        self.undo = undo


def tree_from_entrance(entrance, map_raw, current_flow):
    # make a tree from the given entrance
    routes_tree = {entrance: PathElement(entrance, -1, 0)}
    frontier = [entrance]
    while len(frontier) > 0:
        new_frontier = []
        for curr in frontier:
            # find all valid nexts
            for next in range(len(map_raw)):
                if next in routes_tree:
                    # since we are only finding one path
                    # skip the already visited node
                    continue

                flow_tmp = current_flow[next][curr]
                flow = map_raw[curr][next] - current_flow[curr][next]
                if flow > 0:
                    # we have more capability in this path
                    routes_tree[next] = PathElement(next, curr, flow)
                    new_frontier.append(next)
                elif flow_tmp > 0:
                    # allow undo flow
                    routes_tree[next] = PathElement(next, curr, flow_tmp, True)
                    new_frontier.append(next)

        frontier = new_frontier
    return routes_tree


def pick_path_to_exit(routes_tree, exit):
    if exit not in routes_tree:
        return False, [], -1

    path = [routes_tree[exit]]
    current = exit
    min_flow = 2000000
    while True:
        ele = routes_tree[current]
        if ele.flow > 0 and ele.flow < min_flow:
            min_flow = ele.flow
        if ele.previous < 0:
            break
        path.append(routes_tree[ele.previous])
        current = ele.previous
    # revert the path
    path.reverse()
    return True, path, min_flow



def find_one_path(entrances, exits, map_raw, current_flow):
    # find a path from entrances to exits
    for entrance in entrances:
        routes_tree = tree_from_entrance(entrance, map_raw, current_flow)

        for exit in exits:
            ret, path, min_flow = pick_path_to_exit(routes_tree, exit)
            if ret:
                return True, path, min_flow
    return False, [], -1



def solution(entrances, exits, map):
    # it is a max flow problem
    # given a directed graph, compute the max flow through entrances to exits

    # initialize the current flow by zeros
    current_flow = []
    for i in range(len(map)):
        current_flow.append([0 for i in range(len(map))])

    while True:
        ret, path, min_flow = find_one_path(entrances, exits, map, current_flow)
        if not ret:
            break
        # fill the path with flow
        for i in range(1, len(path)):
            curr = path[i].current
            prev = path[i].previous
            if path[i].undo:
                current_flow[prev][curr] = current_flow[prev][curr] - min_flow
            else :
                current_flow[prev][curr] = current_flow[prev][curr] + min_flow


    # count the flow output
    result = 0
    for exit in exits:
        for i in range(len(map)):
            result = result + current_flow[i][exit]
    return result



print("\n problem 1: ")
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))

#Input:
print("\n problem 2: ")
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

print("\n problem 3: ")
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 4, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

print("\n problem 4: ")
print(solution([0], [3], [[0, 2, 3, 0], [0, 0, 0, 3], [0, 5, 0, 2], [0, 0, 0, 0]]))

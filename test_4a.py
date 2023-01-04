
def get_target_candidates(region_size, start, target, max_length):
    flip_cnt_x_max = max_length / region_size[0] + 1
    flip_cnt_y_max = max_length / region_size[1] + 1

    current_x = target[0]
    length_x_0 = 2 * (region_size[0] - target[0])
    length_x_1 = 2 * target[0]
    x_dicts = {current_x}
    x_dicts.add(-current_x)
    for cnt_x in range(flip_cnt_x_max):
        # flip in x axis (w.r.t. to y axis)
        if cnt_x%2 == 0:
            current_x = current_x + length_x_0
        else:
            current_x = current_x + length_x_1
        x_dicts.add(current_x)
        x_dicts.add(-current_x)

    current_y = target[1]
    length_y_0 = 2 * (region_size[1] - target[1])
    length_y_1 = 2 * target[1]
    y_dicts = {current_y}
    y_dicts.add(-current_y)
    for cnt_y in range(flip_cnt_y_max):
        # flip in x axis (w.r.t. to y axis)
        if cnt_y%2 == 0:
            current_y = current_y + length_y_0
        else:
            current_y = current_y + length_y_1
        y_dicts.add(current_y)
        y_dicts.add(-current_y)

    # make the points
    target_candidates = []
    max_length_sqr = max_length * max_length

    dy_sqr_list = []
    for y in y_dicts:
        dy = start[1] - y
        dy_sqr_list.append(dy * dy)

    for x in x_dicts:
        dx = start[0] - x
        dx_sqr = dx * dx
        cnt = 0
        for y in y_dicts:
            dy_sqr = dy_sqr_list[cnt]
            cnt = cnt + 1
            if (dx_sqr + dy_sqr) > max_length_sqr:
                continue
            target_candidates.append([x, y])
    return target_candidates

def get_quadrant_slope(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    quadrant = 0
    if dx > 0 and dy >= 0:
        quadrant = 0
    elif dx <= 0 and dy > 0:
        quadrant = 1
    elif dx < 0 and dy <= 0:
        quadrant = 2
    else:
        quadrant = 3
    if dx == 0:
        return quadrant, "inf", dx * dx + dy * dy
    return quadrant, 1.0 * dy / dx, dx * dx + dy * dy


def filter_special_case(special_candidates, start, slope_candidates):
    for target_t in special_candidates:
        quadrant, slope, sqr_length = get_quadrant_slope(start, target_t)
        if sqr_length == 0:
            continue
        if slope not in slope_candidates[quadrant]:
            continue

        if sqr_length < slope_candidates[quadrant][slope]:
            del slope_candidates[quadrant][slope]


def solution(region_size, start, target, max_length):
    target_candidates = get_target_candidates(region_size, start, target, max_length)

    # * filter traget candidates in the same line
    #   since distance < 1e5, we could check with double
    # * each slope could have one single result in each quadrant
    slope_candidates = {0:{}, 1:{}, 2:{}, 3:{}}
    for target_t in target_candidates:
        quadrant, slope, sqr_length = get_quadrant_slope(start, target_t)
        if slope not in slope_candidates[quadrant]:
            slope_candidates[quadrant][slope] = sqr_length
        elif sqr_length < slope_candidates[quadrant][slope]:
            slope_candidates[quadrant][slope] = sqr_length

    # check if the candidates pass the beginning
    start_candidates = get_target_candidates(region_size, start, start, max_length)
    filter_special_case(start_candidates, start, slope_candidates)

    # filter hit corner case
    corner_candidates = get_target_candidates(region_size, start, start, max_length)
    filter_special_case(corner_candidates, start, slope_candidates)

    # if start in a corner, we might has limited available quadrant
    invalid_quadrant = set()
    if start[0] == 0:
        invalid_quadrant.add(1)
        invalid_quadrant.add(2)
    elif start[0] == region_size[0]:
        invalid_quadrant.add(0)
        invalid_quadrant.add(3)

    if start[1] == 0:
        invalid_quadrant.add(2)
        invalid_quadrant.add(3)
    elif start[1] == region_size[1]:
        invalid_quadrant.add(0)
        invalid_quadrant.add(1)

    for key in invalid_quadrant:
        del slope_candidates[key]

    # count the final result
    result = 0
    for key in slope_candidates:
        result = result + len(slope_candidates[key])
    return result;

# solution.solution([3,2], [1,1], [2,1], 4) # 7
# solution.solution([300,275], [150,150], [185,100], 500) # 9

print(solution([3,2], [0,0], [2,1], 4))
print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
print(solution([3,2], [1,1], [2,1], 2000))

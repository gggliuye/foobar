
def process(num_blocks, start_step_blocks, buffer):
    key = str(num_blocks) + "_" + str(start_step_blocks)
    if key in buffer:
        rest = buffer[key]
        return rest[0], rest[1]
    if start_step_blocks > num_blocks:
        return 0, True

    # return number of possible solution
    num_left = num_blocks - start_step_blocks
    if num_left <= start_step_blocks:
        return 1, True

    solutions = 0
    new_start_step_blocks = start_step_blocks + 1
    while new_start_step_blocks <= num_left:
        new_sols, if_break = process(num_left, new_start_step_blocks, buffer)

        # buffer the solution
        key_t = str(num_left) + "_" + str(new_start_step_blocks)
        if key_t not in buffer:
            buffer[key_t] = [new_sols, if_break]

        solutions = solutions + new_sols
        new_start_step_blocks = new_start_step_blocks + 1
        if if_break:
            break

    return solutions, False


def solution(N):
    buffer = {}
    solutions, _ = process(N, 0, buffer)
    return solutions - 1

print(3, solution(3))
print(4, solution(4))
print(5, solution(5))
print(6, solution(6))
print(200, solution(200))

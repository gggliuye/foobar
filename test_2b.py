def run_iteration(numbers, k, b):
    # make x
    x = sorted(numbers, reverse=True)

    # make y
    y = sorted(numbers, reverse=False)
    
    # compute z
    z = []
    for i in range(k):
       x_i = x[k - i - 1]
       y_i = y[k - i - 1]
       if x_i < y_i:
           # this won't happen for the begginng numbers
           x[k - i - 2] = x[k - i - 2] - 1
           x_i = x_i + b
       z.append(x_i - y_i)

    z.reverse()
    return z
    

def make_base_ten(z, k, b):
    # make the number to base ten
    result = 0
    base = 1
    for i in range(k):
       result = result + z[k - i - 1] * base
       base = base * b
    return result


def solution(n, b):
    # extract numbers in n and get k 
    numbers = []
    for i in range(len(n)):
        numbers.append(int(n[i]))

    k = len(numbers)
    init = make_base_ten(numbers, k, b)
    queue = [init]
    number_set = {init: 0}
    num_iter = 0

    while True:
        num_iter += 1
        numbers = run_iteration(numbers, k, b)
    	number = make_base_ten(numbers, k, b)
        if number in number_set:
            return num_iter - number_set[number]
        queue.append(number)
        number_set[number] = num_iter

    return 0


print(solution('1211', 10))
print(solution('210022', 3))

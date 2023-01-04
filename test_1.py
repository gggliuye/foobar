from collections import Counter
import random

def solution_wr(data, n):
    counted = Counter(data)
    result = []
    for ele in data:
        if counted[ele] <= n:
           result.append(ele)
    return result

def solution0(data, n): 
    # Your code here
    max_num = 100
    data_sum = [0 for i in range(max_num)]
    
    check_list = []
    for ele in data:
        if data_sum[ele] > n:
            continue
        data_sum[ele] = data_sum[ele] + 1
        if data_sum[ele] <= n:
            check_list.append(ele)

    result = []
    for ele in check_list:
        if data_sum[ele] > 0 and data_sum[ele] <= n:
            result.append(ele)

        data_sum[ele] = 0
    return result


def solution(data, n): 
    # Your code here
    data_dict = {}

    recheck_list = []
    for ele in data:
        cnt = 0
        if ele not in data_dict:
            data_dict[ele] = 0
        else:
            cnt = data_dict[ele]

        if cnt > n:
            continue
        else:
            recheck_list.append(ele)

        data_dict[ele] = cnt + 1

    result = []
    for ele in recheck_list:
        if data_dict[ele] > 0 and data_dict[ele] <= n:
            result.append(ele)
        #data_dict[ele] = 0

    return result



print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
print(solution([2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 1, -1, -1, -2, -4], 1))
print(solution_wr([2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 1, -1, -1, -2, -4], 1))


# make an random test

num_test = 1000
test_body = []
for i in range(num_test):
  test_body.append(random.randrange(100))

print(solution(test_body, 10))
print(solution_wr(test_body, 10))




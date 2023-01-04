from collections import Counter
import random


def solution(data): 
    list_0 = []
    list_1 = []
    list_2 = []
    
    for ele in data:
        if ele % 3 == 0:
            list_0.append(ele)
        elif ele % 3 == 1:
            list_1.append(ele)
        else:
            list_2.append(ele)
    
    # all the element in list_0 could be added

    # add list_1 & list_2 separately
    num_in_list1 = len(list_1) / 3
    num_in_list2 = len(list_2) / 3
    rest_list1 = len(list_1) % 3
    rest_list2 = len(list_2) % 3

    # add list_1 list_2 pair
    num_pair = min(rest_list1, rest_list2)

    take_from_list1 = num_in_list1 * 3 + num_pair
    take_from_list2 = num_in_list2 * 3 + num_pair

    list_1.sort(reverse=True)
    list_2.sort(reverse=True)

    for i in range(take_from_list1):
        list_0.append(list_1[i])
    
    for i in range(take_from_list2):
        list_0.append(list_2[i])

    result = 0
    list_0.sort(reverse=False)

    for i in range(len(list_0)):
        result = result + pow(10, i) * list_0[i]

    return result


print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))



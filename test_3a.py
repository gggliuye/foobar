
def check_larger(M, F):
    if len(M) > len(F):
        return True
    if len(F) > len(M):
        return False
    # F and M has the same size
    for idx in range(len(F)):
        if F[idx] != M[idx]:
            return M[idx] > F[idx]
    # they are equal
    return True


def remove_heading_zeros(list_num):
    while len(list_num) > 0 and list_num[0] == 0:
        list_num.remove(0)
    return list_num


def larger_minus_smaller(larger, smaller):
    # larger = larger - smaller
    for i in range(len(smaller)):
        idx_l = len(larger) - i - 1
        int_l = larger[idx_l]
        int_s = smaller[len(smaller) - i - 1]
        if int_l < int_s:
            larger[idx_l - 1] = larger[idx_l - 1] - 1
            int_l = int_l + 10
            
        larger[idx_l] = int_l - int_s

    # fix negative value
    for i in range(len(larger)):
        idx_l = len(larger) - i - 1
        if larger[idx_l] < 0:
            larger[idx_l - 1] = larger[idx_l - 1] - 1
            larger[idx_l] = larger[idx_l] + 10
    return remove_heading_zeros(larger)


def run_iteration(m_list, f_list):
    # find the smaller element
    if check_larger(m_list, f_list):
        smaller = f_list
        larger = m_list
    else:
        smaller = m_list
        larger = f_list

    # if larger one is to many times larger
    # fasten the iteration by directly apply multiple substraction
    delta = len(larger) - len(smaller)
    if delta > 1:
        # process 10^(delta-1) substraction
        iter_used = pow(10, delta - 1)
        smaller_tmp = smaller[:]
        for i in range(delta - 1):
            smaller_tmp.append(0)
        return larger_minus_smaller(larger, smaller_tmp), smaller, iter_used


    larger = larger_minus_smaller(larger, smaller)
    return larger, smaller, 1


def check_quit(m_list, f_list):
    if len(m_list) < 1 or len(f_list) < 1:
        return True
    if len(m_list) == 1:
        if m_list[0] == 0:
            return True

    if len(f_list) == 1:
        if f_list[0] == 0:
            return True

    if len(m_list) == len(f_list):
        if len(m_list) == 1:
            if f_list[0] == 1 and m_list[0] == 1:
                return True
        is_same = True
        for i in range(len(m_list)):
            if m_list[i] != f_list[i]:
                is_same = False
                break
        if is_same:
             return True
        
    return False


def to_int_list(string):
    result = []
    for i in range(len(string)):
        result.append(int(string[i]))
    return result


def check_list(m_list):
    for ele in m_list:
        if ele > 9 or ele < 0:
            return False
    return True


def solution(M, F):
    num_iter = 0
    m_list = remove_heading_zeros(to_int_list(M))
    f_list = remove_heading_zeros(to_int_list(F))
    while not check_quit(m_list, f_list):
        m_list, f_list, iter_used = run_iteration(m_list, f_list)
        num_iter = num_iter + iter_used
        #print(num_iter, m_list, f_list)
        if not check_list(m_list):
            break
        if not check_list(f_list):
            break

    if len(m_list) == len(f_list):
        if len(m_list) == 1:
            if f_list[0] == 1 and m_list[0] == 1:
                return str(num_iter)
    return 'impossible'


print(solution('1', '1'))
print(solution('2', '1'))
print(solution('7', '4'))
print(solution('1', '101'))
print(solution('0000144556548645454213', '11215484952412554452'))
print(solution('1121548495242164512125544554654122', '1445565486416546146642843132121545421311'))
#print(solution('1415641312312313123131312154849524216451212554455465411', '1415641312312313123131312154849524216455212554455465412'))

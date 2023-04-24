def print_task_result(v_list list)
    v_list.sort()
    print(fMin = {v_list[0]}, max = {v_list[-1]}, sum = {sum(v_list)})


print_task_result([int(i) for i in input().split()])

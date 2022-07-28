# Selection-Sort Algorithm by Ruzen
# 2022-07-28 First try

def selectionSort (input_list):
    for unsorted_head_index in range(len(input_list)):
        # Find minimum element's index in unsorted list
        min_target_index = unsorted_head_index
        for i in range(unsorted_head_index, len(input_list)):
            if input_list[min_target_index] > input_list[i]:
                min_target_index = i
        # insert it to sorted list and, arrange unsorted list
        for i in range(min_target_index - unsorted_head_index):
            temp = input_list[min_target_index - i]
            input_list[min_target_index - i] = input_list[min_target_index - i - 1]
            input_list[min_target_index - i - 1] = temp
    return input_list
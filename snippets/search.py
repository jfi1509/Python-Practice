# Program for Linear and Binary search

def linear_search(num_list, num_search):
    for index, number in enumerate(num_list):
        if(number == num_search):
            return index

    return -1


def binary_search(num_list, num_search):
    left_index = 0
    right_index = len(num_list) - 1

    while(left_index < right_index):
        mid_index = (left_index + right_index)/2
        mid_number = num_list[mid_index]

        if(mid_number == num_search):
            return mid_index
        
        if(mid_number < num_search):
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(num_list, low, high, num_search):
    left_index = low
    right_index = high

    if(left_index < right_index):
        mid_index = (left_index + right_index)/2
        mid_number = num_list[mid_index]

        if(mid_number == num_search):
            return mid_index
        
        elif(mid_number < num_search):
            binary_search_recursive(num_list, mid_index+1, high, num_search)
        else:
            binary_search_recursive(num_list, low, mid_index-1, num_search)
    
    else:
        return -1


def ballon_arrow_problem(ballon_height):
    arrows_num = 0
    rev_height = ballon_height[::-1]

    for index, height in enumerate(rev_height):
        elements_to_remove = []
        list_to_check = rev_height[index+1 :len(rev_height)]

        if(height+1 not in list_to_check):
            arrows_num = arrows_num + 1
        else:
            for num in list_to_check:
                if(num - height == 1):
                    elements_to_remove.append(num)
                    height = height + 1
            
            [rev_height.remove(number) for number in elements_to_remove]
            arrows_num = arrows_num + 1

    return arrows_num


def main():
    # Number list and number to search
    num_list = [23, 34, 56, 78, 90, 123, 345, 567, 1000]
    num_search = 90
    found_index = -1

    # ballon_height = [5, 6, 7, 8, 9]
    # ballon_height = [5, 4, 5, 4, 3, 1, 2] # o/p = 3
    ballon_height = [7, 6, 2, 1, 5, 4, 3] # o/p = 3
    # ballon_height = [2, 1, 4]
    # ballon_height = [9, 8, 3, 2, 7, 6, 5]
    # ballon_height = [2, 3]
    # ballon_height = [5, 5, 6, 7, 5, 4, 8, 10]

    search_choice = int(input(
        "Choose type of search \n1. Linear Search \n2. Binary Search \n3. Balloon problem\n4. Binary Search Recursive\n"))
    if search_choice == 1:
        found_index = linear_search(num_list, num_search)
    elif search_choice == 2:
        found_index = binary_search(num_list, num_search)
    elif search_choice == 3:
        found_index = ballon_arrow_problem(ballon_height)
    elif search_choice == 4:
        found_index = binary_search_recursive(num_list, 0, len(num_list)-1, num_search)
    else:
        print("Choice is Invalid")
    
    print(found_index+1)


main()
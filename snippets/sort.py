# Bubble sort
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        # flag to check for already sorted numbers
        swapped = False
        for j in range(size-1-i):
            if(elements[j] > elements[j+1]):
                # sort the numbers
                elements[j+1], elements[j] = elements[j], elements[j+1]
                swapped = True
    
        if not swapped:
            break


def insertion_sort(elements):
    size = len(elements)
    for i in range(1, size):
        anchor_element = elements[i]
        j = i - 1
        while(j >= 0 and elements[j] > anchor_element):
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor_element


def insertion_sort_diff_way(elements):
    for i in range(len(elements)):
        for j in reversed(range(i)):
            if(elements[j+1] < elements[j]):
                elements[j+1], elements[j] = elements[j], elements[j+1]



def main():
    elements = [4, 3, 1, 10, 6, 7, 33, 20, 11]
    print('Before sorting : {}'.format(elements))

    sort_choice = int(input("Choose type of sort \n1. Bubble Sort \n2. Insertion Sort \n3. Insertion Sort Diff way\n"))
    if sort_choice == 1:
        bubble_sort(elements)
    if sort_choice == 2:
        insertion_sort(elements)
    if sort_choice == 3:
        insertion_sort_diff_way(elements)
    else:
        print('Invalid choice')

    print('After sorting : {}'.format(elements))

main()
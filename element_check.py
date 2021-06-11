def sorting(x):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


def search_binary(search_list, element, left_half, right_half):
    if left_half > right_half:
        return False

    middle = left_half + (right_half - left_half) // 2
    if search_list[middle] == element:
        if search_list[0] == element:
            return f'Entered value is minimal in a list, index of next element is 0'
        elif search_list[-1] == element:
            return f'Entered value is maximum in a list, index of previous element is {len(search_list) - 2}'
        else:
            x = 1
            while search_list[middle] == search_list[middle - x]:
                x += 1
            return f'Index of previous element is {middle - x}, index of next is {middle - x + 2}'

    elif element < search_list[middle]:
        return search_binary(search_list, element, left_half, middle - 1)
    else:
        return search_binary(search_list, element, middle + 1, right_half)


def check_value_index():
    while type:
        entered_value = input("Enter integer values with whitespaces between them: ")
        try:
            base_list = list(map(int, entered_value.split()))
            if len(base_list) == 0:
                raise ValueError
        except ValueError:
            print("Please make sure you entered integer values with whitespaces between them! ")
        else:
            break

    while True:
        number = input("Enter integer value: ")
        try:
            new_element = int(number)
        except ValueError:
            print('"{0}" is not an integer value'.format(number))
        else:
            break
    changed_list = base_list + [new_element]
    print(search_binary(sorting(changed_list), new_element, 0, len(changed_list)))


check_value_index()

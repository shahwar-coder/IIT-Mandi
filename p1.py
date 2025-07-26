def find_unique_elements(input_list):
    unique_elements = []
    for item in input_list:
        if input_list.count(item) == 1:
            unique_elements.append(item)
    return unique_elements

my_list = [1, 2, 2, 3, 4, 5, 3, 6, 4]
result = find_unique_elements(my_list)
print(result)

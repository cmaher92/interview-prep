# 4/13  1 hour
# 4/14  1 hour

my_list = [1, 2, 3, 4]

def get_products_of_all_ints_except_at_index(my_list):
    new_list = []
    for item in my_list:
        for nested_item in my_list:
            if item != nested_item:
                item *= nested_item
            else:
        new_list.append(item)
    print(new_list)


print(get_products_of_all_ints_except_at_index(my_list))

# use two loops to multiply the integer at every index by the integer at every
# nested_index, unless index == nested_index.

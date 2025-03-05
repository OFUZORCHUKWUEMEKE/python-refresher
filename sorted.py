numbers = [6,9,3,1]
sort = sorted(numbers)
print(sort)

numbers_set = {6,9,3,1}
sort_set = sorted(numbers_set)
print(sort_set)

string_numbers = "6931"
sort_string = sorted(string_numbers)
print(sort_string)


new_numbers = [6,9,3,1,100,290]
new_numbers_ref =sorted(new_numbers, reverse=True)
print(new_numbers_ref)
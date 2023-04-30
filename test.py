# Task 1
def get_student_names(names_dict):
    names_list = [name for name in names_dict.values()]
    return names_list

print(get_student_names({
    "Студент 1": "Артем",
    "Студент 2": "Иван",
    "Студент 3": "Роман"
}))


# Task 2
def three_args(var1, var2, var3):
    args_values = locals()
    for key, value in args_values.items():
        if value:
            print(f'{key} = {value}', end=', ')

three_args(None, None, 2)
print()
# Task 3

def my_max(*args):
    max_n = 0
    for i in args:
        if type(i) is list:
            for j in i:
                if j > max_n:
                    max_n = j
        elif type(i) is int:
            if i > max_n:
                max_n = i
        elif type(i) is str:
            max_n = ''
            for j in i:
                if j > max_n:
                    max_n = j
    return max_n
print(my_max([1, 2, 3, 4]))
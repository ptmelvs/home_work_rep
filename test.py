
def get_student_names(names_dict):
    names_list = [name for name in names_dict.values()]
    return names_list
print(get_student_names({
    "Студент 1": "Артем",
    "Студент 2": "Иван",
    "Студент 3": "Роман"
}))

# Task 1

def min_to_sec(var_minute):
    return var_minute * 60

result = min_to_sec(int(input('Введите количество минут: ')))
print(f'{result // 60} минут = {result} секунд')


# Task 2

def year_to_day(var_year):
    return var_year * 365

days = year_to_day(int(input('Введите количество лет: ')))
print(f'{days // 365} лет = {days} дней')
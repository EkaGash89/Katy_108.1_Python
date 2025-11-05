#Високосный год
def is_year_leap(year):
    return False if year % 4 == 0 else True

god = int(input("Введите год: "))

result = is_year_leap(god)

print(f"Год {god}? - {result}")
import datetime

year_input, month_input, day_input = input().split()
class_date = datetime.date(int(year_input), int(month_input), int(day_input))
delta_input = int(input())
class_delta = datetime.timedelta(days=delta_input)
class_sum = class_date + class_delta
print(class_sum.year, class_sum.month, class_sum.day)

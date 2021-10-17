import time
import pandas

day_hours = 24
week_days = 7.3
print(type(day_hours), type(week_days), day_hours * week_days, 2)

some_str: int = "abcdef"
print(type(some_str), some_str[:3], f'23 {some_str}')

# dir(str)
# dir(__builtins__)
# help(int.bit_count)

some_list = [1, 3, 4, 4]
print(type(some_list), some_list, 'avr:', sum(
    some_list) / len(some_list), some_list[1:3])

a = 'a'
some_dir = {a: 5, "b": 7}
print(type(some_dir), some_dir, some_dir.values())

some_tuple = (1, 2)
print(type(some_tuple), some_tuple)

print(['abc', 'def', 'ghi', 'jkl', 'mno'][-2][-2])

# experience_years = int(input("Enter your experience in months: ")) / 12

temps = [10, 20, 15, 60]
new_temps_1 = [temp / 10 for temp in temps if temp % 2 == 0]
new_temps_2 = [temp / 10 if temp % 2 == 0 else 'asd' for temp in temps]
print('Comprehension', new_temps_1, new_temps_2)


def sum_of(a, *args):
    to_sum = list(args)
    to_sum.append(a)
    return sum(to_sum)


print(type(sum_of), sum_of(1, 2, 3))

print('Sleeping...')
time.sleep(1)
print('Slept 1 sec')

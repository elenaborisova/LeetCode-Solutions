def average(salary):
    salary.remove(max(salary))
    salary.remove(min(salary))
    average_salary = sum(salary) / len(salary)
    return average_salary


print(average([4000, 3000, 1000, 2000]))
print(average([1000, 2000, 3000]))
print(average([6000, 5000, 4000, 3000, 2000, 1000]))
print(average([8000, 9000, 2000, 3000, 6000, 1000]))

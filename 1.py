def average_grade(a,b,c):
    return (a+b+c)/3
def grade_message(average):
    if average>=4.5:
        return "Отлично"
    elif average>=3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"
avg1=average_grade(5,4,5)
print(f"Оценки: 5,4,5 | Средний балл: {avg1:.2f} | Сообщение: {grade_message(avg1)}")
avg2=average_grade(3,4,3)
print(f"Оценки: 3,4,3 | Средний балл: {avg2:.2f} | Сообщение: {grade_message(avg2)}")
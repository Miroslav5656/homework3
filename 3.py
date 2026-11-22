def analyze_scores(*scores):
    if not scores:
        return 0,0,0
    total=sum(scores)
    count=len(scores)
    average=total/count
    return total,count,average
def print_report(team_name,**info):
    print(f"Команда:{team_name}")
    for key,value in info.items():
        print(f"{key}: {value}")
print("Результаты (8,10,7,9):",analyze_scores(8,10,7,9))
print("Результаты (5,5):",analyze_scores(5,5))
print("Результаты без аргументов:",analyze_scores())
print("Отчёт по команде:")
print_report("Комета",coach="Леха Карась",city="Витебск")
income = int(input("Валовый доход за прошедший период составил: "))
expenses = int(input("Затраты за прошедший период составили: "))
profit_margin = income - expenses
if income > expenses:
    profit_margin = income - expenses
    cost_effectiveness = profit_margin / income
    print("Рентабельность выручки составиляет: ", cost_effectiveness)
    personnel = int(input("Сколько человек трудится на предприятии: "))
    print("Прибыль фирмы в расчете на одного сотрудника составляет: ", profit_margin // personnel)
if expenses > income:
    print("За прошедший период вы отработали с убытком: ", profit_margin)

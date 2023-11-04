money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
delta = spend - salary
money_capital -= delta
count+=1

while delta <= money_capital:
    spend *= 1 + increase
    delta = spend - salary
    money_capital -= delta
    count+=1

print("Количество месяцев, которое можно протянуть без долгов:", count)
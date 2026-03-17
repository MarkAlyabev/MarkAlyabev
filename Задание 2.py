salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # подушка безопасности
for month in range(months):
    if month > 0:
        spend *= (1 + increase) # увеличиваем траты
    if spend > salary: # если расходы больше чем зп добавляем из подушки безопасности
        money_capital += spend - salary
money_capital = round(money_capital) # округляем
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

price = int(input('Введіть ціну'))
discount = int(input('Введіть знижку'))
final_price = price - (price * discount / 100)
print('Фінальна ціна =', final_price)
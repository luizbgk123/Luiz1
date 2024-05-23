a = 1
b = 20
c = -525

delta = (b ** 2) - 4 * a * c

x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

print(f"Voce tem {(x1)} anos e sua mae tem {(x2 * -1)} anos")
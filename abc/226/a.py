from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

num = float(input())
decimal_num = Decimal(num).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(decimal_num)

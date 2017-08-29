import math
ab = input()
bc = input()
print str(int(round(math.degrees(math.atan2(ab,bc)))))+'°'


# atan2 differ atan : accepts two args in order to return value to proper quadrant and check if it divisible by zero or not

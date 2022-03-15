msg = "54 211 168 309 262 110 272 73 54 137 131 383 188 332 39 396 370 182 328 327 366 70"
print("-----", 366%37)
list_msg = [int(num)%37 for num in msg.split()]
print(list_msg)
flag = ""

for num in list_msg:
    if 0 <= num <= 25:
        flag += chr(num+65)
    if 26 <=num <= 35:
        flag += str(num)
    if num == 36:
        flag += "_"


print("-", "R26UND_N_R26UND_C26A3432313333")
print(flag)
print(chr(90))
print(ord("A"))
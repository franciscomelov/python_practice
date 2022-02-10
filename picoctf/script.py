from turtle import pen


a = "ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿ¼}"

for i in range(0, len(a)+4,4):
    s = a[i-4:i:]
    print(s[::-1], end="")
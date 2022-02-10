# picoCTF{ == 灩捯䍔䙻
# remaining ==ㄶ形楴獟楮獴㌴摟潦弸
# _7 == 強
# remaining == 㕤㐸㤸
# last 扽 == b}

# i =105  o=111  T=84 {=123 7=55 }=125
# p == 112  << 28672
# i =105
# 灩 = 28777
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"

# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

left_char = [ord(i) >> 8 for i in flag]
codes = [112, 99, 67, 70, 49, 95, 105, 115, 105, 115, 51, 100, 111, 95, 95, 53, 52, 57, 98]

dec = [i << 8 for i in codes]

#code  = [28672, 25344, 17152, 17920, 12544, 24320, 26880, 29440, 26880, 29440, 13056, 25600, 28416, 24320, 24320, 13568, 13312, 14592, 25088]

rh = []

for ch, cd in zip(flag, codes):
    ch_value = ord(ch)
    cd_wise = cd << 8
    rh_value = ch_value -cd_wise
    print(chr(cd), chr(rh_value), end="", sep="")

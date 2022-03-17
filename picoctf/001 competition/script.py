msg = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VC85A020}E"

decoded = []
for idx, letter in enumerate(msg):
    
    if (idx+1) % 3 == 0:
        print(idx-2, letter)
        decoded.insert(idx-2, letter)
        continue

    decoded.append(letter)

print("".join(decoded))

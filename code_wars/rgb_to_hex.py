def rgb(r, g, b):
    to_hex = [r,g,b]
    for idx in range(3):
        if to_hex[idx] >255:
            to_hex[idx] = 255
        elif to_hex[idx]<0:
            to_hex[idx] =0
        
        if len(hex(to_hex[idx])[2:]) == 1:
            to_hex[idx]= "0" + hex(to_hex[idx])[2:]
        else:
            to_hex[idx]= hex(to_hex[idx])[2:]
    return "".join(to_hex).upper()

    

print(rgb(-20, 148, 275)) # returns 9400D3

""" 
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""
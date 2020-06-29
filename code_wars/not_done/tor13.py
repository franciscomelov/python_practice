def rot13(message):
    new_me = ""
    for letter in message:
        number_letter = ord(letter) 
        if  number_letter >96 and number_letter+13  > 122 or number_letter+13 >90 and number_letter < 90:
            number_letter = ord(letter) - 13
        else:
            number_letter = ord(letter) + 13
        new_me +=chr(number_letter)
    return new_me
    

print(rot13(">=8?-vf-gjryir;"))#'10+2 vf gjryir.'

print(ord("1"))

""" 
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""



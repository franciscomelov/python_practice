import re

def is_valid_email(str):

    test_email = re.search("[\w*]@[a-z]*[.][a-z]*", str)
    test_email = re.search("\w*@[a-z]*[.][a-z]*", str)
    if test_email:
        print("Correo valido")
        return True
    else:
        print("Correo NO valido")


# Necesita el siguiente formato para ser valido
# https://<caracter alphanumerico>.<letra minuscula>/>
is_valid_email('name@example.c2om')# -> True
is_valid_email('n@ameexample.com') #-> False
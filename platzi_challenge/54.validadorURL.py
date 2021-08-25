import re

def is_url(str):

    test_url = re.search("https://\w*[.][a-z]*/", str)
    if test_url:
        print("Es url valida")
        return True
    else:
        print("No es una url valida")


# Necesita el siguiente formato para ser valido
# https://<caracter alphanumerico>.<letra minuscula>/>
is_url("hello friends")
is_url("https://platzi2.com/")
import ast

# Guardar diccionario a txt  -- se convierte a string
""" dict = [{"hola":"adios"}]
f = open("db.txt","w")
f.write( str(dict))
f.close() """

# Leer diccionario como string y lo convierte a diccionaio
whip =None
with open('db.txt', 'r') as f:
    s = f.read()
    whip = ast.literal_eval(s)
    print(whip)

print(whip)

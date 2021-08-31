# text = "hola como estas"
# a = text.find("c")
# print(a)

import re
x = "My 2 favorites numbers are 19 and 42"

y = re.findall('[0-9]+', x)
print(y)

x = "From paco@hotmail.com sat jan 5:12:31 2008"
y = re.findall('\\S+@\\S+', x)
print(y)

x = "From paco@hotmail.com sat jan 5:12:31 2008"
y = re.findall('^From (\S+@\S+)', x)
print(y)

import re
s = 'A message from #csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)


#extracr provedor correo
s = 'A message from #csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S(@+\S+)', s)
print(lst)

s = 'A message from #csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('@([^ ]*)', s)
print(lst)


s = 'From csev@umich.edu to cwen@iupui.edu about meeting '
lst = re.findall('^From .*@([^ ]*)', s)
print(lst)
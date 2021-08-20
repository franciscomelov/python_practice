import win32com.client
outlook=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#print(dir(outlook))
for i in range(60):
  try:
    box = outlook.GetDefaultFolder(i)
    name = box.Name
    print(i, name)
  except:
    pass

print("____________")
from win32com.client import Dispatch

outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders.Item(1)  
soldy_folder = root_folder.Folders['BANCO']
print(soldy_folder )
# importing the module

import pywhatkit
  
# using Exception Handling to avoid 
# unprecedented errors
try:
    
  # sending message to reciever
  # using pywhatkit
  pywhatkit.sendwhatmsg("+5217225761696", 
                        "I am test", 
                        12, 10)
  print("Successfully Sent!")
  
except:
    
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")
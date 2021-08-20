# import libraries
import win32com.client
import re
import datetime

# set up connection to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.Folders.Item(1).Folders['BANCO']

messages = inbox.Items
message = messages.GetFirst()
today_date = str(datetime.date.today())

current_sender = str(message.Sender).lower()
current_subject = str(message.Subject).lower()
# find the email from a specific sender with a specific subject
# condition
print(current_subject) # verify the subject
print(current_sender)  # verify the sender
attachments = message.Attachments
attachment = attachments.Item(1)
attachment_name = str(attachment).lower()
path = "C:\\Users\\femva\\Git\\python_practice\\download_email"
attachment.SaveASFile(path  + '\\' +attachment_name)



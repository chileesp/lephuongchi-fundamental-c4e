from datetime import datetime
from gmail import GMail, Message

now = datetime.now()
print (now)

if now.hour >=7:
    mail = GMail('rainbow.pc97@gmail.com', 'bong123456789')
    message = Message("Xin nghi om", to="chilehnuehsgs@gmail.com", text = "toi bi om roi")
    mail.send(message)

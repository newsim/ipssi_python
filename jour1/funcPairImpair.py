from datetime import datetime


date = datetime.now()


day = date.day

print(day)
if 'day%2 = 0':
    print("le jour est pair")
else:    
    print("le jour est impair")
# def present():
# 	for keys,values in data.items():
# 	    print(keys, end=": ")
# 	    print(values)
# 	print()
	    
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Copy of Room Booking").sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

# data = {"TT table": 9, "Basketball": 3, "Vollyball": 4, "Squash": 3}
# present()



# request = input("What do you want to book ?\n")
# temp = data[request]
# if(temp != 0):
# 	data[request] = data[request] - 1
# 	print("Booking of ",request," successful.")
# 	print()
# 	present()

# else:
# 	print("Room requested is not available.")	



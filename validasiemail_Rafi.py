import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def UjiValidasi(email):

	if(re.match(regex, email)):
		print(" This is valid email")
	else:
		print("This is invalid email")

if __name__ == '__main__':

	email = input("Masukkan Email Anda : ")
print('Data yang anda masukkan : ', email)
UjiValidasi(email)
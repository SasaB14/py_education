#problem1
for i in ['a','b','c']:
	try:
		print(i**2)
	except:
		print("nije moguce dizati na kvadrat string")

#problem2
x = 5
y = 0

try:
	z = x/y
except ZeroDivisionError:
	print("\nnije moguce deliti s nulom")
except:
	print("\nsve druge greske")
finally:
	print("all done")

#
print("\n\n")
#

#problem3
def ask():
	while True:
		try:
			k = int(input("Unesite integer: "))
		except:
			print("niste uneli integer")
			continue
		else:
			print("kvadrat vaseg broja je: ",k**2)
			break


ask()
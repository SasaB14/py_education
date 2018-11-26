###zapremina
def vol(rad):
	return (4/3)*3.14*(rad**3)

print(vol(3))

def ran_check(num,low,high):
	i = 0
	if num == low or num == high:
		return True
	else:
		for niz in range(low,high+1):
			if num == niz:
				i = 1

	if i>0:
		return True
	else:
		return False

print(ran_check(10,1,10))

def up_lows(string):
	malo_slovo = 0
	veliko_slovo = 0
	interpunkcija = 0
	belina = 0
	for slovo in string:
		if slovo.isupper()==True:
			veliko_slovo += 1
		elif slovo.islower()==True:
			malo_slovo += 1
		elif slovo == ' ':
			belina += 1
		else:
			interpunkcija += 1
	print("Broj velikih slova: {}".format(veliko_slovo))
	print("Broj malih slova: {}".format(malo_slovo))
	print("Broj interpukcijskih znakova: {}".format(interpunkcija))
	print("Broj belina: {}".format(belina))

up_lows('Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(niz):
	x = []
	for a in niz:
		if a not in x:
			x.append(a)
	return x



print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


print('###Warmup###')

def lesser_of_two_events(a,b):
	if a%2==0 and b%2==0:
		if a<b:
			return a
		else:
			return b
	if a%2!=0 or b%2!=0:
		if a>b:
			return a
		else:
			return b


print(lesser_of_two_events(2,4))
print(lesser_of_two_events(16,5))
print(lesser_of_two_events(4,27))
print(lesser_of_two_events(11,99))


def animal_crackers(text):
	reci = text.split()
	if reci[0][0] == reci[1][0]:
		print('isto prvo slovo')
		return True
	else:
		print('razlicito prvo slovo')
		return False

animal_crackers('sasa sasa')
animal_crackers('sasa nevena')


print('###Level 1###')

def old_macdonald(name):
	irski=''
	for i in range(len(name)):
		if i==0:
			irski += name[i].upper()
		elif i==3:
			irski += name[i].upper()
		else:
			irski += name[i]
	return irski

print(old_macdonald('macdonald'))
print(old_macdonald('sasasasasa'))

def master_yoda(tekst):
	reci = tekst.split()
	novi_raspored = ''
	broj_reci = len(reci)
	

	while broj_reci>0:
		indeks = broj_reci-1
		novi_raspored += reci[indeks]
		novi_raspored += ' '
		broj_reci = broj_reci - 1
	
	return novi_raspored

print(master_yoda('I am your father Luke'))


print('###Level 2###')



def has_33(lista):
	for i in range(0, len(lista)-1):
		if lista[i]==3 and lista[i+1] == 3:			
			return True
		
	return False

b = has_33([2,2,3,3])
print(b)	

def blackjack(a,b,c):
	if a == 11 or b == 11 or c == 11:
		return a+b+c-10
	elif a+b+c <= 21:
		return a+b+c
	elif a+b+c >= 21:
		return 'bust'

print(blackjack(9,11,9))

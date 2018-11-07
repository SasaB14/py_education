print('hello world')

x = 50
while x<6:
	print(f'Current value of x is {x}')
	x += 2
else:
	print('x nije manje od 6')



st = 'Print only the words that start with sa in this sentence'


for rec in st.split():
	if rec[0] == 's':
		print(rec)

print('#####')
for i in range(0,11):
	print(i)

print('#####')
mojalista=[x for x in range(1,51) if x%3==0]
print(mojalista)

print('#####')
str = 'Print every word in this sentence that has an even number of letters'
odvojeno = str.split()
#print(len(odvojeno[0]))
for rec in odvojeno:
	if len(rec)%2 == 0:
		#print(rec)
		print('even!')

print('ooooooooooooooooo')
for i in range(1,36):
	if i%15==0:
		print('FizzBuzz')
	elif i%5==0:
		print('Buzz')
	elif i%3==0:
		print('Fizz')
	else:
		print(i)


print('ooooooooooooooooo')
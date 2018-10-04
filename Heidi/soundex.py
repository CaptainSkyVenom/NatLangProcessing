name = input("enter your name: ").lower()


soundex = name[0].upper()

name = name.replace('h', '')
name = name.replace('w', '')

name_new = ''

for l in name:
	if l in 'bfpv':
		name_new += '1'
	if l in 'cgjkqsxz':
		name_new += '2'
	if l in 'dt':
		name_new += '3'
	if l in 'l':
		name_new += '4'
	if l in 'mn':
		name_new += '5'
	if l in 'r':
		name_new += '6'
	if l in 'aeiouy':
		name_new += '!' 

def stringClean(string):
    if not string:
        return ""
    if len(string) == 1:
        return string
    if string[0] == string[1]:
        return stringClean(string[1:])
    return string[0] + stringClean(string[1:])

name_new = stringClean(name_new).replace('!', '') + '000'

if soundex not in 'AEIOUYHW':
	soundex += name_new[1:4]
else:
	soundex += name_new[:3]

print(soundex)

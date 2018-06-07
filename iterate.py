import splitcsv

#num = input('Please enter a number of increment 10, for example, 1, 10, 20: ')

i = 1

while i < 101:
    splitcsv.sort(str(i))

    if i == 1:
        i += 9
    else:
        i += 10

def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))

    for i in xrange(1, number+1):
        d = str(i).rjust(w, ' ')
        b = bin(i).replace('0b','').rjust(w, ' ')
        o = oct(i).replace('0','', 1).rjust(w, ' ')
        h = hex(i).replace('0x','').upper().rjust(w, ' ')
        
        print d, o, h, b

if __name__ == '__main__':
	num = input()
	print_formatted(num)	        

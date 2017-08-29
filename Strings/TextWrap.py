import textwrap

def wrap(string, max_width):
    string = textwrap.fill(string,max_width)
    return string
    
    # we could have used textwrap.wrap(string,max_width)
    #but it will return list instead of string and we have to iterate through
    
if __name__ == '__main__':
	str = raw_input()
	n = input()
	print wrap(str,n)    
    

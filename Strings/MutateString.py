def mutate_string(string, position, character):
    
    string = string[:position]+character+string[position+1:]
    
    return string


if __name__ == '__main__':
	s = raw_input()
	c = raw_input().split()
	print mutate_string(s,int(c[0]),c[1])         
    

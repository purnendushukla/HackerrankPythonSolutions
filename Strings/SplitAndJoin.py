def split_and_join(line):
    # write your code here
    a = line.split(" ")
    s = "-".join(a) 
    return s
    
if __name__ == '__main__':
	s = raw_input()
	print split_and_join(s)     

def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-len(sub_string)+1):
        if(sub_string == string[i:i+len(sub_string)]):
            count+=1
        
    
    return count
    

string = raw_input()
sub_string = raw_input()
print count_substring(string, sub_string)
    

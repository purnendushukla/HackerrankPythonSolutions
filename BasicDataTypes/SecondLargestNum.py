if __name__ == '__main__':
    n = int(raw_input())
    l = map(int, raw_input().split())
    first = -101
    sec = -101
    for i in l:
        if(i>first):
            sec = first
            first = i
        elif(i>sec and i<first):
            sec = i
    
    print sec

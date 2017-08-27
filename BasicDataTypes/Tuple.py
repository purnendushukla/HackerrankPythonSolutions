if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    # Integer Mapping List Composition Method
    #  input_list = [int(x) for x in input_list] 
    t = tuple(integer_list)
    print hash(t)

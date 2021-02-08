import sys


for line in sys.stdin:
    bus_nums = []
    rep = ""
    #check if we've received array
    if len(line.split()) != 1:
        #turn array to list of int and sort
        bus_nums = list(map(int, line.split()))
        bus_nums.sort()
        ptr=0
        while ptr < len(bus_nums):
            #append first bus number to string
            rep = rep + str(bus_nums[ptr]) + ""
            #while we have a lienar seq of bus numbers, keep increasing ptr
            ptr2 = ptr + 1
            while(ptr2 < len(bus_nums) and bus_nums[ptr2]-bus_nums[ptr]==ptr2-ptr):
                ptr2+=1
            #set ptr back to last linear bus number
            ptr2 -= 1
            #append hyphen if we have at least 2 in a row for a difference of 1
            if ptr2-ptr > 1:
                ptr = ptr2+1
                rep = rep + "-" + str(bus_nums[ptr2]) + " "
            #otherwise update regularly
            else:
                rep = rep + " "
                ptr += 1
    print(rep) 



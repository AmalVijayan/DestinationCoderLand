#enter the test case number
T = int(input("Test Case : ").strip())

for i in range(T):
    #enter the number of checkpoints
    N = int(input("Number of Check Points : ").strip())
    
    #enter the list of Cost od petrol per liter at each check point
    cpl = list(input("Enter {}  costs seperated by space : ".format(N)).strip())
    
    #remove all extra spaces and convert each element to integer
    for i in cpl:
        if i==' ':
            cpl.remove(i)
    for i in cpl:
        cpl[cpl.index(i)] = int(i)

    #enter the litres of petrol needed to reach each cp
    lcp = list(input("Enter {} numbers(Petrol required to reach each check point) seperated by space : ".format(N)).strip())
    
    #remove all extra spaces and convert each element to integer
    for i in lcp:
        if i==' ':
            lcp.remove(i)
    for i in lcp:
        lcp[lcp.index(i)] = int(i)
    
    # a function to get total petrol required
    def total_lp(x):
        tot = 0
        for i in x:
            tot = tot + i
        return tot


    # Min petrol cost
    mpc = min(cpl)
    
    #total amount of petrol rewuired to reach destination
    Total_petrol_needed = total_lp(lcp)
    print("Total petrol needed to reach destination : {}".format(Total_petrol_needed))
    
    #initializing best price
    bp = 0
     
    #if the first check point has the minimum petrol cost, fill up the tank with total amount of petrol required
    if cpl[0] == mpc:
        bp = cpl[0] * Total_petrol_needed
        print("The best cost for reaching Coderland is : {} ".format(bp))
    
    #Otherwise check each check point for minimum petrol rate
    else:
        bp=0
        mini=cpl[0]
        while(True):
            i=0
            if cpl[i] != min(cpl):
                if cpl[i] > mini:
                    bp = mini * lcp[i] + bp
                else:
                    mini = cpl[i]
                    bp = cpl[i] * lcp[i] + bp
                del cpl[i]
                del lcp[i]
                pet_req = total_lp(lcp)
            else:
                bp = bp + cpl[i] * pet_req
                break
        print("The best cost for reaching Coderland is : ",bp)


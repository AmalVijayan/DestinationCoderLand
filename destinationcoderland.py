#enter the test case number
T = int(input("Test Case : ").strip())

for i in range(T):
    #enter the number of checkpoints
    N = int(input("Number of Check Points : ").strip())
    
    #enter the list of Cost od petrol per liter at each check point
    cpl = list(map(int,input("Enter {}  costs ".format(N)).split()))
    
    #remove all extra spaces and convert each element to integer
    for i in cpl:
        if i==' ':
            cpl.remove(i)
    cpl=list(map(int,cpl))
    

    #enter the litres of petrol needed to reach each cp
    lcp = list(map(int,input("Enter {} numbers(Petrol required to reach each check point) seperated by space : ".format(N)).split()))
    
    #remove all extra spaces and convert each element to integer
    for i in lcp:
        if i==' ':
            lcp.remove(i)
    lcp=list(map(int,lcp))
  



    # Min petrol cost
    mpc = min(cpl)
    
    #total amount of petrol rewuired to reach destination
    Total_petrol_needed = sum(lcp)
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
        while cpl:
            i=0
            if cpl[i] != min(cpl):
                if cpl[i] > mini:
                    bp = mini * lcp[i] + bp
                else:
                    mini = cpl[i]
                    bp = cpl[i] * lcp[i] + bp
                del cpl[i]
                del lcp[i]
                pet_req = sum(lcp)
            else:
                bp = bp + cpl[i] * pet_req
                break
        print("The best cost for reaching Coderland is : ",bp)



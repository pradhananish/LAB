# fractional Knapsack
def knapSack_Fract(W, wt, val, n):


    maxProfit = 0
    solutions = [format(x, '03b') for x in range(2**n)]


    for sol in solutions:


        i_element = []


        for i, x in enumerate(sol):
            if x == '0':
                i_element.append(i)


        profit = sum(int(sol[i])*val[i] for i in range(n))
        weight = sum(int(sol[i])*wt[i] for i in range(n))


        fraction = 0


        if weight < W:


            for i in i_element:
                if W-weight < wt[i]:
                    remain = W - weight


                else:
                    remain = wt[i]


                frac = (val[i] / wt[i]) * remain
                if frac > fraction:
                    fraction = frac


        profit += fraction


        if weight <= W and profit >= maxProfit:
            maxProfit = profit


    return int(maxProfit)


val = [2,4,3]
wt = [3,4,1]
W = 5
n = len(val)
print ("The maximum value obtained by Bruteforce for fractional knapsack is ",knapSack_Fract(W, wt, val, n))
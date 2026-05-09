from scipy.stats import norm, wilcoxon

def signedranktest(data1, data2, correction=False, alternative='two-sided'):
    d = [(mag:=abs(di), di/mag) for elem1, elem2 
            in zip(data1, data2, strict=True) if (di:=elem1-elem2)!=0]
    sorted_d = sorted(d, key=lambda tup: tup[0]) + [(0, float('inf'))]
    
    Wp = Wn = 0
    prev = sorted_d[0][0]
    accum_ranks = []
    accum_signs = []
    for i, (mag, sign) in enumerate(sorted_d, start=1):
        if mag==prev:
            accum_ranks.append(i)
            accum_signs.append(sign)
        else:
            rank = sum(accum_ranks)/len(accum_ranks)
            for k in accum_signs:
                if k==1: Wp += rank
                else: Wn += rank
            accum_ranks = [i]
            accum_signs = [sign]
        prev = mag
    
    m = len(d)
    cc = 0.5 if correction else 0
    dist = norm(m*(m+1)/4, (m*(m+1)*(2*m+1)/24)**(1/2))
    if alternative=='two-sided':
        return (W:=min(Wn, Wp)), 2*dist.cdf(W+cc), m
    elif alternative=='greater':
        return Wn, dist.cdf(Wn+cc), m
    elif alternative=='less':
        return Wp, dist.cdf(Wp+cc), m
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 2:')
    data2 = input_data(len(data1))
    correct = bool(input('Should the continuity correction be applied?: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = signedranktest(data1, data2, correction=correct, alternative=alt)
    print(results)
    results = wilcoxon(data1, data2, correction=correct, alternative=alt, method='approx')
    print(results)
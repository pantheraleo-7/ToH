from scipy.stats import norm, mannwhitneyu

def utest(data1, data2, correction=True, alternative='two-sided'):
    data1 = [(elem, 1) for elem in data1]
    data2 = [(elem, 2) for elem in data2]
    sorted_samples = sorted(data1+data2, key=lambda tup: tup[0]) + [(0, float('inf'))]
    
    R1 = R2 = 0
    prev = sorted_samples[0][0]
    accum_ranks = []
    accum_nums = []
    for i, (elem, samp_num) in enumerate(sorted_samples, start=1):
        if elem==prev:
            accum_ranks.append(i)
            accum_nums.append(samp_num)
        else:
            rank = sum(accum_ranks)/len(accum_ranks)
            for k in accum_nums:
                if k==1: R1 += rank
                else: R2 += rank
            accum_ranks = [i]
            accum_nums = [samp_num]
        prev = elem
    
    n1, n2 = len(data1), len(data2)
    U1, U2 = R1-(n1*(n1+1)/2), R2-(n2*(n2+1)/2)
    cc = 0.5 if correction else 0
    dist = norm(n1*n2/2, (n1*n2*(n1+n2+1)/12)**(1/2))
    if alternative=='two-sided':
        return (U:=min(U1, U2)), 2*dist.cdf(U+cc)
    elif alternative=='greater':
        return U2, dist.cdf(U2+cc)
    elif alternative=='less':
        return U1, dist.cdf(U1+cc)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 2:')
    data2 = input_data()
    correct = bool(input('Should the continuity correction be applied?: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = utest(data1, data2, correction=correct, alternative=alt)
    print(results)
    results = mannwhitneyu(data1, data2, use_continuity=correct, alternative=alt, method='asymptotic')
    print(results)
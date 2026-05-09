from scipy.stats import binom, norm
from numbers import Number

def signtest(data1, data2, correction=True, alternative='two-sided'):
    data2 = [data2]*len(data1) if isinstance(data2, Number) else data2
    Np = Nn = 0
    for obs1, obs2 in zip(data1, data2, strict=True):
        if obs1-obs2<0: Nn += 1
        elif obs1-obs2>0: Np += 1
    
    m = Np+Nn
    cc = 0.5 if m>25 and correction else 0
    dist = norm(m/2, m**(1/2)/2) if m>25 else binom(m, 0.5)
    if alternative=='two-sided':
        return (S:=min(Nn, Np)), 2*dist.cdf(S+cc), m
    elif alternative=='greater':
        return Nn, dist.cdf(Nn+cc), m
    elif alternative=='less':
        return Np, dist.cdf(Np+cc), m
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    data1 = input_data()
    print(len(data1))
    if input('Population median or second set of observations?: ')=='med':
        data2 = float(input('Enter the population median: '))
    else:
        data2 = input_data(len(data1))
    correct = bool(input('Should the continuity correction be applied?: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = signtest(data1, data2, correction=correct, alternative=alt)
    print(results)
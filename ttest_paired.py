from scipy.stats import t, ttest_rel
import numpy as np

def ttest_dep(data1, data2, alternative='two-sided'):
    d = [elem1-elem2 for elem1, elem2 in zip(data1, data2, strict=True)]
    n = len(d)
    dbar = np.mean(d)
    s = np.std(d, ddof=1)
    T = dbar / (s/(n**(1/2)))
    
    if alternative=='two-sided':
        return T, 2*min(t.cdf(T, n-1), t.sf(T, n-1))
    elif alternative=='greater':
        return T, t.sf(T, n-1)
    elif alternative=='less':
        return T, t.cdf(T, n-1)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 2:')
    data2 = input_data(len(data1))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = ttest_dep(data1, data2, alternative=alt)
    print(results)
    results = ttest_rel(data1, data2, alternative=alt)
    print(results)
from scipy.stats import t, ttest_1samp
import numpy as np

def ttest(data, pop_mean, alternative='two-sided'):
    n = len(data)
    xbar = np.mean(data)
    s = np.std(data, ddof=1)
    T = (xbar-pop_mean) / (s/(n**(1/2)))
    
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
    data = input_data()
    mu = float(input('Enter the population mean: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = ttest(data, mu, alternative=alt)
    print(results)
    results = ttest_1samp(data, mu, alternative=alt)
    print(results)
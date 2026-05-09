from scipy.stats import f
import numpy as np

def ftest(data1, data2, alternative='two-sided'):
    n1, n2 = len(data1), len(data2)
    var1, var2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
    F = var1/var2
    
    if alternative=='two-sided':
        return F, 2*min(f.cdf(F, n1-1, n2-1), f.sf(F, n1-1, n2-1))
    elif alternative=='greater':
        return F, f.sf(F, n1-1, n2-1)
    elif alternative=='less':
        return F, f.cdf(F, n1-1, n2-1)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 2:')
    data2 = input_data()
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = ftest(data1, data2, alternative=alt)
    print(results)
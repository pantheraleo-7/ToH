from scipy.stats import norm
import numpy as np

def ztest(data1, data2, pop_sd1, pop_sd2, alternative='two-sided'):
    n1, n2 = len(data1), len(data2)
    x1bar, x2bar = np.mean(data1), np.mean(data2)
    Z = (x1bar-x2bar) / ((pop_sd1**2/n1)+(pop_sd2**2/n2))**(1/2)
    
    if alternative=='two-sided':
        return Z, 2*min(norm.cdf(Z), norm.sf(Z))
    elif alternative=='greater':
        return Z, norm.sf(Z)
    elif alternative=='less':
        return Z, norm.cdf(Z)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    sigma1 = float(input('Enter the population 1 standard deviation: '))
    print('Sample 2:')
    data2 = input_data()
    sigma2 = float(input('Enter the population 2 standard deviation: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = ztest(data1, data2, sigma1, sigma2, alternative=alt)
    print(results)
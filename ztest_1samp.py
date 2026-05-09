from scipy.stats import norm
import numpy as np

def ztest(data, pop_mean, pop_sd, alternative='two-sided'):
    n = len(data)
    xbar = np.mean(data)
    Z = (xbar-pop_mean) / (pop_sd/(n**(1/2)))
    
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
    data = input_data()
    mu = float(input('Enter the population mean: '))
    sigma = float(input('Enter the population standard deviation: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = ztest(data, mu, sigma, alternative=alt)
    print(results)
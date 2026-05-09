from scipy.stats import chi2
import numpy as np

def chi2test(data, pop_var, alternative='two-sided'):
    n = len(data)
    var = np.var(data, ddof=1)
    CHI2 = (n-1)*var/pop_var
    
    if alternative=='two-sided':
        return CHI2, 2*min(chi2.cdf(CHI2, n-1), chi2.sf(CHI2, n-1))
    elif alternative=='greater':
        return CHI2, chi2.sf(CHI2, n-1)
    elif alternative=='less':
        return CHI2, chi2.cdf(CHI2, n-1)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    data = input_data()
    sigma_squared = float(input('Enter the population variance: '))
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = chi2test(data, sigma_squared, alternative=alt)
    print(results)
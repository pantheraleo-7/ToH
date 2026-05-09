from scipy.stats import t, ttest_ind
import numpy as np

def ttest(data1, data2, equal_var=True, alternative='two-sided'):
    n1, n2 = len(data1), len(data2)
    x1bar, x2bar = np.mean(data1), np.mean(data2)
    var1, var2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
    if equal_var:
        dof = n1+n2-2
        var1 = var2 = ((n1-1)*var1+(n2-1)*var2)/dof
    else:
        dof = (var1/n1+var2/n2)**2 / ((var1/n1)**2/(n1-1)+(var2/n2)**2/(n2-1))
    T = (x1bar-x2bar) / ((var1/n1)+(var2/n2))**(1/2)
    
    if alternative=='two-sided':
        return T, 2*min(t.cdf(T, dof), t.sf(T, dof)), dof
    elif alternative=='greater':
        return T, t.sf(T, dof), dof
    elif alternative=='less':
        return T, t.cdf(T, dof), dof
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 1:')
    data2 = input_data()
    eq_var = input('Do the populations have equal variance?: ')
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = ttest(data1, data2, equal_var=bool(eq_var), alternative=alt)
    print(results)
    results = ttest_ind(data1, data2, equal_var=bool(eq_var), alternative=alt)
    print(results)
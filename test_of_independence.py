from scipy.stats import chi2, chi2_contingency
import numpy as np
from math import log

def chi2test(table, lambda_=1):
    func = (lambda O, E: 2*O*log(O/E), lambda O, E: (O-E)**2/E)[lambda_]
    table = np.asarray(table)
    r, c = table.shape
    N = table.sum()
    margin_row = table.sum(axis=0)
    margin_col = table.sum(axis=1)
    CHI2 = 0
    for i, row in enumerate(table):
        for j, O in enumerate(row):
            E = margin_col[i]*margin_row[j]/N
            CHI2 += func(O, E)
    
    return CHI2, chi2.sf(CHI2, (r-1)*(c-1))


if __name__=='__main__':
    from inputlib import input_table
    table = input_table()
    typ = int(input("Enter 1 for Pearson's test statistic or 0 for G test: "))
    
    results = chi2test(table, lambda_=typ)
    print(results)
    results = chi2_contingency(table, correction=False, lambda_=typ)
    print('statistic={0.statistic}, pvalue={0.pvalue}, df={0.dof}'.format(results))
    print(results.expected_freq)
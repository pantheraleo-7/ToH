from scipy.stats import binom, chi2

def mcnemarstest(table2x2, exact=False, correction=False):
    (_, b), (c, _) = table2x2
    cc = 1 if correction else 0
    if exact:
        B = min(b, c)
        return B, 2*binom.cdf(B-cc, b+c, 0.5)
    else:
        CHI2 = (abs(b-c)-cc)**2/(b+c)
        return CHI2, chi2.sf(CHI2, 1)


if __name__=='__main__':
    from inputlib import input_table
    table2x2 = input_table(2, 2)
    exact = bool(input('Should the test be exact?: '))
    correct = bool(input('Should the continuity correction be applied?: '))
    
    results = mcnemarstest(table2x2, exact=exact, correction=correct)
    print(results)
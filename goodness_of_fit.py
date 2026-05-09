import scipy.stats
from math import log

def chi2test(obs, exp=None, pf=None, args=(), proportions=False, lambda_=1):
    func = (lambda O, E: 2*O*log(O/E), lambda O, E: (O-E)**2/E)[lambda_]
    if pf is not None:
        if isinstance(pf, str):
            dist, pf = pf.split('.')
            pf = getattr(getattr(scipy.stats, dist), pf)
        exp = pf(exp, *args)*sum(obs)
    elif exp is None:
        exp = [sum(obs)/len(obs)]*len(obs)
    elif proportions:
        p = sum(obs)/sum(exp)
        exp = [p*prop for prop in exp]
    
    return (CHI2:=sum(func(O, E) for O, E in zip(obs, exp, strict=True))), scipy.stats.chi2.sf(CHI2, len(obs)-1)


if __name__=='__main__':
    from inputlib import input_data
    print('Observed frequencies:')
    obs = input_data()
    pf = pf if (pf:=input('Enter the probability function name: ')) else None
    if pf is not None:
        props = False
        print('Distribution parameters:')
        params = input_data()
        print('Random variables:')
    else:
        params = ()
        props = bool(input('Will the entered expected frequencies be proportions?: '))
        print('Expected frequencies:')
    exp = input_data(len(obs))
    typ = int(input("Enter 1 for Pearson's test statistic or 0 for G test: "))
    
    results = chi2test(obs, exp, pf, params, props, lambda_=typ)
    print(results)
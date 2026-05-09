from scipy.stats import fisher_exact
from math import factorial

def _f(a, b, c, d):
    return (factorial(a+b)*factorial(c+d)*factorial(a+c)*factorial(b+d)) / (factorial(a+b+c+d)*factorial(a)*factorial(b)*factorial(c)*factorial(d))

def fishersexacttest(table2x2, alternative='two-sided'):
    if alternative not in {'two-sided', 'less', 'greater'}:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")
    
    (a, b), (c, d) = table2x2
    Ps = [pa:=_f(a, b, c, d)]
    if alternative!='greater':
        while a>0<d:
            a -= 1
            b += 1
            c += 1
            d -= 1
            Ps.append(_f(a, b, c, d))
    
    (a, b), (c, d) = table2x2
    if alternative!='less':
        while b>0<c:
            a += 1
            b -= 1
            c -= 1
            d += 1
            Ps.append(_f(a, b, c, d))
    
    return sum(p for p in Ps if p<=pa) if alternative=='two-sided' else sum(Ps)


if __name__=='__main__':
    from inputlib import input_table
    table2x2 = input_table(2, 2, dtype=int)
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'
    
    results = fishersexacttest(table2x2, alternative=alt)
    print(results)
    results = fisher_exact(table2x2, alternative=alt)
    print(results)
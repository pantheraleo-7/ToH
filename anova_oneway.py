from scipy.stats import f, f_oneway
import numpy as np

def oneway(*groups, unbalanced=True):
    all_factors = [data for factor in groups for data in factor] if unbalanced else groups
    N = len(all_factors) if unbalanced else len(groups)*len(groups[0])
    
    SST = N*np.var(all_factors)
    SSW = sum(len(factor)*np.var(factor) for factor in groups)
    SSB = SST-SSW
    
    DFB = len(groups)-1
    DFW = N-len(groups)
    DFT = N-1
    
    MSB = SSB/DFB
    MSW = SSW/DFW
    
    F = MSB/MSW
    pv = f.sf(F, DFB, DFW)
    
    print('='*72)
    print('   Source    |     SS     |  DF  |     MS     |   F-ratio  |   pvalue')
    print('='*72)
    print(f'   Between   |{SSB:12.4f}|{DFB:6}|{MSB:12.4f}|{F:12.4f}|{pv:12.4f}')
    print(f'   Within    |{SSW:12.4f}|{DFW:6}|{MSW:12.4f}|')
    print('-'*72)
    print(f'    Total    |{SST:12.4f}|{DFT:6}|')
    
    return F, pv


if __name__=='__main__':
    from inputlib import input_table
    rag = bool(input('Is the research design unbalanced?: '))
    groups = input_table(ragged=rag)
    
    oneway(*groups, unbalanced=rag)
    print('\n\n')
    print(f_oneway(*groups))
from scipy.stats import f
import pandas as pd

def twoway(table, interaction=False):
    df = pd.DataFrame(table)
    unique_indexes = df.index.unique()
    
    grand_mean = df.mean(axis=None)
    SST = (((df-grand_mean)**2).sum()).sum()
    SSBR = 0
    for row in unique_indexes:
        rfactor = df.loc[row, :]
        SSBR += (rfactor.count().sum()*(rfactor.mean(axis=None)-grand_mean)**2).sum()
    SSBC = 0
    for col in df.columns:
        cfactor = df.loc[:, col]
        SSBC += (cfactor.count()*(cfactor.mean()-grand_mean)**2).sum()
    if interaction:
        SSE = 0
        for row in unique_indexes:
            for col in df.columns:
                rcfactor = df.loc[row, col]
                SSE += ((rcfactor-rcfactor.mean())**2).sum()
        SSI = SST-SSBR-SSBC-SSE
    else: SSE = SST-SSBR-SSBC
    
    DFT = (len(df.index)*len(df.columns))-1
    DFBR = len(unique_indexes)-1
    DFBC = len(df.columns)-1
    DFI = DFBR*DFBC if interaction else 0
    DFE = DFT-DFBR-DFBC-DFI
    
    MSBR = SSBR/DFBR
    MSBC = SSBC/DFBC
    if interaction: MSI = SSI/DFI
    MSE = SSE/DFE
    
    Fr = MSBR/MSE
    pvr = f.sf(Fr, DFBR, DFE)
    Fc = MSBC/MSE
    pvc = f.sf(Fc, DFBC, DFE)
    if interaction:
        Fi = MSI/MSE
        pvi = f.sf(Fi, DFI, DFE)
    
    print('='*72)
    print('   Source    |     SS     |  DF  |     MS     |   F-ratio  |   pvalue')
    print('='*72)
    print(f'    Rows     |{SSBR:12.4f}|{DFBR:6}|{MSBR:12.4f}|{Fr:12.4f}|{pvr:12.4f}')
    print(f'   Columns   |{SSBC:12.4f}|{DFBC:6}|{MSBC:12.4f}|{Fc:12.4f}|{pvc:12.4f}')
    if interaction: print(f' Interaction |{SSI:12.4f}|{DFI:6}|{MSI:12.4f}|{Fi:12.4f}|{pvi:12.4f}')
    print(f'    Error    |{SSE:12.4f}|{DFE:6}|{MSE:12.4f}|')
    print('-'*72)
    print(f'    Total    |{SST:12.4f}|{DFT:6}|')
    
    if interaction: return (Fr, pvr), (Fc, pvc), (Fi, pvi)
    else: return (Fr, pvr), (Fc, pvc)


if __name__=='__main__':
    from inputlib import input_table
    table = input_table()
    repeated_measures = bool(input('Are there repeated measures?: '))
    twoway(table, repeated_measures)
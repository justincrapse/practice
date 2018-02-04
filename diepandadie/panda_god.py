import pandas as pd
import numpy as np
import matplotlib as plt

pd.set_option('display.width', 400)

d = [pd.Series(np.random.randint(0, 100, 5), index=list('ABCDE')),
     pd.Series(np.random.randint(0, 100, 6), index=list('ABCDEZ')),
     pd.Series(np.random.randint(0, 100, 6), index=list('ABCDEZ')),
     pd.Series(np.random.randint(0, 100, 5), index=list('ABCDE')),
     pd.Series(np.random.randint(0, 100, 6), index=list('ABCDEZ')),]

dates = pd.date_range('20130101', periods=5, freq='M')
bdf = pd.DataFrame(d, index=dates) # type: pd.DataFrame

df = pd.read_csv('census.csv')

# df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
#
# for col in df.columns:
#     if col[:2]=='01':
#         df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
#     if col[:2]=='02':
#         df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
#     if col[:2]=='03':
#         df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
#     if col[:1]=='№':
#         df.rename(columns={col:'#'+col[1:]}, inplace=True)
#
# names_ids = df.index.str.split('\s\(') # split the index by '('
#
# df.index = names_ids.str[0] # the [0] element is the country name (new index)
# df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
#
# df = df.drop('Totals') # type: pd.DataFrame



def data_magic(df):
    dfg = df[df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP']
    return dfg.apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
    return (df['Gold'] - df['Gold.1']).abs().idxmax()




results = data_magic(df)
print(results)



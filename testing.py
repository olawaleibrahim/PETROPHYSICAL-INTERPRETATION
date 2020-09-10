import numpy as np
import pandas as pd

df = pd.read_csv('BOGI_02.csv')
#df = df.drop('Unnamed: 0', axis=1)
df.to_csv('BOGI_02.csv', index=False)
df1 = df.dropna()
df2 = df.copy()

#df2['res'] = np.log(df1['res'])

from evaluate_reservoir import FormationEvaluation

a = FormationEvaluation(df2, 'gr', 'nphi', 'dens', 'res', 2885, 6000)
#print(a.show_table())
print(a.summary())
b = a.parameters()
print(type(b))

#summary(df2)
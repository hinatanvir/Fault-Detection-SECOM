#%%
import pandas as pd
from module_clean import read_secom, read_labels

df_data = read_secom()
df_label = read_labels()

df = pd.concat([df_data,df_label],axis=1)

print(df.head())
# %%

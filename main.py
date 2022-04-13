#%%
import pandas as pd
from module_clean import read_secom, read_labels

df_data = read_secom()
df_label = read_labels()

df = pd.concat([df_data,df_label],axis=1)

print(df.head())
# %%
#create a dist of all std and then remove ones that fall under a certain thresold
#ctr+Enter
col_std = [df_data[col].std() for col in df_data.columns]
print(col_std)

from matplotlib import pyplot as plt
plt.hist(col_std)


for i in col_std:
 print(i,' ',col_std.count(i))
    
# %%

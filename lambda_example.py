#lambda


from regex import B
from sympy import C


def sum_we_define(a,b):
    c = a + b
    return c

x = sum_we_define(1,2)

print(x)

#%%

new_sum_function = lambda a,b : a + b

x = new_sum_function(3,4)

print(x)

# %%

#apply?

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)

print(df)
# %%

def plus_one(col):
    new_col = col+ 1
    return new_col
    
df['new_age'] = df['Age'].apply(plus_one)



print(df)
# %%

df['new_age_by_lambda'] = df['Age'].apply(lambda col:col+1)
print(df)

#look into axis -> 0 or 1
# %%
import numpy as np
df['Age'].apply(np.sum,axis=0)

# %%
df['Age'].apply(np.sum,axis=1)
# %%
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df
# %%
df.apply(np.sum, axis=0)
# %%
df.apply(np.sum, axis=1)
# %%

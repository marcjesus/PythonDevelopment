# Vectorization is the technique of implementing (NumPy) array operations on a
# dataset. In the background, it applies the operations to all the elements of an array
# or series in one go (unlike a ‘for’ loop that manipulates one row at a time).


import time
import numpy as np
import pandas as pd

# Finding the sum of numbers
print("CASE 1 : FINDING THE SUM OF NUMBERS======================================================")
start_noVect = time.time()

total = 0 
for item in range(0,1500000):
    total = total + item

print('sum without Vectorization is:' + str(total))
end = time.time()

print(f"Calculation time without vectorization {end-start_noVect}")


start_Vect = time.time()
print(f"Sum with Vectorization {np.sum(np.arange(1500000))}")
end  = time.time()
print(f"Calculation time with vectorization {end-start_Vect}")

# Mathematical Operations (on DataFrame)
print("CASE 2 : MATHEMATICAL OPERATIONS======================================================")
df = pd.DataFrame(np.random.randint(0, 50, size=(5000000, 4)), columns=('a','b','c','d'))
df.shape
# (5000000, 5)
df.head()

start = time.time()

# Iterating through DataFrame using iterrows
for idx, row in df.iterrows():
    # creating a new column 
    df.at[idx,'ratio'] = 100 * (row["d"] / row["c"])  
end = time.time()
print(f"Time without vectorization : {end - start}")


start = time.time()
df["ratio"] = 100 * (df["d"] / df["c"])

end = time.time()
print(f"Time with vectorization : {end - start}")


# Mathematical Operations (on DataFrame)
print("CASE 3 : If-else Statements (on DataFrame)======================================================")
start = time.time()

# Iterating through DataFrame using iterrows
for idx, row in df.iterrows():
    if row.a == 0:
        df.at[idx,'e'] = row.d    
    elif (row.a <= 25) & (row.a > 0):
        df.at[idx,'e'] = (row.b)-(row.c)    
    else:
        df.at[idx,'e'] = row.b + row.c
end = time.time()
print(f"Time without vectorization : {end - start}")

start = time.time()
start = time.time()
df['e'] = df['b'] + df['c']
df.loc[df['a'] <= 25, 'e'] = df['b'] - df['c']
df.loc[df['a'] == 0, 'e'] = df['d']
end = time.time()
print(f"Time with vectorization : {end - start}")


# Mathematical Operations (on DataFrame)
print("CASE 4 : Solving Machine Learning/Deep Learning Networks======================================================")
# setting initial values of m 
m = np.random.rand(1,5)

# input values for 5 million rows
x = np.random.rand(5000000,5)

m = np.random.rand(1,5)
x = np.random.rand(5000000,5)

total = 0
zer = []
tic = time.process_time()
for i in range(0,5000000):
    total = 0
    for j in range(0,5):
        total = total + x[i][j]*m[0][j] 
    zer[i] = total 
toc = time.process_time()
print ("Computation time = " + str((toc - tic)) + "seconds")
####Computation time = 28.228 seconds

#dot product 
np.dot(x,m.T) 
toc = time.process_time()
print ("Computation time = " + str((toc - tic)) + "seconds")
print(f"Time with vectorization : {end - start}")

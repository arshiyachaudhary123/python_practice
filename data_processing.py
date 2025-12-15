import numpy as np
data=[10,20,30,40,None,50]
cleaned_data=[x for x in data if x is not None]
mean_value=np.mean(cleaned_data)
print("Mean:",mean_value)

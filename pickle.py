import pickle as pk
import numpy as np
t=np.arange(0,1,0.01)
f=10
x=np.sin(2*np.pi*f*t)
f=open("title3","wb")
pk.dump(x,f)
f.close()
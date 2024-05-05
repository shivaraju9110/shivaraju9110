import numpy as np
t=np.arange(0,1,0.01)
f=10
x=np.sin(2*np.pi*f*t)
f=open("title1","w")
f.write(str(x))
f.close()
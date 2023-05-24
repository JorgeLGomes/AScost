

import xarray as xr
import matplotlib.pyplot as plt
import sys

try:
    dir=sys.argv[1]
except:
    dir= '/home/nicole/workdir/AScoast/INPUT/'

tu=[] ; tz=[]
for i in range(1,4):
    tu.append(xr.open_dataset(f'{dir}/tu_00{i}.nc'))
    tz.append(xr.open_dataset(f'{dir}/tz_00{i}.nc'))

tide=[
    "m2  ",  
    "s2  ",  
    "n2  ",  
    "k2  ",  
    "k1  ",  
    "o1  ",  
    "p1  ",  
    "q1  ",  
    "mm  ",  
    "mf  ",  
    ]
for m in range(0,10):
    for i in range(1,4):
        tu[i-1][f'uamp_segment_00{i}'][0,m,:,:].plot(label=f'{tide[m]}')
        tz[i-1][f'zamp_segment_00{i}'][0,m,:,:].plot(label=f'{tide[m]}')
        plt.legend()

plt.show()



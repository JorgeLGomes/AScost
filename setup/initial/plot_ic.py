import xarray as xr
import matplotlib.pyplot as plt

ic=xr.open_dataset('/Volumes/A1/workdir/nicole/AScoast/INPUT/glorys_ic_75z.nc')

nz=len(ic.zl.data)
nx=len(ic.xh.data)
ny=len(ic.yh.data)

cmaps = {'temp': 'jet', 'ssh':'PiYG', 'u':'nipy_spectral', 'v':'nipy_spectral',
        'salt': 'gist_earth'}

for v in ic.keys():
    print(v)
    
    try:
        ic[v][0,:,0,:].plot(size=10,cmap=cmaps[v])
        plt.savefig(f"IC{v}_south.png")
        plt.clf()

        ic[v][0,:,-1,:].plot(size=10,cmap=cmaps[v])
        plt.savefig(f"IC{v}_north.png")
        plt.clf()

        ic[v][0,:,:,-1].plot(size=10,cmap=cmaps[v])
        plt.savefig(f"IC{v}_east.png")
        plt.clf()
    except:
        pass

    for z in [0,nz-1]:




        try:
            ic[v][0,z,:,:].plot(size=10,cmap=cmaps[v])
            plt.savefig(f"IC{v}_{z}.png")
            plt.clf()
        except:
            ic[v][0,:,:].plot(size=10,cmap=cmaps[v])
            plt.savefig(f"IC{v}_{z}.png")
            plt.clf()

print('done')
quit()

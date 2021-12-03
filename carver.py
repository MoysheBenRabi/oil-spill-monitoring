import os
from eolearn.core import EOPatch, FeatureType
import numpy as np

def main(): 
    dir = os.path.join('data','2021H','patches')
    outdir = os.path.join('data','2021H','set')
    patches = [f for f in os.listdir(dir)]
    c = len(patches)
    l = 19
    for i in range(c):
        name = patches[i]
        print(f'{i+1}/{c}: {name}')
        try:
            eopatch_path = os.path.join(dir, name)
            eopatch = EOPatch.load(eopatch_path, lazy_loading=True)    
            for j in range(l):
                vis = eopatch.data['L2A'][j][...,[]]
                outname = f"{i}_{j}.npy.gz"
                out = os.path.join(outdir,outname)
                np.savez_compressed(out,np.ravel(vis))
            del eopatch
        except KeyboardInterrupt:
            del eopatch
            break
        except:
            print(f'Error {i+1}')
 
if __name__ == "__main__":
    main()
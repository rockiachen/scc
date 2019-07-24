import sys
import os
"""
在所在目录 python clear_ds_store
或
python clear_ds_store.py {指定根目录}
"""
argv = sys.argv
if len(argv) == 1:
    path = os.path.abspath(os.path.dirname(__file__))
else:
    path = argv[1]
    
    
def traverse(f):
    ret = []
    fs = os.listdir(f)
    for f1 in fs:
        ret.append(f1)
    return ret

        
for i, (root, dirs, files) in enumerate(os.walk(path)):
    for fname in files:
        if fname == '.DS_Store':
            p = os.path.join(root, fname)
            os.remove(p)
            print('%s removed' % p)

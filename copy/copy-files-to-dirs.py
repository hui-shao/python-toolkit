import os
import sys
import shutil
import glob

os.chdir(sys.path[0])
names = os.listdir("./")
raws = glob.glob("./*.bat") + glob.glob("./*.py")
for name in names:
    if os.path.isdir(name):
        for raw in raws:
            print("Copying %s  ----> %s" % (raw, name))
            shutil.copy2(raw, name)

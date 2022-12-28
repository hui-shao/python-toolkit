import cn2an
import re
import os
import sys

os.chdir(sys.path[0])
pattern = re.compile(r"^(.*?)第(.+?)次(.*?)\.(.*)$")
filenames = os.listdir(".")
for filename in filenames:
    names = re.search(pattern, filename)
    if names is None:
        continue
    # print(names.groups())
    front = names.group(1)
    an = int(cn2an.cn2an(names.group(2)))
    end = names.group(3)
    suffix = "." + names.group(4)
    new_name = front + "第" + "%02d" % an + "次" + end + suffix
    print(filename, "=>", new_name)
    os.rename(filename, new_name)

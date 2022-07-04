


import glob
from pathlib import Path
from JE313P.utils import load_plugins
import logging
from JE313P import JE313P

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "JE313P/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("تم تنصيب السورس بنجاح")
print("قناة السورس @JMTHON")

if __name__ == "__main__":
    JE313P.run_until_disconnected()

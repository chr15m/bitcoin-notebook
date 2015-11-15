from subprocess import Popen, PIPE
import os
import re
from datetime import datetime

sep_re = re.compile("[\s=]")

types = {
    "%bl": int,
    "%bv": int,
    "%bs": lambda x: datetime.fromtimestamp(float(x)),
    "%bt": int,
    "%bn": int,
    "%bc": int,
    "%bN": int,

    "%tv": int,
    "%tN": int,
    "%ti": int,
    "%to": int,
    "%tt": lambda x: datetime.fromtimestamp(float(x)) if int(x) > 5000000 else int(x),
    "%tl": int,
    "%tN": int,
    "%tF": int,

    "%ii": int,
    "%il": int,
    "%iN": int,

    "%oa": int,
    "%ol": int,
    "%oN": int,
}

def bi(cmd):
    # extract the fieldnames and set up a structure to store everything
    fieldnames = [p.split(",") for p in sep_re.split(cmd) if "%" in p].pop()
    fields = [(fn, []) for fn in fieldnames]
    # run the external command to parse
    cmd = os.path.dirname(__file__) + "/bitcoin-iterate/bitcoin-iterate -q " + cmd
    stdout, stderr = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True).communicate()
    # catch bad bitcoin-iterate invocation
    if "Usage" in stdout:
        raise Exception("Invalid bitcoin-iterate invocation.\n\n" + stdout)
    # parse the results into our datastructure with python friendly values
    for l in stdout.split("\n"):
        if l:
            vals = l.split(",")
            if vals:
                for f in range(len(fields)):
                    # compute the python friendly values using the types lookup (defaults back to unicode)
                    fields[f][1].append(types.get(fields[f][0], unicode)(vals[f]))
    return {
        "results": dict(fields),
        "stderr": stderr
    }

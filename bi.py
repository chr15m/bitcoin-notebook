from subprocess import Popen, PIPE
import os
import re

types = {
    "%bl": int,
    "%bN": int,
}

def bi(cmd):
    # extract the fieldnames and set up a structure to store everything
    fieldnames = [p.split(",") for p in cmd.split(" ") if "%" in p].pop()
    fields = [(fn, []) for fn in fieldnames]
    # run the external command to parse
    cmd = os.path.dirname(__file__) + "/bitcoin-iterate/bitcoin-iterate -q " + cmd
    stdout, stderr = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True).communicate()
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

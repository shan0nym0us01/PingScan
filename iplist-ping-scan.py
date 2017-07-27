#!/usr/bin/env python

import subprocess
import os
with open(os.devnull, "wb") as limbo:
    file = open("./IPlist.txt")
    for ip in file:
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"

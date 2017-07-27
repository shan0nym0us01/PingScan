#!/usr/bin/env python

import sys
import subprocess
import os
with open(os.devnull, "wb") as limbo:
        #print 'Number of arguments:', len(sys.argv), 'arguments.'
        #print 'Argument List:', str(sys.argv[1])
        subnet=str(sys.argv[1])
        for n in xrange(1, 254):
                ip=subnet + ".{}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"

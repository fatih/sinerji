#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from socket import gethostname
subnames = []

### Takes a tuple of names and write the screen section of synergy.conf
def screens(*screen):
    synergyconf = open(os.path.join(os.path.expanduser("~"), ".synergy.conf"), 'w')
    synergyconf.write('section: screens\n')

    for hostnames in screen[0]:
        if hostnames is not None:    ## If the comboBox is not empty
            host = hostnames.split("_")
            synergyconf.write("\t%s:\n" % host[2])
        else:
            pass

    synergyconf.write('end\n\n')
    synergyconf.close()


def links(*screen):
    synergyconf = open(os.path.join(os.path.expanduser("~"), ".synergy.conf"), 'a')
    synergyconf.write('section: links\n')

    for hostnames in screen[0]:
        if hostnames is not None: ## If the comboBox is not empty
            subnames.append(hostnames.split('_'))
        else:
            pass

    ### writing the host part ####
    synergyconf.write("\t%s:\n" % gethostname())
    for host in subnames:
        if host[0] == 'host':
            pass
        else:
            synergyconf.write("\t\t%s = %s\n" % (host[0], host[2]))

    ### writing the client part ###
    for clients in subnames:
        if clients[2] == gethostname():
            pass
        else:
            synergyconf.write("\t%s:\n" % clients[2])
            synergyconf.write("\t\t%s = %s\n" % (clients[1], gethostname()))

    synergyconf.write('end\n')
    synergyconf.close()

if __name__ == "__main__":
    pass

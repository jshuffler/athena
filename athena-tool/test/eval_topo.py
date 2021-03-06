#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections
from functools import partial
import sys
from mininet.topo import LinearTopo
from mininet.util import waitListening
import os
# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vcontroller_ip = '192.168.0.100'
c1 = RemoteController('c1', '192.168.0.200')
#c1 = RemoteController('c1', '192.168.0.11')
cmd = './mn -c'
os.system(cmd) # returns the exit status

def setupNetwork():
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
#    topo = GeneratedTopo()
    numOfSwitch = int(sys.argv[1])
    topo = LinearTopo(k=numOfSwitch, n=0)
    OVSSwitch13 = partial( OVSSwitch, protocols='OpenFlow13')
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, switch=OVSSwitch13, autoSetMacs=True)

    net.addController(c1)
    #net.addController(c2)

    print "*** Type 'exit' or control-D to shut down network"
    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    setupNetwork()


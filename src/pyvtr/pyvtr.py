#!/usr/bin/python

'''
Created on Jun 8, 2011

@author: BMAllred
'''

from net.TraceRoute import TraceRoute
from net.Hop import Hop

def traceRoute(address):
    # Initialize trace route object.
    trace = TraceRoute(address, 30)
    
    # Display all hops.
    for hop in trace.Execute():
        print hop.HopCount + ": " + hop.Address

if __name__ == '__main__':
    traceRoute("www.google.com")
    pass
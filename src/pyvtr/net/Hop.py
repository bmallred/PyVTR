'''
Created on Jun 8, 2011

@author: BMAllred
'''

class Hop:
    '''
    Trace route hop.
    '''


    def __init__(self, address, roundTrip, hop):
        '''
        Initializes a new instance of the Hop class.
        '''
        
        self.Address = address
        self.RoundTrip = roundTrip
        self.HopCount = hop
        self.HostName = address
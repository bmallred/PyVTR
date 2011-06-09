'''
Created on Jun 8, 2011

@author: BMAllred
'''

import socket
from Hop import Hop

class TraceRoute:
    '''
    Trace route class.
    '''

    def __init__(self, destination, maxHops):
        '''
        Initializes a new instance of the TraceRoute class.
        '''
        
        self._maxHops = maxHops
        self._listenPort = 33434
        self.Destination = destination
        self.Hops = []
        
    def Execute(self):
        '''
        Executes the trace route operation.
        '''
        
        # Clear any previous results.
        self.Hops = []
        
        # Find the IP address of the host.
        destinationAddress = socket.gethostbyname(self.Destination)
        
        # Find the protocols.
        icmp = socket.getprotobyname('icmp')
        udp = socket.getprotobyname('udp')
        
        # Set the current hop count (this is relative to TTL).
        currentHop = 1
        
        # Set the operation flag.
        workInProgress = True
        
        while workInProgress:
            # Create sockets.
            receiveSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
            
            # Bind sockets.
            receiveSocket.bind(("", self._listenPort))
            sendSocket.setsockopt(socket.SOL_IP, socket.IP_TTL, currentHop)
            sendSocket.sendto("", (destinationAddress, self._listenPort))
            
            # Create a new hop object.
            hop = Hop("*", 0, currentHop)
            
            try:
                # Return the first address (discard the data for now).
                # TODO: Retrieve round trip time.
                data = receiveSocket.recvfrom(512)
                hop.Address = data[0]
                
                # TODO: Remove after debugging.
                print data
                
                # Attempt to resolve the host name.
                try:
                    hop.HostName = socket.gethostbyaddr(hop.Address)[0]
                except socket.error:
                    hop.HostName = hop.Address
                
            except socket.error:
                pass
            finally:
                # Clean-up operations.
                sendSocket.close()
                receiveSocket.close()
            
            # Add the hop to the collection.
            self.Hops.append(hop)
            
            # Decide whether we need to continue.
            if hop.Address == destinationAddress or currentHop > self._maxHops:
                workInProgress = False
            else:
                currentHop += 1
        
        return self.Hops

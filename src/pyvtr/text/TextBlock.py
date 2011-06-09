'''
Created on Jun 8, 2011

@author: BMAllred
'''
from pyvtr.text.BlockType import BlockType

class TextBlock:
    '''
    Text block class.
    '''

    def __init__(self, text, blockType = BlockType.Plain, postText = ""):
        '''
        Initializes a new instance of the TextBlock class.
        '''
        
        self.InnerBlocks = []
        self.Text = text
        self.Type = blockType
        self.PostText = postText
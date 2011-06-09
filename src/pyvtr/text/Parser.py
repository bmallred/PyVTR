'''
Created on Jun 8, 2011

@author: BMAllred
'''
from pyvtr.text.TextBlock import TextBlock
from pyvtr.text.BlockType import BlockType

class Parser:
    '''
    Text parser for writing output to various data structures.
    '''

    def __init__(self, templateFile):
        '''
        Initializes a new instance of the Parser class.
        '''
        
        self._Blocks = []
        self.TemplateFile = templateFile
        
    def ReadTemplate(self):
        self._Blocks = []
        
        with open(self.TemplateFile) as file:
            newBlockContext = ""
            
            # Read the next line in the file.
            for line in file.readlines():
            
                # Check for any parsing to be done.
                if line.upper() == "{ROUTES}":
                    self._Blocks.append(TextBlock(newBlockContext))
                    newBlockContext = ""
                
                elif line.upper() == "{/ROUTES}":
                    idx = line.find("{/ROUTES}")
                    trashLength = idx + 9
                    postText = line[trashLength:len(line)]
                    self._Blocks.append(TextBlock(newBlockContext, BlockType.Route, postText))
                    newBlockContext = ""
                
                elif line.upper() == "{HOPS}":
                    self._Blocks.append(TextBlock(newBlockContext, BlockType.Route))
                    newBlockContext = ""
                
                elif line.upper() == "{/HOPS}":
                    idx = line.find("{/HOPS}")
                    trashLength = idx + 7
                    postText = line[trashLength:len(line)]
                    self._Blocks[-1].InnerBlocks.append(TextBlock(newBlockContext, BlockType.Hop, postText))
                    newBlockContext = ""
                
                else:
                    newBlockContext += line
                
                # If there is content then we want to add it to the collection then clear it.
                if len(newBlockContext) > 0:
                    self._Blocks.append(TextBlock(newBlockContext))
                    newBlockContext = ""
            
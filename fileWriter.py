import os

class FileWriter( object ):

    def __init__( self ):
        self.dir = 'Enter your directory'

    def writeListToFile( self, subName, itemList ):
        ''' Write contents of a list to a file '''
        self.filePath = os.path.join(self.dir, subName+'.txt')
        with open (self.filePath, 'w') as f:
            for item in itemList:
                f.write('{0} \n'.format(item))
from savedContentParser import SavedContentParser

class UnsaveContent ( SavedContentParser ):

    def __init__( self ):
        super(UnsaveContent, self).__init__()
        self.savedContent = self.getSavedContent()

    def unsaveContentPerSubreddit( self, subName ):
        ''' Unsave content from a specific subreddit '''
        for content in self.savedContent:
            if content.subreddit.display_name == subName:
                content.unsave()
    
    def unsaveAllContent( self ):
        ''' unsave all saved content '''
        for content in self.savedContent:
            content.unsave()

    def unsaveContent( self, content ):
        ''' unsave the given content '''
        content.unsave()
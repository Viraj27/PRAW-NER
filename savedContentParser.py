from   basePRAW import PRAW, praw
#import praw

class SavedContentParser( PRAW ):

    def __init__(self):
        super(SavedContentParser, self).__init__()
        self.subToUrlsDict = {}

    def getSavedContent(self):
        ''' get all saved posts/comments from the authorized user's profile '''
        savedContent = self.getUser().saved() #ListingGenerator object
        return savedContent

    def getAllSavedSubReddits( self ):
        ''' get all subreddits for which some post/comment was saved in reverse sorted order '''
        savedContent = self.getSavedContent()
        for content in savedContent:
            if content.subreddit.display_name in self.subsDict:
                self.subsDict[content.subreddit.display_name] += 1
            else:
                self.subsDict[content.subreddit.display_name] = 1
        #print(self.subDict)
        #print(sorted(self.subDict.items(), key = lambda x: x[1], reverse = True) )
        a = sorted(self.subsDict.items(), key = lambda x: x[1], reverse = True)
        return dict(a).keys() # find a better way of getting to this

    def getContentUrlsPerSubreddit( self ):
        ''' Return content URLs specific to the subreddit '''
        savedContent = self.getSavedContent()
        for content in savedContent:
            linkUrl = content.link_url if isinstance(content, praw.models.Comment) else content.url
            subName = content.subreddit.display_name
            if subName in self.subToUrlsDict:
                self.subToUrlsDict.get(subName).append(linkUrl)
            else:
                self.subToUrlsDict[subName] = [linkUrl]
        print(self.subToUrlsDict)
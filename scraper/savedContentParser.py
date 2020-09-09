from   base.basePRAW   import PRAW, praw
from   writer.fileWriter import FileWriter 
#import praw
import os
import sys
class SavedContentParser( PRAW ):

    def __init__(self):
        super(SavedContentParser, self).__init__()
        self.subToContentsDict = {}
        self.fileWriter    = FileWriter()

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

    def getContentPerSubreddit( self ):
        ''' Return content URLs specific to the subreddit '''
        savedContent = self.getSavedContent()
        for content in savedContent:
            title   = content.link_title if isinstance(content, praw.models.Comment) else content.title
            linkUrl = content.link_url if isinstance(content, praw.models.Comment) else content.url
            subName = content.subreddit.display_name
            if subName in self.subToContentsDict:
                self.subToContentsDict.get(subName).append(title + '->' + linkUrl)
            else:
                self.subToContentsDict[subName] = [linkUrl]
        
    def sendContentsToWriter( self ):
        ''' Send the contents to the file writer '''
        for subName in self.subToContentsDict.keys():
            self.fileWriter.writeListToFile(subName, self.subToContentsDict.get(subName))

print(os.getcwd())
print(sys.path)
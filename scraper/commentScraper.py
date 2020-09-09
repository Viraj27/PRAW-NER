from writer.fileWriter import FileWriter
import praw

class CommentScraper( object ):

    def __init__( self ):
        # Comment scraping can be done in read only mode
        # Hence, no need to provide username and password to init reddit instance 
        self.reddit      = praw.Reddit('commentScraper')
        self.topComments = []
        self.fileWriter  = FileWriter()

    def scrapeTopCommentsUsingPostID( self, postID ):
        ''' Scrap all the top comments from a post's ID '''
        post = self.reddit.submission(id = postID)
        post.comments.replace_more(limit=0)
        for top_level_comment in post.comments:
            self.topComments.append(top_level_comment.body)

    def scrapeTopCommentsUsingPostUrl( self, postUrl ):
        ''' Scrap all the top comments from a post's URL '''
        post = self.reddit.submission(url = postUrl)
        post.comments.replace_more(limit=0)
        for top_level_comment in post.comments:
            self.topComments.append(top_level_comment.body)

    def sendCommentsToWriter( self ):
        ''' Send scraped comments to writer '''
        self.fileWriter.writeCommentsToFile( self.topComments )
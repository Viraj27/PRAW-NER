import praw
import logging

class PRAW (object):

    def __init__( self ):
        self.reddit   = praw.Reddit('savedPostsParser')
        self.subsDict = {}

    def getUser(self):
        ''' return a Redditor object '''
        user = self.reddit.user.me()
        return user
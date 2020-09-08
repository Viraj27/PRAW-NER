from commentScraper     import CommentScraper
from fileWriter         import FileWriter
import spacy

class NamedEntityRecognizer( CommentScraper, FileWriter ):

    def __init__( self) :
        super(NamedEntityRecognizer, self).__init__()
        self.nerModel = spacy.load('en_core_web_lg')
        self.entities = []

    def recognizeEntityFromTopComments( self, entity ):
        ''' Given the desired entity, only the text matching that entity will be added 
            to the entities list
            For ex : Book name is To Kill A Mockingbird by Harper Lee and entity passed is Books
            In this scenario, self.entities = ['To Kill A Mockinbird'] '''
        for comment in self.topComments:
            doc = self.nerModel(comment)
            for ent in doc.ents:
                if ent.label_ == entity:
                    self.entities.append(ent.text)
    
    def sendEntitiesToWriter( self ):
        ''' Send the list of entities to the writer '''
        self.fileWriter.writeCommentsToFile( self.entities ) 
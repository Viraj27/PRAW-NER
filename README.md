
<H1> <center> PRAW-NER (PRAW) </center> </H1>

PRAW-NER is a toolkit built over the Python Reddit API Wrapper (PRAW) which provides easy access to all the elements of Reddit. It uses the Python API's exposed by Reddit to extract posts, comments and saved content and can be extrapolated to everything that is available on Reddit. NER stands for Named Entity Recognition - this is used to pick out entities from given raw text, in this case, a post or a comment.

The requirement stemmed from the hundreds of saved posts and comments I had gathered over the last 4-5 years and a need to really pick out the most important things only. Scraping posts or top-level comments and then picking out only the relevant entities in them helped me sort out my Reddit profile.

---

<H2> PRAW Information </H2>

[Here is all the information you will need to learn about PRAW.](https://praw.readthedocs.io/en/latest/index.html)

---

<H2> Configuration </H2>

Configuring an instance of PRAW can be found in [PRAW's configuration page](https://praw.readthedocs.io/en/latest/getting_started/configuration.html). PRAW provides multiple ways of configuring an instance of the API, but if the plan is to open-source your work on PRAW, then it is recommended to use a [.ini file](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html) and add it to .gitigore list so that your personal information stays with you.
If you are looking to access a certain user (or your own) profile via the API, then you will need to provide your Reddit username and password on the .ini file along with the user agent name. Along with this, you will need a client secret and client ID which will be used as OAuth by Reddit. The steps to obtain those can be found [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) 

---

<H2> Code Walkthrough </H2>

Once you are set with your configuration, we can look at what this toolkit provides and how you can leverage it for your own purpose.

1. Initializing Reddit instance

I have created 2 distinct configurations or "sites", based on the need of PRAW. One is a site to access my own profile, other is a generic site to access public content on Reddit. Note that one .ini file can hold multiple sites.
These can be found in */base/basePRAW.py and /scraper/commentScraper.py.* 2 sites, **savedPostsParser** and **commentScraper** are the 2 sites that need to be passed to the Reddit object to instantiate the Reddit API.
If one is looking only to scrape content and store it locally, they can use the commentScraper.py config as you won't need to pass in your Reddit Credentials for it.

2. Parsing saved content from user profiles

scraper/savedContentScraper.py provides different methods using which one can extract saved data from Reddit. Depending on what the user needs, they can get the saved subreddit, saved content specific to a subreddit and more generally, all saved content in a user's profile.


3. Unsave Content

Once saved content has been pulled in, the user can easily clear that space by using /unsave/unsaveContent.py.

4. Parsing comments on any post on Reddit

scraper/commentScraper.py provides methods with which users can obtain all top-level comments on a post either using the post URL or using the post ID.


5. File Writer

The file writer takes as input all the scraped content and writes it to a local directory provided by the user. 

6. Named Entity Recognition (NER)

NER/namedEntityRecognizer.py uses spaCy's [English Language model](https://spacy.io/usage/models). [Named Entity Recognition](https://spacy.io/usage/linguistic-features#named-entities) is one of spaCy's linguistic features where they provide a set list of entities that their model has been trained on. 
For my use case, I wanted to extract the book titles in all the posts and comments I had saved. So, I used the *'WORK OF ART'* entity of the spaCy model to get the book titles I wanted. 
Please Note : Sometimes, spaCy may not be able to recognize the entities that you need recognized. For this, spaCy also provides a mechanism to [retrain the original model or create new models from scratch](https://spacy.io/usage/training#ner)
Finally, these entities are all consolidated in a list which is passed to the File Writer.
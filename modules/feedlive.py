from .business import Analytics
from .post import Post


class FeedLive(Post, Analytics):
    """Live streams created by the user."""
    links = ''

    def __init__(self, description=None, **kwargs):
        '''Builder for the live objects
        '''
        super().__init__(description, **kwargs)
        self.links = input('Type the link of your live\n>')

    def read(self):
        '''
        Prints instance attributes
        '''

    def delete(self):
        '''
        Deletes the instance
        '''

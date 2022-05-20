import random

from .constants import locations, filters
from .post import Post
from .business import Analytics
from .feedstory import FeedStory


class FeedPost(Post, Analytics):
    '''
    Posts created by the user
    '''
    filter_selected = None
    location = None

    def __init__(self, location, description=None, **kwargs):
        """Builder for FeedPost instances

        Args:
            location ([string]): [Place where the post is loaded from]
            description ([string], optional): [Description for the FeedPost]. 
                                                Defaults to None.
        """
        super().__init__(description, **kwargs)
        self.location = location
        self.picture = []

    def get_location(user_choice=None):
        '''
        Ask the user to pick a location from the locations list,
        if none is provided, gets a random one
        '''
        if user_choice:
            return locations[user_choice]
        else:
            location = random.sample(locations, 1)[0]
            print(location)
            return location

    def set_filter(self):
        """Enumerates the items of the filters list and uses the numeric input 
        to assign it to self.filter_selected
        """
        print('Select the filter for your picture')
        self.filter_selected = filters[super().list_item_selector(
            filters)]

    def read(self):
        print('#'*15, 'POST', '#'*15)
        super().print_picture()
        print(f'Filter: {self.filter_selected}')
        super().show_description()
        print(self.location)
        super().show_likes()
        super().show_tags()
        for key, value in self.new_attributes.items():
            print(f'{key}: {value}')

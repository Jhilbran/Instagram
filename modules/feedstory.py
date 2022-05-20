from datetime import datetime

from .business import Analytics
from .constants import typography
from .post import Post


class FeedStory(Post, Analytics):
    """Stories created by the user"""
    typography = None
    emoji = None
    background_color = None
    text_color = None
    created = None

    def __init__(self, created, description=None, active=True, **kwargs):
        super().__init__(description, **kwargs)
        self.created = created
        self.active = active
        self.picture = []

    def set_typography(self):
        print('Select the typography for your story')
        self.typography = typography[super().list_item_selector(typography)]

    def delete(self):
        pass

    def is_valid(self):
        """Gets the created datetime for the instance and evaluates if 24 hours have passed
        """
        lifetime = (datetime.now() - self.created).total_seconds()//3600
        if lifetime <= 24:
            print(
                f'The story is will be active for {24 - lifetime} more hours')
            return True
        else:
            print('The story is already inactive')
            self.active = False
            return False

    def read(self):
        """Show the instance attributes only if the duration between the created time
        and datetime.now() is >=24
        """
        print('#'*15, 'STORY', '#'*15)
        if self.is_valid():
            if self.picture:
                super().print_picture()
            super().show_description()
            print(self.typography)
            super().show_likes()
            super().show_tags()
            for key, value in self.new_attributes.items():
                print(f'{key}: {value}')

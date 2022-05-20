from .business import Analytics
from .post import Post
from .constants import music, visual_effects


class FeedReel(Post, Analytics):
    """Reels created by the user"""
    video_file = None
    music_background = None
    visual_effect = None
    music = None
    ext = None

    def __init__(self, description, video=None, music_choice=None,
                 visual_choice=None, **kwargs):
        '''
        Builder for the Reel object
        '''
        super().__init__(description, **kwargs)
        self.video_file = video
        self.music_background = music_choice
        self.visual_effect = visual_choice

    def delete(self):
        '''
        Deletes the instance
        '''
        pass

    def read(self):
        '''Prints the instance attributes
        '''
        print('#'*15, 'REEL', '#'*15)
        super().show_description()
        super().print_picture()
        print(f'Music background: {self.music_background}')
        print(f'Visual effects: {self.visual_effect}')
        super().show_likes()
        super().show_tags()
        for key, value in self.new_attributes.items():
            print(f'{key}: {value}')

    def add_effects(self):
        """Enumerates the items of the filters list and uses the numeric input 
        to assign it to self.visual_effects
        """
        print('Select the visual effect for the reel')
        self.visual_effect = visual_effects[super().list_item_selector(
            visual_effects)]

    def add_music(self):
        """Enumerates the items of the filters list and uses the numeric input 
        to assign it to self.visual_effects
        """
        print('Select the background music for the reel')
        self.music_background = music[super().list_item_selector(
            music)]

from datetime import datetime

from .feedreel import FeedReel
from .feedpost import FeedPost
from .feedstory import FeedStory
from .audio_file import AudioFile
from .business import Business


class User(Business):
    """
    Platform users creation
    """
    username = None
    bio = None
    followers = 0
    following = 0
    address = None

    def __init__(self, username, bio=None, **kwargs):
        self.username = username
        self.user_pic = []
        self.load_userpic()
        self.bio = bio
        self.user_new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def load_userpic(self):
        print('Load your picture and hit Ctrl-D',
              'or Ctrl-Z ( windows ) to save it.')
        while True:
            try:
                line = input()
            except EOFError:
                break
            self.user_pic.append(line)
        try:
            if line:
                return True
        except UnboundLocalError:
            print('Picture load failed')
            return False

    def print_userpic(self):
        if self.user_pic:
            print('')
        for linea in self.user_pic:
            if linea:
                print(linea)
        print('')

    def show_followers(self):
        '''
        Prints the number of likes for the instance
        '''
        print(f'This user has {self.followers} followers')

    def show_following(self):
        '''
        Prints the number of likes for the instance
        '''
        print(f'This user follows {self.following} users')

    def show_bio(self):
        if self.bio:
            return self.bio
        else:
            return "This post doesn't have a description"

    def read_user(self):
        print('#'*15, 'USER', '#'*15)
        print(self.username)
        self.print_userpic()
        self.show_bio()
        print('Address: ')
        print(self.address)
        self.show_followers()
        self.show_following()
        for key, value in self.user_new_attributes.items():
            print(f'{key} = {value}')
        print('#'*80)

    def read_feed(self, feed):
        for post in feed:
            post.read()

    def post(self):
        description = input('Add your post description\n>')
        print('Type:\n 1. To type your location\n',
              '2. To pick a random one')
        location_choice = int(input('>'))
        if location_choice == 1:
            location = input('Type your location: ')
        else:
            location = FeedPost.get_location()
        new_post = FeedPost(location, description)

        if new_post.load_picture("picture"):
            print("Picture loaded!")
        else:
            print("Couldn't load picture")
            return False
        new_post.set_filter()
        new_post.tag_people()
        return new_post

    def story(self):
        description = input('Add the title for your story\n>')
        print('Type:\n 1. To enter a personalized created time\n',
              '2. To set it automatically')
        creation_choice = int(input('>'))
        if creation_choice == 1:
            print("Type the created time in the 'dd/mm/yyyy 24:00:00' format")
            created = datetime.strptime(input('>'), '%d/%m/%Y %H:%M:%S')
        else:
            created = datetime.now()
            print('Created time: ', created.strftime("%d/%m/%Y %H:%M:%S"))
        new_story = FeedStory(created, description)
        story_picture = input(
            'Do you want to load a picture with your story? Y/N\n>').title()
        if story_picture == 'Y':
            if new_story.load_picture("picture"):
                print("Picture loaded!")
            else:
                print("Couldn't load picture")
                return False
        elif story_picture == 'N':
            new_story.picture = None
        new_story.set_typography()
        new_story.tag_people()
        return new_story

    def reel(self):
        description = input('Add a title for your reel\n>')
        new_reel = FeedReel(description)
        if new_reel.load_picture("video"):
            print("Video loaded!")
        else:
            print("Couldn't load video")
            return False
        reel_music = input(
            'Do you want background music in the reel? Y/N\n>').title()
        if reel_music == 'Y':
            new_reel.add_music()
            new_reel.music = AudioFile(new_reel.music_background)
        elif reel_music == 'N':
            new_reel.music_background = None
        reel_effect = input(
            'Do you want a visual effect in the reel? Y/N\n>').title()
        if reel_effect == 'Y':
            new_reel.add_effects()
        elif reel_effect == 'N':
            new_reel.visual_effect = None
        return new_reel

    def give_likes(self, item):
        item.likes += 1
        return True


class Address:
    """docstring for Address."""

    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

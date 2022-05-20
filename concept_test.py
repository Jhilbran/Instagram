# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:51:43 2021

@author: villajh
"""

import datetime
import os

from modules.business import Business
from modules.feedpost import FeedPost
from modules.feedstory import FeedStory
from modules.feedreel import FeedReel
from modules.user import Address, User

postfeed = []
storyfeed = []
reelfeed = []
main_feed = []
days_ago_3 = datetime.datetime.now() - datetime.timedelta(days=3)


def clear():
    '''Clears the screen'''
    os.system('cls')


def get_user():
    '''
    Get Username
    '''
    return input('Type your username\n>')


def get_bio():
    '''
    Gets the user's bio if input 'Y' is received
    '''
    add_bio = input('Do you want to add a bio? Y/N\n>').title()
    if add_bio == 'Y':
        bio = input('Type your bio\n>')
        return bio
    return None


def create_post(user):
    """Creates a FeedPost object from the user.post() function

    Args:
        user ([User Object]): [name of the user]

    Returns:
        [postfeed]: [appends the FeedPost object to a list]
    """
    pub = user.post()
    postfeed.append(pub)
    main_feed.append(pub)
    return main_feed


def create_story(user):
    """[Creates a ]

    Args:
        user ([type]): [description]

    Returns:
        [type]: [description]
    """
    pub = user.story()
    main_feed.append(pub)
    storyfeed.append(pub)
    return main_feed


def create_reel(user):
    """Creates a FeedReel object from the user.reel() function

    Args:
        user ([User Object]): [name of the user]

    Returns:
        [reelfeed]: [appends the FeedReel object to a list]
    """
    pub = user.reel()
    reelfeed.append(pub)
    main_feed.append(pub)
    return main_feed


user1 = User('Jhilbran', 'bio data')
clear()

""" 
print(post2.overview("Post #2"))
main_feed = user1.promotion_post(post3, main_feed) """

post1 = FeedPost('Barranquilla',
                 'Example Post',
                 active=True,
                 advertisement=False,
                 business=False)
clear()
story1 = FeedStory(datetime.datetime.now(),
                   'Story1description')
clear()


main_feed.append(post1)
main_feed.append(story1)


# clear()
reel1 = create_reel(user1)
clear()

main_feed = user1.promotion_post(main_feed[2], main_feed)
user1.read_feed(main_feed)

user1.address = Address(
    'Calle 116 # 42C-80',
    'Barranquilla',
    'Atlantico',
    '080012',
    'Torre F - Apto 1205',
)

user1.read_user()

# porque reel1 == main_feed[2] da false?

# Los feed objects, no estan vinculados al usuari, agregar feed como atributo de instancia

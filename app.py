# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:51:43 2021

@author: villajh
"""
import datetime
import os
import datetime

from modules.user import User
from modules.feedpost import FeedPost
from modules.feedstory import FeedStory

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


user1 = User(get_user(), get_bio())
clear()

create_post(user1)
clear()

create_story(user1)
clear()

create_reel(user1)
clear()

user1.give_likes(postfeed[0])
user1.give_likes(storyfeed[0])

user1.read_feed(postfeed)
user1.read_feed(storyfeed)

from modules.business import Analytics
from modules.post import Post
from .feedreel import FeedReel
from .feedlive import FeedLive


class ExtendedIgtv(Post, Analytics, FeedReel, FeedLive):
    """docstring for ExtendedIgtv."""

    def __init__(self, arg):
        super(ExtendedIgtv, self).__init__()
        self.arg = arg

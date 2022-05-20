import random


class Business:
    business_account = True

    def __init__(self, business_account=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_account = business_account

    def promotion_post(self, pub, feed):
        '''Add the post to the beggining of the feed'''
        try:
            index = feed.index(pub)
        except ValueError:
            print('The post is not in the list \n')
            return feed
        else:
            del feed[index]

        feed.insert(0, pub)
        return feed


class Analytics:
    number_of_views = 0
    accounts_reached = 0

    def __init__(self, number_of_views=0, accounts_reached=0, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.number_of_views = number_of_views
        self.accounts_reached = accounts_reached

    def overview(self, pub_name):
        if self.number_of_views != 0:
            return f'{pub_name} reached {random.randint(self.number_of_views,1000)} % more accounts'

    def engagement(self, user):
        """Prints and returns the engagement rate of the particular feed object

        Args:
            user ([User]): [Name of the user who posted the feed object]

        Returns:
            [engmt_rate]: [Sum of likes and comments of the feed object divided 
            by the amount of followers of the user who posted it expressed in 
            percentage]
        """
        interactions = self.likes + len(self.comments)
        engmt_rate = (interactions/user.followers)*100
        print(f'This post has {engmt_rate}% of engagement rate')
        return engmt_rate

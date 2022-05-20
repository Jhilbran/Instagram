class Post():
    """Superclass for Posts"""
    picture = []

    def __init__(self, description=None, **kwargs):
        """[initialize description, likes, tags, comments and the kwargs]

        Args:
            description ([str], optional): [description]. Defaults to None.
        """
        self.description = description
        self.likes = 0
        self.tags = []
        self.comments = []
        self.new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def show_comments(self):
        """[Prints the comments on the instance and returns the comments 
        attribute]

        Returns:
            [list]: [list with all the comments for the instance]
        """
        if self.comments:
            print(self.comments)
            return self.comments
        else:
            return "This post doesn't have comments"

    def show_likes(self):
        '''
        Prints the number of likes for the instance
        '''
        print(f'{self.likes} likes')

    def get_likes(self):
        '''
        Gets the number of likes for the instance
        '''
        return self.likes

    def show_description(self):
        """Returns the description for the instance, in case there is none, 
        it returns an info msg

        Returns:
            [type]: [description]
        """
        if self.description:
            print(self.description)
            return True
        else:
            print("This post doesn't have a description")
            return False

    def list_item_selector(self, list_name):
        """Prints the items in list_name returning the index of the item 
        selected. Value and Index errors handling built-in

        Args:
            list_name ([iterable]): [Object to choose from]

        Returns:
            [index]: [index of the selected item through an input]
        """
        for i, item in enumerate(list_name, start=1):
            print(f'{i}. {item}')
        try:
            return int(input('>'))-1
        except ValueError:
            print('Please input a numeric value')
            return None
        except IndexError:
            print('The value is not in the list')
            return None

    def tag_people(self):

        print('Tag your friends one by one and use CTRL+D',
              ' or CTRL+z(windows) to save')
        while True:
            try:
                line = input('>')
            except EOFError:
                break
            self.tags.append(line)

    def load_picture(self, type):
        print(f'Load your {type} and hit Ctrl-D',
              'or Ctrl-Z ( windows ) to save it.')
        while True:
            try:
                line = input()
            except EOFError:
                break
            self.picture.append(line)
        try:
            if line:
                return True
        except UnboundLocalError:
            print(f'{type} load failed')
            return False

    def print_picture(self):
        if self.picture:
            print('')
        for linea in self.picture:
            if linea:
                print(linea)
        print('')

    def show_tags(self):
        if self.tags:
            return self.tags
        else:
            print("This post doesn't have tags")
            return None

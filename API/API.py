from Models import Post
import datetime

class API:
    def __init__(self, config=None):
        self.config = config

    def add_post(self, post: Post):
        # Simulating a POST HTTP request to backend
        return True

    def get_posts(self, start_date: datetime.datetime, end_data: datetime.datetime):
        return [
            Post("Adam", "Python is a snake", datetime.datetime(2021, 5, 1)),
            Post("Sara", "Python is a programming language", datetime.datetime(2021, 5, 3))
        ]

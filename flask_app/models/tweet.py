from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import flash


class Tweet:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.user = None
    
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def create_tweet(cls, data):
        query = "insert into tweet (content, user_id) values (%(content)s, %(user_id)s)"
        tweet_id = connect_to_mysql("tweet").query_db(query, data)

    @staticmethod
    def validate_data(data):
        is_valid = True

        if len(data["content"]) == 0:
            is_valid = False
            flash("Content cant be empty")

        if len(data["content"]) > 160:
            is_valid = False
            flash("Content cant be more than 160 chars!")
    
        return is_valid

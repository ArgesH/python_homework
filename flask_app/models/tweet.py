from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import flash


class Tweet:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.user = None

    @classmethod
    def get_by_id(cls, id):
        query = "select * from tweet where id = %(my_id)s"
        data = connect_to_mysql("tweet").query_db(query, {"my_id": id})
        if data:
            row = data[0]
            return cls(row)
        return []

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

    @classmethod
    def update_tweet_by_id(cls, data):
        query = "update tweet set content = %(content)s where id = %(id)s"
        connect_to_mysql("tweet").query_db(query, data)
        return

    @classmethod
    def delete_tweet_by_id(cls, id):
        query = "delete from tweet where id = %(id)s"
        connect_to_mysql("tweet").query_db(query, {"id": id})
        return

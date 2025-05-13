from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app.models.tweet import Tweet


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.name = data["name"]
        self.password = data["password"]
    
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_by_email(cls, data):
        query = "select * from user where email = %(email)s"
        result = connect_to_mysql("tweet").query_db(query, data) # {"email": ...}
        if result: # [] 
            return cls(result[0])

    @classmethod
    def get_all_tweets_by_id(cls, data):
        query = "select * from tweet join user on tweet.user_id = user.id where user.id = %(user_id)s"
        results = connect_to_mysql("tweet").query_db(query, data)


        all_tweets = []
        for row in results:
            # Create a Tweet class instance from the information from each db row
            user_data = {
                "id": row["user.id"],
                "name": row["name"],
                "email": row["email"],
                "password": row["password"]
            }
            user = cls(user_data)
            # Prepare to make a User class instance, looking at the class in models/user.py
            one_tweet_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['users.id'], 
                "content": row['name'],
            }
            # Create the User class instance that's in the user.py model file
            tweet = Tweet(one_tweet_info)
            # Associate the Tweet class instance with the User class instance by filling in the empty creator attribute in the Tweet class
            one_tweet.user = user
            # Append the Tweet containing the associated User to your list of tweets
            all_tweets.append(one_tweet)
        return all_tweets

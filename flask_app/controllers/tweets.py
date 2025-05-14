from flask_app import session, redirect, request, app, render_template
from flask_app.models.user import User
from flask_app.models.tweet import Tweet

# Create tweet
# Show form to create tweet
# List user tweets

@app.route("/tweets/create", methods=["GET"])
def create_tweet_form():
    if "user_id" not in session:
        return redirect("/user/login")

    return render_template("form_tweets.html")

@app.route("/tweet/create", methods=["POST"])
def create_tweet():
    if "user_id" not in session:
        return redirect("/user/login")

    data = {
        "content": request.form["content"],
        "user_id": session["user_id"]
    }

    is_valid = Tweet.validate_data(data)
    if not is_valid:
        return render_template("create_tweet.html")

    Tweet.create_tweet(data)

    return redirect("/tweets")


@app.route("/tweets/all/")
def get_all_tweets():
    if "user_id" not in session:
        return redirect("/user/login")

    user_tweets = User.get_all_tweets_by_id({"user_id": session["user_id"]})

    return render_template("tweets.html", data=user_tweets)


@app.route("/tweets/edit/<int:id>")
def update_tweet_form(id):
    if "user_id" not in session:
        return redirect("/user/login")

    data = Tweet.get_by_id(id)

    return render_template("update_tweet.html", data=data)


@app.route("/tweet/edit/<int:id>", methods=["POST"])
def update_tweet(id):
    if "user_id" not in session:
        return redirect("/user/login")

    data = {
        "id": id,
        "content": request.form["content"]
    }

    Tweet.update_tweet_by_id(data)

    return redirect("/tweets/all")

@app.route("/tweet/delete/<int:id>", methods=["POST"])
def delete_tweet(id):
    if "user_id" not in session:
        return redirect("/user/login")

    Tweet.delete_tweet_by_id(id)

    return redirect("/tweets/all")


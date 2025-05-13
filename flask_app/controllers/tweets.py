from flask_app import session, redirect, request


# Create tweet
# List user tweets

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

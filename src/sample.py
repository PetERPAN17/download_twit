import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url():
    # tweet_fields = "tweet.fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=1600114676691439618"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    # url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)

    tweet_fields = "tweet.fields=created_at,attachments"
    expansions = "expansions=author_id,attachments.media_keys"
    media = "media.fields=media_key,type,width,duration_ms,variants,height,preview_image_url,url"
    return "https://api.twitter.com/2/tweets?{}&{}&{}&{}".format(ids, tweet_fields, expansions, media)


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer AAAAAAAAAAAAAAAAAAAAAPQ%2BkwEAAAAAyElSIZDX5syz3U5WzTeTq1%2FBZi4%3DSjakJqRvMfVjTBZS6tI3pqJ4BIeUH1OsCM6yKT7Ac9Z3piskV3"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
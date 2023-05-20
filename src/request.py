import requests

class TwitterApi:

    def __init__(self):
        self.tweet_fields = "tweet.fields=created_at,attachments"
        self.expansions = "expansions=author_id,attachments.media_keys"
        self.media = "media.fields=media_key,type,width,duration_ms,variants,height,preview_image_url,url"

    def __get_request_url(self, ids):
        ids = f"ids={ids}"
        return "https://api.twitter.com/2/tweets?{}&{}&{}&{}".format(ids, self.tweet_fields, self.expansions, self.media)


    def __bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer AAAAAAAAAAAAAAAAAAAAAPQ%2BkwEAAAAAyElSIZDX5syz3U5WzTeTq1%2FBZi4%3DSjakJqRvMfVjTBZS6tI3pqJ4BIeUH1OsCM6yKT7Ac9Z3piskV3"
        r.headers["User-Agent"] = "v2TweetLookupPython"
        return r


    def get_twitter_data(self, id):
        response = requests.request("GET", self.__get_request_url(id), auth=self.__bearer_oauth)
        # print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

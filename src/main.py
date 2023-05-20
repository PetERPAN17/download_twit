import json

import list
import request
import download

twitterList = list.TwitterList()
request = request.TwitterApi()
download = download.Twitter()

def main():
    # get twitter ids
    twitterIds = twitterList.getTwitterIds()
    print(twitterIds)
    for id in twitterIds:
        # get data
        twitter_data = request.get_twitter_data(id)

        # download
        download.execute(twitter_data)


if __name__ == "__main__":
    main()
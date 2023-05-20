import os

class TwitterList:

    def __init__(self):
        twitter_list_file_name = 'twitter_list.txt'
        root_dir = os.path.dirname(__file__)
        self.twitter_list_path = os.path.join(root_dir, twitter_list_file_name)

        self.twitter_url = 'https://twitter.com/'

    def __getTwitterList(self):
        with open(self.twitter_list_path) as f:
            lines = f.readlines()
        return lines

    def getTwitterIds(self):
        twitter_list = self.__getTwitterList()

        ids = []
        for url in twitter_list:
            # print(url)
            url = url.replace(self.twitter_url, '')
            url = url.replace('/status', '')
            slash_index = url.find('/')
            url = url[slash_index + 1:100]
            question_mark_index = url.find('?')
            url = url[0:question_mark_index]
            # print(url)
            ids.append(url)
        return ids

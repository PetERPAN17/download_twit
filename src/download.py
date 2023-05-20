import json
import re
from datetime import datetime
from datetime import timedelta

import urllib.request
import urllib.error

class Twitter:
    def __init__(self):
        self.JST = 9
        self.text_length = 30
        self.savingDirectoryPath = './download'


    def __getDateTime(self, data):
        created_utc_dt = data[0]['created_at']
        created_utc_dt = datetime.strptime(created_utc_dt[:-5], "%Y-%m-%dT%H:%M:%S")

        created_jst_dt = created_utc_dt + timedelta(hours=self.JST)
        return created_jst_dt.strftime("%y%m%d %H%M%S")


    def __getText(self, data):
        text = data[0]['text'].replace("\n", '')
        https_index = text.index('https')
        text = text[0:https_index]
        text = text[0:self.text_length]
        text = re.sub('[/]', '', text)
        return text


    def __createFilename(self, data):
        date_time = self.__getDateTime(data['data'])
        user_name = data['includes']['users'][0]['username']
        text = self.__getText(data['data'])
        return f"{date_time} twitter_{user_name} {text}"


    def __download(self, downloadUrl, saveFilename):
        print(downloadUrl)
        print(saveFilename)

        try:
            urllib.request.urlretrieve(downloadUrl,"{0}".format(saveFilename))
        except urllib.error.HTTPError as e:
            print('raise HTTPError')
            print(e.code)
            print(e.reason)
        except urllib.error.URLError as e:
            print('raise URLError')
            print(e.reason)
        except FileNotFoundError:
            print('No such file or directory')
        else:
            urllib.request.urlcleanup() # Delete tmp file from urllib.request.urlretrieve


    def __downloadVideo(self, data, filename, video_count):
        bit_rate = 0
        for variant in data:
            if variant['content_type'] == 'video/mp4':
                if variant['bit_rate'] > bit_rate:
                    downloadUrl = variant['url']
                    bit_rate = variant['bit_rate']

        self.__download(downloadUrl, f"{self.savingDirectoryPath}/{filename}_{video_count}.mp4")


    def __downlaodMedia(self, data, filename):
        video_count = 1
        photo_count = 1
        for media_data in data:
            # print(json.dumps(media_data, indent=4, sort_keys=True))
            if media_data['type'] == 'photo':
                self.__download(media_data['url'], f"{self.savingDirectoryPath}/{filename}_{photo_count}.jpg")
                photo_count += 1

            if media_data['type'] == 'animated_gif':
                self.__download(media_data['variants'][0]['url'], f"{self.savingDirectoryPath}/{filename}_{video_count}.mp4")
                video_count += 1

            if media_data['type'] == 'video':
                self.__downloadVideo(media_data['variants'], filename, video_count)
                video_count += 1



    def execute(self, data):
        # print(json.dumps(data, indent=4, sort_keys=True))

        filename = self.__createFilename(data);

        self.__downlaodMedia(data['includes']['media'], filename)

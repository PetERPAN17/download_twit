Run Command

sudo docker rm download-twitter

sudo docker run -v /home/peterpan17/project/twitter/src:/usr/src/app --name download-twitter twitter-api python main.py

sudo docker rm $(sudo docker ps -a)
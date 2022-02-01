# This a sample for selenium to run with docker container
## Introduction:-
* In this Example we saw a linkedin page follower profile link extract
## lib:-
* selenium
# Steps:-
1. Enter your email and password in `credits.py` under `email` and `password`.
2. Get your company number from url when u visit the follower page in  the `credits.py`
3. run the command `docker-compose build`
4. run the command `docker-compose up`
5. you can check the extracted profile links in `data.txt` of app folder.

## check:-
* you can selenium docker is working or not by these steps
* open `docker-compose.yml` file and change the `sh-c "python3 linkedin.py"` to `sh -c "python3 check.py"`
* run  the command `docker-compose build`
* run the command `docker-compose up`
* if you are able to run u can see the screenshot of the page.

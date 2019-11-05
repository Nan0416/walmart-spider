#!/bin/bash

# go to server, start a python3 environment, install scrapyd (and pymongo for database), run scrapyd make sure it can accept outside request.
# go to local, configure scrapy.cfg, make new target that points to the server
# scrapyd-deploy target -p scrapying_scripts // deploy the project
# with the following curl request to start jobs.

# scrapyd-deploy local
# list all spider 
# http://localhost:6800/listspiders.json?project=scrapying_scripts
# check jobs
# http://127.0.0.1:6800/jobs

# url=http://qinnan.dev:6800
url=http://localhost:6800
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-bed
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-cellphone
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-dining-room-set
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-dolls
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-laptop
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-mens-jeans
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-mens-sweaters
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-radio-control-car
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-sports
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-tablet
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-tv
curl ${url}/schedule.json -d project=scrapying_scripts  -d spider=walmart-womens-jeans

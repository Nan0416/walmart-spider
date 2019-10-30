#!/bin/bash


#self defined
#scrapyd is a server that helps starting different spiders.
#scrapy-deploy is a client of the scrapyd that help package project and submit them to scrapyd server.
#submit spider != start spider.
#scrapy use scrapy.cfg and generate setup.py to package the scrapy project.

#API
# scrapyd-deploy local
# list all spider 
# http://localhost:6800/listspiders.json?project=scrapying_scripts
# check jobs
# http://127.0.0.1:6800/jobs

curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-bed
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-cellphone
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-dining-room-set
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-dolls
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-laptop
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-mens-jeans
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-mens-sweaters
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-radio-control-car
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-sports
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-tablet
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-tv
curl http://localhost:6800/schedule.json -d project=scrapying_scripts  -d spider=walmart-womens-jeans

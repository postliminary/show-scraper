#!/bin/bash

#clean
echo "Cleaning..."
rm -f output/shows.json
rm -f output/rc.log
rm -f output/images/full/*
if [ -d ../show-schedule ]
    then
        rm -f ../show-schedule/app/data/shows.json
        rm -f ../show-schedule/app/images/shows/full/*
fi

#run scrapy crawler
echo "Running scraper..."
scrapy crawl rc --logfile=output/rc.log

#copy output to app
echo "Copying output files..."
if [ -d ../show-schedule ]
    then
        cp output/shows.json ../show-schedule/app/data/shows.json
        cp output/images/full/* ../show-schedule/app/images/shows/full
fi

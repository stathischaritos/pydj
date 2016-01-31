INTRODUCTION:
=============
This is a data journalism tool whose purpose is the collection, visualization and analysis of data collected from twitter, facebook and various
new sources defined by the end user. The point is to track certain hashtags , accounts , facebook pages and external news sources and analyze 
topic trends and their relations. Anotation should be requested optionaly from the user and all data can then be gathered and used to implement
supervised methods or improve the current tools.

INSTALLATION:
=============
For now we will focus on using an ubuntu computer and we'll do the installation of all diferent components manually.

UBUNTU:
-------

1. Install Elasticsearch

	https://gist.github.com/wingdspur/2026107
	
2. Make the twitter index and start the river (see section "CREATING THE TWITTER-ELASTICSEARCH RIVER")

3. Make a cronjob for the Facebook script to run every 8 hours (the facebook script goes back in time up to 25 posts so that should be enough to keep everything updated, otehrwise pick you own interval).


TASKS:
======

	1. Make the data collection tool into a python daemon service that can easily be installed into a random computer and run without issues. Start with twitter and facebook for now. Twitter will use the elasticsearch method and facebook the script we already have , after a few improvements.
	
	2. Create a simple browsing interface with javascript for start.
	
CREATING THE TWITTER-ELASTICSEARCH RIVER:
=========================================

1. Make the index:

	curl -XPUT 'http://localhost:9200/twitter/' -d '{
		"settings" : {
			"index" : {
				"number_of_shards" : 1,
				"number_of_replicas" : 0
			}
		}
	}'

2. Start the River:

	curl -XPUT localhost:9200/_river/twitter/_meta -d '
	{
		"type" : "twitter",
		"twitter" : {
			"oauth" : {
				"consumer_key" : "**************",
				"consumer_secret" : "**************",
				"access_token" : "**************",
				"access_token_secret" : "**************"
			},
			"filter" : {
				"follow" : "13514762,567285403,236362651,270839361,1870936627,495277374,106673706,436162711,1324893229,69532732,938790602,1966444098,1869139004,821945424,612076857,262702883,1027404487,603178613,215699843,990052896,216292807,216784891,216650259,562839732,1075102646,615041030,1493885648,602903174,993096637,816959106,521357452,980097320,614409542,1924482961,13294452,147543162,28528873,289400495,19067940,279157541,94336415,87939274,358204197,19017675,158021529,221795831,33318995,410224577,374712154,844126038,158550139,256943061,1420747592,108955199,14291684,14281853,5680622,78085410,217749896,59591873,491776264,528890147,147988448,1192786104,395351827,347851279,472412809,162023981,163951423,474963532,71723706,41778159,105161244,212717686,112273454,97027086,381453862,93826417,325066904,7343682,7599192,28076891,17289752,95455794,19900973,2201623465,2324261167,2199795114,2209485030",
				"tracks" : "#EU, #EP2014, #Stopimmigration, #exitEU, #Europe, #UE, #EU2014, #troika, #stopislam,#Europeas2014, #LosEspañolesPrimero, #pxc, #España2000, #primerelsdecasa, #stopinmigracion, #inmigracion, #eleccionesUE , Europeas2014, LosEspañolesPrimero, pxc, España2000, primerelsdecasa, stopinmigracion, inmigracion, eleccionesUE"
			}
		}
	}'


Facebook Index:
===============
	curl -XPUT 'http://localhost:9200/facebook/' -d '{
		"settings" : {
			"index" : {
				"number_of_shards" : 1,
				"number_of_replicas" : 0
			}
		}
	}'
	
	
LINKS:
======

Enchant:
--------
This is a python library for spellchecking we could use it to filter the tokens so that we dont get garbage
List of dictionaries here:
    http://packages.ubuntu.com/precise/myspell-dictionary

Gensim:
-------
Python library for using LDA and LSA for topic tracking.

    sudo pip install --upgrade gensim
    http://radimrehurek.com/gensim/intro.html


Topic Tracking algs:
--------------------

LDA:

	http://shuyo.wordpress.com/2011/05/18/latent-dirichlet-allocation-in-python/

LSA:

	http://blog.josephwilk.net/projects/latent-semantic-analysis-in-python.html

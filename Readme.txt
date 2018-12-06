Carl Wilhjelm
Georgia State University

About: 

TweetMapper is a series of programs I designed that attempt to identify tweets that implicitly reference drugs using slang words. The tweets provided in this git represent a test sample I use to identify bugs in the full set which contains over 5.5 million tweets. 

These tweets were obtained from a list of search terms which may be referenced in /dictionary/metaDictWordsOnly. This list included terms that both implicitly and explicitly reference drugs i.e. pharmaceutical names and street names, as well as some other terms related to our epidemiological interests. Additionally, a subset of only the explicit terms was also created for identification purposes.

In its current iteration the program identifies 2-grams in both the set of tweets with explicit references and the set of all tweets and maps the frequency of (k/e)/(k/a) with k representing the number of instances over the set. 

To Run:

See the LocalDir.py file and change the directory structure. Any directories included in the structure must be created manually prior to running the code.

The current scheme for __init__.py assumes only that the tweets and the set of explicit terms is provided.

use __init__.py to run. 

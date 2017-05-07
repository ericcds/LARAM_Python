# LARAM_Python
Implements Latent Aspect Rating Analysis Modeling in Python

Code adapted from original Java code from Hongning Wang and Python scripts from Zhang Yin for use in aspect rating analysis of Yelp Review text sanitation aspects.

1. Added error handling for all major text-processing blocks.
2. Corrected issues with data types that prevented the creation of new vocabulary objects.
3. Corrected issues in code that prevented successful bootstrapping using new aspects.
4. Modified initial aspect words to focus on topical aspects related to sanitation (in addition to Value, Food, and Service)

Reference: 
Hongning Wang, Yue Lu and Chengxiang Zhai. Latent Aspect Rating Analysis on Review Text Data: A Rating Regression Approach. The 16th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD'2010), p783-792, 2010.

TODO: Multiprocessing support for the bootstrapping and scoring algorithm
TODO: Handle parsing issues with certain Unicode characters (presumably emoji) commonly found in review text. The code currently handles errors in stemming, parsing, or other issues with text processing with try/except blocks that do little besides skip the "bad" review and print out an error.
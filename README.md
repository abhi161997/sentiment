<!-- This document has been prepared in Github-compliant Markdown -->

#Sentiment Analysis

A Python script for conducting sentiment analysis on text documents.

#Contributors

James O'Sullivan (josullivan.org)  
Patricia Hswe  
Prateek Chandan  
Anurag Shirolkar  
Anthony Durity  
Olexander Yermakov  

#Redistribution

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

Imported libraries and packages remain the property of their respective owners.

Users of this code assume all responsibility for its use.

#Requirements

This script requires the nltk. To install via terminal, use:  

sudo pip install -U nltk

#Usage

usage: sentiment_analysis.py [-h] [-o OUTPUT] [-n N_CHUNKS] infile

positional arguments: infile

optional arguments:

  -h, --help  
  show this help message and exit

  -o OUTPUT, --output OUTPUT  
  name of the results folder

  -n N_CHUNKS, --n_chunks N_CHUNKS  
  Set number of chunks the text should be divided into

example:

$ python sentiment_analysis.py file1.txt -n 10 -o results_folder

The above command will read the file `file1.txt`, break it into 10 chunks and put the 3 plots into the `results_folder` folder. If you don't specify the `-n 10` part the file will be divided into 10 parts by default. If you don't specify the `-o results_folder` part the results will be stored in `sentiment_analysis_results` folder.

#Acknowledgements

With thanks to the Penn State University Libraries.

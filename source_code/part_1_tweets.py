import pymongo
import csv
import re
import io

# Reference of mongo data fetch from http://umashanthan.blogspot.com/2015/01/how-to-retrieve-data-from-mongodb-using.html
# connecting to mongoDB
connection = "mongodb://localhost:27017/"
my_client = pymongo.MongoClient(connection)
my_db = my_client["Data_Assignment_3"]
print "Collecting tweets from", connection

# fetching the data from mongoDB
tweet = my_db.twitter_search
tweetsList = tweet.find()

# maintained an array of positive and negative words
positive_words = []
negative_words = []
# counter for maintaining tweet count
tweet_count = 0

# read the positive words and negative words from file and append the array
file = io.open("positive-words.txt", "r")
# removing the extra kines or spaces from the words while reading
positive_words = file.read().split()
file.close()

file = io.open("negative-words.txt", "r")
# removing the extra kines or spaces from the words while reading
negative_words = file.read().split()
file.close()


# file for visualization
visualizeFile_v = open("visualizeFile.csv", "wb")
vfWriter = csv.writer(visualizeFile_v)
vfWriter.writerow(["All words", "Positive or Negative"])

# cleaning "RT" method from the tweets
def clean_RT(string):
    if string is not None:
        # regex used - .sub() method
        string = re.sub('RT', "", string)
        return string

# Reference from dictionary count from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
def dict_count(str):
    dict_words = dict()
    # converting into lower case and removing spacing
    if str.lower().split() is not None:
        words = str.lower().split()
    # iterating of words in string
    for word in words:
        if word in dict_words:
            #incrementing the count in dict_words
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    return dict_words

# a writer function which is used to return correct values to to write in csv
def writer_fun(words_H, words_S, text):
    # Case: Neutral
    if len(words_S) == 0 and len(words_H) == 0:
        return [tweet_count, text, "","", "neutral"]
    # Case: Positive
    if len(words_H) > len(words_S):
        return [tweet_count, text, ', '.join(words_H), ', '.join(words_S), "positive"]
    # Case: Negative
    if len(words_H) < len(words_S):
        return [tweet_count, text, ', '.join(words_H), ', '.join(words_S), "negative"]
    # Case: Neutral (if tweet has same number of positive and negative words)
    if 0 < len(words_H) == len(words_S):
        return [tweet_count, text, ', '.join(words_H), ', '.join(words_S), "neutral"]

# creating a csv file name tweets_details
# Reference from https://docs.python.org/3/library/csv.html for writer
with open('tweets_details.csv', 'wb') as output_file:
    # writing the columns in the file
    writer = csv.writer(output_file)
    writer.writerow(["Tweet", "Message/tweets", "positive", "negative", "polarity"])

# tweets are already cleaned in assignment 3 except "RT" word
# iterating tweets
    for item in tweetsList:
        # list to store positive and negative words in each tweet
        words_H = []
        words_S = []
        tweet_count += 1
        # cleaning RT from the tweets's text
        item["text"] = clean_RT(item["text"])
        # iterating the positive and negative words for a tweet
        if (item["text"]) is not None:
            list = dict_count(item["text"]).keys()
        for word in positive_words:
            if word in list:
                # appending the positive word for a tweet
                words_H.append(word)
                # writing word in the visualization file
                vfWriter.writerow([word, "positive"])
        for word in negative_words:
            if word in list:
        # appending the negative word for a tweet
                words_S.append(word)
        # writing word in the visualization file
                vfWriter.writerow([word, "negative"])
        # writing the entire content in the file
        writer.writerow(writer_fun(words_H, words_S, item["text"]))

print "tweets_details.csv created"


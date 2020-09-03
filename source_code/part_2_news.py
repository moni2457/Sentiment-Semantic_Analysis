import csv
import os

# constant for total files in created for news articles
N = 699
# search word
word = "canada"
# highest relative frequency article
highest_article = 0
# highest relative frequency
re_fre_high = 0
# highest word Count for Canada
highest_count = 0
highest_count_article = 0

# creating a csv file name news_pt2
# Reference from https://docs.python.org/3/library/csv.html for writer
file = open("news_pt2.csv", "wb")
writer = csv.writer(file)
# writing the columns in the csv file
writer.writerow(["Term", "Canada"])
writer.writerow(["Canada appeared in x documents", "Total Words(m)", "Frequency"])

# iterating through all the N documents in the 'News' directory
# Reference for iterating files in the directory taken from https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
for root, dirs, files in os.walk(os.getcwd()):
 # counter for maintaining file count
    f_no = 0
    for file in files:
        # word Count for Word : canada
        word_Canada_count = 0
        # all file that end with news_article.txt
        if file.endswith("news_article.txt"):
            f_no += 1
            # count the total words in the article file - text file
            # reading each article file
            with open(str(f_no) + "news_article.txt", 'r') as f:
                data = f.read()
                words = data.split()
            # file read to count the occurence of word: canada
            with open(str(f_no) + "news_article.txt", 'r') as f:
                # reading the lines in the text file
                f_reader = f.readlines()
                # validating file number to be less than equal to N
                if f_no <= N:
                    for lines in f_reader:
                        if word in lines.lower():
                            # counting all the occurences of word: canada
                            word_Canada_count = word_Canada_count + 1
            # writing the details of occurences in the csv for those file which contains the word : canada
            if word_Canada_count != 0:
                if word_Canada_count > highest_count:
                    highest_count = word_Canada_count
                    highest_count_article = f_no

                # writing in the csv file
                writer.writerow([str(f_no) + "news_article.txt", len(words), word_Canada_count])
                # calculating the highest relative frequency of all the articles containing canada
                rel_fre = float(word_Canada_count) / float(len(words))
                # finding the maximum value of relative frequency among all articles
                if rel_fre > re_fre_high:
                    re_fre_high = rel_fre
                    highest_article = f_no
print "news_pt2.csv created"
f.close()
print "Highest frequency of Canada word in file:"+ str(highest_count_article) + "news_article.txt"
print "Highest relative frequency file: " + str(highest_article) + "news_article.txt"

# writing the article in  a text file
file_1 = open(str(highest_article) + "news_article.txt", 'r')
file_2 = open("highest_frequency_file.txt", 'wb')
file_2.writelines(file_1.readlines())
print "highest_frequency_file.txt" + " created."


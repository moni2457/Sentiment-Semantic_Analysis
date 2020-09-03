import os
import csv
import math

# array of search words
search_words = ["canada", "university", "dalhousie university", "halifax", "business"]
# constant for total files in created for news articles
N = 699

# creating a csv file name news_pt1
# Reference from https://docs.python.org/3/library/csv.html for writer
file = open("news_part1.csv", "wb")
writer = csv.writer(file)
# writing the column names in the csv file
writer.writerow(["Total Documents", str(N)])
writer.writerow(
    ["Search Query", "Document containing term(df)", "Total Documents(N)/ number of documents term appeared (df)",
     "Log10(N/df)"])

#  iterating for all the words
for word in search_words:
    f_no = 1
    df = []
    # iterating through all the N documents in the 'News' directory
    # Reference for iterating files in the directory taken from https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    for root, dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith("news_article.txt"):
                with open(str(f_no) + "news_article.txt", 'r') as f:
                    f_reader = f.readlines()
                    # iterating to 699 files
                    if f_no <= N:
                        for lines in f_reader:
                            if word in lines.lower():
                                # appending the number in df list
                                df.append(f_no)
                                break
                # incrementing the files
                f_no += 1
    # writing the values in the csv file
    writer.writerow([word, str(len(df)), str(N) + "/" + str(len(df)), math.log10(N / len(df))])
print "news_part1.csv created"


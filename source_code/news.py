import pymongo

# Reference of mongo data fetch from http://umashanthan.blogspot.com/2015/01/how-to-retrieve-data-from-mongodb-using.html
# connecting to mongoDB
connection = "mongodb://localhost:27017/"
my_client = pymongo.MongoClient(connection)
my_db = my_client["Data_Assignment_3"]
print "Collecting tweets from", connection

# fetching the data from mongoDB
data = my_db.NewsApi
newsList = data.find()

# counter for file count
f_no = 1
# iterating news article
for item in newsList:
    # validating the articles
    if f_no < 700:
        # writing articles with title, description & content
        # the articles are already cleaned in Assignment 3
        if item["title"] is not None and item["description"] is not None and item["content"] is not None:
            file_content = "Title:" + item["title"] + "\n" + "Description:" + item["description"] + "\n" + "Content:" + \
                               item["content"] + "\n"
            with open(str(f_no) + "news_article.txt", "wb") as f:
                f.write(file_content)
                # writing articles with title & content where description is None
        if item["title"] is not None and item["description"] is None:
            file_content = "Title:" + item["title"] + "\n" + "Content:" + item["content"] + "\n"
            with open(str(f_no) + "news_article.txt", "wb") as f:
                f.write(file_content)
                # writing articles with title & description where content is None
        if item["title"] is not None and item["content"] is None:
            file_content = "Title:" + item["title"] + "\n" + "Description:" + item["description"] + "\n"
            with open(str(f_no) + "news_article.txt", "wb") as f:
                f.write(file_content)
        # incrementing the file counter
        f_no += 1

N = f_no - 1
print "Total files " + str(N) + " txt files"

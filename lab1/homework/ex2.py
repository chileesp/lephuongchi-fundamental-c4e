from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
posts = db["posts"]
post = {
    'title': "ok bai gi day",
    'author': "chi",
    'content': "ok bai gi do haha"
}
posts.insert_one(post)

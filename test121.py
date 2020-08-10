import pymongo
client = pymongo.MongoClient("mongodb://root:qingclass2020@123.57.53.215:27017/")
collection_users = client['mysb']['users']
cursor =collection_users.find_one(
{"_id":"obR2_v2knAfgqSiv4hd7TJdpZT3I"},{"learnHistory.subjects.subject-1000000.levels.level-1000005.lessons.lesson-236.record":1})
# for c in cursor:
#     print(c)
print(cursor)
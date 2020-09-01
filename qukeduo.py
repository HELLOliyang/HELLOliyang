import requests
import json
import random
from faker import Faker
fakerCN = Faker(locale='zh_CN')
print(fakerCN.address())
print(fakerCN.name())
print(fakerCN.user_name())
random_name = fakerCN.user_name()
base_url = 'https://api-test-admin-zuul.qkduo.cn/'
payload = {
    'email':'admin@qingclass.com',
    'password':'e10adc3949ba59abbe56e057f20f883e'
}
session = requests.session()
r = session.post(base_url+'auth-center/nologin/login',data=payload)
print(r.text)
a = json.loads(r.text)
print(a.get('data').get('token'))
token = a.get('data').get('token')
header = {'cookie':'zuulToken='+token}
get_userinfo = session.get(base_url+'auth-center/noauth/getUserInfo',headers=header)
print(get_userinfo.text)


# 课程组管理
# 课程组列表
course_group_data = {
    'title':'',
    'termId':'',
    'courseId':'',
    'pageSize':20,
    'pageNo':1
}
course_group = session.get(base_url+'qkd-admin7/course/getList',params = course_group_data,headers=header)
print(course_group.text)
# 课程组分类列表
courseCategory_data = {
    "pageSize":'10',
    "pageNo":'1'
}
courseCategory = session.get(base_url+'qkd-admin7/courseCategory/getList',params = courseCategory_data,headers = header)
print(courseCategory.text)
# 班级系统列表
skuClass_data = {
    "pageSize":'10',
    "pageNo":'1'
}
skuClass = session.get(base_url+'qkd-admin7/skuClass/getList',params = skuClass_data,headers = header)
print(skuClass.text)
# # 组管理id遍历
# organize = session.get(base_url+'qkd-admin7/organize/autoComplete',params={'title':''},headers = header)
# print(organize.text)
# organize_dict = json.loads(organize.text)
# organizeDict_list = organize_dict['data']['list']
# organizeDict_id = []
# for i in range(len(organizeDict_list)):
#     organizeDict_id.append(organizeDict_list[i]['id'])
# a = organizeDict_id[random.randint(0,len(organizeDict_list)-1)]
# print(a)
#获取课程组分类名称遍历
courseCategoryName_data = {
    "title":'',
    "organizeId":'92'
}
courseCategory_name = session.get(base_url+'qkd-admin7/courseCategory/autoComplete',params = courseCategoryName_data,headers = header)
print(courseCategory_name.text)
courseCategoryName_dict = json.loads(courseCategory_name.text)
courseCategoryList = courseCategoryName_dict['data']['courseCategoryList']
courseCategory_id = []
for i in range(len(courseCategoryList)):
    courseCategory_id.append(courseCategoryList[i]['id'])
print(len(courseCategoryList))
print(courseCategory_id[random.randint(0,len(courseCategoryList))-1])
# 添加课程组
# addCourse_data = {
#     'title':'课程组-'+fakerCN.first_romanized_name(),
#     'organizeId':92,
#     'categoryId':courseCategory_id[random(0,len(courseCategoryList)-1)],
#     'type':1
# }
# addCourse = session.post(base_url+'qkd-admin7/course/addCourse',data=addCourse_data,headers = header)
# print(addCourse.text)
# addCourse_dict = json.loads(addCourse.text)
# addCourse_id = addCourse_dict['data']['courseId']
# print(addCourse_id)
#学期列表
termList_data = {
    'title':'',
    'termId':'',
    'status':'',
    'pageSize':'10',
    'pageNo':'1'
}
termList = session.get(base_url+'qkd-admin7/term/getList',params = termList_data,headers = header)
print(termList.text)
#学期门类列表
subject_data = {
    'pageSize':'20',
    'pageNo':'1'
}
subject = session.get(base_url+'qkd-admin/subject/getList',params = subject_data,headers = header)
# print(subject.text)
subject_dict = json.loads(subject.text)
subjectList_dict = subject_dict['data']['list']
print(subjectList_dict)
print(subjectList_dict[1]['subjectList'][1]['id'])
#辅导员列表
staff = session.get(base_url+'qkd-admin7/staff/getAllStaff',headers = header)
print(staff.text)
staff_dict = json.loads(staff.text)
print(staff_dict['data']['list'][1]['id'])
# 所属分类列表
category = session.get(base_url+'qkd-admin7/category/getAllCategory',headers = header)
print(category.text)
category_dict = json.loads(category.text)
print(category_dict['data']['list'][1]['id'])
# 新增学期
addTerm_data = {
    'courseId':'',
    'title':'学期-'+random_name,
    'shortTitle':'简称-'+random_name,
    'image':'',# 学期封面
    'slogan':'slogan',
    'comment':'',#评论图片
    'introduction':'',#介绍图片
    'reviewIntroduction':'',#空
    'lessonCount':random.randint(5,10),#课程总数
    'expireTime':'',#过期日期，空为永不过期
    'wechatImage':'',
    'wechatCode':'',#空
    'wechatName':'',#微信号
    'beginTime':'',#开售时间
    'endTime':'',#停售时间
    'lessonService':'',#课程服务
    'productId':'',#苹果内购Id，空
    'applePrice':'',#苹果内购价格，空
    'learningPeriod':'',#学习周期
    'staffs':'',#辅导员
    'needAddress':'',#是否需要地址
    'categoryList':'',
    'payType':'',
    'subjectList':'',
    'openDay':''#开课时间
}
addTerm = session.get(base_url+'qkd-admin7/term/addTerm',data=addTerm_data,headers = header)
print(addTerm.text)
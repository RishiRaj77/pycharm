# class User:
#
#     def __init__(self,username,user_id):
#         self.username= username
#         self.id = user_id
#         self.following = 0
#         self.followers = 0
#
#     def follow(self, user):
#         user.following += 1
#         self.following += 1
#
# user_1 = User(" nikhik" , "1")
# user_2 = User(" nikhik" , "1")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

class Question:

    def __init__(self,text,answser):
        self.text= text
        self.answer = answser

new_q = Question(" rishi ", " false")
print(new_q.text)




















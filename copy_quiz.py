import markdown as md
from canvasapi import Canvas

# See the README.md for more details on how to get the key.  Mine is stored in a file called token.txt
# This 'token.txt' is specifically excluded from git!
API_URL = "https://aueems.cce.af.mil/"
with open("token.txt") as f:
    key = f.read().strip()

canvas = Canvas(API_URL, key)

# This is really my sanity check
user = canvas.get_current_user()
print('Got user: ' + user.name)
# These are magic numbers.  Easiest is to go to the quiz in Canvas
# and look at the URL.  It will have these two numbers in there.
course = canvas.get_course(12208)
quiz = course.get_quiz(50835)

# This takes the quize and the "1" a the end becomes a "2" 
quiz.title = quiz.title[:-1] + chr(ord(quiz.title[-1])+1)
new_quiz_data = {}
for field in dir(quiz):
    if field == 'title':
        new_quiz_data[field] = quiz.title[:-1] + chr(ord(quiz.title[-1])+1)
    if field[0]=='_' or callable(getattr(quiz, field)) or field=='id' or "url" in field or "get" in field or "set" in field:
        continue
    new_quiz_data[field] = getattr(quiz, field)
# print(new_quiz_data)
new_quiz=course.create_quiz(new_quiz_data)

# Now copy the questions as well
questions = quiz.get_questions()
for question in questions:
    question_data = {}
    for field in dir(question):
        if field[0]=='_' or callable(getattr(question, field)) or 'id' in field or \
            "url" in field or "get" in field or "set" in field:
            continue
        question_data[field] = getattr(question, field)
    new_question=new_quiz.create_question(question=question_data)
    # new_question.edit()

# When this is done, it seems to have created everything, but you have to go in and click "save"
# in the edit tab in the web interface of Canvas.  I don't know how to get it "save" from Python...  
# It does copy though, so that is nice.
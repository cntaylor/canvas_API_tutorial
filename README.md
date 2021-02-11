# canvas_API_tutorial

For now this repository is just there to record what I had to do to get things working in Canvas.  In general, I am trying to use Python to create quizzes in Canvas.  To do this, I am using [this github project](https://github.com/ucfopen/canvasapi/) which creates a Python library called canvasapi.  It interfaces with Canvas' API which is documented [here](https://canvas.instructure.com/doc/api/)

## Getting started
To start with, install canvasapi in your Python environment (`pip install canvasapi` should work).  Following [this example](https://canvasapi.readthedocs.io/en/stable/examples.html#boilerplate), you will need the URL of Canvas and an API_KEY.  To get the API_KEY:
* Login into Canvas
* On the left, click on the "person in a circle" icon and go to Settings
* Click the button called "New Access Token"
* This will give you a token that you need to copy and put somewhere. This token is your "API_KEY"

At this point, in Python, you can create a canvas object and it will be linked to your account.  To find the course I am interested in, I did:
```
canvas.get_current_user().get_courses()
for course in courses:
  print(course)
```
From the printout, I grabbed the course number I was interested in (21903, if you care) and then did:
`course = canvas.get_course(21903)`

I am now living in the course.

## Creating a new quiz
The key to creating a new quiz is creating a dictionary in Python.  This dictionary should have fields as described in [this webpage](https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.update).  I was able to create a quiz with just the following information:
```
quiz_data = {'title' : 'Test Quiz', 'quiz_type': 'assignment'}
new_quiz=course.create_quiz(quiz_data)
```
A couple of other fields that may be of interest are: 'description', which is the text up front that you can describe the quiz with.  You can also modify the due dates using 'all_dates'.  For example, 
```
{'due_at': '2021-02-16T20:30:00Z',
  'unlock_at': None,
  'lock_at': None,
  'base': True}
```

## Editing an existing quiz
The format for doing this confused me a bit.  So I have `new_quiz`, but I want to change the 'assignment' for example to more accurately describe the quiz.  I have a string called `desc` that holds the new description.  To edit the quiz, I run the command:
`new_quiz.edit(quit={'description':desc} )`
You have to call edit, you have to pass in a names parameter `quiz` and then have a dictionary with the new information.  A bit counter-intuitive to me, but now it is documents, so have fun editing things!

# NewsPaper App

This is a skeleton structure that i will use for my django projects. To use it in a new project, do the following:
1.

Also, follow this django best practices: 
1. Keep your code organised:

project/
    app1/
        __init__.py
        models.py
        views.py
        urls.py
    app2/
        __init__.py
        models.py
        views.py
        urls.py
    templates/
        base.html
        app1/
            index.html
            detail.html
        app2/
            index.html

2. Follow the DRY principle
DRY stands for Don’t Repeat Yourself. It means that you should avoid duplicating code as much as possible. Instead, write reusable code that can be used in multiple places. This not only saves time but also makes your code easier to maintain.

# Bad code 😿
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# Good code 😸
def calculate(length, width, operation):
    if operation == 'area':
        return length * width
    elif operation == 'perimeter':
        return 2 * (length + width)

3. Use Django’s built-in features
Django provides many built-in features such as authentication, database migrations, and template rendering. Using these features can save you a lot of time and effort. You don’t have to reinvent the wheel every time you need to implement a feature.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# created 
from myapp.models import MyModel
from myapp.forms import MyForm

@login_required
def my_view(request):
    template_name = 'my_template.html'
    # Example, if you have model or form 
    data = MyModel.objects.all()
    form = MyForm()
    # Do something 
    # ...
    # ..
    # .
    context = {
          'posts': data,
          'form': form,
          }
    return render(request, template_name, context)

4. Use the Django ORM wisely
The Django ORM (Object-Relational Mapping) is a powerful tool for interacting with databases. However, it’s important to use it wisely. Avoid making too many queries to the database, as this can slow down your application. Use query optimization techniques such as prefetch_related and select_related to minimize the number of queries.
# Bad code 😿
users = User.objects.all()
for user in users:
    print(user.username)

# Good code 😸 
users = User.objects.only('username')
for user in users:
    print(user.username)

6. Use version control
7. Document your code


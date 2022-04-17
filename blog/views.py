from django.shortcuts import render


posts = [ {
			'author': 'John Doe',
			'title': 'Blog Post 1',
			'content': 'First Blog content',
			'date_published': 'November 22, 2020'
			},
		{
			'author': 'Bob Smith',
			'title': 'Blog Post 2',
			'content': 'Second Blog content',
			'date_published': 'November 23, 2020'
			}
		]

def home(request):
	context = {'posts': posts}
	return render(request, 'blog/home.html', context)

def about(request):
	context = {'title': 'About'}
	return render(request, 'blog/about.html', context)

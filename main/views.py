from django.shortcuts import render

def homeView(request):
	data = {
		"title": "home page",
		"users": [
			{
			"id": 1,
			"name" : "amir",
			"email" : "amir@gmail.com"
			},
			{
			"id": 2,
			"name" : "hossein",
			"email" : "hossein@gmail.com"
			},
			{
			"id": 3,
			"name" : "ali",
			"email" : "ali@gmail.com"
			}
		]

	}

	return render(request,"main/home.html",data)

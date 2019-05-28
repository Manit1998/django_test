from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
from account.models import data

from django.views.decorators.csrf import csrf_exempt
import hashlib

@csrf_exempt
def login(request):

	#Post request handling
	if request.method == 'POST':
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		print("hello",username,password)
		hash_object = hashlib.sha1(password.encode())
		hex_dig = hash_object.hexdigest()
		print(hex_dig)

		#validating user
		user = data.objects.filter(username=username,password=hex_dig)
		print(user)
		# print(user[0].username)

		# if (request.session['username']=="sujeet"):
		# 	print("hello everyone")
		# 	status = 'already logged in ..'

		# if wrong matching..
		if not user:
			status = 'wrong username and password'

			#sending back Json Response
			
		else:
			status = 'logged in successfully'
			request.session['username']=username
			print(request.session['username'])

		return JsonResponse({'status':'ok','result':{'response':status}})


	#handling other request
	else:
		return JsonResponse({'status':'ok','result':{'response':'invalid request!!'}})


@csrf_exempt
def signup(request):

	#handling post request
	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		email=request.POST.get("email")

		print("hello",username,password,email)
		hash_object = hashlib.sha1(password.encode())
		hex_dig = hash_object.hexdigest()
		print(hex_dig)

		user = data(username=username,password=hex_dig,email=email)
		user.save()

		#sending back Json Response
		return JsonResponse({'status':'ok','result':{'response':'successfully created'}})

	#handling other requests
	else:
		
		return JsonResponse({'status':'ok','result':{'response':'invalid request!!'}})


from django.shortcuts import render, redirect, HttpResponse
import random

# Declare all global values
activity = []

# Function to return activity string from the dictionary bldgLegend to be placed into the list activity
def getResponse(click, num):

	bldgLegend = {"farm": "Earned " + str(num) + " golds from the farm", "cave": "Earned " + str(num) + " golds from the cave", "house": "Earned " + str(num) + " golds from the house", "casino+": "Entered a casino and won " + str(num) + " golds...Yay!", "casino-" : "Entered a casino and lost " + str(num) + " golds...Ouch!"}

	bldgResponse = bldgLegend[click]

	return bldgResponse

# Function to generate a random number for the game when envoked
def randomGold(click):
	randFarm = random.randrange(9, 21)
	randCave = random.randrange(4, 11)
	randHouse = random.randrange(1, 6)
	randCasino = random.randrange(-51, 51)

	if click == "farm":
		return randFarm
	elif click == "cave":
		return randCave
	elif click == "house":
		return randHouse
	elif click == "casino":
		return randCasino

# Function to determine whether a positive or negative result for casino activity should be generated
def checkCasino(random):
	if random < 0:
		click = "casino-"
		response = getResponse(click, random)
	elif random >= 0:
		click = "casino+"
		response = getResponse(click, random)
	print click, random
	return response

# Function to get the activity string
def getActivity(click, random):
	if click =="casino":
		act = checkCasino(random)
	elif click == "farm":
		act = getResponse(click, random)
	elif click == "cave":
		act = getResponse(click, random)
	elif click == "house":
		act = getResponse(click, random)
	return act

# Create your views here.
def index(request):
	return render(request, 'gold_app/index.html')

def process(request):
	if request.method == 'POST':
		# request.session["activity"] = []
		click = request.POST["building"]
		try:
			yourGold = request.session["yourGold"]
		except:
			request.session['yourGold'] = 0
			yourGold = request.session['yourGold']
		counter = 0
		if click == "farm":
			random = randomGold(click)
			yourGold += random
			act = getActivity(click, random)
			activity.append(act)
		elif click == "cave":
			random = randomGold(click)
			yourGold += random
			act = getActivity(click, random)
			activity.append(act)
		elif click == "house":
			random = randomGold(click)
			yourGold += random
			act = getActivity(click, random)
			activity.append(act)
		elif click == "casino":
			random = randomGold(click)
			yourGold += random
			act = getActivity(click, random)
			activity.append(act)

		request.session["yourGold"] = yourGold
		request.session["activity"] = activity
		request.session["counter"] = counter
		counter += 1

	return redirect('/')

def reset(request):
	request.session['yourGold'] = 0
	request.session['counter'] = 0
	for activities in range(len(activity)):
		activity.pop()
	try:
		del request.session['activity']
		return redirect('/')
	except:
		return redirect('/')

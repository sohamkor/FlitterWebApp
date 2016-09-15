from django.shortcuts import render
from django.http  import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime

from .models import Fleeter, Post, Follower
from .forms import AuthenticationForm, SearchForm, StatusUpdateForm, SignUpForm

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
        
    form = AuthenticationForm()
    context = {'authForm': form}
    return render(request, 'flitterMainApp/index.html', context)

def signUpUser(request):
    signUpForm = SignUpForm()
    return render(request, 'flitterMainApp/signUpPage.html', {'signUpForm': signUpForm})

def processSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstNameBox']
            lastName = form.cleaned_data['lastNameBox']
            userName = form.cleaned_data['usernameBox']
            passWord = form.cleaned_data['passwordBox']
            confirmedPassWord = form.cleaned_data['confirmPasswordBox']

            if len(passWord) < 5:
                error_msg = "The password you have chosen is too short. Please pick a longer one."
                return render(request, 'flitterMainApp/userError.html', {'message':error_msg})

            if passWord != confirmedPassWord:
                error_msg = "The passwords don't match."
                return render(request, 'flitterMainApp/userError.html', {'message':error_msg})

            if User.objects.filter(username=userName).exists():
                error_msg = "The username chosen has already been taken. Please pick another one."
                return render(request, 'flitterMainApp/userError.html', {'message':error_msg})

            user = User.objects.create_user(userName, password=passWord)
            user.first_name = firstName
            user.last_name = lastName
            user.save()

            fleeter = Fleeter(user=user)
            fleeter.save()

            return render(request, 'flitterMainApp/successfulCreationOfUser.html', {'firstName': firstName})

    return HttpResponseRedirect('/signUp')

def authenticateUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data["usernameBox"]
            password = form.cleaned_data["passwordBox"]

            mainUser = authenticate(username=username, password=password)
            if mainUser is not None:
                login(request, mainUser)
                return HttpResponseRedirect('/home')
            else:
                error_msg = "The username or password you entered doesn't seem to be right."
                return render(request, 'flitterMainApp/userError.html', {'username':username, 'message':error_msg})
        else:
            return HttpResponseRedirect('/')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/')

def getTimeOfPost(post):
    return post.dateTimePosted

def homePage(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    searchForm = SearchForm()
    statusUpdateForm = StatusUpdateForm()
    contextDict = {}

    postCount = 0
    followersCount = 0
    followingCount = 0

    thisFleeter = Fleeter.objects.filter(user__username=request.user.username)
    myPosts = Post.objects.filter(fleeter__user__username=request.user.username)
    fleetersImFollowing = Follower.objects.filter(theUserWhoIsFollowing__user__username=request.user.username)
    fleetersWhoAreFollowingMe = Follower.objects.filter(userWhoIsBeingFollowed__user__username=request.user.username)

    allPostsForMyFeed = myPosts
    for fleeterImFollowing in fleetersImFollowing:
        postsFromFleeterImFollowing = Post.objects.filter(fleeter__user__username=fleeterImFollowing.userWhoIsBeingFollowed.user.username)
        allPostsForMyFeed = allPostsForMyFeed | postsFromFleeterImFollowing

    #myPosts = sorted(myPosts, key = getTimeOfPost, reverse=True)
    allPostsForMyFeed = sorted(allPostsForMyFeed, key = getTimeOfPost, reverse=True)

    if len(thisFleeter) > 0:
        postCount = len(myPosts)
        followersCount = len(fleetersWhoAreFollowingMe)
        followingCount = len(fleetersImFollowing)
        
    contextDict['username'] = request.user.username
    contextDict['postCount'] = postCount
    contextDict['followersCount'] = followersCount
    contextDict['followedCount'] = followingCount
    contextDict['searchForm'] = searchForm
    contextDict['statusUpdateForm'] = statusUpdateForm
    contextDict['allPostsForMyFeed'] = allPostsForMyFeed
    contextDict['myUsername'] = request.user.username
                
    return render(request, 'flitterMainApp/home.html', contextDict)

def postStatusUpdate(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    statusUpdateForm = StatusUpdateForm()

    return render(request, 'flitterMainApp/postStatusUpdate.html', {'statusUpdateForm': statusUpdateForm})    

def saveStatusUpdate(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = StatusUpdateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            thisFleeter = Fleeter.objects.filter(user__username=request.user.username)
            
            if len(thisFleeter) > 0:
                fleeter = thisFleeter[0]               
                print("Found it")
            else:
                print("Can't find it")
                fleeter = Fleeter(user=request.user)
                fleeter.save()

            post = Post(fleeter=fleeter)
            post.contentString = form.cleaned_data['statusUpdateBox']
            post.dateTimePosted = datetime.datetime.now()
            post.save()

    return HttpResponseRedirect('/home')

def searchPage(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            searchTerms = form.cleaned_data['searchBox']

            if searchTerms == request.user.username:
                searchList = []
                listWithUsers = []
                followerList = []
            else:
                searchList = Fleeter.objects.filter(user__username=searchTerms)
                followerList = Follower.objects.filter(theUserWhoIsFollowing__user__username=request.user.username)
                listWithUsers = User.objects.filter(username=searchTerms)

            peopleWhoAreFleeters = []
            peopleButNotFleeters = []
            peopleImFollowing = []

            for individualFleeter in searchList:
                if not individualFleeter.user.username == "":
                    peopleWhoAreFleeters.append(individualFleeter.user.username)

            for individualPerson in listWithUsers:
                if not individualPerson.username in peopleWhoAreFleeters:
                    if not individualPerson.username == "":
                        peopleButNotFleeters.append(individualPerson)

            for follower in followerList:
                peopleImFollowing.append(follower.userWhoIsBeingFollowed)

            return render(request, 'flitterMainApp/searchPage.html', {'searchTerms': searchTerms, 'searchList': searchList, 'peopleButNotFleeters': peopleButNotFleeters, 'peopleImFollowing': peopleImFollowing})

    return HttpResponseRedirect('/home')

def processFollow(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    thisFleeter = Fleeter.objects.filter(user__username=request.user.username)
    
    if len(thisFleeter) > 0:
        fleeter = thisFleeter[0]               
        print("Found it")
    else:
        print("Can't find it")
        fleeter = Fleeter(user=request.user)
        fleeter.save()

    nameOfUsernameToFollow = request.POST.get("followButton")
    
    fleeterObjectOfUsernameToFollow = Fleeter.objects.filter(user__username=nameOfUsernameToFollow)

    newFollower = Follower(userWhoIsBeingFollowed=fleeterObjectOfUsernameToFollow[0], theUserWhoIsFollowing=fleeter)
    newFollower.save()

    return HttpResponseRedirect('/home')

def processUnFollow(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    nameOfUsernameToUnFollow = request.POST.get("unfollowButton")
    thisFollow = Follower.objects.filter(theUserWhoIsFollowing__user__username=request.user.username, userWhoIsBeingFollowed__user__username=nameOfUsernameToUnFollow).delete()

    return HttpResponseRedirect('/home')

def exploreCommunity(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    usernameList = list(User.objects.all().values_list('username', flat=True))
    usernameList.remove(request.user.username)
    followerList = Follower.objects.filter(theUserWhoIsFollowing__user__username=request.user.username)

    for individualFollower in followerList:
        if individualFollower.userWhoIsBeingFollowed.user.username in usernameList:
            usernameList.remove(individualFollower.userWhoIsBeingFollowed.user.username)

    return render(request, 'flitterMainApp/exploreCommunity.html', {'usernameList': usernameList})

def logOff(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect('/')

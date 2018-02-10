from django.contrib.auth import logout
from django.shortcuts import render
from .auth_up_in import *
from starnavi.models import Post, Like_Unlike
from django.contrib.auth.models import User

# web version
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            current_user = request.user
            return render(request, "my_cabinet.html", {'posts': Post.objects.all(),
                                                       'user': User.objects.get(pk=current_user.id)})
        else:
            return render(request, "index.html")

    if request.method == 'POST':
        if 'Login_in' in request.POST and 'Password_in' in request.POST:
            username = request.POST['Login_in']
            password = request.POST['Password_in']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                print('OK')
                return render(request, "my_cabinet.html", {'posts': Post.objects.all(),
                                                           'user': User.objects.get(
                                                            pk=User.objects.get(username=request.user.username).pk)})
            else:
                return render(request, "index.html")

        if '_signup' in request.POST:
            email = request.POST['Email_up']
            login_in = request.POST['Login_up']
            password = request.POST['Password_up']
            firstname = request.POST['FirstName_up']
            lastname = request.POST['LastName_up']
            signupresult = newuser(email, login_in, password, firstname, lastname)
            if signupresult == request.POST['Login_up']:
                user = authenticate(request, username=login_in, password=password)
                login(request, user)
                return render(request, "my_cabinet.html", {'posts': Post.objects.all(),
                                                           'user': User.objects.get(
                                                            pk=User.objects.get(username=request.POST['Login_up']).pk)})
            else:
                return render(request, "index.html", {'message': signupresult})

        # Like
        if '_like' in request.POST:
            current_user = request.user
            newlike = Like_Unlike(post_id_id=request.POST['_like'],
                                  login_id_id=current_user.id,
                                  value=True)
            newlike.likeadd()
            # t = Post.objects.get(pk=request.POST['_like'])
            # t.like = Like_Unlike.objects.filter(post_id_id=request.POST['_like'],
            #                       login_id_id=current_user.id,
            #                       value=True).count()
            # t.save()
            return render(request, "my_cabinet.html", {'posts': Post.objects.all(),
                                                       'user': User.objects.get(
                                                           pk=current_user.id)})
        # Dislike
        if '_dislike' in request.POST:
            current_user = request.user
            newdislike = Like_Unlike(post_id_id=request.POST['_dislike'],
                                  login_id_id=current_user.id,
                                  value=False)
            newdislike.likeadd()
            # t = Post.objects.get(pk=request.POST.get("_dislike", ""))
            # t.dislike = Like_Unlike.objects.filter(post_id_id=request.POST['_dislike'],
            #                       login_id_id=current_user.id,
            #                       value=False).count()
            # t.save()
            return render(request, "my_cabinet.html", {'posts': Post.objects.all(),
                                                       'user': User.objects.get(
                                                           pk=current_user.id)})
        # Add post
        if '_addpost' in request.POST:
            current_user = request.user
            newpost = Post(author_id_id=current_user.id,
                           title=request.POST['post_theme'],
                           text=request.POST['post_text'])
            newpost.save()
            return render(request, "my_cabinet.html", {'posts': Post.objects.all(),
                                                       'user': User.objects.get(
                                                           pk=current_user.id)})


        if '_signout' in request.POST:
            logout(request)
            return render(request, "index.html")

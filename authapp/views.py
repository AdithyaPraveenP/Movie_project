from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# from  .forms import NewUserForm
from django.contrib import messages, auth
from .models import UserData
from .models import AddMovie
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AddMovie, Comment
from .forms import CommentForm
from .models import Profile

# Create your views here.


def login(request):
    if request.method == 'POST':

        username = request.POST.get("username", False)
        password1 = request.POST.get("password1", False)
        user = auth.authenticate(username=username, password=password1)

        if user is not None:
            auth.login(request, user)
            # return redirect('homeapp:index')
            return redirect('authapp:index')
        else:
            messages.info(request, 'invalid Credentials please check your Credentials')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":

        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        dp = request.FILES.get('dp',None)

        password1 = request.POST.get("password1", False)
        password2 = request.POST.get('password2', False)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name taken")
                return redirect('authapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('authapp:register')
            else:
                # userdata = UserData(username=username,email=email,first_name=first_name,last_name=last_name,password1=password1,password2=password2,dp=dp)
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                profile = Profile.objects.create(user=user, profile_image=dp)
                # if dp:
                #     user.profile.profile_image = dp
                #     user.profile.save()
                # userdata.save()
                profile.save()
                print("user created")
                messages.info(request, "user exist")
                return redirect('authapp:login')

        else:
            messages.info(request, "password is not matched")
            return redirect('authapp:register')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('authapp:login')


def view_user_data(request):
    user_data = User.objects.all()
    context = {"user_data_key": user_data}
    # user_data = UserData.objects.get(dp=request.user.username)
    return render(request, "index.html", context)


def add_movie(request):
    user_data = request.user
    context = {"user_data_key": user_data}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        release = request.POST.get("release")
        url = request.POST.get("url")
        actor = request.POST.get("actor")

        cover = request.FILES['cover']
        genre = request.POST.get("genre", False)
        movie_length = request.POST.get("movie_length")
        rating = request.POST.get("rating", False)

        movie_adding = AddMovie(title=title, description=description, release=release, cover=cover, genre=genre,
                                movie_length=movie_length,url=url,actor=actor,rating=rating)
        movie_adding.save()

    return render(request, 'addmovie.html', context)


def movie_searcher(request):

    return render(request, 'moviesearcher.html')


def filter_movies(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        user_data = UserData.objects.all()
        filterd_movies = AddMovie.objects.filter(genre=genre, title__icontains=title)
        context = { "movies": filterd_movies}
        return render(request, "filteredmovie.html", context)
    else:
        user_data = UserData.objects.all()
        context = {"user_data_key": user_data}
        return render(request,'moviesearcher.html',context)


def view_movie_info(request,id):
    if request.method == 'POST':
        comments = request.POST.get('comment')
        rating = request.POST.get('rating')

        movie = get_object_or_404(AddMovie, pk=id)
        comment = Comment.objects.create(
            movie=movie,
            user=request.user,
            text=comments,
            rating=rating
        )
        comment.save()
        #return redirect('view_movie_info', id=id)
        return redirect('authapp:view_movie_info',id=id)
    else:

        movie = get_object_or_404(AddMovie, pk=id)
        comments = Comment.objects.filter(movie=movie)
        return render(request, "movie_info.html", {"movies": movie, "comments": comments})

# def view_filtered_movie_info(request):
#     movie = AddMovie.objects.get()
#     return render(request, "movie_info.html", {"movies": movie})



def all_movies(request):
    user_data = request.user
    movies = AddMovie.objects.all()
    context = {"all_movies":movies,"user_data_key": user_data}
    return render(request,"all_movies.html",context)



# def rate_movie(request, movie_id):
#     movie = get_object_or_404(AddMovie, pk=movie_id)
#     if request.method == 'POST':
#         rating_value = request.POST.get('rating')
#         if rating_value:
#             rating, created = Rating.objects.get_or_create(
#                 movie=movie,
#                 user=request.user,
#                 defaults={'rating': int(rating_value)}
#             )
#             if not created:
#                 rating.rating = int(rating_value)
#                 rating.save()
#     return redirect('movie_detail', pk=movie.pk)


def user_profile(request):
    user_form = UserChangeForm(instance=request.user)
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_profile')

    comments = Comment.objects.filter(user=request.user)
    context = {
        'user_form' : user_form,
        'comments' : comments
    }
    return render(request,'user_profile.html',context)


from django.shortcuts import get_object_or_404
from .models import Comment

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        comment.text = request.POST.get('comment')
        # Assuming you have a hidden input in your form for the movie_id
        comment.movie_id = request.POST.get('movie_id')
        comment.save()
        return redirect('authapp:user_profile')

    form = CommentForm(instance=comment)
    context = {
        'comment': comment,
        'form': form
    }
    return render(request, 'edit_comment.html', context)


def search_movies(request):

    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        movie_id = request.POST.get('movie_id')

        if search_query:
            filtered_movies = AddMovie.objects.filter(title__icontains=search_query)
        else:
            filtered_movies = AddMovie.objects.all()
        context = { "movies": filtered_movies,"movie_id": movie_id}
        return render(request, "searchedmovies.html", context)
    else:
        return render(request,'index.html')
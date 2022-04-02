from django.urls import path

from user import views

app_name = "user"   

# importing views from views..py
# from .views import main_view

urlpatterns = [
	#path('', main_view),
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    #path("user", views.user_view, name="userpage"),
    path("userpage", views.userpage_view, name="userpage"),
    path("userinput", views.user_form, name="user_form"),
    path("contact", views.contact, name="contact"),
    path("listed_company", views.company_view, name="companies"),
    path("listed_company/<id>", views.delete_company, name="delete_company"),
    path("about_dse", views.about_dse, name="about_dse"),
]

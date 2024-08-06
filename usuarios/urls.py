from django.urls import path
from . import views 

urlpatterns = [
    # Nesse path, eu crio uma url "cadastro". Quando chamo o views, necessariamente passando um paramentro, no caso, "cadastro"
    # Assim eu crio a função "cadastro" na pasta views da aplicação.
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logar/', views.logar, name='logar')
]

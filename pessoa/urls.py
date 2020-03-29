from django.urls import path
from pessoa import views

################################################
# CADA NOVA VIEW DEVE SER INSERIDA ABAIXO
# SEGUINDO OS PADRÕES DAS ANTERIORES E DE ACORDO
# COM OS NOMES DEFINIDOS PARA AS VIEWS CRIADAS
################################################

urlpatterns = [
    path('discente', views.DiscenteList.as_view(), name='discente_list'),
    path('discente/view/<int:pk>', views.DiscenteView.as_view(), name='discente_view'),
    #path('discente/new', views.DiscenteCreate.as_view(), name='discente_new'),
    path('discente/new', views.new_discente, name='discente_new'),
    path('discente/edit/<int:pk>', views.DiscenteUpdate.as_view(), name='discente_edit'),
    path('discente/delete/<int:pk>', views.DiscenteDelete.as_view(), name='discente_delete'),
    path('docente', views.DocenteList.as_view(), name='docente_list'),
    path('docente/view/<int:pk>', views.DocenteView.as_view(), name='docente_view'),
    path('docente/new', views.DocenteCreate.as_view(), name='docente_new'),
    path('docente/edit/<int:pk>', views.DocenteUpdate.as_view(), name='docente_edit'),
    path('docente/delete/<int:pk>', views.DocenteDelete.as_view(), name='docente_delete')
]
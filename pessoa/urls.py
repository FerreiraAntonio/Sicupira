from django.urls import path
from pessoa import views

################################################
# CADA NOVA VIEW DEVE SER INSERIDA ABAIXO
# SEGUINDO OS PADRÕES DAS ANTERIORES E DE ACORDO
# COM OS NOMES DEFINIDOS PARA AS VIEWS CRIADAS
################################################

urlpatterns = [    
    path('discente', views.DiscenteList.as_view(), name='discente_list'),
    #path('discente/view/<int:pk>', views.DiscenteView.as_view(), name='discente_view'),
    path('discente/view/<int:id>', views.discente_detail_view, name='discente_view'),
    path('discente/new', views.save_discente, name='discente_new'),
    path('discente/edit/<int:id>', views.save_discente, name='discente_edit'),
    path('discente/delete/<int:pk>', views.DiscenteDelete.as_view(), name='discente_delete'),
    path('docente', views.DocenteList.as_view(), name='docente_list'),
    #path('docente/view/<int:pk>', views.DocenteView.as_view(), name='docente_view'),
    path('docente/view/<int:id>', views.docente_detail_view, name='docente_view'),
    path('docente/new', views.save_docente, name='docente_new'),
    path('docente/edit/<int:id>', views.save_docente, name='docente_edit'),
    path('docente/delete/<int:pk>', views.DocenteDelete.as_view(), name='docente_delete')
]
from django.urls import path
from .views import (
    PersonaList,PersonaByDocumento,ActualizarPersona,CrearPersona,TareaList,TareaByFecha,TareaByPersona,TareaByRangoFechas,CrearTarea,EliminarPersona,EliminarTarea,ActualizarTarea

)

urlpatterns = [
    #personas
    path('personas/',PersonaList.as_view(),name='persona-list '),
    path('personas/crear/',CrearPersona.as_view(),name='persona-crear'),
    path('personas/actualizar/<int:pk>',ActualizarPersona.as_view(),name='persona-actualizar'),
    path('personas/documento/<str:documento>',PersonaByDocumento.as_view(),name='persona-por-documento'),
    path('personas/eliminar/<int:pk>',EliminarPersona.as_view(),name='persona-eliminar'),
    #tareas
    path('tareas/crear', CrearTarea.as_view(), name='crear-tarea'),
    path('tareas/',TareaList.as_view(),name='tarea-list'),
    path('tareas/actualizar/<int:pk>',ActualizarTarea.as_view(),name='tarea-actualizar'),
    path('tareas/eliminar/<int:pk>',EliminarTarea.as_view(),name='tarea-eliminar'),
    path('tareas/fecha/<str:fecha>',TareaByFecha.as_view(),name='tarea-por-fecha'),
    path('tareas/rango-fechas/<str:fecha_inicio>/<str:fecha_fin>',TareaByRangoFechas.as_view(),name='tarea-por-rango-fechas'),
    path('tareas/persona/<int:persona_id>',TareaByPersona.as_view(),name='tarea-por-persona'),
    


]
from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.productosIndex, name='productosIndex'),
    path('crear/',views.crearProducto, name='crearProductos'),
    path('detalle/<id>/',views.detalleProducto, name='detalleProducto'),
    path('eliminar/<id>/',views.eliminarProducto, name='eliminarProducto'),
    path('gestion/',views.gestionProducto, name='gestionProducto')

]
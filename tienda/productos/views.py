from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Producto,Categoria
from .forms import ProductoForm

# Vista principal de Productos
def productosIndex(request):
    categorias = Categoria.objects.all()

    #Consultar productos
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 15)
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)
    #Obtener el template
    template = loader.get_template("productos.html")
    #Agregar el contexto
    context = {"page_obj": page_obj,"categorias":categorias}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def crearProducto(request):
    #Obtener el template
    template = loader.get_template("crearProducto.html")
    #Generar Formulario
    if request.method == "POST":
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            #Guardar Producto
            producto_nuevo.save()
    else:
        form = ProductoForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def detalleProducto(request, id):
    #Consultar producto
    producto = Producto.objects.get(id=id)           

    #Consultar datos de producto
    context = {'producto':producto}
    #Obtener el template
    template = loader.get_template("detalleProducto.html")
    return HttpResponse(template.render(context,request))

def eliminarProducto(request,id):
    #Obtener el template
    template = loader.get_template("eliminarProducto.html")
    #Buscar el producto
    obj = get_object_or_404(Producto, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('productosIndex')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))


def gestionProducto(request):
    #Consultar productos
    productos_list = Producto.objects.all()
    #Configurar paginación cada 10 productos
    paginator = Paginator(productos_list, 10)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)

    #Obtener el template
    template = loader.get_template("gestionProducto.html")
    #Agregar el contexto
    context = {"page_obj": page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))


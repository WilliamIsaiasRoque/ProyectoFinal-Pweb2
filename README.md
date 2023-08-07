
<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para inscripción de laboratorios</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2023/08/06</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>15-Jul-2022</td><td>FECHA FIN:</td>
        <td>06-Aug-2022</td><td>DURACIÓN:</td><td>04 horas</td>
    </tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
        </ul>
        <td colspan="3">Alumnos:
        <ul>
        <li>Jeremy Joshua Perez Huamani - jperezhua@unsa.edu.pe</li>
        <li>Jorge Luis Escobedo Ocaña - jescobedooc@unsa.edu.pe</li>
        <li>William Isaias Roque Quispe - wroquequi@unsa.edu.pe</li>
        <li>Alan Jorge García Apaza - agarciaa@unsa.edu.pe</li>
        <li>Luis Efraín Yana Agramonte - jperezhua@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>  
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    Se trata de una aplicación web construida con el framework Django 4, que permita la inscripción de los alumnos en los horarios de laboratorios establecidos cada inicio de semestre.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema debe estar disponible en Internet a traves de una URL.
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.
    - RQ03 : El sistema debe permitir gestionar el año académico, cursos, profesores y las asignaciones de carga académica.
    -   ...

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Accounts : En esta entidad se almacenan las cuentas de admin que tendrán la facultad de poder realizar el CRUD con los productos.
    -   Comments : En esta entidad se almacena los datos de los clientes que realizan un comentario y se muestra en la sección de comentarios.
    -   PDF : En esta entidad se almacena los datos de las compras que se realizaron en un periodo de un día y las muestra junto con el total de cada una.
    -   Products : En esta entidad se encuentran los productos que se pueden agregar, borrar, editar y comprar

    ...

##  Diccionario de datos

| PRODUCTS | | | | | |
| -- | -- | -- | -- | -- | -- |
| Producto  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| name  | Cadena| No | Si | Ninguno | Nombre |
| description  | Cadena| No | No | Ninguno | Nombre |
| price  | Numerico| No | Si | Ninguno | Precio |
...

| VENTAPRODUCTO | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Product  | Cadena| No | Si | Ninguno | Cadena |
| Amount | Numerico| No | Si | Ninguno | Precio |
| Buyer | Cadena| No | Si | Ninguno | Nombres |

...
| COMMENTS | | | | | |
| -- | -- | -- | -- | -- | -- |
| Producto  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| description  | Cadena| No | No | Ninguno | Comentario |
...
| PDF | | | | | |
| -- | -- | -- | -- | -- | -- |
| Producto  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| VentaProducto  | Objeto| No | Si | Ninguno | Ventas |
...
| ACCOUNTS | | | | | |
| -- | -- | -- | -- | -- | -- |
| Producto  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| EMAIL  | Cadena| No | Si | Ninguno | correo electrónico |
| Password  | Cadena| No | Si | Ninguno | Contraseña |


##  Diagrama Entidad-Relación
![Diagrama](https://photos.app.goo.gl/aUSRMRWqfqqT9Sco8)
    ...

##  Administración con Django
    Se crean 4 Apps que son Accounts, Products, PDF y Comments, cada una con sus propios métodos y distintas opciones. En Accounts se registra en este caso al dueño de la app mediante este código.

    def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            return render(request, 'accounts/register.html', {'success': True})
        else:
            return render(request, 'accounts/register.html', {'error': 'Las contraseñas no coinciden.'})

    return render(request, 'accounts/register.html')
    def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pag_main')
        else:
            return render(request, 'accounts/login.html', {'error': 'Ingresó algún dato incorrecto.'})

    return render(request, 'accounts/login.html')
    def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get_or_create(username=username)[0]
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('pag_main')

    return render(request, 'accounts/client_login.html')


-   Luego se habilita el poder agregar, borrar, editar o listar los productos
   ```sh
   def pag_main(request):
    return render(request, 'inicio.html')

def prod_list(request):
    prods = Producto.objects.all().order_by('nombre')
    return render(request, 'productos_list.html', {'prods': prods})

def prod_detail(request, pk):
    prods = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos_detail.html', {'prods': prods})

def prod_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            prods = form.save(commit=False)
            prods.save()
            return redirect('prod_list')
    else:
        form = PostForm()
    return render(request, 'productos_edit.html', {'form': form})

def prod_edit(request, pk):
    prods = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=prods)
        if form.is_valid():
            prods = form.save(commit=False)
            prods.save()
            return redirect('prod_detail', pk=prods.pk)
    else:
        form = PostForm(instance=prods)
    return render(request, 'productos_edit.html', {'form': form})

def prod_delete(request, pk):
    prods = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        prods.delete()
        return redirect('prod_list')
    return render(request, 'productos_delete.html', {'prods': prods})

def sell_list(request):
    sells = VentaProducto.objects.all()
    return render(request, 'ventas_list.html', {'sells': sells})

def sell_new(request):
    if request.method == "POST":
        form = VentaProductoForm(request.POST)
        if form.is_valid():
            venta_producto = form.save(commit=False)
            venta_producto.calcular_precio_total()  # Calcular el precio total
            venta_producto.save()
            return redirect('sell_list')
    else:
        form = VentaProductoForm()
    return render(request, 'ventas_edit.html', {'form': form})

def sell_detail(request, pk):
    sells = get_object_or_404(VentaProducto, pk=pk)
    return render(request, 'ventas_detail.html', {'sells': sells})

def sell_edit(request, pk):
    sells = get_object_or_404(VentaProducto, pk=pk)
    if request.method == "POST":
        form = VentaProductoForm(request.POST, instance=sells)
        if form.is_valid():
            sells = form.save(commit=False)
            sells.save()
            return redirect('sell_detail', pk=sells.pk)
    else:
        form = VentaProductoForm(instance=sells)
    return render(request, 'ventas_edit.html', {'form': form})

def sell_delete(request, pk):
    sells = get_object_or_404(VentaProducto, pk=pk)
    if request.method == "POST":
        sells.delete()
        return redirect('sell_list')
    return render(request, 'ventas_delete.html', {'sells': sells})
   ```
   -Entrando como cliente únicamente se permite ver el lístado de productos y agregar comentarios, además de recibir un correo con el que se ve lo comprado.
   ```sh
   def contacto(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'contacto.html', {'comments': comments})

def comment(request):
    comments = Comment.objects.all().order_by('-created_at')
    data = [{'username': comment.user.username, 'created_at': comment.created_at, 'content': comment.content} for comment in comments]
    return JsonResponse(data, safe=False)

def form_comment(request):
    return render(request, 'comentario_form.html')

def add_comments(request):
    user = request.user
    content = request.POST.get('content', None)

    if content:
        comment = Comment.objects.create(user=user, content=content)
        return JsonResponse({'success': True, 'comment_id': comment.id})
    else:
        return JsonResponse({'success': False, 'error': 'Content is required.'})

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender_email = form.cleaned_data['sender_email']
            message = form.cleaned_data['message']

            # Agrega aquí la dirección de correo del receptor
            recipient_email = 'jluisLAB@gmail.com'
            
            all_message = f"De: {sender_email}\n\n{message}"

            # Envía el correo
            send_mail(subject, all_message, sender_email, [recipient_email], fail_silently=False)

            messages.success(request, '¡Correo enviado con éxito!')
            
            return redirect('send_email')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})
   ```
    ...

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Comments: Comentarios a realizar
    Products: Productos disponibles

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
Products
-
   ```sh
  class PostForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre del producto'
        self.fields['descripcion'].label = 'Descripción del producto'
        self.fields['precio'].label = 'Precio del producto'
        self.fields['imagen'].label = 'Imagen del producto'
        
class VentaProductoForm(forms.ModelForm):
    comprador = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Seleccione un comprador")
    cantidad = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Seleccione un producto")

    class Meta:
        model = VentaProducto
        fields = ['producto', 'cantidad', 'comprador']
        widgets = {
            'comprador': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
        }
   ```
   Comments
-
   ```sh
  class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
   ```
```sh
 urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
    path('comment/', views.comment, name='comment'),
    path('comments/add/', views.add_comments, name='add_comments'),
    path('comments/new/', views.form_comment, name='form_comment'),
    path('send_email/', views.send_email, name='send_email'),
]
   ```
   PDF
-
   ```sh
  
def generar_pdf(request):
    # Obtener todos los objetos del modelo VentaProducto
    ventas_productos = VentaProducto.objects.all()

    # Configurar la respuesta HTTP con el tipo MIME para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Lista de Ventas.pdf"'

    # Crear el PDF utilizando ReportLab
    p = canvas.Canvas(response, pagesize=A4)
    y = 800  # Posición vertical inicial
    x = 1
    for venta_producto in ventas_productos:
        p.drawString(100, y, f"Venta {x} : {venta_producto.producto}")
        p.drawString(100, y-20, f"Cantidad: {venta_producto.cantidad}")
        p.drawString(100, y-40, f"Precio: {venta_producto.precio_total}")
        y -= 60  # Espaciado entre objetos
        x += 1

    p.save()
    return response
   ```
   ACCOUNTS
-
   ```sh
  def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            return render(request, 'accounts/register.html', {'success': True})
        else:
            return render(request, 'accounts/register.html', {'error': 'Las contraseñas no coinciden.'})

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pag_main')
        else:
            return render(request, 'accounts/login.html', {'error': 'Ingresó algún dato incorrecto.'})

    return render(request, 'accounts/login.html')

def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get_or_create(username=username)[0]
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('pag_main')

    return render(request, 'accounts/client_login.html')

def logout_view(request):
    logout(request)
    return redirect('pag_main')
   ```
   ```sh
   urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('client-login/', views.client_login, name='client_login'),
    path('logout/', views.logout_view, name='logout'),
]
   ```
       ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El dueño inicia sesión.
    2. El dueño selecciona el o los productos a listar.
    3. El dueño puede realizar CRUD con los productos.
    4. El alumno tiene la posibilidad de anular un producto: confusión, precio no actualizado etc.
    5. El dueño puede ver las ventas.
    6. El dueño puede realizar la venta.

    ...

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá las ventas realizadas para que el cliente sobre todo vea esta información en cualquier otro medio. En formato PDF. 
    2. POST : Con este método se enviará el correo y las ventas. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    ...

##  Investigación: Email, Upload.
    - Email: Se utilizará la funcionalidad del uso de envío de correos electrónicos cuando el proceso de inscripciones culmine y al profesor le llegue la lista de alumnos inscritos en sus grupos a cargo.
    - Upload: Se utilizará esta funcionalidad para subír, archivos CSV para importar y exportar información en el sistema.
    Se muestran los pasos realizados para su funcionamiento correcto.
    ...

Github del proyecto: https://github.com/WilliamIsaiasRoque/ProyectoFinal-Pweb2.git

URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 - Sistema - Requisitos.
Video 02 - Modelo de datos - DD - DER.
etc…


## REFERENCIAS
-   

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
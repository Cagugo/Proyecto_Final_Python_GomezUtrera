eCommerce de Gorros Quirúrgicos
Descripción del Proyecto
Este proyecto es una aplicación web estilo eCommerce dedicada a la venta de gorros quirúrgicos. La aplicación permite a los usuarios navegar por los productos, agregarlos a un carrito de compras y realizar compras una vez que han iniciado sesión. Los administradores tienen la capacidad de gestionar los productos y las imágenes asociadas a estos productos. La aplicación está desarrollada en Python utilizando el framework Django.

Tecnologías Utilizadas
Python 3.12.2
Django 5.0.6
Bootstrap 4.3.1
SQLite (Base de datos por defecto)
HTML5
CSS3
Font Awesome (para iconos sociales y de carrito de compras)
Funcionalidades Principales
Registro y autenticación de usuarios (login/logout/signup)
Visualización de productos con imágenes
Carrito de compras
Gestión de productos (CRUD) para administradores
Página de "Acerca de mí"
Sistema de mensajes
Footer con enlaces a redes sociales
Estructura del Proyecto
arduino
Copiar código
medicalApparel/
├── media
├── manage.py
├── medicalApparel/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── register/
└── store/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── context_processors.py
    ├── forms.py
    ├── models.py
    ├── templates/
    │   └── store/
    │       ├── base.html
    │       ├── add_to_cart.html
    │       ├── cart.html
    │       ├── home.html
    │       ├── login.html
    │       ├── profile.html
    │       ├── product_list.html
    │       ├── signup.html
    ├── static/
    │   └── store/
    │       ├── css/
    │       │   └── styles.css
    │       └── img/
    │           ├── logo.png
    │           ├── carousel1.jpg
    │           ├── carousel2.jpg
    │           ├── carousel3.jpg
    │           ├── carousel4.jpg
    │           ├── carousel5.jpg
    │           ├── carousel6.jpg
    │           ├── carousel7.jpg
    │           ├── carousel8.jpg
    │           ├── carousel9.jpg
    ├── templatetags/
    │   ├── __init__.py
    │   └── multiply.py
    ├── urls.py
    └── views.py
Configuración y Ejecución del Proyecto
Prerrequisitos
Python 3.12.2
pip (gestor de paquetes de Python)
Instalación
Clona el repositorio en tu máquina local:

bash
Copiar código
git clone https://github.com/tuusuario/medicalApparel.git
cd medicalApparel
Crea un entorno virtual y actívalo:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Realiza las migraciones de la base de datos:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Carga datos de ejemplo (opcional):

bash
Copiar código
python manage.py loaddata initial_data.json
Ejecuta el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Archivos Estáticos y Medios
Asegúrate de que los archivos estáticos y de medios están correctamente configurados:

Archivos estáticos: STATIC_URL = '/static/'
Directorio de archivos estáticos: STATICFILES_DIRS = [BASE_DIR / 'store' / 'static']
Archivos de medios: MEDIA_URL = '/media/'
Directorio de archivos de medios: MEDIA_ROOT = BASE_DIR / 'media'
Estructura del Proyecto
store/static/store/css/styles.css: Contiene todos los estilos personalizados para la aplicación.
store/templates/store/base.html: Plantilla base que incluye el navbar, el footer, y los bloques para contenido.
store/templates/store/: Contiene todas las plantillas HTML específicas para cada vista (home, login, profile, etc).
Pruebas Unitarias
Archivos de Pruebas
Las pruebas unitarias se encuentran en el directorio store/tests.py. A continuación, se describen algunos casos de prueba:

Prueba de modelo de Producto

python
Copiar código
from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(title="Test Product", brand="Test Brand", price=10.00, author="Test Author")

    def test_product_creation(self):
        product = Product.objects.get(title="Test Product")
        self.assertEqual(product.brand, "Test Brand")
Prueba de vista de Lista de Productos

python
Copiar código
from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductListViewTest(TestCase):
    def setUp(self):
        Product.objects.create(title="Test Product", brand="Test Brand", price=10.00, author="Test Author")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
Prueba de vista de Detalle de Producto

python
Copiar código
from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(title="Test Product", brand="Test Brand", price=10.00, author="Test Author")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('product_detail', args=[str(self.product.id)]))
        self.assertEqual(response.status_code, 200)
Ejecución de Pruebas
Para ejecutar las pruebas, usa el siguiente comando:

bash
Copiar código
python manage.py test
Deployment
Configuración de Entorno de Producción
Configura ALLOWED_HOSTS en settings.py:

python
Copiar código
ALLOWED_HOSTS = ['tu_dominio.com', 'www.tu_dominio.com']
Configura STATIC_ROOT y MEDIA_ROOT para la producción:

python
Copiar código
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'mediafiles'
Ejecuta las siguientes órdenes para recopilar archivos estáticos y configurar la base de datos:

bash
Copiar código
python manage.py collectstatic
python manage.py migrate
Configura un servidor web (Nginx, Apache) y un servidor de aplicaciones (Gunicorn, uWSGI).

Notas Adicionales
Seguridad: Asegúrate de configurar adecuadamente las variables de entorno, la clave secreta de Django (SECRET_KEY), y las configuraciones de seguridad.
Escalabilidad: Considera el uso de una base de datos más robusta como PostgreSQL en lugar de SQLite para un entorno de producción.

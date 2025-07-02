import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from new_life_app.models import Categoria, Produto

# Criar categorias principais
esportes, created = Categoria.objects.get_or_create(nome='Esportes', defaults={'slug': 'esportes'})
beleza, created = Categoria.objects.get_or_create(nome='Beleza', defaults={'slug': 'beleza'})
bem_estar, created = Categoria.objects.get_or_create(nome='Bem-estar', defaults={'slug': 'bem-estar'})

# Criar subcategorias para Esportes
shakes, created = Categoria.objects.get_or_create(
    nome='Shakes', 
    defaults={'slug': 'shakes', 'categoria_pai': esportes}
)
suplementos, created = Categoria.objects.get_or_create(
    nome='Suplementos', 
    defaults={'slug': 'suplementos', 'categoria_pai': esportes}
)

# Criar subcategorias para Bem-estar
cafes, created = Categoria.objects.get_or_create(
    nome='Cafés', 
    defaults={'slug': 'cafes', 'categoria_pai': bem_estar}
)
chas, created = Categoria.objects.get_or_create(
    nome='Chás', 
    defaults={'slug': 'chas', 'categoria_pai': bem_estar}
)
inibidores, created = Categoria.objects.get_or_create(
    nome='Inibidores', 
    defaults={'slug': 'inibidores', 'categoria_pai': bem_estar}
)

print("Categorias e subcategorias criadas com sucesso!")
print(f"Categorias principais: {Categoria.objects.filter(categoria_pai__isnull=True).count()}")
print(f"Subcategorias: {Categoria.objects.filter(categoria_pai__isnull=False).count()}")

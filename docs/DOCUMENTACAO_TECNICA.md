# Documentação Técnica - New Life

## Arquitetura do Sistema

### Padrão MVC (Model-View-Controller)
O projeto segue o padrão MVC do Django:
- **Models**: Definição dos dados (Categoria, Produto, Depoimento, Contato)
- **Views**: Lógica de negócio e processamento de requisições
- **Templates**: Apresentação e interface do usuário

### Estrutura de Banco de Dados

#### Tabela: new_life_app_categoria
```sql
CREATE TABLE new_life_app_categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT 1
);
```

#### Tabela: new_life_app_produto
```sql
CREATE TABLE new_life_app_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(200) NOT NULL,
    descricao TEXT NOT NULL,
    beneficios TEXT NOT NULL,
    composicao TEXT NOT NULL,
    contraindicacao TEXT NOT NULL,
    modo_uso TEXT NOT NULL,
    link_compra VARCHAR(500) NOT NULL,
    destaque BOOLEAN NOT NULL DEFAULT 0,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    categoria_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES new_life_app_categoria(id)
);
```

#### Tabela: new_life_app_depoimento
```sql
CREATE TABLE new_life_app_depoimento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente VARCHAR(100) NOT NULL,
    video_youtube_id VARCHAR(20) NOT NULL,
    citacao TEXT NOT NULL,
    texto_transformacao TEXT NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    data_criacao DATETIME NOT NULL
);
```

#### Tabela: new_life_app_contato
```sql
CREATE TABLE new_life_app_contato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    assunto VARCHAR(200) NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio DATETIME NOT NULL
);
```

## Views e URLs

### HomeView
- **URL**: `/`
- **Template**: `home.html`
- **Contexto**: categorias ativas, produtos em destaque, depoimentos ativos

### ProdutosCategoriaView
- **URL**: `/produtos/<slug:categoria_slug>/`
- **Template**: `produtos_categoria.html`
- **Contexto**: categoria, produtos da categoria, outras categorias

### DetalheProdutoView
- **URL**: `/produtos/<slug:categoria_slug>/<int:produto_id>/`
- **Template**: `detalhe_produto.html`
- **Contexto**: produto, produtos relacionados

### DepoimentosView
- **URL**: `/depoimentos/`
- **Template**: `depoimentos.html`
- **Contexto**: depoimentos ativos

### ContatoView
- **URL**: `/contato/`
- **Template**: `contato.html`
- **Métodos**: GET (exibir formulário), POST (processar envio)

## Sistema de Templates

### Template Base (base.html)
Contém a estrutura comum:
- Meta tags para SEO e responsividade
- Links para Bootstrap, Font Awesome e CSS personalizado
- Navegação principal
- Rodapé
- Scripts JavaScript

### Herança de Templates
Todos os templates estendem `base.html`:
```django
{% extends 'new_life_app/base.html' %}
{% load static %}

{% block title %}Título da Página{% endblock %}
{% block content %}
<!-- Conteúdo específico da página -->
{% endblock %}
```

## Sistema de Arquivos Estáticos

### Configuração
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### Organização
```
static/
├── css/
│   └── style.css          # Estilos personalizados
├── js/
│   └── main.js            # JavaScript principal
└── img/
    ├── banner/            # Imagens do banner
    └── produtos/          # Imagens dos produtos
```

## Formulários

### ContatoForm
```python
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
            }),
            # ... outros campos
        }
```

## Configurações de Segurança

### Settings.py
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Alterar para False em produção

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-...'  # Gerar nova chave para produção

ALLOWED_HOSTS = []  # Configurar hosts permitidos em produção
```

## Performance e Otimização

### CSS
- Uso de variáveis CSS para consistência
- Minificação recomendada para produção
- Lazy loading para imagens

### JavaScript
- Event delegation para melhor performance
- Throttling em eventos de scroll
- Lazy loading de componentes

### Django
- Uso de `select_related` para otimizar queries
- Cache de templates recomendado para produção
- Compressão de arquivos estáticos

## Deployment

### Checklist para Produção
1. **Configurações**:
   - `DEBUG = False`
   - Configurar `ALLOWED_HOSTS`
   - Gerar nova `SECRET_KEY`
   - Configurar banco de dados de produção

2. **Arquivos Estáticos**:
   ```bash
   python manage.py collectstatic
   ```

3. **Migrações**:
   ```bash
   python manage.py migrate
   ```

4. **Servidor Web**:
   - Nginx + Gunicorn (recomendado)
   - Apache + mod_wsgi (alternativa)

### Exemplo de Configuração Gunicorn
```bash
gunicorn --bind 0.0.0.0:8000 setup.wsgi:application
```

## Monitoramento e Logs

### Configuração de Logs
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

## Backup e Manutenção

### Backup do Banco de Dados
```bash
# SQLite
cp db.sqlite3 backup_$(date +%Y%m%d_%H%M%S).sqlite3

# PostgreSQL
pg_dump dbname > backup_$(date +%Y%m%d_%H%M%S).sql
```

### Manutenção Regular
- Limpeza de sessões expiradas
- Backup regular do banco de dados
- Monitoramento de logs de erro
- Atualização de dependências

## Extensões Futuras

### Funcionalidades Sugeridas
1. **Sistema de Usuários**: Registro e login de clientes
2. **Carrinho de Compras**: Integração com gateway de pagamento
3. **Blog**: Sistema de artigos sobre saúde
4. **Newsletter**: Sistema de email marketing
5. **API REST**: Para integração com aplicativos móveis
6. **Multilíngue**: Suporte a múltiplos idiomas
7. **SEO Avançado**: Meta tags dinâmicas e sitemap

### Integrações Possíveis
- Google Analytics
- Facebook Pixel
- WhatsApp Business API
- Mercado Pago / PagSeguro
- Correios (cálculo de frete)
- Google Maps (localização da loja)

---

Esta documentação técnica serve como guia para desenvolvedores que irão manter ou expandir o projeto New Life.


## 🆕 Atualizações do Sistema (Junho 2025)

### Novos Campos no Modelo Produto

#### Campos Adicionados
```python
class Produto(models.Model):
    # ... campos existentes ...
    composicao = models.TextField(help_text="Composição detalhada do produto")
    contraindicacao = models.TextField(help_text="Contraindicações e precauções")
    modo_uso = models.TextField(help_text="Instruções de uso do produto")
    # ... outros campos ...
```

#### Métodos Helper Adicionados
```python
def get_composicao_list(self):
    """Retorna a composição como uma lista"""
    return [item.strip() for item in self.composicao.split('\n') if item.strip()]

def get_contraindicacao_list(self):
    """Retorna as contraindicações como uma lista"""
    return [item.strip() for item in self.contraindicacao.split('\n') if item.strip()]

def get_modo_uso_list(self):
    """Retorna o modo de uso como uma lista"""
    return [item.strip() for item in self.modo_uso.split('\n') if item.strip()]
```

### Migrações Aplicadas

#### Migração 0002
```python
# new_life_app/migrations/0002_produto_composicao_produto_contraindicacao_and_more.py
operations = [
    migrations.AddField(
        model_name='produto',
        name='composicao',
        field=models.TextField(default='Informação não disponível', help_text='Composição detalhada do produto'),
        preserve_default=False,
    ),
    migrations.AddField(
        model_name='produto',
        name='contraindicacao',
        field=models.TextField(default='Consulte um profissional de saúde antes do uso', help_text='Contraindicações e precauções'),
        preserve_default=False,
    ),
    migrations.AddField(
        model_name='produto',
        name='modo_uso',
        field=models.TextField(default='Siga as instruções da embalagem', help_text='Instruções de uso do produto'),
        preserve_default=False,
    ),
]
```

### Atualizações nos Templates

#### Sistema de Abas Bootstrap
```html
<!-- Navegação por Abas -->
<ul class="nav nav-tabs nav-fill" id="productTabs" role="tablist">
    <li class="nav-item" role="presentation">
        <button class="nav-link active" id="composicao-tab" data-bs-toggle="tab" data-bs-target="#composicao">
            <i class="fas fa-flask me-2"></i>Composição
        </button>
    </li>
    <li class="nav-item" role="presentation">
        <button class="nav-link" id="modo-uso-tab" data-bs-toggle="tab" data-bs-target="#modo-uso">
            <i class="fas fa-info-circle me-2"></i>Modo de Uso
        </button>
    </li>
    <li class="nav-item" role="presentation">
        <button class="nav-link" id="contraindicacao-tab" data-bs-toggle="tab" data-bs-target="#contraindicacao">
            <i class="fas fa-exclamation-triangle me-2"></i>Contraindicações
        </button>
    </li>
</ul>
```

#### Conteúdo das Abas
- **Composição**: Lista de ingredientes com ícones
- **Modo de Uso**: Instruções numeradas em layout responsivo
- **Contraindicações**: Alertas com cores de aviso e recomendações médicas

### Script de População Atualizado

#### Arquivo: populate_db_updated.py
- Dados realistas para todos os produtos
- Informações técnicas detalhadas
- Contraindicações específicas por tipo de produto
- Instruções de uso personalizadas

### Impacto na Performance

#### Consultas de Banco
- Novos campos não afetam consultas existentes
- Métodos helper otimizados para processamento de listas
- Índices mantidos para performance

#### Tamanho do Banco
- Aumento estimado: ~30% devido aos novos campos de texto
- Compressão recomendada para produção
- Backup incremental sugerido

### Compatibilidade

#### Versões Suportadas
- Django 5.2.3+
- Python 3.11+
- Bootstrap 5.x
- Font Awesome 6.x

#### Navegadores Testados
- Chrome 120+
- Firefox 115+
- Safari 16+
- Edge 120+

### Manutenção

#### Atualizações Futuras
- Considerar campo para "Ingredientes Ativos"
- Implementar sistema de certificações
- Adicionar campo para "Posologia Detalhada"
- Integração com APIs de regulamentação sanitária

#### Monitoramento
- Logs de acesso às abas de produto
- Métricas de engajamento com informações técnicas
- Feedback de usuários sobre clareza das informações


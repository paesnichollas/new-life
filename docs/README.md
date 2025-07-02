# New Life - Site Institucional

## Sobre o Projeto

O **New Life** é um site institucional desenvolvido para uma empresa que comercializa produtos voltados à saúde e bem-estar. O projeto foi construído utilizando **Django** no backend e tecnologias frontend modernas como **HTML5**, **CSS3**, **JavaScript** e **Bootstrap**.

## Características Principais

### 🎯 Funcionalidades
- **Página Inicial**: Banner impactante, categorias principais e produtos em destaque
- **Sistema de Produtos**: Organização por categorias (Esportes, Beleza, Bem-estar)
- **Depoimentos**: Integração com vídeos do YouTube e histórias de clientes
- **Formulário de Contato**: Sistema completo de contato com validação
- **Design Responsivo**: Compatível com desktop, tablet e mobile

### 🛠 Tecnologias Utilizadas
- **Backend**: Django 5.2.3, Python 3.11
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Banco de Dados**: SQLite (desenvolvimento)
- **Estilização**: CSS personalizado com variáveis e animações
- **Ícones**: Font Awesome

## Estrutura do Projeto

```
new_life_website/
├── setup/          # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── new_life_app/              # Aplicação principal
│   ├── models.py              # Modelos de dados
│   ├── views.py               # Views do Django
│   ├── urls.py                # URLs da aplicação
│   ├── forms.py               # Formulários
│   └── admin.py               # Configuração do admin
├── templates/                 # Templates HTML
│   └── new_life_app/
│       ├── base.html          # Template base
│       ├── home.html          # Página inicial
│       ├── produtos_categoria.html
│       ├── detalhe_produto.html
│       ├── depoimentos.html
│       └── contato.html
├── static/                    # Arquivos estáticos
│   ├── css/
│   │   └── style.css          # CSS personalizado
│   ├── js/
│   │   └── main.js            # JavaScript principal
│   └── img/                   # Imagens do site
├── venv/                      # Ambiente virtual
├── manage.py                  # Script de gerenciamento Django
└── populate_db.py             # Script para popular o banco
```

## Modelos de Dados

### Categoria
- `nome`: Nome da categoria
- `slug`: URL amigável
- `ativo`: Status da categoria

### Produto
- `nome`: Nome do produto
- `categoria`: Relacionamento com Categoria
- `descricao`: Descrição detalhada
- `beneficios`: Lista de benefícios
- `composicao`: Composição detalhada do produto
- `contraindicacao`: Contraindicações e precauções
- `modo_uso`: Instruções de uso do produto
- `link_compra`: URL para compra externa
- `destaque`: Produto em destaque
- `ativo`: Status do produto

### Depoimento
- `nome_cliente`: Nome do cliente
- `video_youtube_id`: ID do vídeo no YouTube
- `citacao`: Citação curta
- `texto_transformacao`: História completa
- `ativo`: Status do depoimento

### Contato
- `nome`: Nome do contato
- `email`: Email do contato
- `assunto`: Assunto da mensagem
- `mensagem`: Conteúdo da mensagem
- `data_envio`: Data e hora do envio

## URLs do Site

- `/` - Página inicial
- `/produtos/<categoria>/` - Produtos por categoria
- `/produtos/<categoria>/<id>/` - Detalhes do produto
- `/depoimentos/` - Página de depoimentos
- `/contato/` - Página de contato
- `/admin/` - Painel administrativo Django

## Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone ou extraia o projeto**
```bash
cd new_life_website
```

2. **Crie e ative o ambiente virtual**
```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install Django Pillow
```

4. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Popule o banco de dados com dados de exemplo**
```bash
python manage.py shell < populate_db.py
```

6. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

7. **Execute o servidor de desenvolvimento**
```bash
python manage.py runserver
```

8. **Acesse o site**
- Site: http://localhost:8000
- Admin: http://localhost:8000/admin

## Dados de Exemplo

O projeto inclui um script (`populate_db.py`) que popula o banco com:
- **3 categorias**: Esportes, Beleza, Bem-estar
- **9 produtos**: 3 produtos por categoria
- **5 depoimentos**: Com vídeos do YouTube e histórias

### Credenciais do Admin
- **Usuário**: admin
- **Senha**: admin123

## Personalização

### Cores e Estilo
As cores principais podem ser alteradas no arquivo `static/css/style.css`:
```css
:root {
    --primary-color: #28a745;    /* Verde principal */
    --secondary-color: #6c757d;  /* Cinza secundário */
    --success-color: #28a745;    /* Verde de sucesso */
    /* ... outras variáveis */
}
```

### Conteúdo
- **Produtos**: Adicione através do Django Admin
- **Imagens**: Substitua os placeholders em `static/img/`
- **Vídeos**: Atualize os IDs do YouTube nos depoimentos
- **Textos**: Edite diretamente nos templates HTML

## Funcionalidades Implementadas

### ✅ Página Inicial
- Banner com call-to-action
- Seções de categorias com ícones
- Produtos em destaque
- Depoimentos em carrossel
- Design responsivo

### ✅ Sistema de Produtos
- Listagem por categoria
- Página de detalhes completa com sistema de abas
- **Composição**: Ingredientes detalhados do produto
- **Modo de Uso**: Instruções passo a passo de utilização
- **Contraindicações**: Alertas e precauções de segurança
- Links para compra externa
- Produtos relacionados
- Sistema de destaques

### ✅ Depoimentos
- Integração com YouTube
- Histórias de transformação
- Estatísticas da empresa
- Layout em grid responsivo

### ✅ Formulário de Contato
- Validação completa
- Informações de contato
- FAQ integrado
- Links para redes sociais

### ✅ Design e UX
- Mobile-first responsive
- Animações suaves
- Hover effects
- Loading states
- Feedback visual

## Próximos Passos

Para colocar o site em produção, considere:

1. **Configurar SMTP** para envio real de emails
2. **Adicionar imagens reais** dos produtos
3. **Configurar vídeos reais** do YouTube
4. **Implementar SSL** para segurança
5. **Otimizar imagens** para performance
6. **Configurar CDN** para assets estáticos
7. **Implementar analytics** (Google Analytics)
8. **Adicionar SEO** meta tags

## Suporte

Para dúvidas ou suporte técnico, consulte:
- [Documentação do Django](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- Arquivo `teste_report.md` para detalhes dos testes realizados

---

**Desenvolvido com ❤️ para New Life - Transformando vidas através da saúde e bem-estar**



## 🆕 Atualizações Recentes

### Novos Campos de Produto (Junho 2025)
Foram adicionados três novos campos essenciais aos produtos:

#### 📋 Composição
- Lista detalhada de todos os ingredientes
- Informações sobre concentrações e componentes ativos
- Dados técnicos para transparência total

#### ⚠️ Contraindicações
- Alertas de segurança e precauções
- Informações sobre alergias e intolerâncias
- Orientações médicas importantes
- Design com cores de alerta para destaque

#### 📖 Modo de Uso
- Instruções passo a passo de utilização
- Dosagens recomendadas
- Horários ideais de consumo
- Dicas de preparo e administração

### Interface Aprimorada
- **Sistema de Abas**: Navegação intuitiva entre as informações
- **Design Responsivo**: Compatível com todos os dispositivos
- **Ícones Temáticos**: Visual claro para cada tipo de informação
- **Cores Diferenciadas**: Azul (composição), laranja (modo de uso), amarelo (contraindicações)

### Benefícios da Atualização
- ✅ **Transparência**: Informações completas sobre os produtos
- ✅ **Segurança**: Alertas claros sobre contraindicações
- ✅ **Usabilidade**: Instruções detalhadas de uso
- ✅ **Confiança**: Dados técnicos para decisões informadas
- ✅ **Compliance**: Atendimento a regulamentações de produtos de saúde


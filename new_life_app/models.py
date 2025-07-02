from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    categoria_pai = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategorias')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.categoria_pai:
            return f"{self.categoria_pai.nome} > {self.nome}"
        return self.nome
    
    def is_categoria_principal(self):
        """Retorna True se é uma categoria principal (não tem pai)"""
        return self.categoria_pai is None
    
    def get_subcategorias(self):
        """Retorna as subcategorias desta categoria"""
        return self.subcategorias.all()
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    descricao = models.TextField()
    beneficios = models.TextField(help_text="Lista de benefícios separados por linha")
    composicao = models.TextField(help_text="Composição detalhada do produto")
    contraindicacao = models.TextField(help_text="Contraindicações e precauções")
    modo_uso = models.TextField(help_text="Instruções de uso do produto")
    link_compra = models.URLField(help_text="Link externo para compra do produto")
    destaque = models.BooleanField(default=False, help_text="Marcar para exibir na página inicial")
    lancamento = models.BooleanField(default=False, help_text="Marcar como produto lançamento")
    mais_vendido = models.BooleanField(default=False, help_text="Marcar como produto mais vendido")
    
    def __str__(self):
        return self.nome
    
    def get_beneficios_list(self):
        """Retorna os benefícios como uma lista"""
        return [beneficio.strip() for beneficio in self.beneficios.split('\n') if beneficio.strip()]
    
    def get_composicao_list(self):
        """Retorna a composição como uma lista"""
        return [item.strip() for item in self.composicao.split('\n') if item.strip()]
    
    def get_contraindicacao_list(self):
        """Retorna as contraindicações como uma lista"""
        return [item.strip() for item in self.contraindicacao.split('\n') if item.strip()]
    
    def get_modo_uso_list(self):
        """Retorna o modo de uso como uma lista"""
        return [item.strip() for item in self.modo_uso.split('\n') if item.strip()]
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Depoimento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    video_youtube_id = models.CharField(max_length=20, help_text="Apenas o ID do vídeo do YouTube")
    citacao = models.TextField(help_text="Citação curta do cliente")
    texto_transformacao = models.TextField(help_text="Texto mais longo sobre a transformação")
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Depoimento de {self.nome_cliente}"
    
    def get_youtube_embed_url(self):
        """Retorna a URL de embed do YouTube"""
        return f"https://www.youtube.com/embed/{self.video_youtube_id}"
    
    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Contato de {self.nome} - {self.assunto}"
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['-data_envio']


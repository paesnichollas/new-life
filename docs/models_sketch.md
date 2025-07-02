## Esboço dos Modelos de Dados para New Life Website

### Categoria
- `nome`: CharField (ex: Esportes, Beleza, Bem-estar)
- `slug`: SlugField (para URLs amigáveis)

### Produto
- `categoria`: ForeignKey para Categoria
- `nome`: CharField
- `imagem`: ImageField
- `descricao`: TextField
- `beneficios`: TextField (lista de benefícios)
- `link_compra`: URLField (link externo para compra)

### Depoimento
- `nome_cliente`: CharField
- `video_youtube_id`: CharField (apenas o ID do vídeo do YouTube)
- `citacao`: TextField
- `texto_transformacao`: TextField (texto mais longo sobre a transformação)

### Contato
- `nome`: CharField
- `email`: EmailField
- `assunto`: CharField
- `mensagem`: TextField
- `data_envio`: DateTimeField (auto_now_add=True)



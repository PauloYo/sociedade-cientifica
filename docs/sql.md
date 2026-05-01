# Documentação do Modelo Relacional

Este documento descreve as tabelas do modelo relacional gerado para o minimundo da sociedade científica. O modelo contempla o cadastro de pesquisas, coordenadores, áreas de interesse, publicações bibliográficas, autores, teses, livros, artigos, softwares/tutoriais, endereços e arquivos associados.

![modelo-mysql](../images/model-image.png)

---

## Estrutura de Endereçamento

### Estado

Representa uma unidade federativa (UF).

* idEstado (PK)
* uf

Relacionamento: um estado possui várias cidades.

---

### Cidade

Representa uma cidade.

* idCidade (PK)
* nomCidad
* Estado_idEstado (FK)

Relacionamento: pertence a um estado e possui vários bairros.

---

### Bairro

Representa um bairro.

* idBairro (PK)
* nomBairr
* Cidade_idCidade (FK)

Relacionamento: pertence a uma cidade.

---

### Endereco

Armazena dados completos de endereço.

* idEnder (PK)
* tipoLogradouro
* nomeLogradouro
* numero
* complemento
* cep
* Bairro_idBairro (FK)

Relacionamento: utilizado por coordenadores e softwares.

---

## Entidades principais

### Coordenador

* idCordenador (PK)
* nomeCoordenador
* emailCoordenador
* instituiçãoCoordenador
* Endereco_idEnder (FK)

Relacionamento: um coordenador pode estar associado a várias pesquisas.

---

### AreaInteresse

* idArInt (PK)
* nomeArPes

Relacionamentos:

* associada a pesquisas (1:N)
* associada a publicações (1:N)
* associada a softwares/tutoriais (1:N)

---

### Pesquisa

* idPesquisa (PK)
* nomPesquisa
* descPesquisa
* dataInicio
* dataFimEfetiva
* dataFimPrevista
* Coordenador_idCordenador (FK)
* AreaPesquisa_idArPes (FK)

Relacionamentos:

* pertence a um coordenador
* pertence a uma área de interesse

---

## Publicações Bibliográficas

### Publicacao (Superclasse)

* idPublicacao (PK)
* titulo
* ano
* isbn
* AreaPesquisa_idArPes (FK)

Relacionamentos:

* pertence a uma área de interesse
* possui vários autores (N:N)

---

### Autor

* idAutor (PK)
* nomeAutor

---

### Publicacao_has_Autor (Tabela associativa)

* Publicacao_idPublicacao (FK)
* Autor_idAutor (FK)

PK composta: (Publicacao_idPublicacao, Autor_idAutor)

---

## Especialização de Publicação

A entidade Publicacao é especializada em três tipos:

---

### Tese

* idTese (PK, FK → Publicacao)
* Instituicao_idInst (FK)
* Grau_idGrau (FK)

Relacionamentos:

* pertence a uma instituição
* possui um grau acadêmico

---

### Instituicao

* idInst (PK)
* instituicao

---

### Grau

* idGrau (PK)
* grau

---

### Livro

* idLivro (PK, FK → Publicacao)
* Cidade_idCidade (FK)
* Editora_idEditora (FK)

Relacionamentos:

* possui uma editora
* possui local de publicação (cidade)

---

### Editora

* idEditora (PK)
* nome

---

### Artigo

* idArtigo (PK, FK → Publicacao)
* nomePeriodico
* volume
* numero

Relacionamento:

* representa artigos de revista ou conferência

---

## Softwares e Tutoriais

### SoftwareTutorial

* idSoftTutr (PK)
* nome
* descricao
* responsavel
* equipamento
* url
* Endereco_idEnder (FK)
* Arquivo_idArquivo (FK)
* AreaInteresse_idArInt (FK)

Relacionamentos:

* pertence a uma área de interesse
* possui um endereço de contato
* referencia um arquivo

---

### Arquivo

* idArquivo (PK)
* nome
* caminho

---

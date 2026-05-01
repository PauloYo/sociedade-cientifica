# Documentação do Modelo NoSQL (MongoDB)

Este documento descreve a modelagem NoSQL orientada a documentos para o minimundo da sociedade científica. O modelo foi projetado para o MongoDB, priorizando agregação de dados, redução de junções e eficiência de leitura.

---

## Coleções do modelo

### Pesquisas

Armazena informações completas sobre pesquisas, incluindo coordenador e área.

#### Estrutura

* _id
* nome
* descricao
* datas

  * inicio
  * fim_prevista
  * fim_efetiva
* coordenador

  * nome
  * email
  * instituicao
  * endereco
* area

  * id (opcional)
  * nome

#### Observações

* O coordenador é embutido no documento, pois não há necessidade de reutilização global.
* A área pode ser embutida ou referenciada parcialmente.

---

### Publicacoes

Representa publicações bibliográficas (livros, teses e artigos) em uma única coleção.

#### Estrutura base

* _id
* titulo
* ano
* isbn
* area
* autores (array)
* tipo

#### Especializações

A especialização é controlada pelo campo `tipo`.

---

#### Livro

Campos adicionais:

* livro

  * editora

    * id
    * nome
  * local_publicacao

    * cidade
    * uf

---

#### Tese

Campos adicionais:

* tese

  * grau
  * instituicao

---

#### Artigo

Campos adicionais:

* artigo

  * nome_periodico
  * volume
  * numero

---

#### Observações

* O uso de uma única coleção evita fragmentação e melhora a performance.
* Autores são embutidos como array, evitando necessidade de junções.
* A estrutura permite flexibilidade para diferentes tipos de publicação.

---

### Softwares

Armazena softwares e tutoriais relacionados às áreas de interesse.

#### Estrutura

* _id
* nome
* descricao
* responsavel
* contato

  * endereco
* equipamento
* url
* area
* arquivos (array)

---

### Arquivos (embutido)

Cada software pode conter múltiplos arquivos:

* nome
* caminho
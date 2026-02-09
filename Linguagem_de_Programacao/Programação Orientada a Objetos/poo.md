# Introdução à Programação Orientada a Objetos
## Classes

A estrutura de criação de uma classe é basicamente essa:

```python
class NomeDaClasse:

self.atributo_da_classe = ...

  def __init__(self, p1, p2, ...):
  self.atributo1 = p1
  self.atributo2 = p2
  pass

  def method(self):
  pass


```
# Encapsulamento
## Atributos públicos, protegidos e privados
1. Público:
- Sintaxe: self.atributo
- Acesso: Pode ser acessado e modificado tanto dentro quanto fora da classe.
2. Protegido:
- Sintaxe: self._atributo
- Acesso: Tecnicamente, ainda é público. Porém, por convenção, serve para avisar outros programadores de que é para acessar e alterar apenas dentro da classe e das subclasses.
3. Privado:
- Sintaxe: self.__atributo
- Acesso: O Python "esconde" este atributo alterando o nome dele internamente (um processo chamado Name Mangling). Tentar aceder a obj.__senha diretamente gerará um erro.

## Getters e Setters

- Getters: queremos restringir o acesso aos atributos dos nossos objetos, por isso, usamos @property.
- Setters: Não queremos que qualquer um possa colocar o valor que quiser em nosso atributo, então, utilizamos @atributo.setter para criar uma validação do valor.

```python
class Livro:
    def __init__(self, titulo, autor, genero, estado_inicial):
        # Atributos públicos (sem validação complexa necessária)
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        
        # Atributo com Validação (Usa o Setter abaixo!)
        # Repara: usamos o nome SEM sublinhado para forçar a validação logo ao criar.
        self.estado_conservacao = estado_inicial

    # --- GETTER ---
    @property
    def estado_conservacao(self):
        return self._estado_conservacao

    # --- SETTER (A Regra de Negócio) ---
    @estado_conservacao.setter
    def estado_conservacao(self, novo_estado):
        # Lista de estados permitidos segundo o enunciado
        estados_validos = ["novo", "bom", "gasto"]
        
        if novo_estado.lower() in estados_validos:
            # SUCESSO: Guardamos na variável protegida (com sublinhado)
            self._estado_conservacao = novo_estado.lower()
        else:
            # ERRO: Lançamos um alerta e não mudamos o estado
            raise ValueError(f"Estado inválido! Use apenas: {estados_validos}")

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (Estado: {self.estado_conservacao})"

# --- TESTE DO CÓDIGO ---

# 1. Criar um livro correto
livro1 = Livro("Dom Casmurro", "Machado de Assis", "Romance", "novo")
print(livro1)

# 2. Tentar mudar para um estado inválido
try:
    livro1.estado_conservacao = "rasgado"
except ValueError as e:
    print(f"Erro detetado: {e}")

# 3. O estado original manteve-se protegido
print(f"Estado atual: {livro1.estado_conservacao}")
```

# Relações entre classes
## Associação
Nós dizemos que duas classe estão associadas quando um objeto usa/interage com outro, mas não há um dono. 

```python
class Caneta:
    def __init__(self, marca): self.marca = marca

class Escritor:
    def __init__(self, nome): self.nome = nome
    def escrever(self, ferramenta): print(f"{self.nome} escreve com {ferramenta.marca}")

bic = Caneta("Bic")
joao = Escritor("João")
joao.escrever(bic)  # Escritor usa Caneta
```

## Agregação
Na agregação, uma classe precisa da outra, mas as duas podem existir independentemente. Um onjeto funciona como parte de outro, mas não é criado por ele. Nós temos uma relação de agregação quando uma classe faz referência/possui um objeto de outra classe em seu código. Por exemplo, um guerreiro que possui um método que ataca com outro objeto da classe arma caso ele tenha esse objeto, ou uma classe que possui um objeto de outra classe em um de seus atributos.

```python

class Guerreiro:
  """Essa classe representa um guerreiro
  
  Atributes
  ---------
    nome (str): Nome do guerreiro.
    experiencia (bool): Pontos de experiência que o guerreiro adquiriu.
    arma (Arma): Arma que o guerreiro possui.
  
  Methods
  -------
    equipar_arma(arma): Equipa uma arma em nosso guerreiro.
    atacar(): Ataca com sua arma. Caso o guerreiro não tenho uma arma equipada, ataca com as mãos."""

  def __init__(self, nome):
    self.nome = nome
    self.experiencia = 0.0
    self.arma = None

  def equipar_arma(self, arma: Arma) -> None:
    self.arma = arma

  def atacar(self) -> None:
    if self.arma:
      print(f"{self.nome} atacou com sua arma {self.arma.nome} e causou {self.arma.dano} de dano.")
    else:
      print(f"{self.nome} atacou com os punhos e causou 1 de dano.")

class Arma:
  def __init__(self, nome, dano):
    self.nome = nome
    self.dano = dano
```

## Composição
Nós temos uma relação de coposição quando um objeto de outra classe é criado no momento em que criamos o objeto de uma outra classe. Qunado a existência de um objeto depende da existência do outro.

```python

class Carro:
  def __init__(self, marca, modelo, ano, potencia):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.motor = Motor(potencia)

class Motor:
def __init__(self, potencia):
  self.potencia = potencia
```

Se nós apagarmos um objeto da classe carro, seu motor também é apagado.

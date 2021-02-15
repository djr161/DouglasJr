import time
import sys

class Cliente:
  def __init__(self):
    self.nome=input("Insira seu nome completo: ")
    while True:
      try: 
        self.telefone=input("\nInsira um telefone de contato: ")
        if len(self.telefone)!=9:
          raise ValueError
        break
      except ValueError:
        print("Operação inválida")
        continue
    self.email=input("\nInsira seu endereço de e-mail: ")
    self.senha=input("\nEscolha uma senha: ")
    self.endereco= Endereco()

  def exibirInformacao(self):
    print("\nSeja bem vindo,", self.nome)
    time.sleep(1.5)
    print("\nSeu telefone é:", self.telefone)
    time.sleep(1.5)
    print("\nSeu e-mail é: "+ self.email)
    time.sleep(1.5)
    print("\nSeu endereço é: ")
    print("Rua:",self.endereco.rua) 
    print("Bairro:",self.endereco.bairro) 
    print("Número:",self.endereco.numero)
    print("Complemento:",self.endereco.complemento)
    time.sleep(1.5)

    pergunta=int(input("\nVocê deseja realizar seu pedido agora? Digite 1 para Sim e 2 para Não: "))

    if pergunta==1:
      time.sleep(0.5)
      print("\nDirecionando para o cardápio...\n")
      time.sleep(2.5)
    elif pergunta==2:
      time.sleep(0.5)
      print("Já vai? :(")
      sys.exit()

class Endereco: 
  
  def __init__(self):
    self.rua= None
    self.bairro= None
    self.numero= None
    self.complemento= None
    self.cadastrarEndereco()
    
  def cadastrarEndereco(self):
    self.rua= input("\nDigite sua rua: ")
    self.bairro= input("\nDigite seu bairro: ")
    while True:
      try:
        self.numero= input("\nDigite o número da sua residência: ")
        if len(self.numero)>=4:
          raise ValueError
        break
      except ValueError:
        print("Número de residência incorreto")
        continue
    self.complemento= input("\nDigite o complemento: ")
    self.alterarEndereco()

  def alterarEndereco(self):
    alteracao=int(input("\nDeseja alterar seu endereço? Digite 1 para sim e 2 para não: "))
      
    if alteracao==1:
      self.cadastrarEndereco()
    elif alteracao==2:
      print("\nSeu endereço será mantido.")
    else:
      print("\nValor inválido.")
      self.alterarEndereco()
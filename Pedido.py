import time
import sys
from Pagamento import*

class Pedido:
  def __init__(self,nome,preco):
    self.nome=nome
    self.preco=preco
    #variavel auxiliar sabor
    self.psabor=0
    #itens do Pedido
    self.pizza=None
    self.bebida=None  

  def escolherPizza(self):
    print("\033[1;37m")
    self.psabor=int(input("Escolha o sabor da pizza. Digite 1 para Calabresa, digite 2 para 4 queijos, digite 3 para Brigadeiro, digite 4 para Banana com canela: \033[1;31m"))
    
    if self.psabor == 1:
      self.pizza=Pizza("P","Calabresa",30.00)
      print("\033[1;96m")
      print("Pizza selecionada:",self.pizza.nome )
      self.escolherTamanho()
    elif self.psabor == 2:
      self.pizza=Pizza("P","4 queijos",30.00)
      print("\033[1;96m")
      print("Pizza selecionada: ", self.pizza.nome)
      self.escolherTamanho()
    elif self.psabor== 3:
      self.pizza=Pizza("P","Brigadeiro",30.00)
      print("\033[1;96m")
      print("Pizza selecionada: ", self.pizza.nome)
      self.escolherTamanho()
    elif self.psabor== 4:
      self.pizza=Pizza("P","Banana com canela",30.00)
      print("\033[1;96m")
      print("Pizza selecionada: ", self.pizza.nome)
      self.escolherTamanho()
    else:
      print("\nValor inválido.")
      self.escolherPizza()
  
  def escolherTamanho(self):

    print("\033[1;37m")    
    ptam=int(input("Escolha o tamanho da pizza. Digite 1 para P, 2 para M e 3 para G: \033[1;31m"))

    if ptam == 1:
      self.pizza.tamanho="P"
      self.pizza.preco=30.0
      print("\033[1;96m")
      print("Tamanho selecionado: ",self.pizza.tamanho)
      self.escolherBebida()
    elif ptam == 2:
      self.pizza.tamanho="M"
      self.pizza.preco=35.0
      print("\033[1;96m")
      print("Tamanho selecionado: ",self.pizza.tamanho)
      self.escolherBebida()
    elif ptam == 3:
      self.pizza.tamanho="G"
      self.pizza.preco=40.0
      print("\033[1;96m")
      print("Tamanho selecionado: ",self.pizza.tamanho)
      self.escolherBebida()
    else: 
      print("\nValor inválido.")
      self.escolherTamanho()  
    
  def escolherBebida(self):
    print("\033[1;37m")  
    pbebida=int(input("Você deseja escolher bebida? Digite 1 para Sim e 2 para Não: \033[1;31m"))

    if pbebida == 1:
      print("\033[1;37m")
      pbeb1=int(input("Escolha um tipo de bebida. Digite 1 para Suco e 2 para Refrigerante: \033[1;31m"))

      if pbeb1 == 1:
        print("\033[1;37m")  
        suco1=int(input("Escolha o sabor do suco. Digite 1 para Tampico de Laranja e 2 para Del Valle Uva. \033[1;31m"))
        if suco1 == 1:
          self.bebida=Suco("Laranja","Suco","1,5L","Tampico",7.0)
          print("\033[1;96m")
          print("Bebida selecionada: ",self.bebida.nome,self.bebida.fruta)
          '''self.resumirPedido()'''
          self.pagamento=Pagamento(5.0)
          self.pagamento.confPedidoCompleto(self)
          self.pagamento.calcularValorC(self)

        elif suco1 == 2:
          self.bebida=Suco("Uva","Suco","1,5L","Del Valle",7.0)
          print("\033[1;96m")
          print("Bebida selecionada: ",self.bebida.nome,self.bebida.fruta)
          self.pagamento=Pagamento(5.0)
          self.pagamento.confPedidoCompleto(self)
          self.pagamento.calcularValorC(self)
        else:
          print("\nValor inválido.")
          self.escolherBebida()

      elif pbeb1==2:
        print("[1;37m")  
        refri1=int(input("Escolha o sabor e o conteúdo do refrigerante. Digite 1 para Fanta Uva Lata,2 para Fanta Uva 1,5L, 3 para Coca-Cola Classic Lata e 4 para Coca-Cola Classic 1,5L: "))
        if refri1==1:
          self.bebida=Refrigerante("Fanta Uva","Refrigerante","Lata","Coca-Cola",4.0)
          print("\033[1;96m")
          print("Bebida selecionada: ",self.bebida.nome,self.bebida.sabor,self.bebida.conteudo)
          self.pagamento=Pagamento(5.0)
          self.pagamento.confPedidoCompleto(self)
          self.pagamento.calcularValorC(self)
        elif refri1==2:
          self.bebida=Refrigerante("Fanta Uva","Refrigerante","1,5L","Coca-Cola",7.0)
          print("\033[1;96m")
          print("Bebida selecionada: ",self.bebida.nome,self.bebida.sabor,self.bebida.conteudo)
          self.pagamento=Pagamento(5.0)
          self.pagamento.confPedidoCompleto(self)
          self.pagamento.calcularValorC(self)
        elif refri1==3:
          self.bebida=Refrigerante("Coca-Cola Classic","Refrigerante","Lata","Coca-Cola",4.0)
          print("\033[1;96m")
          print("Bebida selecionada: ",self.bebida.nome,self.bebida.sabor,self.bebida.conteudo)
          self.pagamento=Pagamento(5.0)
          self.pagamento.confPedidoCompleto(self)
          self.pagamento.calcularValorC(self)
        elif refri1==4:
          self.bebida=Refrigerante("Coca-Cola Classic","Refrigerante","1,5L","Coca-Cola",7.0)
          print("\033[1;96m")
          print("Bebida selecionada: ",self.bebida.nome,self.bebida.sabor,self.bebida.conteudo)
          self.pagamento=Pagamento(5.0)
          self.pagamento.confPedidoCompleto(self)
          self.pagamento.calcularValorC(self)
      else:
        print("Valor inválido.")
        self.escolherBebida()
    elif pbebida==2:
      self.pagamento=Pagamento(5.0)
      self.pagamento.confPedidoIn(self)
      self.pagamento.calcularValorI(self)
    else:  
      print("Valor inválido.")
      self.escolherBebida()  

class Pizza(Pedido):
  def __init__(self,tamanho,nome,preco):
    self.tamanho=tamanho
    super().__init__(nome,preco)
  
  def mostrarPizza(self):
    print(" "*20+"\033[1;31m C A R D Á P I O")
    print("	\033[1;93m")
    print("╔"+"═"*50+"╗")
    print("║"+" "*23+"Pizzas"," "*19,"║")
    print("║"," "*48,"║")
    print("║"+" "*20+ pizzaP.tamanho," "*3,pizzaM.tamanho," "*3,pizzaG.tamanho," "*15,"║")
    print("║"," "*18,pizzaP.preco,pizzaM.preco,pizzaG.preco," "*14,"║")
    print("║"," "*48,"║")
    print("║"," "*20,calabresaP.nome," "*17,"║")
    print("║"," "*20,queijoP.nome," "*17,"║")
    print("║"," "*20,brigadeiroP.nome," "*16,"║")
    print("║"," "*17,bananaP.nome," "*12,"║")

    cocaP.mostrarBebida()
    

class Bebida(Pedido):
  def __init__(self,tipo,conteudo,nome,preco):
    self.tipo=tipo
    self.conteudo=conteudo
    super().__init__(nome,preco)

  def mostrarBebida(self):
    print("║"," "*48,"║")
    print("║"+" "*23+ "Bebidas"," "*18,"║")
    print("║"," "*48,"║")
    print("║"+" "*20+ cocaP.conteudo," "*3,cocaG.conteudo," "*15,"║")
    print("║"+" "*20, cocaP.preco," "*3,cocaG.preco," "*16,"║")
    print("║"," "*48,"║")
    print("║"," "*20,saborFUP.sabor," "*17,"║")
    print("║"," "*16,saborCCP.sabor," "*13,"║")
    print("║"," "*18,sucoDU.nome,sucoDU.fruta," "*15,"║")
    print("║"," "*17,sucoTL.nome,sucoTL.fruta," "*14,"║")
    print("║"," "*48,"║")
    print("╚"+"═"*50+"╝")

    cocaP.escolherPizza()

class Refrigerante(Bebida):
  def __init__(self,sabor,tipo,conteudo,nome,preco):
    self.sabor=sabor
    super().__init__(tipo,conteudo,nome,preco)

class Suco(Bebida):
   def __init__(self,fruta,tipo,conteudo,nome,preco):
    self.fruta=fruta
    super().__init__(tipo,conteudo,nome,preco)
    


calabresaP=Pedido("Calabresa",30.00)
queijoP=Pedido("4 queijos",30.00)#objeto do tipo pedido

calabresaM=Pedido("Calabresa",35.0) 
queijoM=Pedido("4 queijos",35.0)

calabresaG=Pedido("Calabresa",40.0)
queijoG=Pedido("4 queijos",40.0)

#pizzas doces Pedido

brigadeiroP= Pedido ("Brigadeiro",30.0)
bananaP= Pedido("Banana com canela",30.0)

brigadeiroM= Pedido("Brigadeiro",35.0)
bananaM= Pedido("Banana com canela",35.0)

brigadeiroG= Pedido ("Brigadeiro",40.0)
bananaG= Pedido("Banana com canela",40.0)

#definindo  o tamanho
pizzaP=Pizza("P","Calabresa",30.0)
pizzaM=Pizza("M","Calabresa",35.0)
pizzaG=Pizza("G","Calabresa",40.0)

#bebidas tipo

cocaP=Bebida("Refrigerante","Lata","Coca-Cola",4.0)
cocaG=Bebida("Refrigerante","1,5L","Coca-Cola",7.0)

saborFUP=Refrigerante("Fanta Uva","Refrigerante","Lata","Coca-Cola",4.0)
saborFUG=Refrigerante("Fanta Uva","Refrigerante","1,5L","Coca-Cola",7.0)
saborCCP=Refrigerante("Coca-Cola Classic","Refrigerante","Lata","Coca-Cola",4.0)
saborCCG=Refrigerante("Coca-Cola Classic","Refrigerante","1,5L","Coca-Cola",7.0)

sucoD=Bebida("Suco","1,5L","Del Valle",7.0)
sucoT=Bebida("Suco","1,5L","Tampico",7.0)

sucoDU=Suco("Uva","Suco","1,5L","Del Valle",7.0)
sucoTL=Suco("Laranja","Suco","1,5L","Tampico",7.0)
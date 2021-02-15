from Pedido import *

class Pagamento:

  def __init__(self, taxaEntrega):
    self.pedidoAtual= None
    self.total= None
    self.taxaEntrega=taxaEntrega
    self.formaPgto= None
  
  def definirPedidoAtual(self,pedido):   
    self.pedidoAtual=pedido

  def confPedidoCompleto(self,pedidoAserConferido):
    self.pedidoAtual=pedidoAserConferido
    print("\nSeu pedido foi: ")
    time.sleep (1)
    print(self.pedidoAtual.pizza.nome, self.pedidoAtual.pizza.tamanho)
    print(self.pedidoAtual.bebida.nome,self.pedidoAtual.bebida.conteudo)
    time.sleep (1)
    return self.pedidoAtual

  def confPedidoIn(self,pedidoAserConferido):
    self.pedidoAtual=pedidoAserConferido
    print("\033[1;96m")
    print("Nenhuma bebida selecionada.")
    print("\033[1;97m")
    print("\nSeu pedido foi:")
    time.sleep (1)
    print(self.pedidoAtual.pizza.nome,self.pedidoAtual.pizza.tamanho)
    time.sleep (1)

  def calcularValorC(self,valorAserConferido):
    self.total= valorAserConferido
    print("\nValor da pizza:",self.pedidoAtual.pizza.preco)
    print("\nValor da bebida:",self.pedidoAtual.bebida.preco)
    print("\nTaxa de entrega:",self.taxaEntrega)
    print("\nTotal a pagar: R$",self.pedidoAtual.pizza.preco+self.pedidoAtual.bebida.preco+self.taxaEntrega)
    self.escolherFormaPgto()
     
  def calcularValorI(self,valorAserConferido):
    self.total= valorAserConferido
    print("\nValor da pizza:",self.pedidoAtual.pizza.preco)
    print("\nTaxa de entrega:",self.taxaEntrega)
    print("\nTotal a pagar: R$",self.pedidoAtual.pizza.preco+self.taxaEntrega)

    self.escolherFormaPgto()

  def escolherFormaPgto(self):
    escolha=int(input("\nEscolha a forma de pagamento. Digite 1 para dinheiro e 2 para cartão. "))

    if escolha == 1:
      print("\nVocê escolheu pagamento no dinheiro. ")
    elif escolha== 2:
      print("\nVocê escolheu pagamento no cartão.")
    else:
      print("\nValor inválido.")
      self.escolherFormaPgto()

  

taxa=Pagamento(5.0)

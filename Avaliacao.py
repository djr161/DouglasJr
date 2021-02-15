import sys
class Avaliacao:
  def __init__(self):
    self.estrela=0
    self.avaliarPedido()

  def avaliarPedido(self):
    self.estrela=int(input("\nVocê deseja avaliar o serviço? Digite 1 para sim ou 2 para não: "))
    if self.estrela==1:
      numEstrelas=int(input("\nQuantas estrelas você daria ao serviço? Digite de 1 até 5: "))
      if numEstrelas==1:
        print("\n★")
        print("\nA PIZZARIA MUCHA LOKA! agradece sua avaliação! Faremos o possível para melhorar!")
      elif numEstrelas==2:
        print("\n★ ★")
        print("\nA PIZZARIA MUCHA LOKA! agradece sua avaliação! Faremos o possível para melhorar!")
      elif numEstrelas==3:
        print("\n★ ★ ★")
        print("\nA PIZZARIA MUCHA LOKA! agradece sua avaliação!")
      elif numEstrelas==4:
        print("\n★ ★ ★ ★")
        print("\nA PIZZARIA MUCHA LOKA! agradece sua avaliação!")
      elif numEstrelas==5:
        print("\n★ ★ ★ ★ ★")
        print("\nA PIZZARIA MUCHA LOKA!agradece sua avaliação!")
      else:
        print("\nValor inválido.")
        self.avaliarPedido()
    elif self.estrela==2:
      print("\nA PIZZARIA MUCHA LOKA! agredece pela sua preferência!")
      sys.exit()
    else:
      print("\nValor inválido.")
      self.avaliarPedido()
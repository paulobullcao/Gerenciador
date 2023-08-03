from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

#Criando a primeira classe para exibição do sistema 
class primeirajanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Gerenciador de Chamados') # Definindo o Título da aplicação. 
        '''
        botao = QPushButton("CLIQUE AQUI!") # Definindo o botão
        self.setFixedSize(QSize(400, 300)) # Definindo o tamanho e largura da janela

        self.setCentralWidget(botao) # Centralizando o botão

        botao.clicked.connect(self.click_botao) #fazendo a conexão do botão com o método de click. 

    def click_botao(botao):
        print(f"Botão Clicado!")

'''
        widget = QLabel(" Segundo aprendizado - textos") # Atribuindo um Texto
        font = widget.font() # Adicionando a propriedade. 
        font.setPointSize(20) # Informando o tamanho do texto
        widget.setFont(font) #atribuindo o tamanho ao widget criado. 

        self.setFixedSize(QSize(400, 300)) # Definindo o tamanho e largura da janela
        widget.setAlignment(Qt.AlignCenter | Qt.AlignCenter) # definindo o alinhamento 
        self.setCentralWidget(widget) # Alinhando o texto a tela. 
            



app = QApplication(sys.argv)

Window = primeirajanela()

Window.show() # Exibindo a janela. 
app.exec_() # Executando o aplicativo. 

"""
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os Widgets do PySide6

QWidget e QLayout de PySide6.QtWidgets
QWidget -> genérico
QLayout -> Um widget de layout que recebe outros widgets
"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout


app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red;')
# botao.show() # Adiciona o Widget na hierarquia e exibe a janela


botao2 = QPushButton('botão 2')
botao2.setStyleSheet('font-size: 40px; color: red;')
# botao2.show()



botao3 = QPushButton('botão 2')
botao3.setStyleSheet('font-size: 40px; color: red;')
# botao2.show()

central_widget = QWidget()

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout( )
central_widget.setLayout(layout)
 
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show() # Central widget entre na hierarquia e mostre sua janela
app.exec() # Inicia o loop da aplicação


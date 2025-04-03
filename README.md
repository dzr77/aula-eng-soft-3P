Pong - Jogo Clássico em Python
Este é o clássico jogo Pong, desenvolvido em Python utilizando a biblioteca pygame. O objetivo do jogo é controlar uma raquete e evitar que a bola passe, tentando marcar pontos ao fazer com que a bola ultrapasse a raquete do oponente.

Requisitos
Python 3.x

Pygame (biblioteca)

Instalação
1. Instalar o Python
Se você ainda não possui o Python instalado, baixe e instale a versão mais recente do Python a partir do site oficial: https://www.python.org/.

2. Instalar o Pygame
Depois de instalar o Python, abra o terminal ou prompt de comando e execute o seguinte comando para instalar a biblioteca pygame:

bash
Copiar
pip install pygame
Como Jogar
Controle do Jogador 1 (Esquerda):

W: Mover a raquete para cima

S: Mover a raquete para baixo

Controle do Jogador 2 (Direita):

Seta para cima: Mover a raquete para cima

Seta para baixo: Mover a raquete para baixo

Objetivo: O objetivo é evitar que a bola passe pela sua raquete e tentar fazer a bola ultrapassar a raquete do adversário, marcando pontos.

Pontuação: Quando um jogador marca um ponto, o jogo reinicia com a bola no centro da tela e o placar é atualizado. O jogo não possui um limite de pontos, mas o jogador pode observar a pontuação dos dois jogadores na parte superior da tela.

Como Rodar o Jogo
Baixe ou clone este repositório em seu computador.

Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo jogo-pong.py está localizado.

Execute o jogo com o comando:

bash
Copiar
python jogo-pong.py
Arquivo de Pontuação
Ao final de cada partida, a pontuação será salva em um arquivo chamado scores.txt. O formato da pontuação será o seguinte:

yaml
Copiar
Player 1: X - Player 2: Y
Onde X e Y representam a pontuação de cada jogador.

Exemplo de Pontuação no Arquivo scores.txt
yaml
Copiar
Player 1: 5 - Player 2: 3
Player 1: 2 - Player 2: 4
Player 1: 10 - Player 2: 7
Personalização
Você pode alterar o tamanho da tela do jogo ajustando os valores das variáveis WIDTH e HEIGHT.

Também é possível ajustar as velocidades da bola e das raquetes, alterando os valores de ball_speed_x e ball_speed_y, e a movimentação das raquetes ajustando o valor no comando player1_y += 10 e player2_y += 10.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

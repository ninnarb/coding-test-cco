print('''
      
      Seja bem-vindo ao jogo de perguntas e respostas
      
     Você responderá 5 perguntas, e assim saberá o quanto
    entende do assunto.''')

print('''
      Vamos começar!    
      ''')
print('1) Qual é a unidade básica de armazenamento de dados em um computador?')

print('''
      a) bit
      ''')

print('''
      b) pen drive
      ''')

print('''
      c) hd externo
      ''')


resposta = input('Digite uma das opções:')
pontos = 0 

if resposta == 'a':
    print('  Você acertou!')
    pontos += pontos + 15
    print('''
            Agora você possui 15 pontos!
          ''')

if resposta == 'b':
    print('Você errou. :(')
    pontos == pontos - 0 
            
    print('Você possui 0 pontos.')

if resposta == 'c':
    print('Você errou, poxa!')
    pontos == pontos - 0

    print('Você possui 0 pontos.')

print('''
      
      Okay! Vamos para a próxima!
      
      ''')

print('2) O que significa a sigla "HTML" em termos de desenvolvimento web?')

print('''
      a) é para a criação de aplicativos
      ''')

print('''
      b) análise de dados
      ''')

print('''
      c) criação de uma página na web
      ''')

resposta = input('Digite uma das opções:')

if resposta == 'a':
    print('Você errou!')
    pontos == pontos - 0
    print('Você ganho 0 pontos!')

if resposta == 'b':
    print('Você errou!')
    pontos == pontos - 0
    print('Você não ganhou nenhum ponto')

if resposta == 'c':
    print('Você acertou!')
    pontos += + 15
    print('Parabéns! Você ganhou mais 15 pontos!')

    print('''
          Próxima! Estamos quase no fim!
          ''')
    
print('3) Qual é a linguagem de programação mais amplamente usada para o desenvolvimento de aplicativos móveis?')

print('''
      a) bublle
      ''')

print('''
      b) java
      ''')

print('''
      c) korntype
      ''')

resposta = input('Digite uma das opções:')

if resposta == 'a':
    print('Você errou!')
    pontos == pontos - 0
    print('Você não ganhou nenhum ponto!')

if resposta == 'b':
    print('Você acertou!')
    pontos += pontos + 15
    print('Você ganhou mais 15 pontos!')

if resposta == 'c':
    print('Você errou.')
    pontos == pontos - 0
    print('Você não ganhou nenhum ponto')
    
    
    print('''
          Próxima! Estamos quase no fim!
          ''')
    
    print('4)Qual é o principal objetivo da linguagem de programação Python?')

    print('a) Desenvolvimento de aplicativos móveis')
    print('b) Análise de dados e automação de tarefas')
    print('c) Criação de páginas web dinâmicas')

    resposta = input('Digite uma das opções:')

if resposta == 'a':
    print('Que pena! Você errou.')
    pontos == pontos - 0
    print('Você não ganhou nenhum ponto')

if resposta == 'b':
    print('Parabéns! Você acertou')
    pontos += pontos + 15
    print('Você ganhou mais 15 pontos!')

if resposta == 'c':
    print('Que pena, você errou.')
    pontos == - 0
    print('Você não ganhou nenhum ponto.')

    print('Vamos para a última pergunta!')
    print('''
              Valendo 50 pontos!!
          ''')
    
    print('5) O que significa a sigla "URL" na internet?')

    print('a) Universal Resource Locator')
    print('b) Uniform Resource Language')
    print('c) Universal Repository Link')

if resposta == 'a':
    print('Você acertou!!')
    pontos += 50
    print('Você ganhou os 50 pontos! Parabéns!')

if resposta == 'b':
    print('Que pena, você errou')
    pontos == - 0
    print('Você não ganhou nenhum ponto')

if resposta == 'c':
    print('Que pena, você errou')
    pontos == - 0
    print('Você não ganhou os 50 pontos')

    print('Sua pontuação final foi', pontos)
    
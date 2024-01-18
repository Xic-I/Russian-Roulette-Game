# Criado por: Xic_I
# GitHub: https://github.com/Xic-I
# Jogo feito em base de: Buckshot Roulette

import random
import os
import time
import sys

# Função para iniciar o jogo.
def Jogo():
    # Variaveis do jogo.
    global VidaDoAdversário
    VidaDoAdversário = 100
    global VidaDoJogador
    VidaDoJogador = 100
    Balas = 1
    global BalaRevolver
    BalaRevolver = random.randint(1,6)
    QuantidadeDeDecisoes = 0 # Verifica a quantidade de decisões do jogador
    QuantidadeDeCompras = 0 # Verifica a quantidade de compras do jogador
    Polvora = 0
    KitMedico = 0
    ColeteBalistico = 0
    global CamaraDaMunição
    CamaraDaMunição = 1
    Luvas = 0
    Moedas = 100
    Armas = [
        "Revolver",
        "Espingarda",
        "Rifle"
    ]
    ArmaSelecionada = random.choice(Armas)
    Itens = [
        "Pólvora",
        "Kit Médico",
        "Colete Balístico",
        "Luvas"
    ]
    global DanoDasArmas
    DanoDasArmas = [
        28,
        38,
        50
    ]
    # Inicio do jogo.
    LimparTela()
    print('O jogo começou!\n')
    print('Tem',Balas,'Bala(s) na arma. O Jogador começa.')
    while True:
        print('Turno de: ',NomeJogador)
        print('Sua Vida: ', VidaDoJogador)
        print('Vida do Adversário: ', VidaDoAdversário)
        print('Moedas: '+str(Moedas))
        print('O que você decide fazer?\n')
        decisao = int(input('( 1 ) Atirar em mim\n( 2 ) Atirar no oponente\n( 3 ) Itens\n( 4 ) Loja\nVocê> '))
        match decisao:
            case 1:
                if BalaRevolver == CamaraDaMunição: # a câmara da munição.
                    print('Você recebeu '+str(DanoDasArmas[0])+' de dano.')
                    VidaDoJogador-=DanoDasArmas[0]
                    time.sleep(2)
                    BalaRevolver = random.randint(1,6) # Munição sendo colocada em outra câmara.
                    CamaraDaMunição+=1 # Tambor sendo girado
                    time.sleep(1)
                    LimparTela()
                    Bot()
                else:
                    print('Nada aconteceu.', NomeJogador,'Joga novamente.')
                    CamaraDaMunição+=1
                    time.sleep(1)
 
                        
            case 2:
                if BalaRevolver == CamaraDaMunição:
                    print('O oponente recebeu '+str(DanoDasArmas[0])+' de dano.')
                    VidaDoAdversário-=DanoDasArmas[0]
                    time.sleep(2)
                    BalaRevolver = random.randint(1,6)
                    CamaraDaMunição+=1
                    print('Arma recarregada.')
                    print(NomeJogador,'Joga novamente.')
                    time.sleep(1)
                else:
                    print('Nada aconteceu. Turno de', NomeAdversario)
                    CamaraDaMunição+=1
                    time.sleep(1)
                    LimparTela()
                    Bot()
            case 3:
                while True:
                    UsarItem = int(input('\n( 1 )'+Itens[0]+':'+str(Polvora)+'\n( 2 )'+Itens[1]+':'+str(KitMedico)+'\n( 3 )'+Itens[2]+':'+str(ColeteBalistico)+'\n( 4 )'+Itens[3]+':'+str(Luvas)+'\n( 5 ) Voltar\nUsar> '))
                    match UsarItem:
                        case 1:
                            if Polvora == 0:
                                print('Você não tem', Itens[0])
                                time.sleep(2)
                            else:
                                print('Você usou', Itens[0])
                                time.sleep(2)
                                Polvora-=1
                                DanoDasArmas[0]+=20
                        case 2:
                            if KitMedico == 0:
                                print('Você não tem', Itens[1])
                                time.sleep(2)
                            else:
                                print('Você usou', Itens[1])
                                time.sleep(2)
                                KitMedico-=1
                                VidaDoJogador+=40
                                if VidaDoJogador > 100:
                                    while True:
                                        VidaDoJogador-=1
                                        if VidaDoJogador == 100:
                                            break
                        case 3:
                            if ColeteBalistico == 0:
                                print('Você não tem', Itens[2])
                                time.sleep(2)
                            else:
                                print('Você usou', Itens[2])
                                time.sleep(2)
                                ColeteBalistico-=1
                                DanoDasArmas[0]-=11
                        case 4:
                            if Luvas == 0:
                                print('Você não tem', Itens[3])
                                time.sleep(2)
                            else:
                                print('Você usou', Itens[3])
                                time.sleep(2)
                                Luvas-=1
                                if CamaraDaMunição == BalaRevolver:
                                    print('Há uma munição na câmara que irá ser disparada.')
                                    time.sleep(2)
                                else:
                                    print('Não há munição na câmara que irá ser disparada.')
                                    time.sleep(2)
                        case 5:
                            break
                QuantidadeDeDecisoes+=1
            case 4:
                while True:
                    print('\nProdutos:\n( 1 ) Pólvora: 100 Moedas\n<Aumenta dano da arma>\n( 2 ) Kit Médico: 100 Moedas\n<Cura personagem>\n( 3 ) Colete Balístico: 100 Moedas\n<Reduz o dano recebido pela arma>\n( 4 ) Luvas: 100 Moedas\n<Permite o jogador ver se há munições na arma>\n( 5 ) Voltar\nVocê tem '+str(Moedas),'moedas')
                    escolha_produto = int(input('Comprar> '))
                    match escolha_produto:
                        case 1:
                            if Moedas < 100:
                                print('Você não tem moedas o suficiente.')
                            else:
                                print('Você comprou um(a)', Itens[0])
                                Polvora+=1
                                QuantidadeDeCompras+=1
                                Moedas-=100
                                time.sleep(2)
                        case 2:
                            if Moedas < 100:
                                print('Você não tem moedas o suficiente.')
                            else:
                                print('Você comprou um(a)', Itens[1])
                                KitMedico+=1
                                QuantidadeDeCompras+=1
                                Moedas-=100
                                time.sleep(2)
                        case 3:
                            if Moedas < 100:
                                print('Você não tem moedas o suficiente.')
                            else:
                                print('Você comprou um(a)', Itens[2])
                                ColeteBalistico+=1
                                QuantidadeDeCompras+=1
                                Moedas-=100
                                time.sleep(2)
                        case 4:
                            if Moedas < 100:
                                print('Você não tem moedas o suficiente.')
                            else:
                                print('Você comprou um(a)', Itens[3])
                                Luvas+=1
                                QuantidadeDeCompras+=1
                                Moedas-=100
                                time.sleep(2)
                        case 5:
                            break
                QuantidadeDeDecisoes+=1
        if QuantidadeDeDecisoes == 3:
            print('Quantidade de decisões excedidas. Turno de', NomeAdversario)
            time.sleep(2)
            Bot()
        if QuantidadeDeCompras == 2:
            print('Você não pode mais comprar nada. Turno de', NomeAdversario)
            time.sleep(2)
            Bot()
        if CamaraDaMunição > 6:
            while True:
                CamaraDaMunição-=1
                if CamaraDaMunição == 1:
                    break
        if VidaDoJogador <= 0:
            print('Você perdeu.')
            time.sleep(2)
            JogarNovamente = int(input('( 1 ) Sim\n( 0 ) Não\n> '))
            if JogarNovamente == 1:
                Jogo()
            else:
                Menu()
        if VidaDoAdversário <= 0:
            print('Parabéns, você venceu!')
            VidaDoAdversário = 100
            VidaDoJogador = 100
            Moedas+=50

# Atividade do Bot
def Bot():
    global CamaraDaMunição
    global VidaDoAdversário
    global VidaDoJogador
    time.sleep(3)
    Atirar = random.randint(1,6)
    if Atirar in (2,4,6):
        print(NomeAdversario,'Decidiu atirar em si mesmo.')
        time.sleep(2)
        if BalaRevolver == CamaraDaMunição:
            print(NomeAdversario,'Recebeu '+str(DanoDasArmas[0]),'de dano.')
            VidaDoAdversário-=DanoDasArmas[0]
            CamaraDaMunição+=1
            time.sleep(1)
            LimparTela()
        else:
            print('Nada aconteceu.')
            CamaraDaMunição+=1
            time.sleep(1)
            LimparTela()
            Bot()

    if Atirar in (1,3,5):
        print(NomeAdversario,'Decidiu atirar em você.')
        time.sleep(2)
        if BalaRevolver == CamaraDaMunição:
            print('Você recebeu '+str(DanoDasArmas[0]),'de dano.')
            VidaDoJogador-=DanoDasArmas[0]
            CamaraDaMunição+=1
            time.sleep(1)
            LimparTela()
            Bot()
        else:
            print('Nada aconteceu.')
            time.sleep(1)
            LimparTela()

# Apenas limpando sua tela mano, tem uma moedinha aí?
def LimparTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Função Menu, criada para retornar ao menu.
def Menu():
    LimparTela()
    print('Desenvolvido por: Xic_I\nGitHub: https://github.com/Xic-I\nRussian Roulette Game (Beta Version 1.0)\n')
    print('( 1 ) Jogo\n( 2 ) Regras\n( 3 ) Roleta Binária\n( 4 ) Sair')
    while True:
        escolha = int(input('> '))
        match escolha:
            case 1:
                global NomeJogador
                NomeJogador = input('Digite seu nome (Caso não queira dar um nome, deixe vazio): ')
                global NomeAdversario
                NomeAdversario = input('Digite o nome para o bot (Caso não queira dar um nome, deixe vazio): ')
                if NomeAdversario == '':
                    NomeAdversario = 'Bot'
                if NomeJogador == '':
                    NomeJogador = 'Otário'
                Jogo()
            case 2:
                print('Regra 1: Você pode fazer uma ação somente após digitar o número correspondente daquela ação.')
                print('Regra 2: Você só pode fazer três ações.')
                print('Regra 3: A cada vitória você ganha 50 moedas.')
                print('Regra 4: Você sempre começará o jogo com 100 moedas, juntamente de seu adversário. (Sistema inativo nesta versão.)')
                print('Regra 5: A cada 3 vitórias, uma bala será adicionada a arma. (Sistema inexistente nesta versão.)')
                print('Regra 6: Caso você atire em si mesmo pórem a arma não atire, você joga novamente, caso o contrário, será a vez do bot.')
                print('Regra 8: ')
                print('Regra 7: Se você decidir atirar no seu adversário e a arma não atirar, você perderá sua chance de fazer uma segunda ação.')
            case 3:
                print('Modo ainda não criado.')
            case 4:
                sys.exit()
            case _:
                print('Escolha inexistente.')
Menu()
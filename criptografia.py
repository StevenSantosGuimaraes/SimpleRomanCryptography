from cryptography.fernet import Fernet
import os


def limparTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exportarTextoChave(txt):
    with open("./arquivos/chave.txt", "wb") as arquivo:
        arquivo.write(txt)
        arquivo.close()

def exportarTextoMensagem(string):
    with open('./arquivos/mensagem.txt', 'wb') as file:
        file.write(string)

def exibirChave(key):
    print(f'Chave: {key}')

def exibirMensagem(mensagem):
    print(mensagem)

def inteiroParaRomano(numeroOriginal):
    numerosRomanos = {
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    numeroConvertido = ''
    for valor, representacao in numerosRomanos.items():
        while numeroOriginal >= valor:
            numeroConvertido += representacao
            numeroOriginal -= valor

    return numeroConvertido

def informarPosicoes():
    
    feed = True
    while feed:
        direcaoLatitude = input('Insira a latitude (N ou S): ')
        feed = validarLatitude(direcaoLatitude)
    
    feed = True
    while feed:
        grauLatitude = int(input('Informe o grau: '))
        feed = validarGrauLatitude(grauLatitude)
    
    feed = True
    while feed:
        minutosLatitude = int(input('Informe os minutos latitude: '))
        feed = validarMinutoOuSegundo(minutosLatitude)
    
    feed = True
    while feed:
        segundosLatitude = int(input('Informe os segundos latitude: '))
        feed = validarMinutoOuSegundo(segundosLatitude)
    
    feed = True
    while feed:
        direcaoLongitude = input('Insira a longitude (O ou L): ')
        feed = validarLogitude(direcaoLongitude)
    
    feed = True
    while feed:
        grauLongitude = int(input('Informe o grau: '))
        feed = validarGrauLongitude(grauLongitude)
    
    feed = True
    while feed:
        minutosLongitude = int(input('Informe os minutos longitude: '))
        feed = validarMinutoOuSegundo(minutosLongitude)
    
    feed = True
    while feed:
        segundosLongitude = int(input('Informe os segundos longitude: '))
        feed = validarMinutoOuSegundo(segundosLongitude)
    
    direcaoLatitude = 'a' if direcaoLatitude.lower() == 'n' else 'b'
    direcaoLongitude = 'x' if direcaoLongitude.lower() == 'o' else 'y'
    
    coordenada = [
                    direcaoLatitude,
                        inteiroParaRomano(grauLatitude),
                        inteiroParaRomano(minutosLatitude),
                        inteiroParaRomano(segundosLatitude),
                    direcaoLongitude,
                        inteiroParaRomano(grauLongitude),
                        inteiroParaRomano(minutosLongitude),
                        inteiroParaRomano(segundosLongitude)
                ]
    
    coordenadaOriginal = ' '.join(coordenada)
    
    chave = gerarChave()
    
    coordenadaEncriptada = encrypt(coordenadaOriginal, chave)
    
    exportarTextoChave(chave)
    exportarTextoMensagem(coordenadaEncriptada)
    
    return True

def validarLatitude(direcaolatitude):
    if direcaolatitude.lower() in ['n', 's']:
        return False
    else:
        limparTela()
        print('\nLatitude invalida, tente novamente.\n')
        return True
    
def validarLogitude(direcaoLatitude):
    if direcaoLatitude.lower() in ['o', 'l']:
        return False
    else:
        limparTela()
        print('\nLogitude invalida, tente novamente.\n')
        return True

def validarGrauLatitude(numeroGrauLatitude):
    try:
        if 0 <= numeroGrauLatitude <= 90:
            return False
        else:
            limparTela()
            print('\nGrau informado e invalido, tente novamente.\n')
            return True
    except ValueError:
        limparTela()
        print('\nGrau para Latitude informada é inválida. Certifique-se de inserir um número inteiro.\n')
        return True

def validarGrauLongitude(numeroGrauLongitude):
    try:
        if 0 <= numeroGrauLongitude <= 180:
            return False
        else:
            limparTela()
            print('\nGrau informado e invalido, tente novamente.\n')
            return True
    except ValueError:
        limparTela()
        print('\nGrau para Logitude informada é inválida. Certifique-se de inserir um número inteiro.\n')
        return True
    
def validarMinutoOuSegundo(numeroMinutoOuSegundo):
    try:
        if 0 <= numeroMinutoOuSegundo < 60:
            return False
        else:
            limparTela()
            print('\nMinuto ou Segundo informado e invalido, tente novamente\n')
            return True
    except ValueError:
        limparTela()
        print('\nValor informado para minuto ou segundo é inválido. Certifique-se de inserir um número inteiro.\n')
        return True


def informarMensagem():
    textoOriginal = input('Texto: ')
    chave = gerarChave()
    textoCifrado = encrypt(textoOriginal, chave)
    exportarTextoChave(chave)
    exportarTextoMensagem(textoCifrado)

def gerarChave():
    return Fernet.generate_key()

def encrypt(textoClaro, chave):
    fernet = Fernet(chave)
    textoCifrado = fernet.encrypt(textoClaro.encode())
    return textoCifrado

def decrypt(mensagemEncriptada, chave):
    try:
        fernet = Fernet(chave)
        textoClaro = fernet.decrypt(mensagemEncriptada)
        return textoClaro.decode()
    except InvalidToken:
        print("Erro: Chave de descriptografia inválida.")
        return None

def main():
    
    limparTela()

    while True:
        
        print("Informe o número da opção desejada:")
        print("1 - Informar posição")
        print("2 - Enviar mensagem")
        print("3 - Decriptar mensagem")
        print("\n0 - Encerrar programa")

        try:

            opcao = int(input("> "))

            if opcao == 1:

                limparTela()

                print("Opção 1 selecionada. Informando posição...")
                informarPosicoes()
                print("\nInformações geradas com sucesso.\n")
                
            elif opcao == 2:

                limparTela()

                print("Opção 2 selecionada. Enviando mensagem...")
                informarMensagem()

                print("\nMensagem enviada com sucesso.\n")
                
            elif opcao == 3:

                limparTela()

                print("Opção 3 selecionada. Decriptando mensagem...")
                mensagem_criptografada = input('\nInforme a mensagem criptografada: ')
                
                chave = input('\nInforme a chave de criptografia: ')
                mensagem_decriptada = decrypt(mensagem_criptografada.encode(), chave.encode())
                
                if mensagem_decriptada is not None:
                    limparTela()
                    print(f'Mensagem decriptada:\n{mensagem_decriptada}\n')
                    
            elif opcao == 0:
                print("\nPrograma finalizado!")
                break
            
            else:
                print("\nOpção inválida. Por favor, escolha um dos número no menu apresentado.\n")

        except ValueError:
            print("\nOpção informada não é um número, por favor insira apenas um número das opções apresentadas.\n")

if __name__ == "__main__":
    main()

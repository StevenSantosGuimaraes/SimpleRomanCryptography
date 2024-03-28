from cryptography.fernet import Fernet
import os


# Este programa é uma aplicação simples de criptografia e manipulação de coordenadas geográficas.

# Opção 1 - Informar posição:
#   - O usuário pode inserir coordenadas geográficas (latitude e longitude), que são convertidas em algarismos romanos.
#   - As coordenadas convertidas são então criptografadas usando uma chave de criptografia gerada aleatoriamente.
#   - A chave de criptografia e a mensagem criptografada são exportadas para arquivos.

# Opção 2 - Enviar mensagem:
#   - O usuário pode inserir uma mensagem, que é criptografada usando uma chave de criptografia gerada aleatoriamente.
#   - A chave de criptografia e a mensagem criptografada são exportadas para arquivos.

# Opção 3 - Decriptar mensagem:
#   - O usuário fornece uma mensagem criptografada e a chave de criptografia correspondente.
#   - A mensagem é descriptografada usando a chave fornecida e exibida no console.

# Essencialmente, o programa permite ao usuário criptografar e descriptografar mensagens,
# bem como manipular coordenadas geográficas e armazenar informações criptografadas em arquivos para uso posterior.


def limparTela():
    os.system('cls')

def exportarTextoChave(txt):
    with open("chave.txt", "wb") as arquivo:  
        #texto = txt.decode('utf-8')
        arquivo.write(txt)
        arquivo.close()

def exportarTextoMensagem(string):
    with open('./mensagem.txt', 'wb') as file:
        file.write(string)

def exibirChave(key):
    print(f'Chave: {key}')

def exibirMensagem(mensagem):
    print(mensagem)

def inteiroParaRomano(graus):
    numeros_romanos = {
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
    numero_convertido = ''
    for value, representacao in numeros_romanos.items():
        while graus >= value:
            numero_convertido += representacao
            graus -= value
    return numero_convertido

def informarPosicoes():
    feed = True
    while feed:
        latitude = input('Insira a latitude(N ou S): ')
        feed = validarLatitude(latitude)
    feed = True
    while feed:
        grau_latitude = int(input('Informe o grau: '))
        feed = validarGrauLatitude(grau_latitude)
    feed = True
    while feed:
        minutos_latitude = int(input('Informe os minutos latitude: '))
        feed = validarMinutoOuSegundo(minutos_latitude)
    feed = True
    while feed:
        segundos_latitude = int(input('Informe os segundos latitude: '))
        feed = validarMinutoOuSegundo(segundos_latitude)
    feed = True
    while feed:
        longitude = input('Insira a longitude(O ou L): ')
        feed = validarLogitude(longitude)
    feed = True
    while feed:
        grau_longitude = int(input('Informe o grau: '))
        feed = validarGrauLongitude(grau_longitude)
    feed = True
    while feed:
        minutos_longitude = int(input('Informe os minutos longitude: '))
        feed = validarMinutoOuSegundo(minutos_longitude)
    feed = True
    while feed:
        segundos_longitude = int(input('Informe os segundos longitude: '))
        feed = validarMinutoOuSegundo(segundos_longitude)
    coordenada = [
                    latitude,
                        inteiroParaRomano(grau_latitude),
                        inteiroParaRomano(minutos_latitude),
                        inteiroParaRomano(segundos_latitude),
                    longitude,
                        inteiroParaRomano(grau_longitude),
                        inteiroParaRomano(minutos_longitude),
                        inteiroParaRomano(segundos_longitude)
                ]
    coordenadaOriginal = ' '.join(coordenada)
    chave = generate_key()
    coordenadaEncriptada = encrypt(coordenadaOriginal, chave)
    exportarTextoChave(chave)
    exportarTextoMensagem(coordenadaEncriptada)
    return True

def validarLatitude(latitude):
    if latitude == 'S' or latitude == 's' or latitude == 'N' or latitude == 'n':
        return False
    else:
        limparTela()
        print('Latitude invalida, tente novamente.')
        return True
    
def validarLogitude(latitude):
    if latitude == 'O' or latitude == 'o' or latitude == 'L' or latitude == 'l':
        return False
    else:
        limparTela()
        print('Logitude invalida, tente novamente.')
        return True

def validarGrauLatitude(num):
    if num <= 90:
        return False
    else:
        limparTela()
        print('Grau informado e invalido, tente novamente.')
        return True

def validarGrauLongitude(num):
    if num <= 180:
        return False
    else:
        limparTela()
        print('Grau informado e invalido, tente novamente.')
        return True
    
def validarMinutoOuSegundo(num):
    if num < 60:
        return False
    else:
        limparTela()
        print('Minuto ou Segundo informado e invalido, tente novamente')
        return True


def informarMensagem():
    textoOriginal = input('Texto: ')
    chave = generate_key()
    textoCifrado = encrypt(textoOriginal, chave)
    #exibirChave(chave)
    #exibirMensagem(textoCifrado)
    exportarTextoChave(chave)
    exportarTextoMensagem(textoCifrado)

def generate_key():
    return Fernet.generate_key()

def encrypt(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt(encrypted_message, key):
    try:
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message)
        return decrypted_message.decode()
    except InvalidToken:
        print("Erro: Chave de descriptografia inválida.")
        return None

def main():
    
    limparTela()
    
    while True:
        
        print("Informe a opção desejada:")
        print("1 - Informar posição")
        print("2 - Enviar mensagem")
        print("3 - Decriptar mensagem")
        print("\n0 - Encerrar programa")

        opcao = int(input("> "))

        if opcao == 1:
            print("Opção 1 selecionada. Informando posição...")
            informar_posicoes()
            print("Informações geradas com sucesso.")
            
        elif opcao == 2:
            print("Opção 2 selecionada. Enviando mensagem...")
            informar_mensagem()
            print("Mensagem enviada com sucesso.")
            
        elif opcao == 3:
            print("Opção 3 selecionada. Decriptando mensagem...")
            mensagem_criptografada = input('Informe a mensagem criptografada: ')
            chave = input('Informe a chave de criptografia: ')
            mensagem_decriptada = decrypt(mensagem_criptografada.encode(), chave.encode())
            
            if mensagem_decriptada is not None:
                limparTela()
                print(f'\nMensagem decriptada:\n{mensagem_decriptada}\n')
                
        elif opcao == 0:
            print("Programa finalizado!")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()

#DesafioSelecaoVendedorInterespacial
print('\n-=-=-=-=-=-Conversor Intergaláctico-=-=-=-=-=-')

print('\nNotação Intergaláctica dos Símbolos Romanos')
print('snob representa I\nkrok representa V\nsquid representa X\nleij representa L\njark representa C\nblop representa D\ngur representa M')

print('\nValor em créditos dos minérios:\nPrata: 17 créditos\nOuro: 14450 créditos\nFerro: 195.5\n')

#Iniciando a Lista com a linguagem intergalática.
alienL = ['snob','krok','squid','leij','jark','blop','gur']

#loop com a pergunta quanto vale, e resposta para caso seja digitado algo errado
verificarpalavra = True
while verificarpalavra:
    #cria uma lista com as palavras digitadass
    alienCred = str (input('Quanto vale: ' )).lower().split(' ')
    for x in range(len(alienCred)):
        #verifica se digitou uma palavra conhecida na linguagem intergaláctica
        if  alienCred[x] not in alienL:
            print('Nem ideia do que isto significa!')
            verificarpalavra = True
            break
        else:
            verificarpalavra = False
    

#pergunta qual minerio deseja e insere o preço do minério escolido numa variavel          
while True:
    minerio =  (str (input('Digite o minério deseja (prata, ouro ou ferro): ' )).lower())
    if minerio == 'prata':
        credMin = 17
        break
    elif minerio == 'ouro':
        credMin = 14450
        break
    elif minerio == 'ferro':
        credMin = 195.5
        break
    else:
        print('Não vendemos este minério')
    
#pergunta quantas unidades deseja deste minério
alienMin = str (input('Digite a quantidade de minério em Intergaláctico: ' )).lower().split(' ')

#Funcao para converter linguagem alienigena (similar aos numerais romanos) para numeros inteiros
def alien_decimal(alien):
    #dicionario para representar uma equilavencia com o simbolo alien com seu respectivo valor numerico decimal
    aliens = {'snob': 1, 'krok': 5, 'squid': 10, 'leij': 50, 'jark': 100, 'blop': 500, 'gur': 1000}
    #var decimal que vai conter o resultado
    decimal = 0
    #passamos por todos caracteres que representam o numero alien
    for i in range(len(alien)):
        #comprovacao, se o i > 0 e o simbolo alien for maior que o anterior, 
        #vai somar o simbolo alien atual e subtrair 2x o simbolo alien anterior 
        if i > 0 and aliens[alien[i]] > aliens[alien[i - 1]]:
            decimal += aliens[alien[i]] - 2 * aliens[alien[i - 1]]
        #se o i<=0 ou o simbolo alien for menor que o anterior, soma ao var decimal
        else:
            decimal += aliens[alien[i]]
        
    return decimal

#Variavel com valor de creditos do total de minério escolhido
credMinT = (alien_decimal(alienMin) * credMin)
print ('\nRespostas:')
print (f'{" ".join(alienCred)} vale {alien_decimal(alienCred)}')
print (f'{" ".join(alienMin)} de {minerio} vale {credMinT}')

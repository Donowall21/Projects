import time
#Gustavo Henrique Palu
#faz introducao ao usuario
time.sleep(2)
print('\n\nNos entrelaçados caminhos cósmicos, onde o destino sussurra os segredos do universo, quais cartas abrirão a porta para sua verdade?')
print('Entre as irmãs do céu, o poderoso Mago e a Torre que toca as estrelas, que suas escolhas sejam guiadas por esses arcanos, iluminando sua jornada rumo ao desconhecido.')

#input do usuario para escolha entre Sol, Lua, Torre ou Mago
Decisao1 = input('\nEscolha entre: Sol; Lua; Torre; Mago: ')
Decisao2 = input('\nEscolha novamente entre: Sol; Lua; Torre; Mago: ')

#Normaliza a Decisao para minusculo
Decisao1_normal = Decisao1.lower()
Decisao2_normal = Decisao2.lower()

#aqui acarreta todos os if e elifs, basicamente é feito uma sequencia de if elif para a decisao1 e dentro de cada if elif tem uma sequencia de if elif para a decisao2, bem simples. no final tem o else para erros.
if Decisao1_normal == 'sol':

    if Decisao2_normal == 'sol':
        print('\nUau, você realmente conseguiu escolher uma sequência impossível de dois sóis! Que talento incrível!')
        time.sleep(2)
        print('Super brilhante, quase como um farol em dia nublado.')

    elif Decisao2_normal == 'lua':
        print('\nComo os dois lados da mesma moeda, a única coisa em comum entre Sol e Lua é o preço que você paga para acreditar que eles realmente se importam com você.')
        time.sleep(2)
        print('Afinal, quem precisa de equilíbrio quando se pode ter drama?')

    elif Decisao2_normal == 'torre':
        print('\nO Sol ilumina a Torre em toda sua glória, revelando suas falhas ocultas...')
        time.sleep(2)
        print('O que você esperava? Que tudo fosse perfeito? Até as Torres têm seus momentos de fraqueza.')

    elif Decisao2_normal == 'mago':
        print('\nBrilhante como o Sol e com talento raro, você avança para grandes feitos...')
        time.sleep(2)
        print('Mas cuidado! Se sua luz ofuscar, pode acabar como um guru de tavernas, pregando conselhos vazios em vez de ser um verdadeiro herói. Afinal, quem precisa de glória quando se pode brilhar e divagar?')
    
    else:
        print('\nO Sol mostra...')
        time.sleep(2)
        print('Mostra o Erro que acontece com um input Inválido...')
        time.sleep(2)
        print(f'A real pergunta é, porque {Decisao2}?')

elif Decisao1_normal == 'lua':

    if Decisao2_normal == 'sol':
        print('\nAh, como irmãs que nunca se encontram, a Lua e o Sol mostram que a relação não anda bem...')
        time.sleep(2)
        print('Mas ei, isso é só uma oportunidade disfarçada! Afinal, quem precisa de harmonia quando se pode trabalhar no autoconhecimento, não é mesmo?')

    elif Decisao2_normal == 'lua':
        print('\nUm doppelganger? Ah, como se a noite pudesse ficar mais densa.')
        time.sleep(2)
        print('Prepare-se para dançar com suas sombras, porque o autoconhecimento pode ser bem... iluminador!')

    elif Decisao2_normal == 'torre':
        print('\nA Lua, com seu brilho azulado, sussurra à Torre que é hora de se render ao descanso.')
        time.sleep(2)
        print('Às vezes, deixar o trabalho de lado é o melhor plano porque, afinal, quem precisa de sucesso quando se pode abraçar a preguiça mística?')

    elif Decisao2_normal == 'mago':
        print('\nA Lua, com sua majestosidade etérea, inspira o Mago a tecer feitiços de grandeza.')
        time.sleep(2)
        print('Afinal, quem precisa de fórmulas quando se pode simplesmente deixar a intuição brilhar?')
    
    else:
        print('\nA Lua enaltece e...')
        time.sleep(2)
        print('Se fosse algo valido talvez daria sono?')
        time.sleep(2)
        print(f'E o que que a lua tem a ver com {Decisao2}?')

elif Decisao1_normal == 'torre':
    
    if Decisao2_normal == 'sol':
        print('\nA luz do Sol brilha sobre as sombras da Torre, prometendo revelações à vista.')
        time.sleep(2)
        print('Afinal, onde há luz, sempre há espaço para um drama... e quem não adora um bom mistério no meio do dia?')

    elif Decisao2_normal == 'lua':
        print('\nA Lua observa a Torre, prometendo mistérios. O que será que se esconde atrás das paredes?')
        time.sleep(2)
        print('Provavelmente só um monte de *oportunidades de crescimento pessoal* esperando para serem descobertas.')

    elif Decisao2_normal == 'torre':
        print('\nA Torre reflete sua própria fortaleza, ou talvez apenas sua falta de sorte. Escolher duas vezes a mesma carta? Bravo! Você é mais forte do que pensa.')
        time.sleep(2)
        print('ou simplesmente um mestre da repetição.')

    elif Decisao2_normal == 'mago':
        print('\nO Mago diante da Torre diz: busque sabedoria na estrutura que você construiu.')
        time.sleep(2)
        print('Ou seja, olhe bem para sua bagunça e veja se encontra algo além do seu caos habitual!')
    
    else:
        print('\nA Torre infinita inspira...')
        time.sleep(2)
        print('Inspira a tentativa falha... Mas ele te mostra que existem escolhas certas.')
        time.sleep(2)
        print(f'E vamos ser bem sinceros, é uma torre, o que {Decisao2} tem a ver com isso?')

elif Decisao1_normal == 'mago':
    
    if Decisao2_normal == 'sol':
        print('\nA luz do Sol encontra o Mago, trazendo clareza às suas intenções.')
        time.sleep(2)
        print('Ou seja, é hora de parar de fazer wishful thinking e realmente manifestar alguma coisa...')
        time.sleep(2)
        print('ou só mais um café?')

    elif Decisao2_normal == 'lua':
        print('\nO Mago e a Lua dançam na noite, revelando o poder da intuição. Então, ouça seu coração...')
        time.sleep(2)
        print('ou pelo menos faça o que ele diz antes de pedir pizza!')

    elif Decisao2_normal == 'torre':
        print('\nO Mago ao lado da Torre diz que a transformação é necessária. Hora de questionar suas fundações!')
        time.sleep(2)
        print('Afinal, quem precisa de estabilidade quando se pode ter uma boa crise de identidade?')

    elif Decisao2_normal == 'mago':
        print('\nDois Magos juntos? Ah, o poder da criatividade se multiplica! Ou você simplesmente decidiu ignorar as regras do jogo.')
        time.sleep(2)
        print('O que você vai criar? Um espetáculo de caos ou uma nova receita de desastre?')
    
    else:
        print('\nO Mago usa de suas magias e criatividade para...')
        time.sleep(2)
        print(f'Criar O que ele sempre quis, {Decisao2}, O estopim que o levou a aprender magia...')
        time.sleep(2)
        print('Na verdade nao, isso aqui é só um erro mesmo...')

else:
    print('\nEscolha Invalida...')
    time.sleep(2)
    print(f'Porque voce escolheu {Decisao1} ao inves das cartas certas?')

#aqui é finalizacao, fora dos if elif e elses para concluir o programa e fechar com estilo. (mas é um segredo, esse control+J so funciona se for no VSCode)
time.sleep(3)
print('\n\nA verdadeira mensagem do Oráculo sussurra entre os códigos e silêncios, o encantamento que encerra o terminal, como se a sabedoria se esvaísse em um suspiro.')
time.sleep(2)
print('Aperte... Control+J\n\n')
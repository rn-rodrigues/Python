
def DonPython(moedas_validas,troco,cont,resp_local):
 for i in range(1,troco+1): # range dos n*'s
  contador=i
  qual_pegar=1 # caso base: troco todo em moeda de 1 centavo
  for j in moedas_validas:
   if j<=i: # não continua se moeda tiver valor maior que n*
    if cont[i-j]+1<contador: # tira moeda 'i' do total; se quantidade ótima para troco de n* for menor que o minimo provisório:
     contador=cont[i-j]+1 # atualizar quantidade ótima
     qual_pegar=j # qual moeda escolher para minimizar quantidade exigida para troco de n*
   cont[i]=contador # armazena na tabela os trocos ótimos para todos os n*'s
   resp_local[i]=qual_pegar # para todo n*, qual moeda 'marginalmente' deve ser escolhida?
 print(cont[troco]) # função retorna quantidade ótima para o 'n' original

def caminho(resp_local,troco): # quais moedas efetivamente pegar
 moedas=[] # lista vazia
 while troco>0: # repetir até zerar troco
  devo_pegar_essa=resp_local[troco] # qual moeda escolher dado 'n'?
  moedas.append(devo_pegar_essa) # guarda essa moeda na lista
  troco=troco-devo_pegar_essa # atualiza troco, diminuindo valor da moeda escolhida
 print(moedas) # função retorna quais moeda são selecionadas
	
	
quantia=68
moedas=[100,50,25,10,5,1]
resp_local=[0]*(quantia+1)
contador=[0]*(quantia+1)


DonPython(moedas,quantia,contador,resp_local)
caminho(resp_local,quantia) # moedas escolhidas pela estratégia programação dinâmica

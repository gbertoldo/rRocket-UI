DOCUMENTAÇÃO EM CONSTRUÇÃO

# rRocket-UI 🚀 
 Interface gráfica para computador de bordo de minifoguetes modelo [rRocket](https://github.com/gbertoldo/rRocket).

# Versão
Versão 1.1.0

# Como usar
1. [Baixe](https://github.com/gbertoldo/rRocket-UI/releases) a versão mais recente do executável (disponível apenas para Windows).
1. Descompacte o arquivo zip baixado.
1. No diretório do arquivo extraído há o executável rRocketUI.exe. Não é necessário realizar instalações, basta rodar esse arquivo. Se não houver erros, surgirá uma janela como ilustrado na figura abaixo:
![rRocket-Start](https://github.com/user-attachments/assets/a294f31b-66ab-49e9-859d-e745f8a30fcb)

A janela da interface gráfica está organizada em cinco abas, detalhadas a seguir.

## Conexão
Algumas das funcionalidades (configuração, leitura de memória e simulação) da interface gráfica são habilitadas apenas se o rRocket estiver conectado. Para realizar a conexão:
1. Na aba *Conexão*, verifique as portas USB disponíveis
![rRocket-Connection1b](https://github.com/user-attachments/assets/caaf5ef6-676d-477b-9f76-0eebcc7bc446)
*Observação: a numeração das portas varia de um computador para outro.*
1. Conecte o rRocket a uma porta USB do computador.
1. Clique no botão para atualizar a lista de portas USB disponíveis ![rRocket-Connection1c](https://github.com/user-attachments/assets/ef589657-1311-4361-aa65-6f988ca14d4d).
 Selecione a porta que apareceu após a conexão do rRocket (passo 2). 
![rRocket-Connection1d](https://github.com/user-attachments/assets/1569bac2-ff04-4f5a-9920-1fe8743dad14)
1. Clique no botão *Conectar*. Se a conexão for bem sucedida, o ícone mudará de vermelho para verde.
![rRocket-Connection](https://github.com/user-attachments/assets/d386e3fb-8b3d-4128-969f-e89558cd01a0)

## Configuração
⚠️ As funcionalidades desta aba são habilitadas apenas se o rRocket estiver conectado.

A aba *Configuração* permite ajustar os parâmetros de voo do rRocket. 
![rRocket-Setup](https://github.com/user-attachments/assets/13b0ae66-016d-4036-af4d-346689ce2a66)

No topo da aba é exibida a versão de _firmware_ do rRocket (_firmware_ é o _software_ que faz o dispositivo funcionar). Logo abaixo, há um formulário que lista (a) os parâmetros de voo, (b) os valores que estão gravados na memória do rRocket e (c) os valores desejados pelo usuário dos respectivos parâmetros. Abaixo do formulário há quatro botões:
1. *Ler parâmetros*: solicita ao rRocket que envie a lista de parâmetros de voo gravados em sua memória permanente.
1. *Relatório de parâmetros*: cria uma listagem textual dos parâmetros de voo gravados na memória. Esta listagem pode ser salva em arquivo para conferência futura.
1. *Restaurar parâmetros originais*: solicita que rRocket substitua os parâmetros gravados pelos valores padrão definidos no _firmware_.
1. *Gravar parâmetros*: envia os parâmetros desejados para gravação na memória permanente do rRocket.

⚠️ *Para que os parâmetros desejados sejam gravados na memória do rRocket é necessário clicar no botão _Gravar parâmetros_ e observar a atualização dos valores gravados!* 

⚠️ *Após o carregamento de firmware no Arduino, a memória permanente (EEPROM) estará preenchida com dados desconhecidos. Isso deve gerar valores absurdos para os parâmetros de voo. Deste modo, no primeiro uso do altímetro, deve-se clicar em _Restaurar parâmetros originais_ para que os valores padrão sejam gravados na memória.* 

## Memória de voo
⚠️ As funcionalidades desta aba são habilitadas apenas se o rRocket estiver conectado.

Os dados do último voo do rRocket são recuperados nesta aba. Na parte central há o gráfico da altura acima do ponto de lançamento como função do tempo. Neste mesmo gráfico são apresentados os eventos de voo: detecção de lançamento (F), deteção de apogeu e acionamento de paraquedas auxiliar (A), detecção de ponto de lançamento de paraquedas principal (P) e detecção de aterissagem (L). 
![rRocket-Memory1](https://github.com/user-attachments/assets/033b1f9b-d62b-4b90-b293-75bd17a08d00)

Abaixo do gráfico, há três botões:
- *Ler memória*: solicita a leitura/releitura de memória do rRocket. 
- *Limpar memória*: apaga a memória do último voo.
- *Relatório de voo*: gerar um relatório do último voo. Como ilustrado na figura abaixo, o relatório apresenta a versão de _firmware_ do rRocket, os parâmetros estáticos (definidos no _firmware_ e que não podem ser alterados na interface gráfica), os parâmetros de voo, códigos de erro, eventos de voo e a trajetória.
![rRocket-Memory2](https://github.com/user-attachments/assets/578825f9-5454-4cfe-b5df-66b777db1d9a)

⚠️ ANTES DE CADA LANÇAMENTO É NECESSÁRIO LIMPAR A MEMÓRIA DE VOO! É possível realizar essa operação pela interface, como descrito acima, ou pelo rRocket, segurando o botão pressionado por cinco segundos. Caso a memória de voo esteja limpa, o computador de bordo emitirá um bipe a cada 1,5 s.

## Simulação
⚠️ As funcionalidades desta aba são habilitadas apenas se o rRocket estiver conectado.

## Estatística

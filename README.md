# rRocket-UI 🚀 
 Interface gráfica para computador de bordo de minifoguetes modelo [rRocket](https://github.com/gbertoldo/rRocket).

# Versão
Versão 1.1.0

# Como usar
1. [Baixe](https://github.com/gbertoldo/rRocket-UI/releases) a versão mais recente do executável (disponível apenas para Windows).
1. Descompacte o arquivo zip baixado.
1. No diretório do arquivo extraído há o executável rRocketUI.exe. Não é necessário realizar instalações, basta rodar esse arquivo. Se não houver erros, surgirá uma janela como ilustrado na figura abaixo:
<p align="center">
<img src="https://github.com/user-attachments/assets/a294f31b-66ab-49e9-859d-e745f8a30fcb">
</p>
A janela da interface gráfica está organizada em cinco abas, detalhadas a seguir.

## Conexão
Algumas das funcionalidades da interface gráfica são habilitadas apenas se o rRocket estiver conectado. Para realizar a conexão:
1. Na aba **Conexão**, verifique as portas USB disponíveis, como ilustrado a seguir:
<p align="center">
<img src="https://github.com/user-attachments/assets/caaf5ef6-676d-477b-9f76-0eebcc7bc446" width=300>
</p> 

**Observação: a numeração das portas varia de um computador para outro.**

2. Conecte o rRocket a uma porta USB do computador.
   
4. Clique no botão para atualizar a lista de portas USB disponíveis:
<p align="center">
<img src="https://github.com/user-attachments/assets/ef589657-1311-4361-aa65-6f988ca14d4d" width=50>.
</p>

4. Selecione a porta que apareceu após a conexão do rRocket (passo 2).
<p align="center">
<img src="https://github.com/user-attachments/assets/1569bac2-ff04-4f5a-9920-1fe8743dad14">
</p>

5. Clique no botão **Conectar**. Se a conexão for bem sucedida, o ícone de _status_ de conexão mudará de vermelho para verde.
<p align="center">
<img src="https://github.com/user-attachments/assets/d386e3fb-8b3d-4128-969f-e89558cd01a0">
</p>

## Configuração
⚠️ As funcionalidades desta aba são habilitadas apenas se o rRocket estiver conectado.

A aba **Configuração** permite ajustar os parâmetros de voo do rRocket. 
<p align="center">
<img src="https://github.com/user-attachments/assets/13b0ae66-016d-4036-af4d-346689ce2a66">
 </p>
 
No topo da aba é exibida a versão de _firmware_ do rRocket (_firmware_ é o _software_ que faz o dispositivo funcionar). Logo abaixo, há um formulário que lista (a) os parâmetros de voo, (b) os valores que estão gravados na memória do rRocket e (c) os valores desejados pelo usuário para os respectivos parâmetros. Abaixo do formulário há quatro botões:
1. **Ler parâmetros**: solicita ao rRocket que envie a lista de parâmetros de voo gravados em sua memória permanente.
1. **Relatório de parâmetros**: cria uma listagem textual dos parâmetros de voo gravados na memória. Esta listagem pode ser salva em arquivo para conferência posterior.
1. **Restaurar parâmetros originais**: solicita que rRocket substitua os parâmetros gravados pelos valores padrão definidos no _firmware_.
1. **Gravar parâmetros**: envia os parâmetros desejados para gravação na memória permanente do rRocket.

⚠️ **Para que os parâmetros desejados sejam gravados na memória do rRocket, é necessário clicar no botão _Gravar parâmetros_. Antes de qualquer voo, observe se valores gravados estão corretos!**

⚠️ *Após o carregamento de firmware no Arduino, a memória permanente (EEPROM) estará preenchida com dados desconhecidos. Isso deve gerar valores absurdos para os parâmetros de voo. Deste modo, no primeiro uso do altímetro, deve-se clicar em **Restaurar parâmetros originais** para que os valores padrão sejam gravados na memória.* 

### Parâmetros de voo
- **Velocidade (em módulo) para detecção de decolagem (m/s)**: velocidade a partir da qual gera-se o evento de decolagem. Se este parâmetro for muito baixo (abaixo de 10 m/s, por exemplo), rajadas de vento laterais podem causar falso evento de decolagem enquanto o minifoguete ainda está na rampa de lançamento. Por outro lado, se o parâmetro for muito alto (acima de 50 m/s, por exemplo), é possível que voos mais baixos não sejam detectados.
- **Velocidade (em módulo) para detecção de queda (m/s)**: velocidade a partir da qual detecta-se queda em uma situação de reinicialização do computador de bordo durante o voo. A reinicialização durante o voo é totalmente indesejável, mas pode ocorrer devido à falha de alimentação de energia ou caso o botão do Arduino seja pressionado acidentalmente, por exemplo. Neste caso, o rRocket tenta detectar a queda e acionar os paraquedas.
- **Velocidade para detecção de apogeu (m/s)**: o apogeu ocorre quando a componente vertical do vetor velocidade é nula. No entanto, é possível ajustar este parâmetro para acionar o paraquedas auxiliar (drogue) um pouco antes (velocidade positiva) ou um pouco depois (velocidade negativa) do apogeu. 
- **Altura acima do ponto de lançamento para acionamento do paraquedas principal (m)**: caso o minifoguete possua dois paraquedas, o primeiro (drogue) é acionado no apogeu e o segundo (paraquedas principal) é acionado na altura definida por este parâmetro.
- **Deslocamento máximo para detecção de pouso (m)**: o rRocket mantém um registro de N leituras de altura, onde o N é um número inteiro definido no _firmware_. Para gerar o evento de pouso, a variação de altura nos N registros deve ser menor que o valor definido neste parâmetro.
- **Número máximo de tentativas de acionamento de paraquedas (por paraquedas)**: determina o número de tentativas de acionamento dos paraquedas. O acionamento dos paraquedas é realizado através da descarga de um capacitor. Como o rRocket não possui um sistema de _feedback_ para avaliar se o paraquedas foi acionado, é recomendável realizar pelo menos três tentativas de acionamento.
- **Multiplicador de passo de tempo para registro de trajetória após acionamento do drogue**: determina a frequência de armazenamento de dados na memória permanente após o apogeu. Até o apogeu, a trajetória é registrada com frequência de 10 Hz, ou seja, a cada 0,1 segundo. Para voos mais longos, pode ser interessante reduzir a frequência de registro, tendo em vista que a memória EEPROM do Arduino Nano é de apenas 1024 bytes. Se o multiplicador for definido como 5, por exemplo, após o apogeu os dados serão gravados a cada 0,5 s, isto é, 5 x 0,1 s.

⚠️  Recomenda-se testar os parâmetros de voo utilizando o recurso de [simulação](#simulação).

## Memória de voo
⚠️ As funcionalidades desta aba são habilitadas apenas se o rRocket estiver conectado.

Os dados do último voo do rRocket são recuperados nesta aba. Na parte central há o gráfico da altura acima do ponto de lançamento como função do tempo. Neste mesmo gráfico são apresentados os eventos de voo: detecção de lançamento (F), deteção de apogeu e acionamento de paraquedas auxiliar (D), detecção de ponto de lançamento de paraquedas principal (P) e detecção de aterissagem (L). 
<p align="center">
<img src="https://github.com/user-attachments/assets/033b1f9b-d62b-4b90-b293-75bd17a08d00">
 </p>
 
Abaixo do gráfico, há três botões:
- **Ler memória**: solicita a leitura/releitura de memória do rRocket. 
- **Limpar memória**: apaga a memória do último voo.
- **Relatório de voo**: gerar um relatório do último voo. Como ilustrado na figura abaixo, o relatório apresenta a versão de _firmware_ do rRocket, os parâmetros estáticos (definidos no _firmware_ e que não podem ser alterados na interface gráfica), os parâmetros de voo, códigos de erro, eventos de voo e a trajetória. O relatório pode ser salvo em arquivo de texto para análise posterior.
<p align="center">
<img src="https://github.com/user-attachments/assets/578825f9-5454-4cfe-b5df-66b777db1d9a">
</p>

⚠️ ANTES DE CADA LANÇAMENTO É NECESSÁRIO LIMPAR A MEMÓRIA DE VOO! É possível realizar essa operação pela interface, como descrito acima, ou pelo rRocket, segurando o botão pressionado por cinco segundos. Caso a memória de voo esteja limpa, o computador de bordo emitirá um bipe a cada 1,5 s.

## Simulação
⚠️ As funcionalidades desta aba são habilitadas apenas se o rRocket estiver conectado.

É possível observar/analisar o comportamento do rRocket quando sujeito a uma trajetória predefinida através do recurso de simulação. Para isso, na aba **Simulação**, basta fornecer o arquivo de texto com a tabela de dados de trajetória (altura _vs_ tempo) e clicar no botão **Iniciar simulação**. A interface solicita que o rRocket ative o modo simulado e utilize os dados da trajetória informada ao invés da leitura do barômetro. Com este recurso, é possível avaliar se os parâmetros de voo estão adequados para a trajetória informada.
<p align="center">
<img src="https://github.com/user-attachments/assets/14ab204d-5086-4e1d-9d43-af540005be0b">
</p>

O formato do arquivo de entrada pode ser especificado clicando-se no botão **Configurar formato**. Na janela de configuração, deve-se informar o caracter separador de campos (separador de colunas), o separador decimal (ponto ou vírgula), se há caractere usado para indicar comentário, o número de linhas de cabeçalho (que são ignoradas na leitura do arquivo), as colunas do tempo e da altura, bem como a unidade da altura.
<p align="center">
<img src="https://github.com/user-attachments/assets/eae38cee-0999-47b4-9425-caf786eabeb8">
</p>

Por praticidade, os formatos de arquivo dos altímetros rRocket, MicroPeak e Stratologger já são predefinidos.
<p align="center">
<img src="https://github.com/user-attachments/assets/6c4e9e02-51cc-43a7-8532-fd02e55b1ece">
</p>

Por fim, é possível gerar um relatório da simulação clicando-se em **Gerar relatório**.
<p align="center">
<img src="https://github.com/user-attachments/assets/db617ae1-42cc-4dcb-90fb-59ab4862b01a">
</p>

A interface gráfica é acompanhada de vários arquivos para simulações (verifique o subdiretório _sim_). Os arquivos estão agrupados em dados de lançamentos reais (subdiretório _launch_) e voos fabricados (subdiretório _mms_).  

## Estatística

Esta aba permite analisar estatisticamente um voo. A análise pode ser realizada para qualquer trajetória, isto é, não é estritamente vinculada ao rRocket. Para realizar a análise, basta carregar o arquivo da trajetória que se deseja analisar. A formatação do arquivo de entrada pode ser configurada como explicado na seção anterior. É possível também selecionar o modelo estatístico clicando-se no botão **Configurar**. Na versão atual há dois modelos: (a) filtro Kalman-Alfa e (b) média móvel. O primeiro combina o tradicional filtro de Kalman com um filtro alfa dinâmico para a velocidade. O segundo utiliza média móvel central para suavizar a velocidade e a aceleração.
<p align="center">
<img src="https://github.com/user-attachments/assets/d38730fd-90f3-4773-99d5-c8cc4cf48ba1">
</p>
<p align="center">
<img src="https://github.com/user-attachments/assets/0dbfd129-a289-4c84-bbc1-3107371a6cbf">
</p>

Após o carregamento do arquivo, gera-se um gráfico com a altura bruta (isto é, a original), a altura filtrada, a velocidade e a aceleração. 
<p align="center">
<img src="https://github.com/user-attachments/assets/b787cc25-acfc-40c0-ba3c-a045579e7a57">
</p>

O relatório da análise estatística pode ser acessado através do botão **Gerar relatório**
<p align="center">
<img src="https://github.com/user-attachments/assets/ae3dbcf8-5dc7-4c5d-803f-a63a2ce57068">
</p>

⚠️ Atenção: a análise estatística apreentada nesta aba não é necessariamente igual à realizada pelo rRocket. Para obter resultados gerados pelo rRocket, utilize a ferramenta de [simulação](#simulação). 

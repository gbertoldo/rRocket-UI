Conexão (janela independente criada a partir de clique na janela principal)
  selecionar porta
  atualizar portas
  conectar
  desconectar
  exibir status de Conexão na janela principal

Configuração (janela independente criada a partir de clique na janela principal)
  Exibir os parâmetros gravados
  Editar os parâmetros
  Grvar parâmetros

Memória
  Exibir gráfico do último voo (com eventos de voo: decolagem, drogue, paraquedas, pouso)
  Exibir relatório
    Lista de erros
    Parâmetors de voo
    apogeu
    velocidade máxima
    aceleração máxima
    listagem de h x t
    Gravar relatório em arquivo
  Limpar

Simulação
  Exibir parâmetros de voo
  Selecionar arquivo de trajetória
  Iniciar Simulação
  Parar Simulação
  Gráfico da Simulação
  Exibir relatório
    listagem de t, h, v, a, status

TODO
ok criar relatório de voo
ok incluir versão do firmware
ok ler eventos de voo da simulação
ok gerar relatório da simulação
ok ao ler a memória, os dados da simulação são apagados
ok incluir mensagens de início e fim de inicialização do altimetro
ok incluir mensagem de fim de envio de dados de voo
ok implementar eventos de voo no altimetro
ok retirar os dados da trajetória da memória do relatório da simulação
ok ler eventos de voo da memória
ok conferir o cálculo da velocidade e aceleração no altimetro
ok mensagens de inicialização e leitura de memória em andamento
ok incluir campo para visualizar informações adicionais do altímetro
ok incluir eventos de voo no gráfico
ok verificar compatibilidade de firmware
ok ao ler memória, se estiver vazia, limpar o gráfico e notificar o usuário
ok o estado da interface deve ser um reflexo do estado do altímetro, quando o estado mudar, a interface deve mudar
  conectado
    Ready pronto para uso
    Initializing inicializando
    Simulating simulando
    BusyForDataTransfer transferindo dados
  desconectado
ok o estado é impresso com atraso? o valor do evento na memória difere da simulação
ok descobrir porque a Simulação não ocorre quando a memória do altimetro está preenchida
ok apos limpar a memoria via comando, o altimetro não emite o som de inicializado
ok verificar se todo o protocolo de comunicação foi implementado
ok organizar os arquivos de forma modular
ok inserir licença em todos os arquivos
testar todos os voos
remover impressoes no terminal

Bugs
eventualmente o interface fica presa no modo inicializando

Melhorias
ok incluir opção de modelo estatístico
a interface entre o rRocketModel deve ser feita através de métodos (sem acesso direto aos dados)
ler os dados da memória na inicialização
como limpar os gráficos do matplotlib?
se a memória de voo não estiver apagada, o altímetro inicializa no estado landed. Em caso de decolagem rápida, que causa medições de altura negativa, o altímetro pode detectar queda e acionar os paraquedas.
O instante do evento de acionamento de paraquedas na simulação é diferente do registrado na memória quando a condição de abertura de paraquedas ocorre antes do altímetro executar todas as tentativas de acionamento do drogue.
A diferença ocorre porque a transmissão das informações da simulação ocorre com frequência de 10 Hz, ao passo que o evento de mudança de estado pode ocorrer entre dois envios de dados.

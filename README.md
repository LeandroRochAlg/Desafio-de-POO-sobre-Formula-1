# Desafio de Programação Orientada a Objetos - Formula 1

Neste desafio, desenvolvemos um sistema de gerenciamento de resultados de corridas de Fórmula 1 que utiliza os seguintes conceitos: persistência de objetos (usando pickle), exceptions, modelo MVC, tkinter, classes abstratas, frações e datetime.

## Descrição do sistema

O sistema é responsável por gerenciar os resultados de corridas de Fórmula 1. Ele permite o cadastro de pilotos, equipes e corridas, além de registrar os resultados de cada corrida, incluindo a posição de chegada de cada piloto.

O sistema é dividido em três partes principais:

1. **Model:** Contém as classes que representam os objetos do sistema (pilotos, equipes, corridas, etc.) e a lógica de negócio do sistema.
2. **View:** Responsável pela interface gráfica do sistema, utilizando a biblioteca Tkinter.
3. **Controller:** Faz a intermediação entre a camada Model e View, controlando o fluxo de dados e eventos.

### Funcionalidades do sistema

O sistema fornece as seguintes funcionalidades:

1. **Cadastro de pilotos:** Permite o cadastro de pilotos com nome, país, número e equipe.
2. **Cadastro de equipes:** Permite o cadastro de equipes com nome, país e chefe de equipe.
3. **Cadastro de corridas:** Permite o cadastro de corridas com data, local e número de voltas.
4. **Registro de resultados:** Permite o registro dos resultados de uma corrida, incluindo a posição de chegada de cada piloto.
5. **Consulta de resultados:** Permite a consulta dos resultados de uma corrida específica, exibindo a posição de chegada de cada piloto.

### Requisitos do sistema

O sistema atende aos seguintes requisitos:

1. Utiliza persistência de objetos para salvar e carregar os dados do sistema, utilizando o módulo `pickle`.
2. Utiliza classes abstratas para definir as classes base do sistema, como as classes abstratas `Piloto` e `Equipe`.
3. Utiliza exceptions para tratar erros e situações excepcionais durante a execução do programa.
4. Utiliza frações para representar a posição de chegada dos pilotos, permitindo uma representação mais precisa do resultado da corrida.
5. Utiliza a biblioteca `datetime` para manipular as datas das corridas.
6. Utiliza o padrão de arquitetura MVC (Model-View-Controller) para estruturar o código do sistema.

### Como executar o sistema

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe todos os arquivos do projeto em um diretório local.
3. Execute o arquivo `main.py` para iniciar o sistema.
4. A interface gráfica será exibida, permitindo que você interaja com o sistema e realize as funcionalidades descritas acima.

### Como utilizar a persistência de objetos

O sistema utiliza a persistência de objetos para salvar e carregar os dados do sistema. Ao sair do programa, os dados são salvos em um arquivo utilizando o módulo `pickle`. Ao iniciar o programa novamente, os dados são carregados a partir desse arquivo.

### Como utilizar as exceptions

O sistema utiliza exceptions para tratar erros e situações excepcionais que possam ocorrer durante a execução do programa. Por exemplo, se você tentar cadastrar um piloto sem informar o nome, será lançada uma exception informando que o nome é obrigatório.

### Como utilizar o modelo MVC

O sistema utiliza o padrão de arquitetura MVC (Model-View-Controller) para estruturar o código do sistema. A camada Model contém as classes que representam os objetos do sistema e a lógica de negócio. A camada View é responsável pela interface gráfica do sistema, utilizando a biblioteca Tkinter. A camada Controller faz a intermediação entre a camada Model e View, controlando o fluxo de dados e eventos.

### Considerações finais

Este desafio visa explorar conceitos avançados de Programação Orientada a Objetos em Python, como persistência de objetos, exceptions, modelo MVC, fração e datetime. Ele oferece uma oportunidade de praticar esses conceitos em um contexto realista e aplicar suas habilidades de programação em um projeto completo.

**Observação:** Certifique-se de incluir os requisitos necessários para a execução do sistema, como a instalação das bibliotecas necessárias (por exemplo, o tkinter).

## Solução Implementada

A solução implementada para o problema segue os princípios da Programação Orientada a Objetos (POO) em Python. Utilizamos o padrão de arquitetura MVC para organizar o código, facilitando a manutenção e extensão do sistema. A persistência de objetos foi implementada usando o módulo `pickle`, garantindo que os dados sejam salvos entre diferentes execuções do programa. O uso de exceptions aprimora a robustez do sistema ao lidar com situações excepcionais.

### Arquivo principal: [`main.py`](main.py)

O arquivo `main.py` é responsável pela execução do sistema. Aqui, temos as classes `LimitePrincipal` e `ControlePrincipal`, representando a camada de View e Controller, respectivamente.

A classe `LimitePrincipal` cria a interface gráfica utilizando a biblioteca Tkinter. Ela configura a barra de menus com opções para cada entidade do sistema (Equipe, Piloto, Pista, Grande Prêmio, Tabelas, Sair, e Extra). Cada opção do menu está vinculada a um método do `ControlePrincipal`.

A classe `ControlePrincipal` inicializa as instâncias de controle para cada entidade (Equipe, Piloto, Pista, Grande Prêmio, Tabelas) e cria a instância da interface gráfica (`LimitePrincipal`). Além disso, ela possui métodos para chamar os métodos correspondentes de cada classe de controle, garantindo a comunicação adequada entre a camada de View e Model.

O método `salva` é responsável por salvar os dados do sistema antes de encerrar a execução. O método `resetarPontos` reinicia os pontos das equipes e pilotos.

```python
# Trecho final do arquivo main.py
if __name__ == '__main__':
    c = ControlePrincipal()
```

### Model do sistema: [`model.py`](model.py)

O arquivo `model.py` contém as classes que representam os principais objetos do sistema, como Piloto, Equipe, Pista, Resultado, Corrida e Grande Prêmio (GP). Essas classes encapsulam a lógica de negócio do sistema, oferecendo métodos para realizar operações como cadastro de resultados, consulta de informações, entre outras.

#### Classe Abstrata `Competidor`:

- Representa um competidor genérico, sendo a classe base para as classes `Equipe` e `Piloto`.
- Possui propriedades como nome, país e pontos.
- Oferece métodos para adicionar pontos e uma representação string genérica.

#### Classe `Equipe`:

- Herda de `Competidor` e representa uma equipe de Fórmula 1.
- Adiciona propriedades específicas, como chefe de equipe e motor.
- Possui uma representação string personalizada.

#### Classe `Piloto`:

- Herda de `Competidor` e representa um piloto de Fórmula 1.
- Adiciona propriedades específicas, como número e equipe.
- Possui uma representação string personalizada.

#### Classe `Pista`:

- Representa uma pista de corrida.
- Possui propriedades como nome, país, cidade e tamanho.
- Oferece uma representação string personalizada.

#### Classe `Resultado`:

- Representa o resultado de uma corrida para um piloto.
- Inclui informações como posição, se o piloto obteve a volta mais rápida, entre outros.
- Oferece uma representação string personalizada.

#### Classe `Corrida`:

- Representa uma corrida, contendo informações como horário de largada, número de voltas e resultados.
- Permite adicionar resultados e oferece uma representação string personalizada.

#### Classe `GP`:

- Representa um Grande Prêmio (GP), que consiste em uma pista, data de início e opções para corrida e sprint.
- Oferece uma representação string personalizada.

Essas classes fornecem a estrutura fundamental para o gerenciamento de resultados de corridas de Fórmula 1, encapsulando dados e comportamentos relevantes para cada entidade do sistema. A utilização de herança, propriedades e métodos específicos contribui para uma implementação modular e coesa.

### Controle de equipes: [`Menu/equipe.py`](Menu/equipe.py)

No módulo `equipe.py`, é implementada a interação entre a camada de View e Controller relacionada às equipes do sistema. As classes presentes neste arquivo gerenciam o cadastro, exibição e alteração de equipes. A seguir, são descritas as principais classes e métodos desse controle:

#### `LimiteCadastraEquipe`

Esta classe representa a interface gráfica para cadastrar equipes. Ela utiliza o módulo Tkinter para criar uma janela com campos de entrada e botões para realizar o cadastro.

- **Métodos Principais:**
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `LimiteMostraEquipes`

Esta classe é responsável por exibir uma lista de equipes em uma tabela na interface gráfica.

- **Métodos Principais:**
  - `__init__(equipes)`: Inicializa a interface gráfica com a lista de equipes fornecida.
  
#### `LimiteAlteraEquipe`

Essa classe cria uma janela que permite selecionar uma equipe para alteração e, em seguida, apresenta campos de entrada para modificar os dados da equipe escolhida.

- **Métodos Principais:**
  - `alteraEquipe(event)`: Método chamado ao selecionar uma equipe na combobox, que exibe os campos de alteração.
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `CtrlEquipe`

Esta classe é responsável pelo controle das operações relacionadas às equipes. Gerencia o cadastro, listagem, alteração e persistência de equipes.

- **Métodos Principais:**
  - `cadastrarEquipe()`: Inicia o processo de cadastro de uma nova equipe.
  - `enterHandlerEquipe(event)`: Método chamado ao pressionar o botão "Enter" na interface de cadastro, realiza o cadastro da equipe.
  - `clearHandlerEquipe(event)`: Limpa os campos de entrada na interface de cadastro.
  - `fechaHandlerEquipe(event)`: Fecha a janela de cadastro de equipes.
  - `listarEquipes()`: Exibe uma janela com a lista de equipes cadastradas.
  - `fechaHandlerAviso(event)`: Fecha a janela de aviso quando não há equipes cadastradas.
  - `salvaEquipes()`: Salva as equipes cadastradas em um arquivo.
  - `getNomesEquipes()`: Retorna uma lista com os nomes das equipes cadastradas.
  - `alterarEquipe()`: Inicia o processo de alteração de uma equipe existente.
  - `enterAlteraHandler(event)`: Método chamado ao pressionar o botão "Enter" na interface de alteração, realiza a alteração da equipe selecionada.
  - `fechaHandler(event)`: Fecha a janela de alteração de equipes.
  - `getListaEquipes()`: Retorna a lista de equipes cadastradas.
  - `getEquipe(nome)`: Retorna a instância de uma equipe com o nome fornecido.

### Controle de pilotos: [`Menu/piloto.py`](Menu/piloto.py)

O módulo `piloto.py` implementa o controle das operações relacionadas aos pilotos no sistema de gerenciamento de resultados de corridas de Fórmula 1. Abaixo estão descritas as principais classes e métodos desse controle:

#### `LimiteCadastroPiloto`

Essa classe representa a interface gráfica para cadastrar pilotos. Utiliza o módulo Tkinter para criar uma janela com campos de entrada e botões para realizar o cadastro.

- **Métodos Principais:**
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `LimiteMostraPilotos`

Esta classe é responsável por exibir uma lista de pilotos em uma caixa de texto na interface gráfica.

- **Métodos Principais:**
  - `__init__(pilotos)`: Inicializa a interface gráfica com a lista de pilotos fornecida.
  
#### `LimiteAlteraPiloto`

Cria uma janela que permite selecionar um piloto para alteração e, em seguida, apresenta campos de entrada para modificar os dados do piloto escolhido.

- **Métodos Principais:**
  - `alterarPiloto(event)`: Método chamado ao selecionar um piloto na combobox, que exibe os campos de alteração.
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `CtrlPiloto`

Responsável pelo controle das operações relacionadas aos pilotos. Gerencia o cadastro, listagem, alteração e persistência de pilotos.

- **Métodos Principais:**
  - `cadastrarPiloto()`: Inicia o processo de cadastro de um novo piloto.
  - `enterHandler(event)`: Método chamado ao pressionar o botão "Enter" na interface de cadastro, realiza o cadastro ou a alteração do piloto.
  - `clearHandler(event)`: Limpa os campos de entrada na interface de cadastro.
  - `fechaHandler(event)`: Fecha a janela de cadastro de pilotos.
  - `listarPilotos()`: Exibe uma janela com a lista de pilotos cadastrados.
  - `fechaListaHandler(event)`: Fecha a janela de listagem de pilotos.
  - `salvaPilotos()`: Salva os pilotos cadastrados em um arquivo.
  - `getNomesPilotos()`: Retorna uma lista com os nomes dos pilotos cadastrados.
  - `getListaPilotos()`: Retorna a lista de pilotos cadastrados.
  - `alterarPiloto()`: Inicia o processo de alteração de um piloto existente.
  - `enterAlteraHandler(event)`: Método chamado ao pressionar o botão "Enter" na interface de alteração, realiza a alteração do piloto selecionado.
  - `fechaAlteraHandler(event)`: Fecha a janela de alteração de pilotos.

### Controle de pistas: [`Menu/pista.py`](Menu/pista.py)

O módulo `pista.py` implementa o controle das operações relacionadas às pistas no sistema de gerenciamento de resultados de corridas de Fórmula 1. Abaixo estão descritas as principais classes e métodos desse controle:

#### `LimiteCadastraPista`

Essa classe representa a interface gráfica para cadastrar pistas. Utiliza o módulo Tkinter para criar uma janela com campos de entrada e botões para realizar o cadastro.

- **Métodos Principais:**
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `LimiteMostraPistas`

Esta classe é responsável por exibir uma lista de pistas em uma caixa de texto na interface gráfica.

- **Métodos Principais:**
  - `__init__(listaPistas)`: Inicializa a interface gráfica com a lista de pistas fornecida.

#### `CtrlPista`

Responsável pelo controle das operações relacionadas às pistas. Gerencia o cadastro, listagem e persistência de pistas.

- **Métodos Principais:**
  - `cadastrarPista()`: Inicia o processo de cadastro de uma nova pista.
  - `enterHandler(event)`: Método chamado ao pressionar o botão "Enter" na interface de cadastro, realiza o cadastro da pista.
  - `clearHandler(event)`: Limpa os campos de entrada na interface de cadastro.
  - `fechaHandler(event)`: Fecha a janela de cadastro de pistas.
  - `listarPistas()`: Exibe uma janela com a lista de pistas cadastradas.
  - `fechaListaHandler(event)`: Fecha a janela de listagem de pistas.
  - `salvaPistas()`: Salva as pistas cadastradas em um arquivo.

### Controle de GPs e suas corridas e sprints: [`Menu/GP.py`](Menu/GP.py)

Este módulo (`Menu/GP.py`) contém classes e métodos relacionados ao controle de Grandes Prêmios (GPs), suas corridas e sprints. Abaixo estão as principais classes e métodos fornecidos por este módulo.

#### `LimiteCriaGP(tk.Toplevel)`
Esta classe representa a interface gráfica para criar um novo GP. Possui campos para inserir o nome do GP, escolher uma pista e definir a data de início do GP. Além disso, oferece botões para cadastrar sprints, cadastrar corridas, cancelar e concluir.

- **Métodos:**
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `LimiteCadastraCorrida(tk.Toplevel)`
Representa a interface gráfica para cadastrar os resultados de uma corrida ou sprint em um GP. Permite selecionar os pilotos, registrar informações sobre a corrida (hora, voltas) e cadastrar os resultados dos pilotos.

- **Métodos:**
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.
  - `aumentaPosicao()`: Incrementa a posição do piloto a ser cadastrado.
  - `diminuiPosicao()`: Decrementa a posição do piloto a ser cadastrado.

#### `LimiteConsultaGP(tk.Toplevel)`
Essa classe fornece uma interface gráfica para buscar informações sobre um GP específico. Permite inserir um termo de busca e exibe os resultados encontrados.

- **Métodos:**
  - `mostraJanela(titulo, msg)`: Exibe uma janela pop-up com o título e a mensagem fornecidos.

#### `CtrlGP`
Esta classe é o controlador principal para as operações relacionadas a GPs, corridas e sprints. Possui métodos para cadastrar GPs, sprints, corridas, consultar GPs, cadastrar pilotos e gerenciar a pontuação.

- **Métodos:**
  - `cadastrarGP()`: Inicia o processo de cadastro de um novo GP.
  - `cadastrarSprint(event)`: Inicia o processo de cadastro de uma nova sprint.
  - `cadastrarCorrida(event)`: Inicia o processo de cadastro de uma nova corrida.
  - `cadastra()`: Realiza o cadastro de um GP.
  - `cancelaHandler(event)`: Manipula o cancelamento do cadastro do GP.
  - `concluiHandler(event)`: Conclui o cadastro do GP.
  - `consultarGP()`: Inicia o processo de consulta de um GP.
  - `cadastrarPiloto(event)`: Cadastra o resultado de um piloto em uma corrida ou sprint.
  - `getPilotos()`: Obtém a lista de pilotos disponíveis para cadastro.
  - `removePiloto(event)`: Remove o último piloto cadastrado.
  - `concluiCorridaHandler(event)`: Conclui o cadastro de resultados de uma corrida ou sprint.
  - `atribuiPontosSprint(Sprint)`: Atribui pontos aos pilotos e equipes em uma sprint.
  - `atribuiPontosCorrida(Corrida)`: Atribui pontos aos pilotos e equipes em uma corrida.
  - `cancelaCorridaHandler(event)`: Manipula o cancelamento do cadastro de resultados de uma corrida ou sprint.
  - `salvaGPs()`: Salva a lista de GPs em um arquivo.
  - `cancelaBuscaHandler(event)`: Manipula o cancelamento da busca de um GP.
  - `enterHandler(event)`: Realiza a busca de um GP com base no termo inserido.
  - `fechaConsultaHandler(event)`: Manipula o fechamento da janela de consulta.
  - `getListaGPs()`: Obtém a lista de GPs cadastrados.

### Exibição de tabelas: [`Menu/tabela.py`](Menu/tabela.py)

O módulo `Menu/tabela.py` é responsável pela exibição de tabelas de pilotos e construtores. Abaixo está uma breve descrição do código contido neste arquivo:

#### Classe `CompetidorTabela`

A classe `CompetidorTabela` é uma classe auxiliar utilizada para criar objetos que representam informações de pilotos ou construtores na tabela. Cada objeto desta classe possui atributos como número de vitórias, segundos lugares, terceiros lugares, voltas mais rápidas e sprints, associados ao respectivo competidor.

#### Classes `LimiteTabelaPilotos` e `LimiteTabelaConstrutores`

Essas classes são responsáveis pela criação de janelas de exibição das tabelas de pilotos e construtores, respectivamente. Elas utilizam a biblioteca tkinter para criar interfaces gráficas. As tabelas são exibidas usando o widget `ttk.Treeview`, e os dados são preenchidos com informações relevantes sobre pilotos ou construtores.

#### Classe `CtrlTabela`

A classe `CtrlTabela` contém métodos para exibir as tabelas de pilotos e construtores. O método `exibirTabelaPilotos` cria uma tabela de pilotos com base nas informações disponíveis, enquanto `exibirTabelaConstrutores` cria uma tabela de construtores. O método `ordenaEmpate` é utilizado para lidar com empates nas posições da tabela.

Esperamos que essas informações forneçam uma compreensão clara de como o módulo `Menu/tabela.py` funciona e como ele é integrado ao seu projeto.

### Cadastros

Por enquanto, estão cadastrados em [`Cadastros`](/Cadastros/):
- Todos os pilotos e equipes que participaram da temporada de 2021;
- Cinco pistas:
    - Bahrain;
    - Ímola;
    - Portimão;
    - Barcelona;
    - Interlagos;
- Os 3 primeiros GPs da temporada com os resultados das corridas.
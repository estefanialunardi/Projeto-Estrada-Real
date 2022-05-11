![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://github.com/estefanialunardi/Projeto-Estrada-Real/blob/main/PROJETO%20ESTRADA%20REAL.ipynb)
<img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=whitehttps://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=whitee" />
<img src="https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white" />

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/estefanialunardi/) 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/estefanialunardi/projeto-estrada-real/main/estrada_real.py)

# Para onde ir na Estrada Real?
<img src="https://apps.streamlitusercontent.com/estefanialunardi/projeto-estrada-real/main/estrada_real.py/+/media/839aa942db04b67bf22ed6cf4e237c352b0dfe845094f2b6e3ab1ea9.jpeg" />
Com mais de 1600km de extensão total, a Estrada Real é a maior rota turística do Brasil. São 245 municípios dos estados de Minas Gerais, Rio de Janeiro e São Paulo, por onde passavam os percursos delegados pela Coroa Portuguesa para o transporte de ouro e diamantes mineiros até os portos cariocas. Esses trajetos foram divididos em quatro trilhas oficiais: Caminho Velho, Caminho Novo, Caminho dos Diamantes e Caminho do Sabarabuçu. Hoje, esses roteiros são destinos polivalentes com características múltiplas, com opções de turismo cultural, religioso, gastronômico e ecoturismo. Para escolher os destinos, dentre as centenas de opções da Estrada, é fundamental alinhar as preferências de viagem e perfil do turista, tempo disponível e meio de locomoção com a vocação turística de cada município e com as características específicas dos trajetos a serem percorridos.

Este projeto busca trazer informações dos percursos e municípios da Estrada Real, favorecendo a escolha racional dos destinos de viagem, bem como dos melhores trechos a serem percorridos com diferentes opções de locomoção, a partir dos objetivos do turista.

## ETL
### Bibliotecas utilizadas
<table>
    <tr>
        <td>Beautifulsoup4</td>
        <td>Requests</td>
        <td>Pandas</td>
        <td>Lxml</td>
<td>Selenium</td>
    </tr>
     <tr>
        <td>Time</td>
      <td>SQLAlchemy</td>
        <td>Plotly</td>
        <td>Pymysql</td>
        <td>Streamlit</td>
    </tr>
</table>


### Métodos
#### Extração:
<img src="https://user-images.githubusercontent.com/101064720/167266423-adec1e73-3876-4d66-9f5e-1ea7deb71da0.PNG" width="350" align="right">

Para a extração dos dados da internet, foram utilizadas métodos de web scraping para coletar dados-chave sobre os destinos da Estrada Real.
As tabelas com informações regionais (tabela_micro_meso_mg etabelas_micro_municipio_mg) foram extraídas de duas tabelas em página única da Wikipedia, utilizando a biblioteca Beautiful Soup.

Para extrair os dados do site do Instituto Estrada Real foram criadas rotinas para navegação automatizada com a biblioteca Selenium de diversas páginas diferentes do site. Como o site utiliza o mesmo formato de página para informações da mesma natureza, foi possível aplicar funções para extrair os dados sobre diferentes destinos.
Foram utilizados três modelos de página do site do Instituto para criar quatro tabelas. A tabela "caminhos" foi criada a partir da página com informações específicas do caminho, que além das informações gerais dessa trilha (como início, fim e distância), possibilitou extrair uma lista de links para páginas com informações de cada município parte do destino, como número de habitantes e vocação turística (de onde foram retirados os dados da tabela "cidades".
<img src="https://user-images.githubusercontent.com/101064720/167266476-29e9f975-50fd-461c-87c2-e4ba9dd87056.PNG" width="350" align="right">

Dessas mesmas páginas com dados sobre as cidades, foi gerado um dicionário com todas as atrações turísticas da Estrada Real, por município - que foi convertido na tabela "pontos_turisticos". Finalmente, para a tabela "roteiros" foram utilizadas os dados específicos de cada trecho, nas páginas com Roteiros Planilhados. 

Para extração das informações sobre hoteis que aceitem animais nos destinos da Estrada Real, foi necessário desabilitar o JavaScript para possibilitar a navegação automatizada. Com isso, todos os filtros de pesquisa (que normalmente são selecionados por objetos dinâmicos/interativos) precisaram ser definidos a priori, para armazenamento das preferências de pesquisa ainda no endereço URL, alterando apenas o nome do município no campo específico do caminho HTML a partir de iteração da tabela de cidade.
#### Transformação:
De maneira geral, os dados foram extraídos de forma objetiva e com bastante qualidade, já com a preocupação de extrair o dado no formato mais provavelmente adequado para a análise, sem qualquer valor nulo e com pouquíssima necessidade de limpeza. Pontualmente, foi utilizada o método .loc seguido do ".replace()" para correção de pequenas incorreções, erros de digitação ou informações desviantes (por diferenças na padronização da alimentação de alguns dados nos sites fonte). Para facilitar a leitura e trabalho com os dados, foram utilizados métodos de padronização de valores em massa(.lower(), .strip(), .replace(), etc.).

#### Carregamento:
Todos os dados foram carregados e armazenados em uma database no MySQL, utilizando as bibliotecas SQLAlchemy e Pymysql para conexão com a ferramenta de banco de dados e da biblioteca Pandas para envio das tabelas ("pandas.DataFrame.to_sql").

 #### Apresentação:
<figure class="gif">
            <img src="https://user-images.githubusercontent.com/101064720/167270079-369f2b09-023e-4f5d-98a9-41dcd73241e4.gif" width="400" align="right">
      </figure>
O conteúdo, de texto e de dados, foi preparado no Visual Studio Code, com código em Python puro para ser apresentado em uma aplicação Web utilizando a biblioteca Streamlit. Além da análise dos dados, o usuário tem acesso a todas as informações de bibliotecas e métodos utilizados nesse projeto.

      
#### Sistema de recomendações:
Foi desenvolvido um sistema de recomendações de viagem com filtragem baseada em conteúdo, a partir das preferência e perfil de viagem que o usuário informa. 
Ele considera o tempo, meio de locomoção, preferências de destino turístico e a necessidade de acomodar pets e, então, calcula a similaridade dos atributos entre os caminhos e recomenda um destino.


## Análise dos dados
### Extensão dos caminhos
O caminho mais extenso da Estrada Real é o Caminho Velho, com 710km e 27 rotas. Os caminhos Novo e dos Diamantes têm a mesma quantidade de rotas: 18. Entretanto, o Caminho Novo conta com 515km de extensão contra 395 dos Diamantes. O caminho do Sabarabuçu é o menor, com apeas 6 rotas e uma distância total de 160 km.

A extensão dos caminhos deve ser considerada em todas as análises quantitativas, com atenção especial para as proporções.

## Destinos por vocação turística
<img src="https://user-images.githubusercontent.com/101064720/167267104-ccafbfc4-00a0-4986-a980-a6ad67849f28.png" width="300" align="left">
Em todos os caminhos da Estrada Real, é possível encontrar opções de turismo que valorizem as tradições e a cultura, a gastronomia, o meio ambiente ou a religião. Entretanto, alguns destinos têm mais alternativas para quem busca determinados tipos de atividade em sua viagem. Para quem busca contato com a natureza, boa notícia: todos os municípios da Estrada Real têm opções de ecoturismo ou turismo de aventura. Já para os turistas procurando alternativas de turismo gastronômico, o Caminho Velho traz 51 municípios com essa vocação: 48% do total. Já o Caminho do Sabarabuçu tem opções de turismo gastronômico em metade das cidades: 6 municípios da rota. No Caminho dos diamantes, são 17 cidades (26%) com essa vocação. E no Caminho Novo são 18 munícipios com essas alternativas (27%) Se o objetivo for religioso, o viajante encontra igrejas, artes sacras e festas religiosas em 9 das 12 cidades do Caminho do Sabarabuçu (75%). Muitas opções também em 45 cidades do Caminho dos Diamantes (69%). No Caminho novo há 36 cidades com essa vocação (54%) e no Caminho Velho, 48 municípios (45%). Finalmente, quem busca turismo cultural e histórico vai encontrar em 91% dos destinos do Caminho do Sabarabuçu (em 11 das 12 cidades).No caminho Novo, 45 municípios tem casarões, museus ou patrimônio histórico em geral (68%). No Caminho dos Diamantes 60% dos destinos oferecem alguma dessas opções. E no Caminho Velho, em 51 cidades (48%) há atrações turísticas voltadas para a cultura, história e valorização das tradições.

## Destinos Pet Friendly
Para quem vai viajar com pet, é fundamental encontrar uma hospedagem preparada para receber seu amiguinho. Existem acomodações pet friendly em todos os caminhos. Em 16 dos 65 municípios do Caminho dos Diamantes (24%), há hoteis que declararam aceitar animais na hospedagem. Mesmo número de cidades preparadas para receber os peludos no Caminho novo: 16 dos 66 municípios. Já no Caminho Velho, existem 43 cidades com hospedagem garantida para os pequenos: isso corresponde a 40,5% dos 106 municípios do trajeto. Já Sabarabuçu é, proporcionalmente, o caminho mais preparado para os pets: 41,6% dos 12 municípios tem opções de pouso para quem está com animais de estimação
![newplot (1)](https://user-images.githubusercontent.com/101064720/167267108-c6925654-8cb9-4781-bdeb-a2800e128b94.png)


## Para quem vai de bicicleta ou a pé
<img src="https://user-images.githubusercontent.com/101064720/167267116-49e3f981-5082-4894-bfae-f4d7954db66c.png" width="350" align="left">
Dos 395km do Caminho dos Diamantes, quase 3/4 das estradas são de terra (73,5%), 26% são de asfalto e apenas meio porcento de trilha, no trecho que vai de Santa Bárbara à Catas Altas.

Já no Caminho novo, 32% dos 515 km são de asfalto, 5% são de trilhas e os 63% restantes são de estrada de terra.

O caminho velho tem 82,5% de estradas de terra, 11,5% de asfalto e 6% de trilhas.

No menor caminho, Sabarabuçu, a maior proporção de trilhas: 22,5% do total. Os outros 82% são de estrada de terra.

<img src="https://user-images.githubusercontent.com/101064720/167267146-d67a1c6a-acdf-4c9d-8505-3e88ed881286.png" width="300" align="right">

### Dificuldade de caminhada
O grau de dificuldade física é medido de 1 a 5, sendo 5 o que mais exige do caminhante. Para realizar este cálculo, são considerados a quilometragem total do trecho, a parte do percurso em subidas (e sua inclinação média), descidas e a quantidade de sombras. O Caminho Velho tem uma média mais baixa de dificuldade física (3.29) e o Caminho Novo é o mais exigente (3.72). Sabarabuçu e Caminho dos Diamantes têm média de 3.5.


### Dificuldade para ciclistas
<img src="https://user-images.githubusercontent.com/101064720/167267147-b03c59ce-6082-4333-86e8-a5c9b3e6104b.png" width="300" align="right">
O grau de dificuldade técnica se assemelha ao de dificuldade física, inclusive utilizando a mesma escala. Além dos dados para caminhada, considera o espaço para passar com a bicicleta e condições gerais da trilha. O Caminho dos Diamantes tem uma média mais baixa de dificuldade física (3.77) e o Caminho Novo divide com o Sabarabuçu o posto de mais exigentes (4.5). O caminho velho têm média de 3.92.





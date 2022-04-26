O projeto:
Com mais de 1600km de extensão total, a Estrada Real é a maior rota turística do Brasil. São 245 municípios dos estados de Minas Gerais, Rio de Janeiro e São Paulo, por onde passavam os percursos delegados pela Coroa Portuguesa para o transporte de ouro e diamantes mineiros até os portos cariocas. Esses trajetos foram divididos em quatro trilhas oficiais: Caminho Velho, Caminho Novo, Caminho dos Diamantes e Caminho do Sabarabuçu. Hoje, esses roteiros são destinos polivalentes com características múltiplas, com opções de turismo cultural, religioso, gastronômico e ecoturismo.

Para escolher os destinos, dentre as centenas de opções da Estrada, é fundamental alinhar as preferências de viagem e perfil do turista, tempo disponível e meio de locomoção com a vocação turística de cada município e com as características específicas dos trajetos a serem percorridos.

Este projeto busca trazer informações dos percursos e municípios da Estrada Real, favorecendo a escolha racional dos destinos de viagem, bem como dos melhores trechos a serem percorridos com diferentes opções de locomoção, a partir dos objetivos do turista. 


Bibliotecas:
Beautifulsoup4
Requests
Pandas as
Lxml
Selenium 
Time
SQLAlchemy
Pymysql

Fontes de dados
Wikipedia - Lista de mesorregiões e microrregiões de Minas Gerais
tabela_micro_meso_mg
tabelas_micro_municipio_mg

Instituto Estrada Real
caminhos_df
estrada_real_df
pontos_turisticos_df
roteiros_df

Hoteis.com
hoteis_pet_friendly_df


Métodos:

Extração
Para a extração dos dados da internet, foram utilizadas métodos de web scraping para coletar dados-chave sobre os destinos da Estrada Real. 

As tabelas com informações regionais (tabela_micro_meso_mg etabelas_micro_municipio_mg) foram extraídas de duas tabelas em página única da Wikipedia, utilizando a biblioteca Beautiful Soup.

Para extrair os dados do site do Instituto Estrada Real (caminhos_df, estrada_real_df, pontos_turisticos_df, roteiros_df) foram criadas rotinas para navegação automatizada com a biblioteca Selenium de diversas páginas diferentes do site. Como o site utiliza o mesmo formato de página para informações da mesma natureza, foi possível aplicar funções para extrair os dados sobre diferentes destinos.

Foram utilizados três modelos de página do site do Instituto para criar quatro tabelas. A tabela "caminhos" foi criada a partir da página com informações específicas do caminho, que além das informações gerais dessa trilha (como início, fim e distância), possibilitou extrair uma lista de links para páginas com informações de cada município parte do destino, como número de habitantes e vocação turística (de onde foram retirados os dados da tabela "cidades". Dessas mesmas páginas com dados sobre as cidades, foi gerado um dicionário com todas as atrações turísticas da Estrada Real, por município - que foi convertido na tabela "pontos_turisticos". Finalmente, para a tabela "roteiros" foram utilizadas os dados específicos de cada trecho, nas páginas com Roteiros Planilhados.

Finalmente, para extração das informações sobre hoteis que aceitem animais nos destinos da Estrada Real, foi necessário desabilitar o JavaScript para possibilitar a navegação automatizada. Com isso, todos os filtros de pesquisa (que normalmente são selecionados por objetos dinâmicos/interativos) precisaram ser definidos a priori, para armazenamento das preferências de pesquisa ainda no endereço URL, alterando apenas o nome do município no campo específico do caminho HTML a partir de iteração da tabela de cidade. 


Transformação
De maneira geral, os dados foram extraídos de forma objetiva e com bastante qualidade, já com a preocupação de extrair o dado no formato mais provavelmente adequado para a análise, sem qualquer valor nulo e com pouquíssima necessidade de limpeza. Pontualmente, foi utilizada o método .loc seguido do ".replace()" para correção de pequenas incorreções, erros de digitação ou informações desviantes (por diferenças na padronização da alimentação de alguns dados nos sites fonte). Para facilitar a leitura e trabalho com os dados, foram utilizados métodos de padronização de valores em massa(.lower(), .strip(), .replace(), etc.). 

Carregamento
Todos os dados foram carregados e armazenados em uma database no MySQL, utilizando as bibliotecas SQLAlchemy e Pymysql para conexão com a ferramenta de banco de dados e da biblioteca Pandas para envio das tabelas ("pandas.DataFrame.to_sql").


 















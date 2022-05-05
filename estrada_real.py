import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from PIL import Image


st.title('Para onde ir na Estrada Real?')
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    st.image(('https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54'), width=60)
with col2:
    st.image(('https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white'), width=60)
with col3:
    st.image(('https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white'), width=60)
with col4:
    st.image(('https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=whitehttps://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white'), width=60)
with col5:
    st.image(('https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white'), width=60)
with col6:
    st.image(('https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white'), width=60)
with col7:
    st.image(('https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white'), width=120)
        
st.image(('passaporte-estrada-real (11).jpg'))
st.write('''Com mais de 1600km de extensão total, a Estrada Real é a maior rota turística do Brasil. São 245 municípios dos estados de Minas Gerais, Rio de Janeiro e São Paulo, por onde passavam os percursos delegados pela Coroa Portuguesa para o transporte de ouro e diamantes mineiros até os portos cariocas. Esses trajetos foram divididos em quatro trilhas oficiais: Caminho Velho, Caminho Novo, Caminho dos Diamantes e Caminho do Sabarabuçu. Hoje, esses roteiros são destinos polivalentes com características múltiplas, com opções de turismo cultural, religioso, gastronômico e ecoturismo.

Para escolher os destinos, dentre as centenas de opções da Estrada, é fundamental alinhar as preferências de viagem e perfil do turista, tempo disponível e meio de locomoção com a vocação turística de cada município e com as características específicas dos trajetos a serem percorridos.

Este projeto busca trazer informações dos percursos e municípios da Estrada Real, favorecendo a escolha racional dos destinos de viagem, bem como dos melhores trechos a serem percorridos com diferentes opções de locomoção, a partir dos objetivos do turista. ''')

caminhos = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\caminhos.csv')
cidades = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\cidades.csv')
pontos_turisticos = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\pontos_turisticos.csv')
roteiros = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\roteiros.csv')
hoteis_pet_friendly = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\hoteis_pet_friendly.csv')
micro_mesorregioes_mg = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\micro_mesorregioes_mg.csv')
micro_municipios_mg = pd.read_csv('C:\\Users\\Tete\\Curso - DA\\Estrada Real\\data\\micro_municipios_mg.csv')


st.sidebar.markdown('#### Escolha seu destino')
cam_dia=0
cam_nov=0
cam_vel=0
cam_sab=0
duracao = st.sidebar.slider('Qual a duração da sua viagem?', min_value=2, max_value=30)
if duracao < 2:
    cam_dia+=6
    cam_nov+=4
    cam_vel+=2
    cam_sab+=8
elif duracao < 4:
    cam_dia+=8
    cam_nov+=4
    cam_vel+=4
    cam_sab+=4
elif duracao < 6:
    cam_dia+=6
    cam_nov+=8
    cam_vel+=6
    cam_sab+=2
else:
    cam_dia+=4
    cam_nov+=6
    cam_vel+=8
    cam_sab+=2
transporte = st.sidebar.selectbox('Qual o meio de transporte?', ('Carro', 'Ônibus','Moto','Cavalo','Bicicleta','A pé'))
if transporte == 'Carro' or transporte == 'Ônibus'or transporte == 'Moto':
    pass
elif transporte == 'Cavalo' or transporte == 'Bicicleta':
    dificuldade_bike = st.sidebar.slider ('Qual grau de dificuldade de trilhas você busca?', min_value=1, max_value=5)
    if dificuldade_bike <2:
        cam_dia+=3
        cam_nov+=1
        cam_vel+=2
        cam_sab+=1
    elif dificuldade_bike <3:
        cam_dia+=2
        cam_nov+=1
        cam_vel+=2
        cam_sab+=1
    elif dificuldade_bike <4:
        cam_dia+=1
        cam_nov+=3
        cam_vel+=2
        cam_sab+=3
    else:
        cam_dia+=1
        cam_nov+=4
        cam_vel+=2
        cam_sab+=4
elif transporte == 'A pé':
    dificuldade_pe = st.sidebar.slider ('Qual grau de dificuldade de trilhas você busca?', min_value=1, max_value=5)
    if dificuldade_pe <2:
        cam_dia+=2
        cam_nov+=1
        cam_vel+=3
        cam_sab+=2
    elif dificuldade_pe <3:
        cam_dia+=2
        cam_nov+=1
        cam_vel+=2
        cam_sab+=2
    elif dificuldade_pe <4:
        cam_dia+=3
        cam_nov+=4
        cam_vel+=2
        cam_sab+=3
    else:
        cam_dia+=3
        cam_nov+=4
        cam_vel+=1
        cam_sab+=3
turismo = st.sidebar.multiselect('Que atrações você deseja?', ('Ecoturismo e Turismo de Aventura','Turismo Cultural e Histórico', 'Turismo Gastronômico', 'Turismo Religioso'))
if 'Ecoturismo e Turismo de Aventura' in turismo:
    cam_dia+=2
    cam_nov+=2
    cam_vel+=3
    cam_sab+=1
if 'Turismo Cultural e Histórico' in turismo:
    cam_dia+=3
    cam_nov+=4
    cam_vel+=1
    cam_sab+=2
if 'Turismo Gastronômico' in turismo:
    cam_dia+=2
    cam_nov+=3
    cam_vel+=4
    cam_sab+=1
if 'Turismo Religioso' in turismo:
    cam_dia+=4
    cam_nov+=2
    cam_vel+=3
    cam_sab+=2
pets = st.sidebar.radio(
     "Precisa de hospedagem para pets?",
     ('Sim', 'Não'))
if pets == "Sim":
    cam_dia+=1
    cam_nov+=2
    cam_vel+=4
    cam_sab+=4
else:
    pass
if cam_dia > cam_nov and cam_dia > cam_vel and cam_dia > cam_sab:
    st.sidebar.info('Considere conhecer o Caminho dos Diamantes')
elif cam_dia < cam_nov and cam_nov > cam_vel and cam_nov > cam_sab:
    st.sidebar.info('Considere conhecer o Caminho Novo')
elif cam_dia < cam_sab and cam_sab > cam_vel and cam_nov < cam_sab:
    st.sidebar.info('Considere conhecer o Caminho Sabarabuçu')
elif cam_dia < cam_vel and cam_sab < cam_vel and cam_nov < cam_vel:
    st.sidebar.info('Considere conhecer o Caminho Velho')
else:
    st.sidebar.info('Que tal conhecer todos os roteiros?')



st.markdown('## ETL')
cola, colb, colc = st.columns(3)
with cola:
    checkbox_bibliotecas = st.checkbox('Bibliotecas utilizadas')
if checkbox_bibliotecas:
    st.markdown('### Bibliotecas utilizadas:')
    st.markdown(''' 
        - Beautifulsoup4
        - Requests
        - Pandas
        - Lxml
        - Selenium 
        - Time
        - SQLAlchemy
        - Pymysql ''')
with colb:
    checkbox_metodos = st.checkbox('Métodos')
if checkbox_metodos:
    st.markdown('#### Métodos')
    st.markdown('''         __* Extração: *__

        Para a extração dos dados da internet, foram utilizadas métodos de web scraping para coletar dados-chave sobre os destinos da Estrada Real. 

        As tabelas com informações regionais (tabela_micro_meso_mg etabelas_micro_municipio_mg) foram extraídas de duas tabelas em página única da Wikipedia, utilizando a biblioteca Beautiful Soup.

        Para extrair os dados do site do Instituto Estrada Real foram criadas rotinas para navegação automatizada com a biblioteca Selenium de diversas páginas diferentes do site. Como o site utiliza o mesmo formato de página para informações da mesma natureza, foi possível aplicar funções para extrair os dados sobre diferentes destinos.

        Foram utilizados três modelos de página do site do Instituto para criar quatro tabelas. A tabela "caminhos" foi criada a partir da página com informações específicas do caminho, que além das informações gerais dessa trilha (como início, fim e distância), possibilitou extrair uma lista de links para páginas com informações de cada município parte do destino, como número de habitantes e vocação turística (de onde foram retirados os dados da tabela "cidades". Dessas mesmas páginas com dados sobre as cidades, foi gerado um dicionário com todas as atrações turísticas da Estrada Real, por município - que foi convertido na tabela "pontos_turisticos". Finalmente, para a tabela "roteiros" foram utilizadas os dados específicos de cada trecho, nas páginas com Roteiros Planilhados.
        Finalmente, para extração das informações sobre hoteis que aceitem animais nos destinos da Estrada Real, foi necessário desabilitar o JavaScript para possibilitar a navegação automatizada. Com isso, todos os filtros de pesquisa (que normalmente são selecionados por objetos dinâmicos/interativos) precisaram ser definidos a priori, para armazenamento das preferências de pesquisa ainda no endereço URL, alterando apenas o nome do município no campo específico do caminho HTML a partir de iteração da tabela de cidade. 

        __* Transformação: *__

        De maneira geral, os dados foram extraídos de forma objetiva e com bastante qualidade, já com a preocupação de extrair o dado no formato mais provavelmente adequado para a análise, sem qualquer valor nulo e com pouquíssima necessidade de limpeza. Pontualmente, foi utilizada o método .loc seguido do ".replace()" para correção de pequenas incorreções, erros de digitação ou informações desviantes (por diferenças na padronização da alimentação de alguns dados nos sites fonte). Para facilitar a leitura e trabalho com os dados, foram utilizados métodos de padronização de valores em massa(.lower(), .strip(), .replace(), etc.). 

        __* Carregamento: *__

        Todos os dados foram carregados e armazenados em uma database no MySQL, utilizando as bibliotecas SQLAlchemy e Pymysql para conexão com a ferramenta de banco de dados e da biblioteca Pandas para envio das tabelas ("pandas.DataFrame.to_sql").
        ''')

with colc:
    checkbox_dados = st.checkbox('Dados extraídos')
if checkbox_dados:
    dados = st.multiselect('Quais dados você gostaria de acessar?',
    ['Todos os Dados Disponíveis', 'Dados dos Caminhos','Dados das Cidades','Dados dos Roteiros', 'Dados dos Pontos Turísticos', 'Dados dos Hoteis Pet Friendly', 'Dados das Mesorregiões de MG', 'Dados das Microrregiões de MG'])
try: 
    if 'Todos os Dados Disponíveis' in dados:
        st.write(caminhos)
        st.write(cidades)
        st.write(roteiros)
        st.write(pontos_turisticos)
        st.write(hoteis_pet_friendly)
        st.write(micro_mesorregioes_mg)
        st.write(micro_municipios_mg)
except:
    pass
try: 
    if 'Dados dos Caminhos' in dados:
        st.write(caminhos)
except:
    pass
try: 
    if 'Dados das Cidades' in dados:
        st.write(cidades)
except:
    pass
try: 
    if 'Dados dos Roteiros' in dados:
        st.write(roteiros)
except:
    pass
try: 
    if 'Dados dos Pontos Turísticos' in dados:
        st.write(pontos_turisticos)
except:
    pass
try: 
    if 'Dados dos Hoteis Pet Friendly' in dados:
        st.write(hoteis_pet_friendly)
except:
    pass
try: 
    if 'Dados das Mesorregiões de MG' in dados:
     st.write(micro_mesorregioes_mg)
except:
    pass
try: 
    if 'Dados das Microrregiões de MG' in dados:
        st.write(micro_municipios_mg)
except:
    pass


st.markdown('## Análise dos dados')
with st.expander("Veja a análise"):
    col1extensao, col2extensao = st.columns(2)
    with col1extensao: 
        st.markdown(''' ''')
        st.markdown('### Extensão dos caminhos')
        st.markdown(''' O caminho mais extenso da Estrada Real é o Caminho Velho, com 710km e 27 rotas. \n  Os caminhos Novo e dos Diamantes têm a mesma quantidade de rotas: 18. \n Entretanto, o Caminho Novo conta com 515km de extensão contra 395 dos Diamantes. \n O caminho do Sabarabuçu é o menor, com apeas 6 rotas e uma distância total de 160 km. \n\n A extensão dos caminhos deve ser considerada em todas as análises quantitativas, com atenção especial para as proporçõnes''')
    with col2extensao:
        st.markdown(''' ''')
        #mapa_estrada = Image.open('fd7098cd46c2858f9e4065447343ef3f.png')
        st.image(mapa_estrada, width=250)

    st.markdown('### Destinos por vocação turística')
    pontos_turisticos_dict = {'Acaiaca': ['Estação Ferroviária'], 'Alvinópolis': ['Igreja Matriz de Nossa Senhora do Rosário'], 'Alvorada de Minas': ['Cachoeira da Campina','Igreja Matriz Santo Antônio','Mirante da Escadinha'],
 'Barão de Cocais': ['Cachoeira Cocais',
  'Cachoeira da Cambota',
  'Cruzeiro das Almas',
  'Santuário de São João Batista'],
 'Barra Longa': [],
 'Bela Vista de Minas': ['Cachoeira do Taquaril'],
 'Bento Rodrigues': [],
 'Bom Jesus do Amparo': ['Igreja Matriz Bom Jesus do Amparo'],
 'Camargos': [],
 'Carmésia': [],
 'Catas Altas': ['Aqueduto Bicame de Pedra',
  'Banho do Belchior',
  'Capela Santa Quitéria',
  'Caraça Bier Fest - Catas Altas',
  'Igreja de Nossa Senhora do Rosário',
  'Igreja Matriz de Nossa Senhora da Conceição',
  'Pico de Catas Altas',
  'Pico do Baiano'],
 'Cocais': ['Fazenda da Estalagem',
  'Igreja de Nossa Senhora do Rosário',
  "Igreja de Sant'Anna",
  'Sitio Arqueológico Pedra Pintada',
  'Sobrado do Cartório'],
 'Conceição do Mato Dentro': ['Balneário Córrego do Baú',
  'Balneário  Piscina de Água Quente',
  'Cachoeira do Tabuleiro',
  'Cachoeira Rabo de Cavalo',
  'Cachoeira Três Barras',
  'Fubá Suado - Conceição do Mato Dentro',
  'Igreja Matriz de Nossa Senhora da Aparecida',
  'Igreja Matriz de Nossa Senhora da Conceição'],
 'Congonhas do Norte': ['Cachoeira da Barragem (do Levi)'],
 'Corregos': [],
 'Couto de Magalhães de Minas': ['Água Santa',
  'Cachoeira da Fábrica',
  'Cachoeira dos Vaqueiros',
  'Cachoeira do Tomé',
  'Capela Senhor de Bom Jesus de Matozinhos',
  'Igreja Nossa Senhora da Conceição',
  'Pinturas Rupestres'],
 'Datas': ['Igreja Matriz do Divino Espírito Santo',
  'Lapa Pintada',
  'Morango - Datas'],
 'Diamantina': ['Cachoeira das Fadas',
  'Cachoeira da Toca',
  'Cachoeira dos Cristais',
  'Cachoeira dos Remédios',
  'Cachoeira do Telésforo',
  'Caminho dos Escravos',
  'Capela Imperial de Nossa Senhora do Amparo',
  'Casa da Chica da Silva'],
 'Dom Joaquim': ['APA Gameleira', 'Complexo Turístico da Barragem'],
 'Dores de Guanhães': ['Cachoeira da Guarda', 'Cachoeira do Sabiá'],
 'Felício dos Santos': ['Cachoeira do Palmito',
  'Igreja Dona Izabel',
  'Igreja Sagrado Coração de Jesus',
  'Lajeado do Noronha'],
 'Ferros': [],
 'Gouveia': ['Ampar Barão Capivara',
  'Cachoeira Capivara',
  'Cachoeira do Cuiabá',
  'Cachoeira Engenho',
  'Igreja Matriz de Santo Antônio',
  'Igreja Nossa Senhora das Dores',
  'Rio Capivara',
  'Serra do Pasmarra'],
 'Guanhães': ['Casa de Cultura Laet Berto',
  'Igreja Matriz de São Miguel e Almas',
  'Parque Estadual Serra da Candonga'],
 'Ipoema': ['Cachoeira Alta',
  'Cachoeira do Meio',
  'Cachoeira do Patrocínio Amaro',
  'Igreja de Nossa Senhora da Conceição',
  'Mirante Morro Redondo',
  'Museu do Tropeiro - Ipoema',
  'Parque Estadual Mata do Limoeiro'],
 'Itabira': ['Capela de São José',
  'Igreja Nossa Senhora do Rosário dos Pretos',
  'Memorial Carlos Drummond de Andrade',
  'Pico do Amor',
  'Reserva da Biosfera da Serra do Espinhaço'],
 'Itambé do Mato Dentro': ['Cachoeira das Crioulas',
  'Cachoeira da Serenata',
  'Cachoeira da Vitória',
  'Cachoeira do Funil',
  'Cachoeira do Lúcio',
  'Cânion da Serenata',
  'Festival da Banana - Itambé do Mato Dentro',
  'Igreja Matriz Nossa Senhora das Oliveiras'],
 'Itapanhoacanga': [],
 'Jaboticatubas': ['Cachoeira do Sr. Dimas',
  'Fazenda do Cipó',
  'Igreja Matriz Nossa Senhora da Conceição',
  'Igreja Matriz Nossa Senhora do Rosário',
  'Pequi - Jaboticatubas',
  'Serra do Bené'],
 'João Monlevade': [],
 'Lagoa Santa': ['Gruta da Lapinha', 'Lagoa do Sumidouro'],
 'Lapinha da Serra': ['Vale do Soberbo'],
 'Mariana': ['Cachoeira do Brumado',
  'Cachoeira Matadouro',
  "Capela de Sant'Anna",
  'Catedral da Sé',
  'Estação Ferroviária',
  'Igreja Nossa Senhora da Boa Morte',
  'Igreja Nossa Senhora das Mercês',
  'Igreja Nossa Senhora do Carmo'],
 'Milho Verde': ['Cachoeira do Carijó',
  'Cachoeira do Moinho',
  'Chafariz da Goiabeira',
  'Igreja do Rosário',
  'Rio Jequitinhonha'],
 'Monjolos': ['Cachoeira do Bueno'],
 'Morro D´Agua Quente': [],
 'Morro do Pilar': ['Cachoeira das Pedras',
  'Cachoeira do Lageado',
  'Cachoeira do Pica Pau',
  'Cachoeira do Tombo',
  'Igreja do Canga',
  'Monumento Intendente Câmara',
  'Óleo de Indaiá - Morro do Pilar',
  'Quintais e Quitandas - Morro do Pilar'],
 'Nova União': [],
 'Ouro Preto': ['Cachaças - Ouro Preto',
  'Capela de Nossa Senhora da Piedade',
  'Capela de Nossa Senhora das Dores do Monte Calvário',
  'Capela de Santana',
  'Capela de São João Batista',
  'Casa da Câmara',
  'Casa de Thomaz Antônio Gonzaga',
  'Casa dos Contos'],
 'Passabém': ['Igreja Matriz de São José'],
 'Ponte Nova': ['Cachoeira do Vau Açu',
  'Carne de porco - Ponte Nova',
  'Queijos - Ponte Nova'],
 'Presidente Kubitschek': ['Cachoeira da Paca',
  'Cachoeira do Guaribas',
  'Cachoeira do Laércio',
  'Cachoeira do Tamanduá',
  'Cânion do Funil',
  'Capela Nossa Senhora de Fátima',
  'Cascata Ananias',
  'Igreja de Nossa Senhora das Dores'],
 'Rio Piracicaba': [],
 'Sabinópolis': ['Igreja de Nossa Senhora do Rosário',
  'Igreja Matriz de São Sebastião'],
 'Santa Bárbara': ['Antiga Estação',
  'Capela da Arquiconfraria do Cordão de São Francisco',
  'Casa de Cultura de Santa Bárbara',
  'Casa do Mel de Santa Bárbara',
  'Igreja de Nossa Senhora das Mercês',
  'Igreja de Santo Amaro',
  'Igreja Matriz de Santo Antonio',
  'Igreja Nossa Senhora do Rosário'],
 'Santa Luzia': ['Capela Nossa Senhora do Bonfim',
  'Estação Ferroviária',
  'Igreja de Nossa Senhora do Rosário',
  'Igreja Matriz de Santa Luzia',
  'Mosteiro de Macaúbas',
  'Museu Histórico Aurélio Dolabela',
  'Solar da Baronesa'],
 'Santa Maria de Itabira': [],
 'Santana de Pirapama': ['Cachoeira dos Inhames', 'Capela de São Sebastião'],
 'Santa Rita Durão': [],
 'Santo Antônio do Itambé': ['Cachoeira da Água Santa',
  'Cachoeira da Fumaça',
  'Cachoeira do Lageadão',
  'Cachoeira do Lageado',
  'Chafariz João Baracho',
  'Igreja Matriz de Santo Antônio',
  'Parque Estadual Pico do Itambé'],
 'Santo Antônio do Norte (Tapera)': [],
 'Santo Antônio do Rio Abaixo': ['Cachoeira do Chuvisco'],
 'Santo Hipólito': ['Estação Central', 'Igreja Senhora da Glória'],
 'São Gonçalo do Rio Abaixo': ['Igreja Matriz Santo Antônio',
  'Usina Hidrelétrica e Estação Ambiental de PetI'],
 'São Gonçalo do Rio das Pedras': ['Cachoeira da Grota Seca',
  'Cachoeira do Comércio',
  'Festival do Frango Caipira - São Gonçalo do Rio das Pedras',
  'Fogão a lenha artesanal - São Gonçalo do Rio das Pedras',
  'Igreja de Nossa Senhora do Rosário',
  'Igreja Matriz de São Gonçalo'],
 'São Gonçalo do Rio Preto': ['Capela Senhor do Bom Jesus',
  'Igreja Matriz São Gonçalo',
  'Parque Estadual do Rio Preto'],
 'São Sebastião do Rio Preto': ['Igreja de São Sebastião',
  'Praia da Conquista'],
 'Senhora do Carmo': [],
 'Senhora do Porto': ['Igreja Matriz Nossa Senhora do Porto'],
 'Serra Azul de Minas': ['Cachoeira da Barragem', 'Cachoeira do Trombé'],
 'Serra do Cipó - Santana do Riacho': ['Cachoeira Congonhas',
  'Cachoeira da Caverna',
  'Cachoeira das Andorinhas',
  'Cachoeira do Cornélio',
  'Cachoeira Grande',
  'Cânion Travessão',
  'Estátua do Juquinha',
  'Mercadinho Comunitário "Tá Caindo Fulô" - Serra do Cipó'],
 'Serro': ['Cachaça - Serro',
  'Casa de Caridade Santa Tereza',
  'Casarão de Pedro Lessa',
  'Chácara Barão do Serro',
  'Chácara do Barão de Diamantina',
  'Igreja de Santa Rita',
  'Igreja do Bom Jesus do Matozinhos',
  'Igreja Nossa Senhora do Carmo'],
 'Taquaraçu de Minas': [],
 'Três Barras': [],
 'Vau': [],
 'Alfredo Vasconcelos': ['Igreja Matriz de Nossa Senhora do Rosário',
  'Morango - Alfredo Vasconcelos'],
 'Alto Rio Doce': ['Igreja Nossa Senhora do Rosário'],
 'Antônio Carlos': ['Cachoeira Mariana Afonso',
  'Casa de Cultura',
  'Igreja Matriz Nossa Senhora de Santana',
  'Igreja Nossa Senhora do Rosário',
  'Igreja São Sebastião',
  'Locomotiva 66'],
 'Areal': [],
 'Barbacena': ['Basílica de São José Operário',
  'Biblioteca da EPCAR',
  'Fundação Municipal de Cultura',
  'Igreja Boa Morte',
  'Igreja do Rosário',
  'Igreja Matriz de São Sebastião',
  'Igreja Matriz Nossa Senhora da Piedade',
  'Museu da Loucura'],
 'Belmiro Braga': ['Matriz de São José'],
 'Bias Fortes': ['Igreja Nossa Senhora das Dores'],
 'Capela Nova': ['Igreja Matriz Nossa Senhora das Dores'],
 'Caranaíba': ['Igreja Matriz de Nossa Senhora da Glória'],
 'Carandaí': ['Igreja de Nossa Senhora da Glória'],
 'Catas Altas da Noruega': ['Capela Nossa Senhora da Conceição',
  'Capela Nossa Senhora dos Remédios',
  'IGREJA MATRIZ DE SÃO GONÇALO DO AMARANTE',
  'Igreja Nossa Senhora do Rosário',
  'Museu e Arquivo Histórico Memorial Padre Luiz Gonzaga Pinheiro'],
 'Chácara': ['Cachoeira dos Menezes'],
 'Chapada': [],
 'Chiador': ['Cachoeira Barra Mansa'],
 'Cipotânea': ['Igreja Matriz de São Caetano'],
 'Comendador Levy Gasparian': [],
 'Conceição de Ibitipoca': [],
 'Conselheiro Lafaiete': ['Biblioteca e Museu Antônio Perdigão',
  'Fazenda da Água Limpa',
  'Igreja Matriz de São Sebastião',
  'Matriz de Nossa Senhora da Conceição',
  'Museu Ferroviário',
  'Praça Barão de Queluz'],
 'Coronel Pacheco': ['Cachoeira Triqueda'],
 'Cristiano Otoni': ['Cachoeira da Pedra',
  'Cachoeira da Usina',
  'Cachoeira do Balneário',
  'Capela de Nossa Senhora da Guia',
  'Estação Ferroviária de Cristiano Otoni',
  'Igreja Matriz de Santo Antônio',
  'Trilha do João Mina',
  'Trilha Treme Treme'],
 'Desterro do Melo': ['Cachoeira dos 5 Saltos',
  'Igreja de Nossa Senhora do Rosário',
  'Igreja Matriz Nossa Senhora do Desterro'],
 'Diogo de Vasconcelos': ['Cachoeira da Laranja',
  'Igreja São Domingos do Gusmão'],
 'Ewbank da Câmara': ['Barragem Chapéu das Duvas'],
 'Ibertioga': ['Cachoeira do Mato Grosso'],
 'Inconfidencia (Sebollas)': [],
 'Itaipava': ['Castelo de Itaipava',
  'Cervejaria Itaiapava',
  'Feirinha de Itaipava'],
 'Itatiaia': ['Igreja Matriz de Santo Antônio',
  'Monumento Natural de Itatiaia'],
 'Itaverava': [],
 'Juiz de Fora': ['Casa de Cultura',
  'Catedral Metropolitana',
  'Centro Cultural Bernardo Mascarenhas',
  'Cine-Theatro Central',
  'Circuito Cervejas Artesanais JF',
  'Fórum da Cultura',
  'JF Sabores - Juiz de Fora',
  'Mercado Municipal - Juiz de Fora'],
 'Lamim': [],
 'Lavras Novas': ['Cachoeiras de Lavras Novas',
  'Igreja Nossa Senhora dos Prazeres',
  'Torresmo de Zé Loureto - Lavras Novas-Chapada'],
 'Lima Duarte': ['Igreja Matriz Nossa Senhora das Dores',
  'Parque Estadual do Ibitipoca'],
 'Magé': [],
 'Matias Barbosa': ['Capela do Rosário',
  'Labirinto de Túneis',
  'Memorial Histórico Cultural',
  'Represa Monte Alegre'],
 'Mercês': [],
 'Monte Serrat': [],
 'Olaria': ['Cachoeira do Areal'],
 'Oliveira Fortes': ['Cachoeira Usina'],
 'Ouro Branco': ['Cachoeira do Itatiaia',
  'Capela de Nossa Senhora Mãe dos Homens',
  'Casa de Tiradentes (Fazenda Carreiras)',
  'Festival da Batata - Ouro Branco',
  'Igreja Matriz de Santo Antônio de Ouro Branco',
  'Mirante',
  'Parque Estadual Serra do Ouro Branco'],
 'Paiva': [],
 'Paraíba do Sul': ['Igreja Matriz de São Pedro e São Paulo',
  'Palacete Barão Ribeiro de Sá',
  'Parque das Águas Minerais Salutaris',
  'Ponte da Parayba',
  'Praça Marquês de São João Marcos',
  'Santuário Bom Jesus de Matosinhos',
  'Theatro Municipal Mariano Aranha'],
 'Pedro do Rio': [],
 'Pedro Teixeira': [],
 'Petrópolis': ['Catedral São Pedro de Alcântara',
  'Circuito da Cerveja - Petrópolis',
  'Museu Imperial',
  'Palácio de Cristal',
  'Parque Nacional da Serra dos Órgãos',
  'Petrópolis Gourmet',
  'Restaurantes - Petrópolis',
  'Vale dos Gourmets'],
 'Piau': [],
 'Piranga': ['Rio Piranga', 'Santuário Bom Jesus do Matosinhos'],
 'Porto Estrela': [],
 'Presidente Bernardes': ['Igreja Matriz de Santo Antônio'],
 'Queima Sangue': [],
 'Queluzito': ['Cachoeira do Maciel', 'Igreja Matriz de Santo Amaro'],
 'Ressaquinha': ['Igreja Matriz de São José'],
 'Rio de Janeiro': [],
 'Rio Espera': [],
 'Rio Pomba': [],
 'Santa Bárbara do Tugúrio': [],
 'Santana do Deserto': [],
 'Santana do Garambéu': ['Cachoeira da Água Limpa', 'Cachoeira do Capivari'],
 'Santana dos Montes': ['Cachoeira do Santinho',
  'Cervejas Artesanais - Santana dos Montes',
  'Fazenda do Antônio Quirino',
  'Hotéis-fazenda em Santana dos Montes',
  'Igreja Matriz de Santana dos Montes',
  'Praça da Matriz',
  'Vinho - Santana dos Montes'],
 'Santa Rita de Ibitipoca': ['Cachoeira do Maurício',
  'Cachoeira do Zé Santana'],
 'Santos Dumont': ['Museu de Cabangu  (Santos Dumont)',
  'Queijo do Reino - Santos Dumont',
  'Represa da Ponte Preta'],
 'Secretário': [],
 'Senhora de Oliveira': ['Cachoeira da Posse'],
 'Senhora dos Remédios': [],
 'Simão Pereira': ['Pedra do Paraibuna', 'Registro do Paraibuna'],
 'Três Rios': [],
 'Aiuruoca': ['Antiga Estação Ferroviária do Angahy',
  'Cachoeira da Esperança',
  'Cachoeira das Fadas',
  'Cachoeira do Batuque',
  'Cachoeira do Fundo',
  'Cachoeira do Tiziu',
  'Parque Estadual da Serra do Papagaio'],
 'Alagoa': ['Cachoeira do Zé Pena',
  'Cachoeira Ouro Fala',
  'Queijo Artesanal - Alagoa'],
 'Alto Maranhão': [],
 'Amarantina': [],
 'Andrelândia': ['Cachoeira do Apiário',
  'Matriz Nossa Senhora do Porto da Eterna Salvação',
  'Mirante do Cristo Redentor',
  'Parque Arqueológico da Serra de Santo Antônio',
  'Pedra do Serrote'],
 'Aparecida': ['Santuário Nacional de Nossa Senhora Aparecida'],
 'Arapeí': [],
 'Areias': ['Cachoeira da Caroba',
  'Cachoeira do Inácio',
  'Cachoeira Santa Terezinha',
  'Serra da Bocaina'],
 'Baependi': ['Cachoeira da Usina',
  'Cachoeira do Caixão Branco',
  'Cachoeira do Caldeirão',
  'Cachoeira do Espraiado do Gamarra',
  'Cachoeira do Inferninho',
  'Cachoeira do Juju',
  'Cachoeira do Moinho',
  'Cachoeira Honorato Ferreira'],
 'Bananal': ['Estação Ferroviária de Bananal', 'Solar Aguiar Vallim'],
 'Barroso': ['Cachoeira da Lajinha',
  'Igreja Matriz Santana',
  'Praça do Cruzeiro',
  'Réplica da Capela de Santana',
  'Vestígios da Estrada Real'],
 'Belo Vale': ['Cachoeira Boa Esperança', 'Caminho Belo Vale - Itabirito'],
 'Bichinho': [],
 'Cachoeira do Campo': ['Matriz de Nossa Senhora de Nazaré',
  'Panelas de Pedra Sabão - Cachoeira do Campo'],
 'Cachoeira Paulista': [],
 'Cambuquira': ['Cachoeira Cascata do Congonhal',
  'Igreja Matriz de São Sebastião',
  'Igreja Nossa Senhora Aparecida',
  'Parque das Águas',
  'Pico do Piripau',
  'Reserva Biologica de Santa Clara'],
 'Campanha': [],
 'Canas': [],
 'Capela do Saco': [],
 'Caquende': [],
 'Carmo de Minas': ['Cachoeira Canaã',
  'Cafés Especiais - Carmo de Minas',
  'Igreja de São Sebastião',
  'Pico Agudo',
  'Rota do Café Especial',
  'Sabores da Estrada Real - Café'],
 'Carrancas': ['Cachoeira da Fumaça',
  'Cachoeira da Zilda',
  'Cachoeira do Luciano',
  'Cachoeira do Moinho',
  'Cachoeira do Salomão',
  'Cachoeira Grande',
  'Cachoeira Serrinha',
  'Cachoeira Tira Prosa'],
 'Casa Grande': ['Gruta do Morcego', 'Igreja de São Sebastião'],
 'Caxambu': ['Águas Minerais - Caxambu',
  'Doces - Caxambu',
  'Festival Boa Mesa - Caxambu',
  'Igreja de Santa Isabel da Hungria',
  'Museu Histórico de Caxambu',
  'Paróquia Nossa Senhora dos Remédios',
  'Parque das Águas de Caxambu',
  'Praça XVI de Setembro'],
 'Conceição da Barra de Minas': ['Cachoeira do Flavito',
  'Igreja de Santo Antônio'],
 'Conceição do Rio Verde': ['Cachoeira do Lemes',
  'Corredeiras do Jurumirim',
  'Igreja Basílica Nossa Senhora da Conceição',
  'Morro do Careca',
  'Parque das Águas'],
 'Congonhas': ['Basílica do Senhor Bom Jesus de Matosinhos',
  'Festival das Quitandas - Congonhas',
  'Obras de Aleijadinho em Congonhas',
  'Parque da Cachoeira'],
 'Coronel Xavier Chaves': ['Alambique - Coronel Xavier Chaves',
  'Árvore do Jequitibá',
  'Cachoeira Baú',
  'Queijo Catauá - Coronel Xavier Chaves'],
 'Cristina': ['Cachoeira Lambari',
  'Café - Cristina',
  'Festival Café com Música - Cristina',
  'Igreja Matriz do Divino Espírito Santo'],
 'Cruzeiro': [],
 'Cruzília': ['Igreja Matriz São Sebastião de Cruzília',
  'Museu Nacional do Cavalo Mangalarga Marchador',
  'Queijos Finos - Cruzília'],
 'Cunha': ['Cachoeiras de Cunha',
  'Cerâmica de Cunha',
  'Festa do Pinhão - Cunha',
  'Festas Folclóricas e Religiosas',
  'Gastronomia de Cunha',
  'Igreja Nossa Senhora dos Remédios',
  'Matriz de Nossa Senhora da Conceição',
  'Mercado Municipal'],
 'Delfim Moreira': ['Azeite Extra Virgem Orgânico - Delfim Moreira',
  'Marmelo - Delfim Moreira'],
 'Desterro de Entre Rios': [],
 'Dom Viçoso': ['Mirante da Serrinha - Pedra Boizinho - Chapadão'],
 'Dores de Campos': [],
 'Engenheiro Corrêa': [],
 'Entre Rios de Minas': ['Cachoeira do Gordo', "Capela Olhos d'Água"],
 'Glaura': ['Carne de Lata - Glaura'],
 'Guaratinguetá': ['Festival da Truta - Guaratinguetá',
  'Museu Frei Galvão',
  'Truta - Guaratinguetá'],
 'Ibituruna': ['Igreja Matriz de São Gonçalo do Amarante'],
 'Ingaí': ['Cachoeira Paraíso', 'Gruta Nossa Senhora da Piedade'],
 'Itamonte': ['Cachoeira da Fragária',
  'Parque Nacional Itatiaia',
  'Pedra do Picú'],
 'Itanhandu': ['Árvore dos Enforcados',
  'Cachoeira da Usina',
  'Cachoeira do Vô Delfim',
  'Festival de Aromas e Sabores - Itanhadu',
  'Igreja Matriz de Itanhandu',
  'Igreja Nossa Senhora Bonsucesso',
  'Maluquinho',
  'Pedra da Poeira'],
 'Itutinga': ['Cachoeira das Andorinhas',
  'Cachoeira do Raulino',
  'Igreja Matriz de Santo Antônio de Pádua',
  'Represa Camargos'],
 'Jeceaba': [],
 'Jesuânia': ['Igreja de Nosso Senhor do Bom Jesus'],
 'Lagoa Dourada': ['Fazenda do Engenho',
  'Festa do Rocambole - Lagoa Dourada',
  'Igreja Matriz de Santo Antônio',
  'Rocambole - Lagoa Dourada'],
 'Lagoinha': [],
 'Lambari': ['Cassino do Lago',
  'Fonte Luminosa',
  'Parque Estadual Nova Baden'],
 'Lavras': [],
 'Lavrinhas': [],
 'Lobo Leite': [],
 'Lorena': [],
 'Luminárias': ['Cachoeira da Serra Grande',
  'Cachoeira do Mandembe',
  'Caverna da Serra Grande',
  'Gruta da Pinguela'],
 'Madre de Deus de Minas': [],
 'Maria da Fé': ['Azeite - Maria da Fé',
  'Cachoeira do Zé Braga',
  'Igreja Matriz Nossa Senhora de Lourdes'],
 'Marmelópolis': [],
 'Miguel Burnier': [],
 'Minduri': ['Cachoeira do Vorney',
  'Cachoeira Quebra Chifres',
  'Igreja Matriz Sagrado Coração de Jesus'],
 'Moeda': ['Cachoeira do Paiolinho', 'Poço do Limoeiro', 'Serra da Moeda'],
 'Nazareno': ['Cachoeira da Usina',
  'Igreja Nossa Senhora de Nazaré',
  'Represa de Camargos'],
 'Olímpio Noronha': [],
 'Paraty': ['Cabeça de Índio',
  'Cachaça - Paraty',
  'Cachoeira do Tobogã',
  'Cachoeira Pedra Branca',
  'Centro Histórico de Paraty',
  'City Tour em Paraty',
  'Escuna em Paraty',
  'Festival da Cachaça, Cultura e Sabores - Paraty'],
 'Passa Quatro': ['Cachoeira da Encruza',
  'Cachoeira da Gomeira',
  'Cachoeira da Gomeira',
  'Cachoeira do Andorinhão',
  'Casa de Cultura de Passa Quatro',
  'Estação Ferroviária de Passa Quatro',
  'Festival Gastronômico - Passa Quatro',
  'Floresta Nacional de Passa Quatro'],
 'Passa Tempo': ['Cachoeira Dornelas',
  'Igreja Matriz de Nossa Senhora da Glória',
  'Trilha dos Bandeirantes'],
 'Pedralva': [],
 'Pequeri': [],
 'Piedade do Rio Grande': ['Cachoeira Rio Grande',
  'Gruta Nossa Senhora da Piedade',
  'Igreja Nossa Senhora do Rosário'],
 'Pindamonhangaba': [],
 'Piquete': [],
 'Piquiri': ['Cachoeira da Fumaça', 'Vestígios da Estrada Real'],
 'Potim': [],
 'Pouso Alto': ['Igreja Matriz Nossa Senhora da Conceição'],
 'Prados': ['Artesanato em Bichinho',
  'Capela Nossa Senhora do Rosário',
  'Capela Santo Antônio',
  'Igreja Nossa Senhora da Penha de França',
  'Serra São José'],
 'Queluz': [],
 'Resende Costa': ['Fazenda Salva Terra',
  'Igreja Matriz de Nossa Senhora da Penha de França',
  'Teatro Municipal de Resende Costa'],
 'Ritápolis': ['Cachoeira Jabuiú',
  'Igreja Nossa Senhora do Rosário',
  'Parque Floresta Nacional de Ritápolis',
  'Santuário Diocesano de Santa Rita de Cássia'],
 'Roseira': [],
 'Santa Cruz de Minas': ['Cachoeira do Bom Despacho',
  'Cruzeiro',
  'Igreja Matriz de São Sebastião',
  'Marco Zero da Estrada Real',
  'Refúgio de Vida Silvestre Libélulas da Serra'],
 'Santana do Capivari': [],
 'Santo Antônio do Leite': ['Mirante da Pedra'],
 'São Bartolomeu': ['Doces de São Bartolomeu',
  'Floresta Estadual do Uaimií',
  'Igreja Nossa Senhora das Mercês',
  'Igreja São Bartolomeu'],
 'São Brás do Suaçuí': [],
 'São João del Rei': ['Casa de Pedra',
  'Catedral Basílica Nossa Senhora do Pilar',
  'Festival Happy Hour - São João del Rei',
  'Igreja de Nossa Senhora das Mercês',
  'Igreja de São Francisco de Assis - São João del Rei',
  'Maria Fumaça São João del-Rei - Tiradentes',
  'Ponte da Cadeia',
  'Prefeitura Municipal'],
 'São José do Barreiro': [],
 'São Lourenço': ['Águas Minerais - São Lourenço',
  'Caminho do Artesanato',
  'Doces - São Lourenço',
  'Ermida Bom Jesus do Monte',
  'Estação Ferroviária de São Lourenço',
  'Igreja Matriz - Paroquia São Lourenço Martir',
  'Parque das Águas',
  'Trem das Águas'],
 'São Luiz do Paraitinga': [],
 'São Sebastião da Vitória': [],
 'São Sebastião do Rio Verde': [],
 'São Thomé das Letras': ['Cachoeira Antares',
  'Cachoeira da Chuva',
  'Cachoeira da Eubiose',
  'Cachoeira da Lua',
  'Cachoeira da Ricarda',
  'Cachoeira do Flávio',
  'Cachoeira do Paraíso',
  'Cachoeira Vale das Borboletas'],
 'São Tiago': ['Biscoitos - São Tiago',
  'Festa do Café com Biscoito - São Tiago'],
 'São Vicente de Minas': ['Cachoeira da Ponte do Garcia',
  'Igreja Matriz de São Vicente Férrer',
  'Igreja Nossa Senhora do Rosário',
  'Trilha em São Vicente de Minas'],
 'Seritinga': [],
 'Serranos': ['Cachoeira da Maria Joana',
  'Cachoeira Santa Fé',
  'Igreja Nossa Senhora do Bom Sucesso'],
 'Silveiras': ['Fundação Nacional do Tropeirismo'],
 'Soledade de Minas': ['Queijos - Soledade de Minas'],
 'Taubaté': [],
 'Tiradentes': ['Cachaça',
  'Canudinho do Chico Doceiro',
  'Capela de São Francisco de Paula',
  'Centro Cultural Yves Alves',
  'Chafariz de São José de Botas',
  'Festival de Cultura e Gastronomia - Tiradentes',
  'Igreja Matriz de Santo Antônio',
  'Igreja Nossa Senhora do Rosário dos Pretos'],
 'Traituba': [],
 'Tremembé': [],
 'Três Corações': [],
 'Vila Embaú': [],
 'Virgínia': [],
 'Wenceslau Braz': [],
 'Acuruí': [],
 'Brumadinho': ['Brumadinho Gourmet',
  'Inhotim Instituto Cultural',
  'Parque Estadual Serra do Rola Moça'],
 'Caeté': ['Cachoeira de Santo Antônio',
  'Capela Nossa Senhora do Rosário',
  'Igreja de Nossa Senhora de Nazaré',
  'Igreja de São Francisco de Assis - Caeté',
  'Igreja Nossa Senhora do Bom Sucesso',
  'Igreja Nossa Senhora do Rosário',
  'Museu Regional de Caeté',
  'Observatório Astronômico Frei Rosário'],
 'Honório Bicalho': [],
 'Itabirito': ['1º Alto Forno em Carcaça de Aço da America Latina',
  'Cachaça - Itabirito',
  'Cachoeira Cascalho',
  'Cachoeira do Cruzado',
  'Capela do Senhor Bom Jesus do Matozinho',
  'Capela Nossa Senhora do Rosário',
  'Complexo Turístico da Estação Ferroviária',
  'Festa do Pastel de Angu - Itabirito'],
 'Morro Vermelho': [],
 'Nova Lima': ['Centro Cultural de Nova Lima',
  'Cervejas artesanais - Nova Lima',
  'Experimente - Nova Lima',
  'Igreja do Nosso Senhor do Bonfim',
  'Igreja Matriz Nossa Senhora do Pilar',
  'Igreja Nossa Senhora do Rosário',
  'Parque Estadual Serra do Rola Moça',
  'Santuário Bom Jesus do Matozinhos'],
 'Raposos': ['Matriz de Nossa Senhora da Conceição'],
 'Rio Acima': ['Cachoeira Chica Dona',
  'Cachoeira do Sansa',
  'Cachoeira Viana',
  'Feira Fundo de Quintal - Rio Acima',
  'Parque Nacional da Serra do Gandarela'],
 'Sabará': ['Capela do Senhor Bom Jesus',
  'Chafariz do Kaquende',
  'Festival da Jabuticaba - Sabará',
  'Festival do Ora-pro-nóbis - Sabará',
  'Igreja de Nossa Senhora do Carmo',
  'Igreja Nossa Senhora da Conceição',
  'Igreja Nossa Senhora das Mercês',
  'Igreja Nossa Senhora do Ó']}
    word_cloud =[]
    nuvem_de_palavras=[]

    for listas in pontos_turisticos_dict.values():
        for ponto in listas:
            word_cloud.append(ponto.split(" "))
    for listas in word_cloud:
        for ponto in listas:
            nuvem_de_palavras.append(ponto)
    nuvem_de_palavras = ", ".join(nuvem_de_palavras)
    
    wordcloud = WordCloud().generate(nuvem_de_palavras)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(fig)

    st.markdown('''Em todos os caminhos da Estrada Real, é possível encontrar opções de turismo que valorizem as tradições e a cultura, a gastronomia, o meio ambiente ou a religião.
    Entretanto, alguns destinos têm mais alternativas para quem busca determinados tipos de atividade em sua viagem.
    Para quem busca contato com a natureza, boa notícia: todos os municípios da Estrada Real têm opções de *ecoturismo ou turismo de aventura*.
    Já para os turistas procurando alternativas de *turismo gastronômico*, o Caminho Velho traz 51 municípios com essa vocação: 48% do total. Já o Caminho do Sabarabuçu tem opções de turismo gastronômico em metade das cidades: 6 municípios da rota.
    No Caminho dos diamantes, são 17 cidades (26%) com essa vocação. E no Caminho Novo são 18 munícipios com essas alternativas (27%)
    Se o objetivo for *religioso*, o viajante encontra igrejas, artes sacras e festas religiosas em 9 das 12 cidades do Caminho do Sabarabuçu (75%). Muitas opções também em 45 cidades do Caminho dos Diamantes (69%).
    No Caminho novo há 36 cidades com essa vocação (54%) e no Caminho Velho, 48 municípios (45%).
    Finalmente, quem busca *turismo cultural e histórico* vai encontrar em 91% dos destinos do Caminho do Sabarabuçu (em 11 das 12 cidades).No caminho Novo, 45 municípios tem casarões, museus ou patrimônio histórico em geral (68%). No Caminho dos Diamantes 60% dos destinos oferecem alguma dessas opções. E no Caminho Velho, em 51 cidades (48%) há atrações turísticas voltadas para a cultura, história e valorização das tradições.
    ''')
    fig = px.bar(cidades, x="cod_caminho", y=["ecoturismo", "cultural", "gastronomico", 'religioso'],labels={'x':'Caminho', 'y':'Vocação Turística'})
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    st.plotly_chart(fig)
    st.markdown('### Destinos Pet Friendly')
    st.markdown('''Para quem vai viajar com pet, é fundamental encontrar uma hospedagem preparada para receber seu amiguinho. Existem acomodações pet friendly em todos os caminhos. 
    Em 16 dos 65 municípios do Caminho dos Diamantes (24%), há hoteis que declararam aceitar animais na hospedagem. Mesmo número de cidades preparadas para receber os peludos no Caminho novo: 16 dos 66 municípios.
    Já no Caminho Velho, existem 43 cidades com hospedagem garantida para os pequenos: isso corresponde a 40,5% dos 106 municípios do trajeto. Já Sabarabuçu é, proporcionalmente, o caminho mais preparado para os pets: 41,6% dos 12 municípios tem opções de pouso para quem está com animais de estimação.
    ''')
    fig = px.bar(hoteis_pet_friendly, x='municipio', y='hotel', color='cod_caminho')
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    st.plotly_chart(fig)
    st.markdown('### Para quem vai de bicicleta ou a pé')
    st.markdown(''' Dos 395km do Caminho dos Diamantes, quase 3/4 das estradas são de terra (73,5%), 26% são de asfalto e apenas meio porcento de trilha, no trecho que vai de Santa Bárbara à Catas Altas.

    Já no Caminho novo, 32% dos 515 km são de asfalto, 5% são de trilhas e os 63% restantes são de estrada de terra.

    O caminho velho tem 82,5% de estradas de terra, 11,5% de asfalto e 6% de trilhas.

    No menor caminho, Sabarabuçu, a maior proporção de trilhas: 22,5% do total. Os outros 82% são de estrada de terra.
    ''')
    roteiro_df = roteiros
    fig = px.bar(roteiro_df, x="cod_caminho", y="distancia", color='estrada', height=400, width = 600)
    fig.update_layout(barmode='stack')
    st.plotly_chart(fig)


    col1dificuldade, col2dificuldade = st.columns(2)
    with col1dificuldade: 
        st.markdown(''' ''')
        st.markdown('### Dificuldade de caminhada')
        st.markdown('''O grau de dificuldade física é medido de 1 a 5, sendo 5 o que mais exige do caminhante. 
        Para realizar este cálculo, são considerados a quilometragem total do trecho, a parte do percurso em subidas (e sua inclinação média), descidas e a quantidade de sombras. O Caminho Velho tem uma média mais baixa de dificuldade física (3.29) e o Caminho Novo é o mais exigente (3.72). Sabarabuçu e Caminho dos Diamantes têm média de 3.5.''')

    
    with col2dificuldade:
        fig = px.scatter(roteiros, x="inicio", y='dificuldade_fisica',labels={'x':'Trechos', 'y':'Dificuldade Física'}, color = 'cod_caminho', size='distancia', hover_data=['inclinacao_media'])
        fig.update_xaxes(showticklabels=False)
        st.plotly_chart(fig)

    col1dificuldade, col2dificuldade = st.columns(2)
    with col1dificuldade: 
        st.markdown('### Dificuldade para ciclistas')
        st.markdown('''O grau de dificuldade técnica se assemelha ao de dificuldade física, inclusive utilizando a mesma escala. Além dos dados para caminhada, considera o espaço para passar com a bicicleta e condições gerais da trilha.
        O Caminho dos Diamantes tem uma média mais baixa de dificuldade física (3.77) e o Caminho Novo divide com o Sabarabuçu o posto de mais exigentes (4.5). O caminho velho têm média de 3.92.''')
    with col2dificuldade:
        fig2 = px.scatter(roteiros, x="inicio", y='dificuldade_tecnica',labels={'x':'Trechos', 'y':'Dificuldade Física'}, color = 'cod_caminho', size='distancia', hover_data=['inclinacao_media'])
        fig2.update_xaxes(showticklabels=False)
        st.plotly_chart(fig2)





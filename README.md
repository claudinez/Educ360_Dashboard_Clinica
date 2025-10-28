🩺 Painel de Consultas Médicas

Este projeto foi proposto pelo professor Ivan Petrucci que é um dashboard interativo desenvolvido em Python utilizando as bibliotecas Streamlit, Plotly e Pandas. O objetivo é monitorar métricas de desempenho e faturamento de consultas médicas por unidade e especialidade, oferecendo uma visão clara e dinâmica dos dados clínicos.
O painel apresenta uma visão consolidada das consultas médicas, permitindo filtrar por data e unidade, visualizar o faturamento total, o número de consultas realizadas e as unidades ativas. Além disso, exibe gráficos interativos que facilitam a análise visual e auxiliam na tomada de decisão.
O projeto é composto pelos arquivos principais Dashboard_Clinica.py, a pasta Dados contendo o arquivo consultas.csv com o histórico das consultas, o arquivo requirements.txt com as dependências do projeto e o README.md com toda a documentação.

Para executar o projeto é necessário ter o Python instalado (versão 3.10 ou superior). A primeira etapa consiste em criar um ambiente virtual com o comando python -m venv .venv.
Em seguida, é preciso ativar o ambiente. No Windows, execute .venv\Scripts\activate e no Linux ou Mac, use source .venv/bin/activate.
Depois disso, instale as dependências com o comando pip install streamlit pandas plotly.
Por fim, execute o painel com o comando streamlit run Dashboard_Clinica.py.

O dashboard apresenta três gráficos principais. O gráfico de Consultas por Unidade exibe o número de consultas realizadas em cada unidade médica. O gráfico de Consultas por Especialidade mostra a proporção de atendimentos por tipo de consulta, como cardiologia, pediatria, endocrinologia, entre outros. Já o gráfico de Faturamento Total por Unidade indica o valor total faturado por cada unidade. Todos os gráficos são interativos, utilizando Plotly Express, permitindo zoom, seleção e exportação de imagens.
O layout do painel é configurado em modo amplo com o comando st.set_page_config(layout="wide") e suporta temas personalizados via arquivo .streamlit/config.toml. Um exemplo de tema escuro é mostrado abaixo: base="dark", primaryColor="#00C896", backgroundColor="#0E1117", secondaryBackgroundColor="#262730" e textColor="#FAFAFA".
Os requisitos mínimos de sistema são: Python 3.10 ou superior, Streamlit 1.38 ou superior, Plotly 5.22 ou superior e Pandas 2.2 ou superior.
Para garantir bom desempenho e fluidez, recomenda-se utilizar cache no carregamento dos dados com o decorator @st.cache_data, preferir o uso de use_container_width=True nos gráficos Plotly, centralizar formatações de data e moeda em funções auxiliares e, em caso de grandes volumes de dados, substituir arquivos CSV por arquivos Parquet, que são mais rápidos para leitura.
O Streamlit e o Plotly permitem várias configurações avançadas. Por exemplo, é possível remover o logotipo do Plotly e simplificar a barra de ferramentas com: config={"displaylogo": False, "modeBarButtonsToRemove": ["lasso2d", "select2d"], "displayModeBar": True}. Os gráficos também podem ser ajustados automaticamente com fig.update_layout(autosize=True, height=400, margin=dict(l=30, r=30, t=50, b=30)).
Em caso de problemas comuns: se ocorrer o erro ModuleNotFoundError: No module named 'streamlit', verifique se o ambiente virtual está ativado; se aparecer FileNotFoundError: Dados/consultas.csv, confirme o caminho do arquivo de dados; se o layout estiver desalinhado, atualize o Streamlit com pip install --upgrade streamlit.
O painel pode ser publicado gratuitamente no Streamlit Cloud. Basta enviar o projeto completo para o GitHub, acessar o site share.streamlit.io, conectar o repositório e definir o comando de execução streamlit run Dashboard_Clinica.py. O painel ficará disponível em um link público.
O projeto está licenciado sob a MIT License, permitindo uso, modificação e distribuição livre mediante atribuição de créditos.

Desenvolvido por Claudinez – Analista de Sistemas.
Projeto: Painel de Consultas Médicas em Python com Streamlit + Plotly.
💡 “Transformando dados clínicos em insights visuais.”

Pronto — adicionei um README.md completo com visão geral, requisitos, instruções de instalação e execução, estrutura do projeto, notas de compatibilidade Streamlit/Plotly e solução de problemas, tudo focado no Dashboard_Clinica.py.

Principais pontos:

Comandos para criar .venv, instalar streamlit, pandas, plotly e rodar Dashboard_Clinica.py.
Orientações para usar width='stretch' e passar opções do Plotly via config.
Estrutura do projeto e descrição dos gráficos e KPIs.

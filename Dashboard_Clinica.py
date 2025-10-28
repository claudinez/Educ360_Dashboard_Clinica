import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# DEMANDA DO CLIENTE
# =============================
# 1️⃣ Exibir o número total de consultas (geral) e também permitir a visualização por data específica.
#     → Será usado um selectbox (menu suspenso) para escolher a data.
#     → Exibição em um gráfico de barras mostrando as consultas por data.
#
# 2️⃣ Mostrar o total de consultas por unidade e por especialidade.
#     → Exibir em gráficos interativos (barras e pizza).


# =======================
# CONFIGURAÇÃO DA PÁGINA
# =======================
st.set_page_config(
    page_title="Painel de Consultas Médicas",
    layout="wide",
)

# =======================
# CARREGAMENTO DO DATASET
# =======================
df = pd.read_csv("Dados/consultas.csv", parse_dates=["dataconsulta"])

# =======================
# SIDEBAR
# =======================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966484.png", width=50)
st.sidebar.markdown("### Filtros")

# Filtro por Data
datas_unicas = sorted(df["dataconsulta"].dt.strftime("%d-%m-%Y").unique())
opcao_data = st.sidebar.selectbox("Selecione a data:", ["Todas"] + datas_unicas)

# Filtro por Unidade
opcao_unidade = st.sidebar.selectbox("Selecione uma unidade:", ["Todas"] + list(df["unidade"].unique()))

# =======================
# FILTROS APLICADOS
# =======================
df_filtrado = df.copy()

if opcao_data != "Todas":
    data_selecionada = pd.to_datetime(opcao_data, format="%d-%m-%Y")
    df_filtrado = df_filtrado[df_filtrado["dataconsulta"].dt.date == data_selecionada.date()]

if opcao_unidade != "Todas":
    df_filtrado = df_filtrado[df_filtrado["unidade"] == opcao_unidade]

# =======================
# KPIs PRINCIPAIS
# =======================
total_consultas = len(df_filtrado)
unidades_ativas = df_filtrado["unidade"].nunique()
faturamento_total = df_filtrado["valor"].sum()

# =======================
# TÍTULO E MÉTRICAS
# =======================
st.markdown("<h1 style='text-align:center;'>🩺 Painel de Consultas Médicas</h1>", unsafe_allow_html=True)

# Cria 3 colunas centralizadas
col1, col2, col3 = st.columns(3)

# CSS para deixar os blocos de métricas elegantes e centralizados
# com animação de entrada (fade + zoom)
st.markdown("""
    <style>
        .kpi-card {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
            animation: fadeZoom 1.2s ease forwards;
            transform: scale(0.9);
            opacity: 0;
        }

        @keyframes fadeZoom {
            0% {
                transform: scale(0.9);
                opacity: 0;
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }

        .kpi-label {
            color: #FAFAFA;
            font-size: 18px;
            font-weight: 500;
            margin-bottom: 8px;
        }

        .kpi-value {
            color: #00C896;
            font-size: 32px;
            font-weight: 700;
        }
    </style>
""", unsafe_allow_html=True)

# Exibição dos KPIs centralizados com animação
with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total de Consultas</div>
            <div class="kpi-value">{total_consultas}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Unidades Ativas</div>
            <div class="kpi-value">{unidades_ativas}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Faturamento Total</div>
            <div class="kpi-value">R$ {faturamento_total:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =======================
# GRÁFICOS
# =======================
col1, col2, col3 = st.columns(3)

# Cores suaves e consistentes com o tema
cores = ["#00C896", "#C084FC", "#FDE047", "#38BDF8", "#FB7185"]

# 1️⃣ Consultas por Unidade
consultas_unidade = df_filtrado.groupby("unidade").size().reset_index(name="Total Consultas")
fig1 = px.bar(
    consultas_unidade,
    x="unidade",
    y="Total Consultas",
    title="📊 Consultas por Unidade",
    color="unidade",
    color_discrete_sequence=cores
)

# 2️⃣ Consultas por Especialidade
consultas_tipo = df_filtrado.groupby("tipoconsulta").size().reset_index(name="Total")
fig2 = px.pie(
    consultas_tipo,
    values="Total",
    names="tipoconsulta",
    title="🩺 Consultas por Especialidade",
    hole=0.4,
    color_discrete_sequence=cores
)

# 3️⃣ Faturamento por Unidade
faturamento_unidade = df_filtrado.groupby("unidade")["valor"].sum().reset_index()
fig3 = px.bar(
    faturamento_unidade,
    x="unidade",
    y="valor",
    title="💰 Faturamento Total por Unidade",
    color="unidade",
    color_discrete_sequence=cores
)

col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)
col3.plotly_chart(fig3, use_container_width=True)

# =======================
# GRÁFICO DE LINHA - EVOLUÇÃO DAS CONSULTAS
# =======================
st.markdown("---")
st.markdown("### 📈 Evolução de Consultas ao Longo do Tempo")

evolucao = df_filtrado.groupby("dataconsulta").size().reset_index(name="Total Consultas")

fig4 = px.line(
    evolucao,
    x="dataconsulta",
    y="Total Consultas",
    markers=True,
    title="Tendência de Consultas por Data",
    color_discrete_sequence=["#00C896"]
)
fig4.update_traces(line=dict(width=3))
fig4.update_layout(xaxis_title="Data Consulta", yaxis_title="Total de Consultas")
st.plotly_chart(fig4, use_container_width=True)

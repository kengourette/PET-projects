import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io
from io import BytesIO
from io import StringIO

st.set_page_config(
    page_title="Дашборд для М-Тех",
    page_icon="✅",
    layout="wide",
)
st.markdown(':bar_chart: Для начала работы необходимо загрузить файл и выбрать значения на боковой панели')

# sidebar
with st.sidebar:
    uploaded_file = st.file_uploader("Загрузите файл CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(io.BytesIO(uploaded_file.read()))

st.sidebar.header("Фильтры")
age_bar = st.sidebar.multiselect("Выбрать возраст:",
                                 options=df['age'].unique(),
                                 default=None,
                                 max_selections=35
                                 )
work_days_bar = st.sidebar.multiselect("Выбрать количество дней, пропущенных по болезни:",
                                       options=df['work_days'].unique(),
                                       default=None,
                                       max_selections=9
                                       )
gender_bar = st.sidebar.multiselect("Выбрать пол сотрудника:",
                                    options=df['sex'].unique(),
                                    default=None,
                                    max_selections=2
                                    )
st.title("Дашборд для М-Тех")
# create two columns for charts
st.header('Графики распределения пропусков рабочих дней')
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    if gender_bar and work_days_bar:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[df['sex'].isin(gender_bar)]['work_days'],
                     color='blue',
                     alpha=0.5,
                     label=('Выбранный пол:', gender_bar))
        sns.histplot(df[df['work_days'].isin(work_days_bar)]['work_days'],
                     color='pink',
                     alpha=0.5,
                     label=('Пропуски:',work_days_bar))
        plt.xlabel('Рабочие дни, пропущенные по болезни')
        plt.ylabel('Количество сотрудников')
        plt.legend()
        plt.title('В зависимости от пола', fontsize=25)
        st.pyplot(fig, use_container_width=True)

with fig_col2:
    if age_bar and work_days_bar:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[df['age'].isin(age_bar)]['work_days'],
                     color='orange',
                     alpha=0.5,
                     label=('Выбранный возраст:', age_bar))
        sns.histplot(df[df['work_days'].isin(work_days_bar)]['work_days'],
                     color='green',
                     alpha=0.5,
                     label=('Пропуски:', work_days_bar))
        plt.xlabel('Рабочие дни, пропущенные по болезни')
        plt.ylabel('Количество')
        plt.legend()
        plt.title('В зависимости от возраста', fontsize=25)
        st.pyplot(fig, use_container_width=True)

# create two columns for metrics
kpi1, kpi2 = st.columns(2)
# fill in those two columns with respective metrics or KPIs
kpi1.metric(
    label="Гипотеза 1: Мужчины пропускают по болезни значимо чаще женщин",
    value='p-value = 0.433'
)

kpi2.metric(
    label="Гипотеза 2: Работники старше 35лет пропускают значимо чаще",
    value='p-value = 0.655'
)

#top-level filter
#st.header('Общая статистика пропущенных по болезни дней')
days_filter = st.selectbox('Меню для графика общей статистики: Выбрать количество пропущенных дней',
                           pd.unique(df['work_days']))

df = df[df['work_days'] == days_filter]
if work_days_bar:
    fig = px.bar(data_frame=df,
                 x='age',
                 y='work_days',
                 color='sex',
                 barmode='group',
                 title='Общая статистика пропущенных по болезни дней'
                 )
    st.write(fig)


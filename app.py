import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.image(r'C:\Users\T125029\Desktop\streamlit-app\img\symbol011.png',width=100) 

st.markdown("### 高校生のスマートフォンによるインターネット利用時間（平日）［都道府県別］令和６年度")

st.info('このアプリの使い方：左のサイドバーで条件を選んでください')

df = pd.read_csv('統計データ.csv')

with st.sidebar:
    st.subheader('都道府県（複数選択可）')
    prefectures = df['都道府県'].unique()
    prefectures = st.multiselect('都道府県を選択して下さい', prefectures, default=[])

    st.subheader('項目')
    item = st.selectbox('項目を選択してください',
        ['該当数','1時間未満','1時間以上2時間未満','2時間以上3時間未満','3時間以上4時間未満','4時間以上5時間未満','5時間以上6時間未満','6時間以上7時間未満','7時間以上8時間未満','8時間以上9時間未満','10時間以上11時間未満','11時間以上12時間未満','12時間以上','分からない','無回答'])
    
    st.subheader('グラフ表示')
    chart_type = st.radio(
        'グラフの種類を選択してください',
        options=['棒グラフ','散布図'],
    )

if prefectures:
    df = df[df['都道府県'].isin(prefectures)]
else:
    df = df

col = ['都道府県', item] if item in df.columns else df.columns

st.dataframe(df[col], width=600, height=200)

unit = '人'
x_label = '都道府県'
y_label = f'{item}（{unit}）'

chart_df = df[['都道府県', item]].copy()

if chart_type == '棒グラフ':
    fig = px.bar(chart_df, x='都道府県', y=item, labels={'都道府県': x_label, item: y_label})
else:
    fig = px.scatter(chart_df, x='都道府県', y=item, labels={'都道府県': x_label, item: y_label})

st.plotly_chart(fig)

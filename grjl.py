import streamlit as st
from datetime import datetime, timedelta
st.set_page_config(page_title="英雄简介", page_icon="", layout="wide")


st.title("英雄简历生成器")

st.header('英雄信息表')

    
st.markdown('***')

a1,a2=st.columns([1,2])

with a1:
    xingming = st.text_input('名称：', '')
    zhiwei = st.text_input('职业：', '')
    dianghua = st.text_input('获取方法：', '')
    youxiang = st.text_input('召唤方式', '')
    ate = st.date_input("获得日期", value=None)
    def my_format_func(option):
        return f'{option}'
    city = st.radio('种族：', ['精灵','人族','兽族','魔族'], format_func=my_format_func)
    dengji= st.text_input('等级', '')
    sld = st.radio('英雄熟练度：', ['低','中','高',], format_func=my_format_func)
    zdl= st.text_input('战斗力', '')
    def my_format_func(option):
        return f'{option}'

    options_l = st.multiselect(
        '出现地区',
        ['雪原', '沙漠', '高山', '海洋', '森林', '沼泽'],
        format_func=my_format_func,
        )
    w3 = st.time_input("出现时间", step=3600)
    ysbj = st.text_input('英雄背景：', '')
    uploaded_photo = st.file_uploader("图片",type=['png','jpg','jpeg'])
with a2:
    if uploaded_photo:
        st.image(uploaded_photo,width=300,caption='英雄')
    c1,c2=st.columns(2)
    with c1:
        st.header('英雄信息')
        st.write('名称：',xingming )
        st.write('职业：',zhiwei)
        st.write('获取方法：',dianghua)
        st.write('召唤方式：',youxiang )
        st.write("获得日期:", ate)

    with c2:
        st.header('')
        if city == '精灵':
            st.write('种族：**精灵**')
        elif city == '人族':
            st.write('种族：**人族**')
        elif city == '魔族':
            st.write('种族：**魔族**')
        else : 
            st.write('种族：**兽族**')
        st.write("等级:", dengji)
        if  sld== '低':
            st.write('熟练度：**低**')
        elif sld == '中':
            st.write('熟练度：**中**')
        else :
            st.write('熟练度：**高**')
        st.write("战斗力:", zdl)
        s=''
        for yuyan in options_l:
            s=s+yuyan+','
        st.write('出现地区:',s )
        st.write("出现时间:", w3)
    st.markdown('***')
    st.header("英雄背景:",ysbj )
    st.write(" ",ysbj )

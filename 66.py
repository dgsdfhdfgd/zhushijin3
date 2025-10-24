import streamlit as st
st.set_page_config(page_title='音乐',page_icon='🎵')
music = [
    {'url':'https://music.163.com/song/media/outer/url?id=2757544444.mp3',
     'photo':'http://p1.music.126.net/Snu9SMBRxB9k-OuKS1LbYw==/109951172181785487.jpg?param=130y130',
     'name':'开始懂了'},
    {'url':'https://music.163.com/song/media/outer/url?id=2600493765.mp3',
      'photo':'http://p2.music.126.net/1XNXI-PlmlIQAWSV8MCFxg==/109951163375899858.jpg?param=130y130',
     'name':'Young Again'},
    {'url':'https://music.163.com/song/media/outer/url?id=174956.mp3',
     'photo':'http://p2.music.126.net/a82aXr_eNkbFX0BkXuKvgg==/109951172050962571.jpg?param=130y130',
     'name':'坏女孩'}]
if 'ind' not in st.session_state:
    st.session_state['ind']=0


def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(music)
def prevImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(music)
a1,a2=st.columns([1,2])
with a1:
    st.image(music[st.session_state['ind']]['photo'])
with a2:
    st.text(music[st.session_state['ind']]['name'])
   

st.audio(music[st.session_state['ind']]['url'])
c1,c2=st.columns(2)
with c1:
    st.button('上一首',on_click=nextImg,use_container_width=True)
with c1:
    st.button('下一首',on_click=nextImg,use_container_width=True)

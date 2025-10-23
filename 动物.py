import streamlit as st


images = [
    {'url': 'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
          'parm':'鸟'
     },
    { 'url': 'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
       'parm':'狗'
     },
    {  'url': 'https://images2.alphacoders.com/716/71660.jpg',
        'parm': '猫'
     }
       ]
if 'ind' not in st.session_state:
    st.session_state['ind']=0

def nextImg():
   st.session_state['ind']=( st.session_state['ind']+1)%len(images)

def abc():
   st.session_state['ind']=( st.session_state['ind']-1)%len(images)

st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

c1,c2=st.columns(2)

with c1:
    st.button('上一张',on_click=abc,use_container_width=True)
with c2:
    st.button('下一张',on_click=nextImg,use_container_width=True)


import streamlit as st 
st.title("学生调档")

st.header("👱‍♂信息")     
st.text("ID：12345689")
st.text("学院：叼毛学院")     
st.text("专业：叼毛教育")

st.header("👱‍♂培养方向")
st.text(".                     在广西打工              去广东打工             去其它地打工")
st.text("就业工资：      3000                    6000                          不推荐   ")

st.header("👱‍♂培养花费")
import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '第1年':[908 ],
    '第2年':[820 ],
    '第3年':[967 ],
}
# 定义数据框所用的索引
index = pd.Series(['金额'], name=' ')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)


st.dataframe(df)
st.header("目前成果")
import streamlit as st
st.markdown(':red[什么也没有学会，准备重新学习]')







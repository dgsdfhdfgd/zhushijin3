import streamlit as st
import pandas as pd
import numpy as np
st.title('价格表')
data = {
    '肯德基1':[50,48,48,49,47,45,49,51,52,49,52,65],
    '肯德基2':[51,56,56,49,57,53,48,51,56,58,59,59],
    '陈健东龙虾馆':[125,126,145,126,158,142,125,156,145,125,125,126],
    '广顺牛巴王粉店':[15,12,12,13,14,16,12,15,14,12,12,15],
    '东门白切鸡':[104,109,165,126,135,156,123,154,124,109,120,123]
}
df = pd.DataFrame(data)

index = pd.Series(['1月', '2月', '3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'],name='月份')
df.index=index
st.dataframe(df)
image_path=r'D:\streamlit_env\111.jpeg'
st.image(image_path,caption='111')

st.title('价格走势')
st.line_chart(df)
st.title('评分')
st.bar_chart(df)

map_data={
    'latitude':[22.830435,22.823132,22.822598,22.820689,22.816610],
    'longitude':[108.370938,108.377450,108.378367,108.377514,108.375932]
    }
st.map(pd.DataFrame(map_data))


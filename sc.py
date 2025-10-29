import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -------------------- 基础配置 --------------------
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
st.set_page_config(layout="wide")  # 宽屏布局

# -------------------- 数据加载与处理 --------------------
@st.cache_data
def load_data():
    # 这里使用模拟数据，你可以替换为实际数据加载代码
    # 实际使用时请替换为：pd.read_excel("你的文件路径")
    data = {
        "城市": np.random.choice(["太原", "临汾", "大同", "运城", "长治"], 1000),
        "顾客类型": np.random.choice(["会员用户", "普通用户"], 1000),
        "性别": np.random.choice(["男性", "女性"], 1000),
        "总金额": np.random.randint(100, 1000, 1000),
        "评分": np.random.uniform(5, 10, 1000).round(1),
        "小时数": np.random.randint(9, 22, 1000),  # 9-21点
        "产品类型": np.random.choice(["食品饮料", "运动旅行", "电子配件", "时尚服饰", "家居生活", "健康美容"], 1000)
    }
    df = pd.DataFrame(data)
    df["评分"] = df["评分"].clip(5, 10).round(1)  # 确保评分在5-10之间
    return df

df = load_data()

# -------------------- 多选项筛选器实现 --------------------
st.sidebar.header("请筛选数据:")

# 城市筛选（支持多选）
st.sidebar.subheader("请选择城市:")
all_cities = df["城市"].unique().tolist()
selected_cities = st.sidebar.multiselect(
    "城市选项",
    all_cities,
    default=all_cities[:2],  # 默认选前两个城市
    format_func=lambda x: x
)
# 显示已选城市标签（模仿原型样式）
if selected_cities:
    city_tags = " ".join([f"{city} ×" for city in selected_cities]) + " ▼"
    st.sidebar.markdown(f"<div style='color: #333; background: #f0f2f6; padding: 5px 10px; border-radius: 4px; margin-top: 5px'>{city_tags}</div>", unsafe_allow_html=True)

# 顾客类型筛选（支持多选）
st.sidebar.subheader("请选择顾客类型:")
all_types = df["顾客类型"].unique().tolist()
selected_types = st.sidebar.multiselect(
    "类型选项",
    all_types,
    default=all_types,  # 默认全选
    format_func=lambda x: x
)
# 显示已选类型标签
if selected_types:
    type_tags = " ".join([f"{t} ×" for t in selected_types]) + " ▼"
    st.sidebar.markdown(f"<div style='color: #333; background: #f0f2f6; padding: 5px 10px; border-radius: 4px; margin-top: 5px'>{type_tags}</div>", unsafe_allow_html=True)

# 性别筛选（支持多选）
st.sidebar.subheader("请选择性别")
all_genders = df["性别"].unique().tolist()
selected_genders = st.sidebar.multiselect(
    "性别选项",
    all_genders,
    default=all_genders,  # 默认全选
    format_func=lambda x: x
)
# 显示已选性别标签
if selected_genders:
    gender_tags = " ".join([f"{g} ×" for g in selected_genders]) + " ▼"
    st.sidebar.markdown(f"<div style='color: #333; background: #f0f2f6; padding: 5px 10px; border-radius: 4px; margin-top: 5px'>{gender_tags}</div>", unsafe_allow_html=True)

# -------------------- 应用筛选条件 --------------------
filtered_df = df[
    (df["城市"].isin(selected_cities)) &
    (df["顾客类型"].isin(selected_types)) &
    (df["性别"].isin(selected_genders))
]

# -------------------- 主页面布局 --------------------
# 标题
st.markdown("""
    <div style='display: flex; align-items: center; gap: 10px; margin: 20px 0'>
        <div style='width: 30px; height: 30px; background: linear-gradient(45deg, #2ecc71, #3498db, #e74c3c); border-radius: 4px'></div>
        <h1 style='margin: 0'>销售仪表板</h1>
    </div>
""", unsafe_allow_html=True)

# 核心指标卡片
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    total_sales = filtered_df["总金额"].sum()
    st.markdown(f"<h4 style='color: #666; margin-bottom: 5px'>总销售额：</h4>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: #333; margin-top: 0'>RMB ¥ {total_sales:,.0f}</h2>", unsafe_allow_html=True)

with col2:
    avg_rating = filtered_df["评分"].mean().round(1)
    stars = "★" * int(avg_rating) + "☆" * (10 - int(avg_rating))  # 10星评分展示
    st.markdown(f"<h4 style='color: #666; margin-bottom: 5px'>顾客评分的平均值：</h4>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: #333; margin-top: 0'>{avg_rating} {stars}</h2>", unsafe_allow_html=True)

with col3:
    avg_per_order = filtered_df["总金额"].mean().round(2)
    st.markdown(f"<h4 style='color: #666; margin-bottom: 5px'>每单的平均销售额：</h4>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: #333; margin-top: 0'>RMB ¥ {avg_per_order:,.2f}</h2>", unsafe_allow_html=True)

st.divider()

# 图表区域
col4, col5 = st.columns(2, gap="medium")

# 按小时划分的销售额
with col4:
    st.subheader("按小时数划分的销售额")
    hourly_sales = filtered_df.groupby("小时数")["总金额"].sum().reset_index()
    # 确保所有小时都有数据（填补缺失小时）
    all_hours = pd.DataFrame({"小时数": range(9, 22)})  # 9-21点
    hourly_sales = pd.merge(all_hours, hourly_sales, on="小时数", how="left").fillna(0)
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x="小时数", y="总金额", data=hourly_sales, color="#3498db")
    plt.xlabel("小时数")
    plt.ylabel("销售额 (RMB)")
    plt.xticks(hourly_sales["小时数"])  # 显示所有小时刻度
    plt.tight_layout()
    st.pyplot(plt)
    plt.close()

# 按产品类型划分的销售额
with col5:
    st.subheader("按产品类型划分的销售额")
    product_sales = filtered_df.groupby("产品类型")["总金额"].sum().sort_values(ascending=False).reset_index()
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x="总金额", y="产品类型", data=product_sales, color="#3498db")
    plt.xlabel("总价 (RMB)")
    plt.ylabel("产品类型")
    plt.tight_layout()
    st.pyplot(plt)
    plt.close()

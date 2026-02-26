import streamlit as st
import requests

st.title("FIFA20 Player Gallery")

pace = st.slider("Pace", 0,100,60)
shooting = st.slider("Shooting",0,100,50)
passing = st.slider("Passing",0,100,50)
dribbling = st.slider("Dribbling",0,100,50)
defending = st.slider("Defending",0,100,50)
physical = st.slider("Physical",0,100,50)

if st.button("Predict"):
    payload = {
        "pace" : pace,
        "shooting" : shooting,
        "passing" : passing,
        "dribbling" : dribbling,
        "defending" : defending,
        "physical" : physical
    }

    response = requests.post(
        "http://127.0.0.1:8000/cluster",
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Cluster: {result['cluster_id']}")
        st.success(f"Player Type : {result['role']}")
    else:
        st.error("API error")

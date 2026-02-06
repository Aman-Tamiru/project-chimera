import streamlit as st
st.title("Project Chimera Vitals")
st.metric(label="Network", value="Base Sepolia")
st.metric(label="Agent ID", value="aman-chimera.basetest.eth")
st.write("### Recent Trends Processed")
st.table([{"Trend": "AI Agents", "Status": "Success"}])
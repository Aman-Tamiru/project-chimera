import streamlit as st

st.set_page_config(page_title="Chimera Vitals", page_icon="🦁")

st.title("🦁 Project Chimera: Agent Vitals")
st.markdown("---")

# Sidebar - Identity
st.sidebar.header("Agent Identity")
st.sidebar.info("aman-chimera.basetest.eth")
st.sidebar.success("Network: Base Sepolia")

# Main Stats
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Wallet Balance", value="0.042 ETH")
with col2:
    st.metric(label="System Status", value="Governed")

st.subheader("Recent Agent Trajectory")
st.table([
    {"Task": "Trend Research", "Status": "Success", "Timestamp": "2024-02-06 14:00"},
    {"Task": "Content Gen", "Status": "Verified", "Timestamp": "2024-02-06 14:05"},
    {"Task": "On-chain Post", "Status": "Pending", "Timestamp": "2024-02-06 14:10"},
])

st.write("---")
st.caption("Chimera Governance Layer: Active ✅")
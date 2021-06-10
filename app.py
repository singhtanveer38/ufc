import streamlit as st
from helper import loadData, fightersList, filteredData, plot

st.title("UFC RECORDS")

df = loadData("./ufcData/ufc-master.csv")
fighters = fightersList(df)

fighterName = st.selectbox("Select Fighter", fighters)

filteredData = filteredData(df, fighterName)

st.text(f"DOB: {filteredData.iloc[0][-1][:11]}\nHeight: {filteredData.iloc[0][-5]}\nWeight: {filteredData.iloc[0][-4]} pounds\nReach: {filteredData.iloc[0][-3]} inches\nStance: {filteredData.iloc[0][-2]}")

st.table(filteredData[["Event-Name","Fighter-2-Name", "W", "L", "D", "NC"]])

st.pyplot(plot(filteredData))

st.markdown("Created by: Tanveer Singh")
st.markdown("Email: singhtanveer38@yahoo.com")
st.markdown("[Github](https://github.com/singhtanveer38) [LinkedIn](https://www.linkedin.com/in/tanveer-singh-250b02194)")
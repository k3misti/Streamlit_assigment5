import streamlit as st
import pandas as pd

rovaniemi_df = pd.read_csv("https://pxdata.stat.fi/PxWeb/sq/1bf78c99-9372-4ac9-8881-f88228916946", encoding="latin-1")
rovaniemi_df[["Vuosi", "Kuukausinumero"]] = rovaniemi_df["Kuukausi"].str.split("M", expand=True)


st.dataframe(rovaniemi_df)


huone_aste_roi_df = rovaniemi_df[["Kuukausi", "Huonekäyttöaste, % Rovaniemi"]]

st.line_chart(huone_aste_roi_df, x="Kuukausi", y="Huonekäyttöaste, % Rovaniemi")

vuosi_yo_roi_df = rovaniemi_df[["Vuosi","Yöpymiset, lkm Rovaniemi"]].groupby(by="Vuosi").sum()
#st.dataframe(vuosi_yo_roi_df)

st.bar_chart(vuosi_yo_roi_df)
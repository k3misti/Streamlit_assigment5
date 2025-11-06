import streamlit as st
import pandas as pd

rovaniemi_df = pd.read_csv("https://pxdata.stat.fi/PxWeb/sq/1bf78c99-9372-4ac9-8881-f88228916946", encoding="latin-1")
rovaniemi_df[["Vuosi", "Kuukausinumero"]] = rovaniemi_df["Kuukausi"].str.split("M", expand=True)

st.title("Hotellien kuukausittainen kapasiteetti ja yöpymiskustannukset")


st.dataframe(rovaniemi_df)


huone_aste_roi_df = rovaniemi_df[["Kuukausi", "Huonekäyttöaste, % Rovaniemi"]]

st.line_chart(huone_aste_roi_df, x="Kuukausi", y="Huonekäyttöaste, % Rovaniemi")

vuosi_yo_roi_df = rovaniemi_df[["Vuosi","Yöpymiset, lkm Rovaniemi"]].groupby(by="Vuosi").sum()
#st.dataframe(vuosi_yo_roi_df)

st.bar_chart(vuosi_yo_roi_df)

temp_df = rovaniemi_df[["Vuosi","Kotimaiset yöpymiset, lkm Rovaniemi", "Ulkomaiset yöpymiset Rovaniemi"]]
temp_df["Ulkomaiset yöpymiset Rovaniemi"] = temp_df["Ulkomaiset yöpymiset Rovaniemi"].str.replace(".", "")
temp_df["Ulkomaiset yöpymiset Rovaniemi"] = pd.to_numeric(temp_df["Ulkomaiset yöpymiset Rovaniemi"])
vuosi_yo_ulkomaiset_roi_df = temp_df.groupby(by="Vuosi").sum()
st.dataframe(vuosi_yo_ulkomaiset_roi_df)

st.line_chart(vuosi_yo_ulkomaiset_roi_df)

#huone_hinta_df = rovaniemi_df[["Kuukausi" ,"Huoneen keskihinta Rovaniemi", "Huonekäyttöaste, % Rovaniemi"]]

rovaniemi_df["Huoneen keskihinta Rovaniemi"] = rovaniemi_df["Huoneen keskihinta Rovaniemi"].str.replace(".", "")
rovaniemi_df["Huoneen keskihinta Rovaniemi"] = pd.to_numeric(rovaniemi_df["Huoneen keskihinta Rovaniemi"])
#rovaniemi_df["Yöpymiset, lkm Rovaniemi"] = rovaniemi_df["Yöpymiset, lkm Rovaniemi"].str.replace(".", "")
rovaniemi_df["Yöpymiset, lkm Rovaniemi"] = pd.to_numeric(rovaniemi_df["Yöpymiset, lkm Rovaniemi"])
st.area_chart(rovaniemi_df, x = "Kuukausi", y = ["Huoneen keskihinta Rovaniemi", "Yöpymiset, lkm Rovaniemi"])

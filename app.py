import streamlit as st
import pandas as pd

# Configuración para smartphones
st.set_page_config(page_title="Tenis Live", layout="centered")

st.title("🎾 Marcador en Vivo")

# AQUÍ DEBES PEGAR TU LINK DE GOOGLE SHEETS PUBLICADO COMO CSV
# Por ahora dejo uno de ejemplo para que no de error
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRzTscK5RW5EkLnFnk3ZFbcoMU746ws-XZVYZoanTpx_Uo7aiijpbsM0cxbyLbZNxxBL8I_8G9ehoB-/pubhtml"

def load_data():
    try:
        return pd.read_csv(SHEET_URL)
    except:
        return None

df = load_data()

if df is not None:
    for index, row in df.iterrows():
        # Contenedor estilo tarjeta
        with st.container():
            st.markdown(f"### {row['Torneo']}")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label=row['Jugador 1'], value=str(row['Marcador_Visual_J1']))
            with col2:
                st.metric(label=row['Jugador 2'], value=str(row['Marcador_Visual_J2']))
            
            # Etiqueta de estado
            if row['Estado'] == "EN VIVO":
                st.success(f"Estado: {row['Estado']}")
            else:
                st.info(f"Estado: {row['Estado']}")
            st.divider()
else:
    st.warning("Configurando conexión con el Excel... Asegurate de publicar el Google Sheet como CSV y pegar el link en el código.")

# Botón de actualización manual
if st.button('🔄 Actualizar Marcador'):
    st.rerun()

import streamlit as st
import json
import pandas as pd
import os

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="QGB Network Explorer", layout="wide")

# TÍTULO Y ESTILO
st.title("⚛️ QGB NETWORK: QUANTUM GENESIS BLOCK")
st.markdown("### El estándar financiero respaldado por entropía cuántica")
st.markdown("---")

# FUNCIÓN PARA LEER TU BASE DE DATOS REAL
def load_ledger():
    if os.path.exists("qgb_database.json"):
        with open("qgb_database.json", "r") as f:
            return json.load(f)
    else:
        return None

# CARGAMOS LOS DATOS
ledger = load_ledger()

if ledger:
    # CÁLCULOS
    admin_address = "0xd0aa7d261271b8ad9e5a9467c019b4b1addf83ce"
    marketing_address = "0xMARKETING_FUND_DEV_ALLOCATION_888"
    
    admin_balance = ledger.get(admin_address, 0)
    marketing_balance = ledger.get(marketing_address, 0)
    
    # PRECIO SIMULADO (TÚ CONTROLAS ESTO POR AHORA)
    price_per_qgb = 1.35 
    admin_usd_value = admin_balance * price_per_qgb

    # --- MÉTRICAS PRINCIPALES ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="💰 TU SALDO (ADMIN)", value=f"{admin_balance:,.0f} QGB")
    
    with col2:
        st.metric(label="💵 VALOR ESTIMADO (USD)", value=f"${admin_usd_value:,.2f}", delta="Persistente")
        
    with col3:
        st.metric(label="🏦 FONDO MARKETING", value=f"{marketing_balance:,.0f} QGB")

    # --- VISUALIZACIÓN DE LA RED ---
    st.markdown("---")
    st.subheader("📊 Distribución del Suministro")
    
    # Creamos una tabla bonita
    df = pd.DataFrame(list(ledger.items()), columns=['Dirección (Billetera)', 'Saldo (QGB)'])
    st.table(df)

    # BARRA DE ESTADO
    st.success(f"✅ CONEXIÓN ESTABLECIDA CON NODO LOCAL. BASE DE DATOS: qgb_database.json")

else:
    st.error("⚠️ NO SE ENCUENTRA LA BASE DE DATOS. EJECUTA PRIMERO 'python3 qgb_core.py'")

# PIE DE PÁGINA CON TU HASH GÉNESIS
st.markdown("---")
st.caption("Genesis Hash: ec686b3ae0264997a555e3ce72c3cb31acd08a3f666197a11d5318d77b26ce1a")

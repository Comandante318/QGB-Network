import streamlit as st
import json
import pandas as pd
import os
import time
import random

# --- CONFIGURACIÓN DE LA PÁGINA (MODO CINE) ---
st.set_page_config(
    page_title="QGB NETWORK | Quantum Interface",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS AVANZADOS (AQUÍ ESTÁ LA MAGIA VISUAL) ---
st.markdown("""
    <style>
    /* FONDO Y COLORES PRINCIPALES */
    .stApp {
        background-color: #0e0e12;
        background-image: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #000000 100%);
        color: #E6E6FA;
    }
    
    /* TEXTOS Y TÍTULOS */
    h1, h2, h3 {
        color: #D8BFD8 !important; /* Púrpura Claro */
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #9370DB;
    }
    
    /* TARJETAS DE DATOS (GLASSMORPHISM) */
    div[data-testid="stMetric"] {
        background-color: rgba(30, 30, 40, 0.7);
        border: 1px solid #9370DB;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(147, 112, 219, 0.2);
    }
    
    /* BOTONES */
    .stButton>button {
        background-color: #4B0082;
        color: white;
        border: 1px solid #D8BFD8;
        border-radius: 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #9370DB;
        box-shadow: 0 0 20px #D8BFD8;
        transform: scale(1.05);
    }

    /* ANIMACIÓN DEL ÁTOMO CUÁNTICO */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .atom {
        position: relative;
        width: 100px;
        height: 100px;
        margin: 20px auto;
        border-radius: 50%;
        border: 2px solid rgba(216, 191, 216, 0.3);
        box-shadow: 0 0 20px #9370DB;
    }
    .atom::before, .atom::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 50%;
        border: 2px solid transparent;
        border-top: 2px solid #D8BFD8;
        border-bottom: 2px solid #D8BFD8;
        animation: spin 3s linear infinite;
    }
    .atom::after {
        transform: rotate(90deg);
        animation: spin 5s linear infinite;
    }
    
    /* BARRA LATERAL */
    section[data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIONES DE LÓGICA (BACKEND) ---
DB_FILE = "qgb_database.json"

def load_ledger():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_ledger(ledger):
    with open(DB_FILE, "w") as f:
        json.dump(ledger, f, indent=4)

def execute_transfer(sender, receiver, amount):
    ledger = load_ledger()
    sender_bal = ledger.get(sender, 0)
    
    if sender_bal >= amount:
        ledger[sender] = sender_bal - amount
        ledger[receiver] = ledger.get(receiver, 0) + amount
        save_ledger(ledger)
        return True, "Transacción Exitosa y Persistente."
    else:
        return False, "Fondos Insuficientes en la red."

# --- INTERFAZ PRINCIPAL ---

# 1. BARRA LATERAL DE NAVEGACIÓN
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Atom_symbol.svg/100px-Atom_symbol.svg.png", width=50) # Placeholder atom
    st.title("QGB NETWORK")
    st.caption("Quantum Genesis Block v1.0")
    st.markdown("---")
    
    menu = st.radio("SISTEMA DE NAVEGACIÓN", 
        ["📡 DASHBOARD CENTRAL", "💸 BILLETERA / TRANSFERIR", "🔍 EXPLORADOR DE BLOQUES", "🤖 GENESIS AI"])
    
    st.markdown("---")
    st.info("🟢 NODO ACTIVO: Laptop-01\n\n🔒 CONEXIÓN: Segura\n\n⚛️ ENTROPÍA: Estable")

# CARGAR DATOS
ledger = load_ledger()
my_address = "0xd0aa7d261271b8ad9e5a9467c019b4b1addf83ce"
marketing_address = "0xMARKETING_FUND_DEV_ALLOCATION_888"
balance = ledger.get(my_address, 0)

# --- SECCIÓN 1: DASHBOARD ---
if menu == "📡 DASHBOARD CENTRAL":
    st.markdown("<div style='text-align: center;'><h1>QGB COMMAND CENTER</h1></div>", unsafe_allow_html=True)
    
    # Animación del Átomo
    st.markdown('<div class="atom"></div>', unsafe_allow_html=True)
    
    # Métricas Principales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("TU SALDO TOTAL", f"{balance:,.0f} QGB", "Persistente")
    with col2:
        val_usd = balance * 1.35
        st.metric("VALOR MERCADO (USD)", f"${val_usd:,.2f}", "+1.2% Hoy")
    with col3:
        st.metric("SUMINISTRO CIRCULANTE", "21,000,000 QGB", "Fijo")

    st.markdown("---")
    
    # Simulación de Drones / Actividad
    st.subheader("🛰️ VISTA DE DRONES: ACTIVIDAD DE RED")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        # Gráfica simulada de actividad cuántica
        chart_data = pd.DataFrame(
            [random.randint(10, 50) for _ in range(20)],
            columns=["Entropía"]
        )
        st.line_chart(chart_data, color="#D8BFD8")
    with c2:
        st.write("📍 **Zonas Activas:**")
        st.code("""
        > Sector Alpha: ONLINE
        > Sector Beta:  ONLINE
        > Nodo Maestro: SINCRONIZADO
        > Amenazas:     NINGUNA
        """)

# --- SECCIÓN 2: BILLETERA ---
elif menu == "💸 BILLETERA / TRANSFERIR":
    st.title("💸 TRANSFERENCIA CUÁNTICA")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 📤 Enviar Fondos")
        destinatario = st.text_input("Dirección de Destino (0x...)", value=marketing_address)
        monto = st.number_input("Cantidad de QGB", min_value=1.0, max_value=float(balance))
        
        if st.button("AUTORIZAR ENVÍO"):
            with st.spinner("Validando firma cuántica..."):
                time.sleep(1.5) # Efecto dramático
                success, msg = execute_transfer(my_address, destinatario, monto)
                if success:
                    st.success(f"✅ {msg}")
                    st.balloons()
                    time.sleep(1)
                    st.rerun() # Recargar para ver el nuevo saldo
                else:
                    st.error(f"❌ {msg}")

    with col_b:
        st.markdown("### 💳 Tu Tarjeta Digital")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4B0082, #000); padding: 20px; border-radius: 15px; border: 1px solid #D8BFD8;">
            <h3 style="color:white !important; margin:0;">QGB VISUAL CARD</h3>
            <p style="color:#aaa;">Standard Genesis Member</p>
            <br>
            <h2 style="color:white !important;">{balance:,.0f} QGB</h2>
            <p style="color:white; font-family: monospace;">{my_address[:10]}...{my_address[-5:]}</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECCIÓN 3: EXPLORADOR ---
elif menu == "🔍 EXPLORADOR DE BLOQUES":
    st.title("🔍 LEDGER PÚBLICO")
    
    search = st.text_input("🔎 Buscar dirección o hash de transacción...")
    
    st.markdown("### 📋 Cuentas Registradas")
    
    # Convertir el JSON a una tabla bonita
    df = pd.DataFrame(list(ledger.items()), columns=['Dirección', 'Saldo (QGB)'])
    st.dataframe(df, use_container_width=True)

# --- SECCIÓN 4: GENESIS AI ---
elif menu == "🤖 GENESIS AI":
    st.title("🤖 ASISTENTE VIRTUAL GÉNESIS")
    
    c1, c2 = st.columns([1, 3])
    with c1:
        st.markdown("""
        <div style="border: 2px solid #D8BFD8; border-radius: 50%; width: 150px; height: 150px; display: flex; align-items: center; justify-content: center; background-color: black;">
            <h1 style="margin: 0;">AI</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        > **SISTEMA:** Hola, Saúl. Soy la interfaz de Inteligencia Cuántica.
        >
        > He analizado tu Hash Génesis `ec68...ce1a`. La estructura es estable.
        > El mercado muestra un interés potencial del 85% basado en la escasez de tus 21 Millones.
        """)
        
        user_ask = st.text_input("Pregúntale algo a la Red...")
        if user_ask:
            st.write(f"🧠 **Análisis:** Procesando '{user_ask}' con entropía de IBM Torino... (Simulación)")

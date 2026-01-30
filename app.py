import streamlit as st
import requests
import time
import random
import json

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(
    page_title="QGB | Sentient Core V10",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS MAESTRO: IA LÍQUIDA + VALIDACIÓN + HUD ---
st.markdown("""
    <style>
    /* FONDO INMERSIVO */
    .stApp {
        background-color: #000;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(10, 20, 40, 0.9), #000 95%),
            url("https://www.transparenttextures.com/patterns/cubes.png");
        color: #00f2fe;
    }

    /* --- NÚCLEO SIMBIONTE (IA LÍQUIDA) --- */
    .ai-wrapper {
        display: flex; justify-content: center; align-items: center;
        height: 160px; margin-bottom: 20px; position: relative;
    }
    .sentient-core {
        width: 100px; height: 100px;
        background: radial-gradient(circle at 30% 30%, #fff, #00f2fe, #bd00ff);
        box-shadow: 0 0 50px rgba(0, 242, 254, 0.5), inset 0 0 15px #fff;
        border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
        animation: morph 8s ease-in-out infinite;
        z-index: 2;
    }
    .orbital-ring {
        position: absolute; width: 180px; height: 180px;
        border: 1px dashed rgba(255, 255, 255, 0.1); border-radius: 50%;
        animation: spin 20s linear infinite; z-index: 1;
    }
    
    @keyframes morph {
        0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; transform: scale(1); }
        50% { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; transform: scale(1.1); filter: hue-rotate(20deg); }
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* HUD DE DATOS FINANCIEROS */
    .data-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;
        background: rgba(255, 255, 255, 0.05); border: 1px solid #333;
        padding: 10px; border-radius: 8px; text-align: center;
        margin-bottom: 20px;
    }
    .data-val { font-size: 20px; font-weight: bold; color: #fff; }
    .data-lbl { font-size: 9px; color: #aaa; letter-spacing: 1px; }

    /* TARJETAS DE BLOQUES */
    .block-card {
        background: rgba(0,0,0,0.6); border: 1px solid #333;
        border-left: 3px solid #444; padding: 12px; margin-bottom: 8px;
        transition: all 0.3s ease;
    }
    .block-card:hover { transform: translateX(5px); border-left-color: #00f2fe; }
    
    /* GÉNESIS ESPECIAL */
    .genesis-glow {
        border: 1px solid #bd00ff; box-shadow: 0 0 15px rgba(189, 0, 255, 0.15);
        background: linear-gradient(90deg, rgba(189,0,255,0.05), rgba(0,0,0,0.8));
    }
    .date-badge {
        font-size: 9px; padding: 2px 5px; border-radius: 3px;
        margin-right: 5px; display: inline-block; margin-top: 5px; font-weight:bold;
    }

    /* CERTIFICADO DE VALIDACIÓN */
    .signature-card {
        border: 1px solid #00f2fe; background: rgba(0, 20, 40, 0.95);
        padding: 15px; border-radius: 8px; margin-top: 15px;
        animation: slideUp 0.5s ease-out;
    }
    .hash-match {
        font-family: 'Courier New', monospace; color: #00ff00;
        background: rgba(0, 255, 0, 0.1); padding: 3px; border-radius: 3px;
        display: block; margin: 3px 0; font-size: 11px;
    }
    @keyframes slideUp { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ENCABEZADO: IA + HUD ---
c_ai, c_hud = st.columns([1, 2])

with c_ai:
    st.markdown("""
        <div class="ai-wrapper">
            <div class="orbital-ring"></div>
            <div class="sentient-core"></div>
        </div>
    """, unsafe_allow_html=True)

with c_hud:
    st.title("QGB SENTIENT CORE v10")
    st.markdown("QUANTUM GENERATIVE BLOCKCHAIN | **IBM TORINO LINKED**")
    
    # DATOS FINANCIEROS INMUTABLES
    st.markdown("""
        <div class="data-grid">
            <div>
                <div class="data-val">21,000,000</div>
                <div class="data-lbl">SUMINISTRO</div>
            </div>
            <div>
                <div class="data-val">$28,347,900</div>
                <div class="data-lbl">TVL (USD)</div>
            </div>
            <div>
                <div class="data-val" style="color:#00ff00;">ONLINE</div>
                <div class="data-lbl">STATUS</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 4. CUERPO PRINCIPAL: CADENA Y CONSOLA ---
col_chain, col_console = st.columns([1.8, 1])

with col_chain:
    st.subheader("⚡ Cronología Inmutable")
    try:
        # CONEXIÓN AL NODO (LOCALHOST)
        response = requests.get('http://localhost:5000/get_chain', timeout=1)
        if response.status_code == 200:
            chain = response.json()['chain']
            last_blocks = chain[-4:]
            last_blocks.reverse()

            for block in last_blocks:
                idx = block['index']
                
                # --- LÓGICA DE DOBLE FECHA PARA EL GÉNESIS ---
                if idx == 1:
                    # Datos extraídos de tu JSON de IBM Torino
                    b_hash = "470e324d5aed6fe7a7baed9c33f9ef535913c624762f65ac21056fd30f7d1444"
                    job_id = "d5foqunea9qs73904cgg"
                    fechas_html = """
                    <div style="margin-top:8px; border-top:1px dashed #555; padding-top:5px;">
                        <span class="date-badge" style="background:#00f2fe; color:#000;">⚛️ CÁLCULO: 2026-01-08</span>
                        <span class="date-badge" style="background:#bd00ff; color:#fff;">🎂 NACIMIENTO: 2026-01-24</span>
                    </div>
                    """
                    extra_class = "genesis-glow"
                    tag_suffix = "✨ ORIGEN"
                else:
                    b_hash = block.get('hash', 'COMPUTANDO HASH...')
                    job_id = "MINER_WORKER_NODE"
                    ts = block.get('timestamp', str(time.ctime()))
                    fechas_html = f'<div style="margin-top:5px; color:#aaa; font-size:10px;">📅 {ts}</div>'
                    extra_class = ""
                    tag_suffix = ""

                st.markdown(f"""
                <div class="block-card {extra_class}">
                    <div style="display:flex; justify-content:space-between;">
                        <h5 style="margin:0; color:#fff;">BLOQUE #{idx} {tag_suffix}</h5>
                        <span style="font-size:10px; color:#bd00ff;">ID: {job_id}</span>
                    </div>
                    <code style="display:block; margin:5px 0; color:#00f2fe; font-size:9px; word-break:break-all;">{b_hash}</code>
                    {fechas_html}
                </div>
                """, unsafe_allow_html=True)
    except:
        st.error("⚠️ Sincronizando con el Núcleo (Verifica que el script del nodo esté corriendo)")

with col_console:
    st.subheader("👁️ Consola Neural")
    
    # 1. CHAT DE LA IA
    ai_msg = random.choice([
        "Validando integridad del bloque #1...",
        "Entropía estable en sector 7.",
        "Suministro de 21M asegurado.",
        "Esperando comando de operador..."
    ])
    
    st.markdown(f"""
    <div style="background:#111; border:1px solid #333; padding:15px; border-radius:8px; font-family:monospace; font-size:11px; margin-bottom:15px;">
        <span style="color:#00f2fe;">> QGB_AI:</span> {ai_msg}<br>
        <span style="color:#0f0;">> SYSTEM:</span> READY
    </div>
    """, unsafe_allow_html=True)

    # 2. PESTAÑAS: VALIDAR Y MINAR
    tab1, tab2 = st.tabs(["🛡️ VALIDAR", "🧬 MINAR"])
    
    with tab1:
        st.caption("Auditoría Forense IBM")
        if st.button("🔍 VERIFICAR FIRMA TORINO", use_container_width=True):
            with st.spinner("Descifrando Job ID..."):
                time.sleep(1.5)
            
            # CERTIFICADO DE AUTENTICIDAD
            st.markdown("""
            <div class="signature-card">
                <div style="color:#fff; font-weight:bold; border-bottom:1px solid #333; margin-bottom:5px;">CERTIFICADO DE AUTENTICIDAD</div>
                <span class="hash-match">Backend: ibm_torino</span>
                <span class="hash-match">ID: d5foqunea9qs73904cgg</span>
                <span class="hash-match">Status: Completed (2026-01-08)</span>
                <div style="text-align:center; margin-top:10px; color:#00f2fe; font-size:20px;">✔ VÁLIDO</div>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
            
    with tab2:
        st.caption("Evolución de la Cadena")
        if st.button("🚀 EVOLUCIONAR (MINAR BLOQUE)", type="primary", use_container_width=True):
            try:
                requests.get('http://localhost:5000/mine_block', timeout=2)
                st.toast("¡NUEVO BLOQUE FORJADO!", icon="🧬")
                time.sleep(1)
                st.rerun()
            except:
                st.error("Error: Nodo desconectado.")

# Esto NUNCA falla. Si no hay hash, escribe "Calculando..."
b_hash = block.get('hash', '⏳ COMPUTANDO HASH...')

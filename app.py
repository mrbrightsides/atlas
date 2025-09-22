import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SAFE",
    page_icon="📍",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **RANTAI SAFE** Community Report adalah modul blockchain decentralized yang mendukung pelaporan risiko dan kejadian di lapangan dengan transparansi dan auditabilitas penuh. Laporan masyarakat disimpan immutable di blockchain, memastikan data valid, terlacak, dan dapat diverifikasi oleh publik serta otoritas terkait.  
    
    ---
    #### 🔮 Vision Statement
    
    Menjadi sistem pelaporan risiko terdesentralisasi terdepan yang memberdayakan masyarakat dan institusi dengan data terpercaya, sekaligus mendorong keamanan, keberlanjutan, dan ketahanan komunitas melalui teknologi blockchain. Kami percaya transparansi dan kolaborasi berbasis teknologi adalah kunci menuju lingkungan hidup yang lebih aman dan inklusif.
    
    ---
    ### 🧩 STC Ecosystem
    
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ☂ RANTAI Communities
    
    1. [Learn3](https://learn3.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    5. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    6. [Business Intelligence](https://rantai-busi.streamlit.app/)
    7. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    8. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    9. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    10. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    11. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    12. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    13. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    14. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    15. [Real-time Social Sentiment](https://rantai-rss.streamlit.app/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/safe)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <div style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/aa9f2999-7033-4b9a-a990-82311edcf10b"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, hide_bottom_px = 12, height=800)

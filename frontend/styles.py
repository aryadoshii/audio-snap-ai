import streamlit as st

def load_css():
    # Inject Qubrid-style favicon via JS (Streamlit page_icon only accepts emoji/path)
    st.markdown(f"""
    <script>
        var link = window.parent.document.querySelector("link[rel*='icon']") || window.parent.document.createElement('link');
        link.type = 'image/png';
        link.rel = 'shortcut icon';
        link.href = 'data:image/png;base64,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';
        window.parent.document.getElementsByTagName('head')[0].appendChild(link);

    """, unsafe_allow_html=True)

    # Nuclear option: hide mode buttons and fix sidebar toggle via JS + inline style injection
    st.markdown("""
    <script>
    (function() {
        var MODE_LABELS = ["Upload File", "YouTube URL", "Record Live"];

        function fixButtons() {
            var doc = window.parent.document;

            // Kill white bg on ALL stButton wrappers
            doc.querySelectorAll("[data-testid=stButton]").forEach(function(w) {
                w.style.background = "transparent";
                w.style.boxShadow = "none";
                w.style.border = "none";
            });

            // Hide the 3 mode selector buttons by their exact label text
            doc.querySelectorAll("button[kind=secondary]").forEach(function(btn) {
                var t = (btn.innerText || btn.textContent || "").trim();
                if (MODE_LABELS.indexOf(t) !== -1) {
                    var wrap = btn.closest("[data-testid=stButton]");
                    if (wrap) {
                        wrap.style.cssText = "background:transparent!important;border:none!important;box-shadow:none!important;margin-top:-108px!important;height:108px!important;position:relative!important;overflow:visible!important;z-index:10!important;";
                    }
                    btn.style.cssText = "opacity:0!important;width:100%!important;height:108px!important;cursor:pointer!important;background:transparent!important;border:none!important;box-shadow:none!important;display:block!important;";
                }
            });
        }
        fixButtons();
        new MutationObserver(fixButtons).observe(window.parent.document.body, {childList:true, subtree:true});
    })();
    </script>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        /* ── Favicon inject (Qubrid Q logo as SVG) ────────────────────────────── */

        /* ── Force hero subtitle truly centered in flex context ─────────────── */
        .hero-wrap { display: flex !important; flex-direction: column !important; align-items: center !important; }
        .hero-wrap * { text-align: center !important; }

        html, body, .stApp {
            background: radial-gradient(ellipse at 25% 20%, #0a2020 0%, #071a1a 45%, #040f0f 100%);
            font-family: 'Inter', sans-serif;
            color: #e2e8f0;
        }
        .stApp::before {
            content: ''; position: fixed; top: -10%; left: -5%;
            width: 700px; height: 700px;
            background: radial-gradient(circle, rgba(20,184,166,0.18) 0%, transparent 65%);
            border-radius: 50%; pointer-events: none; z-index: 0;
        }
        .stApp::after {
            content: ''; position: fixed; bottom: -15%; right: -5%;
            width: 600px; height: 600px;
            background: radial-gradient(circle, rgba(6,182,212,0.14) 0%, transparent 65%);
            border-radius: 50%; pointer-events: none; z-index: 0;
        }
        header { visibility: hidden; }
        .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 100%; position: relative; z-index: 1; padding-left: 1.5rem !important; padding-right: 1.5rem !important; }

        /* ── Force ALL text white ───────────────────────────────────────────────── */
        p, span, div, label, li, td, th, .stMarkdown,
        [data-testid="stText"], [data-testid="stMarkdownContainer"] { color: #e2e8f0; }
        .stDataFrame td, .stDataFrame th { color: #e2e8f0 !important; background: transparent !important; }
        .stDataFrame thead th { color: #5eead4 !important; background: rgba(20,184,166,0.1) !important; font-size: 0.75rem !important; text-transform: uppercase; letter-spacing: 0.06em; }
        [data-testid="stFileUploader"] label, [data-testid="stFileUploader"] span { color: #94a3b8 !important; }

        /* ── Sidebar ────────────────────────────────────────────────────────────── */
        /* Native sidebar hidden — we use column layout instead */
        section[data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }

        /* ── Centered Hero ──────────────────────────────────────────────────────── */
        .hero-wrap { text-align: center; padding: 52px 0 44px 0; }
        .hero-badge { display: none; }   /* moved to footer */
        .footer-badge {
            position: fixed; bottom: 18px;
            left: 0; right: 0; width: fit-content;
            margin: 0 auto;
            background: rgba(10,13,28,0.85);
            border: 1px solid rgba(20,184,166,0.2);
            color: #475569 !important; font-size: 0.68rem; font-weight: 600;
            letter-spacing: 0.1em; text-transform: uppercase;
            padding: 6px 18px; border-radius: 20px;
            backdrop-filter: blur(12px); z-index: 9999;
            white-space: nowrap; display: flex; align-items: center; gap: 7px;
        }
        .hero-title {
            font-size: 4.4rem; font-weight: 900; margin: 0 0 12px 0; line-height: 1.05;
            color: #ffffff;
            letter-spacing: -0.03em;
            text-shadow: 0 0 60px rgba(20,184,166,0.4), 0 2px 4px rgba(0,0,0,0.5);
        }
        /* Override Streamlit's h1 reset inside hero */
        .hero-wrap h1.hero-title {
            font-size: 4.4rem !important; font-weight: 900 !important;
            margin: 0 0 12px 0 !important; line-height: 1.05 !important;
            color: #ffffff !important; letter-spacing: -0.03em !important;
            text-shadow: 0 0 60px rgba(20,184,166,0.4), 0 2px 4px rgba(0,0,0,0.5);
            padding: 0 !important;
        }
        .hero-tagline {
            color: #64748b !important; font-size: 0.88rem; font-weight: 400;
            letter-spacing: 0.01em; margin: 0 0 14px 0; line-height: 1.6;
        }
        .tagline-highlight {
            color: #5eead4 !important; font-weight: 700;
            background: rgba(20,184,166,0.12);
            padding: 1px 7px; border-radius: 5px;
            border: 1px solid rgba(20,184,166,0.3);
        }
        .tagline-dim {
            color: #475569 !important; font-weight: 500;
        }
        .hero-subtitle {
            color: #64748b !important; font-size: 1rem; margin: 0 auto 4px auto;
            max-width: 560px; line-height: 1.7;
            text-align: center !important; width: 100%; display: block;
        }

        /* ── Animated Progress Bars ─────────────────────────────────────────────── */
        @keyframes flow {
            0%   { transform: translateX(-100%); }
            100% { transform: translateX(400%); }
        }
        @keyframes flowSlow {
            0%   { transform: translateX(-100%); }
            100% { transform: translateX(400%); }
        }
        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50%       { opacity: 0.4; transform: scale(0.7); }
        }
        .progress-wrap {
            background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.07);
            border-radius: 16px; padding: 28px 32px; margin: 8px 0 24px 0;
        }
        .progress-label {
            font-size: 0.8rem; font-weight: 600; color: #5eead4 !important;
            letter-spacing: 0.05em; margin-bottom: 18px;
            display: flex; align-items: center; gap: 10px;
        }
        .pulse-dot {
            width: 8px; height: 8px; background: #14b8a6; border-radius: 50%;
            animation: pulse-dot 1.2s ease-in-out infinite;
        }
        .progress-track {
            background: rgba(255,255,255,0.05); border-radius: 999px;
            height: 5px; overflow: hidden; margin-bottom: 10px; position: relative;
        }
        .progress-bar-1 {
            position: absolute; top: 0; left: 0; height: 100%; width: 35%;
            background: linear-gradient(90deg, transparent, #0d9488, #0891b2, transparent);
            border-radius: 999px;
            animation: flow 2s ease-in-out infinite;
        }
        .progress-bar-2 {
            position: absolute; top: 0; left: 0; height: 100%; width: 25%;
            background: linear-gradient(90deg, transparent, #06b6d4, #22d3ee, transparent);
            border-radius: 999px;
            animation: flow 2.8s ease-in-out infinite 0.6s;
        }
        .progress-bar-3 {
            position: absolute; top: 0; left: 0; height: 100%; width: 45%;
            background: linear-gradient(90deg, transparent, #14b8a6, #0d9488, transparent);
            border-radius: 999px;
            animation: flow 3.4s ease-in-out infinite 1.2s;
        }
        .progress-step {
            font-size: 0.75rem; color: #475569 !important; margin-top: 4px; padding-left: 2px;
        }



        /* ── Tabs ───────────────────────────────────────────────────────────────── */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(255,255,255,0.03); border-radius: 12px;
            padding: 4px; gap: 4px; border: 1px solid rgba(255,255,255,0.06);
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px; color: #64748b !important; font-weight: 500;
            font-size: 0.875rem; padding: 8px 16px; transition: all 0.2s;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(20,184,166,0.2), rgba(6,182,212,0.2)) !important;
            color: #5eead4 !important; border: 1px solid rgba(20,184,166,0.3) !important;
        }
        .stTabs [data-baseweb="tab-highlight"] { display: none; }

        /* ── Cards ──────────────────────────────────────────────────────────────── */
        .chapter-card {
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
            border-radius: 12px; padding: 16px 20px; margin-bottom: 10px; transition: all 0.2s;
        }
        .chapter-card:hover { background: rgba(20,184,166,0.05); border-color: rgba(20,184,166,0.25); }
        .chapter-timestamp {
            font-family: monospace; font-size: 0.78rem; font-weight: 700; color: #2dd4bf !important;
            background: rgba(20,184,166,0.1); border: 1px solid rgba(20,184,166,0.2);
            padding: 2px 8px; border-radius: 6px; margin-right: 10px;
        }
        .chapter-title { font-weight: 600; color: #e2e8f0 !important; font-size: 0.95rem; }
        .chapter-summary { color: #64748b !important; font-size: 0.85rem; margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.04); }

        .moment-card {
            background: rgba(255,255,255,0.025); border: 1px solid rgba(255,255,255,0.06);
            border-left: 3px solid #14b8a6; border-radius: 12px; padding: 18px 20px; margin-bottom: 12px; transition: all 0.2s;
        }
        .moment-card:hover { background: rgba(20,184,166,0.04); border-left-color: #5eead4; }
        .moment-timestamp { font-family: monospace; font-size: 0.78rem; font-weight: 700; color: #2dd4bf !important; background: rgba(20,184,166,0.1); border: 1px solid rgba(20,184,166,0.2); padding: 2px 8px; border-radius: 6px; display: inline-block; margin-bottom: 10px; }
        .moment-quote { font-size: 0.97rem; font-style: italic; color: #99f6e4 !important; font-weight: 500; line-height: 1.55; margin-bottom: 8px; }
        .moment-reason { font-size: 0.82rem; color: #475569 !important; }

        .topic-card { background: rgba(255,255,255,0.025); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 16px 20px; margin-bottom: 10px; }
        .topic-name { font-weight: 600; color: #e2e8f0 !important; font-size: 0.93rem; margin-bottom: 6px; }
        .topic-chapters { font-size: 0.8rem; color: #14b8a6 !important; font-weight: 500; }

        .brief-card {
            background: linear-gradient(135deg, rgba(20,184,166,0.08), rgba(6,182,212,0.05));
            border: 1px solid rgba(20,184,166,0.2); border-radius: 14px; padding: 22px 26px; margin-bottom: 20px;
        }
        .brief-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #2dd4bf !important; margin-bottom: 10px; }
        .brief-text { color: #cbd5e1 !important; font-size: 0.97rem; line-height: 1.8; }

        .match-badge {
            display: inline-block; background: rgba(20,184,166,0.1); border: 1px solid rgba(20,184,166,0.2);
            color: #2dd4bf !important; font-size: 0.75rem; font-weight: 600; padding: 2px 10px; border-radius: 20px; margin-bottom: 12px;
        }

        /* ── Inputs / Misc ──────────────────────────────────────────────────────── */
        .stTextInput input {
            background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 10px !important; color: #e2e8f0 !important;
        }
        .stTextInput input:focus { border-color: rgba(20,184,166,0.5) !important; box-shadow: 0 0 0 3px rgba(20,184,166,0.1) !important; }
        .stTextInput input::placeholder { color: #475569 !important; }

        [data-testid="stFileUploader"] {
            background: rgba(255,255,255,0.02) !important;
            border: 2px dashed rgba(20,184,166,0.25) !important;
            border-radius: 16px !important; transition: border-color 0.2s !important;
        }
        [data-testid="stFileUploader"]:hover { border-color: rgba(20,184,166,0.5) !important; }
        /* Kill the white inner box Streamlit renders inside uploader */
        [data-testid="stFileUploaderDropzone"] {
            background: rgba(255,255,255,0.02) !important;
            border: none !important;
        }
        [data-testid="stFileUploaderDropzone"] * { color: #64748b !important; }
        [data-testid="stFileUploaderDropzone"] button {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.12) !important;
            color: #94a3b8 !important; border-radius: 8px !important;
        }

        .stDownloadButton > button {
            background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(255,255,255,0.1) !important;
            color: #94a3b8 !important; border-radius: 8px !important; font-weight: 500 !important; transition: all 0.2s !important;
        }
        .stDownloadButton > button:hover { background: rgba(20,184,166,0.1) !important; border-color: rgba(20,184,166,0.3) !important; color: #5eead4 !important; }

        /* ── Kill white background on ALL button wrappers ──────────────────────── */
        [data-testid="stButton"],
        [data-testid="stButton"] > div,
        [data-testid="stBaseButton-secondary"],
        .stButton { 
            background: transparent !important;
            box-shadow: none !important;
            border: none !important;
        }

        /* ── Regular sidebar/history buttons ────────────────────────────────────── */
        .stButton > button {
            background: rgba(4,15,15,0.95) !important;
            border: 1px solid rgba(20,184,166,0.08) !important;
            color: rgba(20,184,166,0.3) !important;
            border-radius: 8px !important;
            font-size: 0.75rem !important;
            text-align: left !important;
            box-shadow: none !important;
            transition: all 0.15s !important;
        }
        .stButton > button:hover {
            background: rgba(20,184,166,0.07) !important;
            border-color: rgba(20,184,166,0.2) !important;
            color: #5eead4 !important;
        }

        /* ── Mode card: card sits above, button pulled up to overlay it ─────────── */
        .mode-card {
            margin-bottom: -4px;
        }
        /* Any button immediately after a mode-card div — make it the invisible overlay */
        div:has(> .mode-card) + div button,
        div:has(> .mode-card) ~ div button {
            opacity: 0 !important;
            position: relative !important;
            z-index: 10 !important;
            margin-top: -108px !important;
            height: 108px !important;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            cursor: pointer !important;
            display: block !important;
        }
        div:has(> .mode-card) + div,
        div:has(> .mode-card) ~ div [data-testid="stButton"] {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* ── Primary buttons: teal gradient ─────────────────────────────────────── */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #0d9488, #0891b2) !important;
            border: none !important;
            color: white !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            box-shadow: 0 4px 15px rgba(20,184,166,0.35) !important;
            opacity: 1 !important;
            margin-top: 0 !important;
            height: auto !important;
        }
        .stButton > button[kind="primary"]:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(20,184,166,0.5) !important;
        }

        hr { border-color: rgba(255,255,255,0.06) !important; margin: 20px 0 !important; }
        .stAlert { border-radius: 10px !important; }

        /* ── Use-case pills (hero) ───────────────────────────────────────────── */
        .hero-pills {
            display: flex; flex-wrap: wrap; gap: 8px;
            justify-content: center; margin-top: 24px;
        }
        .hero-pill {
            display: inline-block;
            background: rgba(20,184,166,0.08);
            border: 1px solid rgba(20,184,166,0.22);
            color: #5eead4 !important;
            font-size: 0.8rem; font-weight: 600;
            padding: 7px 16px; border-radius: 20px;
            letter-spacing: 0.01em;
            transition: all 0.2s;
        }
        .hero-pill:hover {
            background: rgba(20,184,166,0.18);
            border-color: rgba(20,184,166,0.45);
            color: #ccfbf1 !important;
            transform: translateY(-1px);
        }
        /* legacy */
        .use-case-pill {
            display: inline-block;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.09);
            color: #64748b !important;
            font-size: 0.75rem; font-weight: 600;
            padding: 5px 12px; border-radius: 20px;
        }

        /* ── Mode selector cards ────────────────────────────────────────────── */
        .mode-card {
            border-radius: 14px; padding: 18px 10px 14px;
            text-align: center; cursor: pointer;
            transition: all 0.2s; margin-bottom: 0;
        }
        .mode-card:hover { filter: brightness(1.15); transform: translateY(-1px); }
        .active-dot {
            width: 6px; height: 6px; border-radius: 50%;
            background: #14b8a6; margin: 8px auto 0;
        }
        /* Mode select buttons — hidden via JS after render (see load_css inject) */

        /* ── Collapse the entire button row below mode cards to zero ────────────── */
        .mode-btn-row {
            height: 0 !important;
            overflow: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
            opacity: 0 !important;
            pointer-events: none !important;
            position: absolute !important;
            top: -9999px !important;
        }

        /* ── Quote postcard cards ────────────────────────────────────────────── */
        .quote-card {
            background: linear-gradient(135deg, rgba(20,184,166,0.08), rgba(6,182,212,0.04));
            border: 1px solid rgba(20,184,166,0.2);
            border-radius: 16px;
            padding: 28px 28px 20px 28px;
            margin-bottom: 16px;
            position: relative;
            overflow: hidden;
            transition: all 0.2s;
        }
        .quote-card::before {
            content: '';
            position: absolute; top: 0; left: 0; right: 0; height: 2px;
            background: linear-gradient(90deg, #0d9488, #0891b2, #06b6d4);
        }
        .quote-card:hover {
            border-color: rgba(20,184,166,0.4);
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(20,184,166,0.12);
        }
        .quote-mark {
            font-size: 4rem; line-height: 0.8; color: rgba(20,184,166,0.2);
            font-family: Georgia, serif; margin-bottom: 8px; display: block;
        }
        .quote-text {
            font-size: 1.05rem; font-style: italic; color: #e2e8f0 !important;
            font-weight: 500; line-height: 1.65; margin-bottom: 16px;
        }
        .quote-footer {
            display: flex; align-items: center; gap: 12px;
            padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.06);
        }
        .quote-reason {
            font-size: 0.8rem; color: #475569 !important; font-style: normal;
        }

        /* ── Confidence bar ──────────────────────────────────────────────────── */
        .confidence-bar {
            display: flex; align-items: center; gap: 8px;
            padding: 10px 16px; margin-bottom: 14px;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 10px;
        }

    </style>
    """, unsafe_allow_html=True)
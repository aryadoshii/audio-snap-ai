# 🎙️ Podcast Chapters

Upload a podcast episode and get a full AI-powered breakdown — transcript, chapters, key moments, energy analysis, topic mapping, and a searchable script.

**Powered by:** Whisper-large-v3 (transcription) + GPT-OSS-120B (all analysis) via Qubrid AI.

## Setup

```bash
uv sync
echo "QUBRID_API_KEY=your_key_here" > .env
streamlit run app.py
```

## Pipeline

```
Audio
  └─► [Whisper-v3]       → raw timestamped transcript
        └─► [Formatter]  → clean segments {timestamp, text, start, end}
              └─► [Chapters] → [Energy] → [Key Moments] → [Topics] → [Brief]
```

> Note: Energy runs after Chapters because it uses chapter data to calculate pace.

## Features

| Tab | What it shows |
|-----|--------------|
| 📖 Chapters | Timestamped chapter breakdown with summaries |
| ✨ Key Moments | Quotable highlights worth clipping |
| ⚡ Energy Map | Bar chart scoring each chapter's energy 1–10 |
| 🔍 Search | Keyword search across the full transcript |
| 🗺️ Topics | Topic-to-chapter mapping |

Episode brief always appears at the top, above the tabs.

## Project Structure

```
├── app.py
├── config/
│   └── settings.py         # API keys, model names, paths
├── backend/
│   ├── state.py            # LangGraph state schema
│   ├── nodes.py            # 7 nodes (1 Whisper + 1 formatter + 5 LLM)
│   └── graph.py            # Linear graph assembly
└── frontend/
    ├── components.py       # Uploader + 5-tab results view
    ├── views.py            # View router
    ├── sidebar.py          # Sidebar
    └── styles.py           # Dark theme CSS
```
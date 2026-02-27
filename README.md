<div align="center">

<!-- <img src="assets/banner.png" alt="AudioSnap AI Banner" width="100%"> -->

<br>

<img src="assets/qubrid_logo.png" alt="Qubrid AI" height="36">

<br><br>

# AudioSnap AI

**Turn any audio into instant intelligence.**  
Chapters · Key Moments · Full Transcript — in seconds.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-14b8a6?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-14b8a6?style=flat-square&logo=streamlit&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper--v3-OpenAI-0891b2?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-0d9488?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-475569?style=flat-square)

</div>

---

## What it does

AudioSnap AI takes any audio — a podcast clip, YouTube video, meeting recording, or voice note — and returns structured intelligence within seconds:

- **Smart Chapters** with timestamps and summaries
- **Key Moments** — the most quotable, shareable clips
- **Full Transcript** with search and CSV export
- **Topic Map** showing which themes appear across chapters
- **AI Confidence Score** — the model rates its own output

Powered by **Whisper-v3** for transcription and **GPT-OSS-120B** for analysis, running on [Qubrid AI](https://qubrid.com) infrastructure.

---

## Screenshots

### 🏠 Interface

<div align="center">

<img src="assets/screenshots/home-collapsed.png" alt="Clean Interface" width="100%">
<sub>Clean, focused interface with collapsed sidebar</sub>

<br><br>

<img src="assets/screenshots/home-sidebar.png" alt="Sidebar with History" width="100%">
<sub>Session history sidebar with one-click recall</sub>

<br><br>

<img src="assets/screenshots/mode-selector.png" alt="Mode Selector" width="100%">
<sub>Three input modes — Upload File · YouTube URL · Record Live</sub>

<br><br>

<img src="assets/screenshots/sidebar-history.png" alt="History Panel" width="100%">
<sub>Full history panel with timestamps</sub>

</div>

---

### ▶️ YouTube URL Analysis

<div align="center">

<img src="assets/screenshots/yt-home.png" alt="YouTube Input" width="100%">
<sub>Paste any YouTube link — thumbnail previews instantly</sub>

<br><br>

<img src="assets/screenshots/yt-analyzing.png" alt="Analyzing" width="100%">
<sub>Downloading audio + running Whisper-v3 transcription and GPT-OSS-120B analysis</sub>

<br><br>

<img src="assets/screenshots/yt-chapters.png" alt="Chapters" width="100%">
<sub>Smart chapters with timestamps and summaries generated automatically</sub>

<br><br>

<img src="assets/screenshots/yt-keymoments.png" alt="Key Moments" width="100%">
<sub>Key moments — the most quotable, shareable clips extracted from the video</sub>

<br><br>

<img src="assets/screenshots/yt-transcript.png" alt="Transcript" width="100%">
<sub>Full searchable transcript with timestamps and CSV export</sub>

<br><br>

<img src="assets/screenshots/yt-topics.png" alt="Topics" width="100%">
<sub>Topic map — themes identified and cross-referenced across chapters</sub>

</div>

---

### 🎙 Podcast / File Upload
> Screenshots coming soon

---

### 🔴 Live Recording
> Screenshots coming soon

---

## Architecture

AudioSnap uses a **LangGraph agentic pipeline** — not a simple linear chain:

```
Audio Input
    │
    ▼
Whisper-v3 Transcription
    │
    ▼
Quality Gate ──── too short? ──► Short Clip Mode
    │
    ▼
Chapter Generation
    │
    ▼
Chapter Retry Loop  (if < 3 chapters generated)
    │
    ▼
Key Moments · Topic Map · Episode Brief
    │
    ▼
Self-Evaluation Node  (model scores its own output 1–10)
    │
    ▼
Structured Result
```

Three agentic behaviors: **conditional routing**, **self-correction loop**, and **self-evaluation**.

---

## Getting Started

### Prerequisites

- Python 3.10+
- A [Qubrid AI](https://qubrid.com) API key
- `ffmpeg` installed (for YouTube audio processing)

### Installation

```bash
# Clone
git clone https://github.com/aryadoshii/audio-snap-ai.git
cd audio-snap-ai

# Install dependencies
pip install -e .

# Configure environment
cp .env.example .env
# Add your QUBRID_API_KEY to .env

# Launch
streamlit run app.py
```

### Environment Variables

```env
QUBRID_API_KEY=your_api_key_here
QUBRID_BASE_URL=https://api.qubrid.com/v1
```

---

## Input Modes

| Mode | Description | Limit |
|------|-------------|-------|
| **Upload File** | MP3, WAV, M4A | 200 MB |
| **YouTube URL** | Any public video | First 12 min |
| **Record Live** | Browser microphone | Session length |

---

## Project Structure

```
audio-snap-ai/
├── app.py                    # Streamlit entry point
├── frontend/
│   ├── components.py         # Hero, mode selector, results UI
│   ├── sidebar.py            # History sidebar
│   ├── styles.py             # All CSS + JS injections
│   └── views.py              # Layout orchestration
├── backend/
│   ├── graph.py              # LangGraph agentic pipeline
│   ├── nodes.py              # Individual agent nodes
│   └── database.py           # SQLite history store
├── config/
│   └── settings.py           # Environment config
├── assets/
│   ├── screenshots/          # UI screenshots
│   └── qubrid_logo.png       # Logo (+ add banner.png here)
├── .env.example
└── pyproject.toml
```

---

## Stack

| Layer | Technology |
|-------|-----------|
| UI | Streamlit + custom CSS/JS |
| Transcription | Whisper-v3 via Qubrid API |
| Intelligence | GPT-OSS-120B via Qubrid API |
| Orchestration | LangGraph |
| YouTube | yt-dlp |
| History | SQLite |

---

<div align="center">

Built with ⚡ on [Qubrid AI](https://qubrid.com)

</div>

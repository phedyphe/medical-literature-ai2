# 🏥 AI-Driven Medical Literature Research Platform

A comprehensive, fully automated platform for spine surgery research that dynamically searches medical journals, extracts structured data, and performs expert critical appraisals using the GRADE framework.

## 🎯 Core Features

- **Dynamic Keyword Mind-Map Engine**: Intelligently expands medical keywords using LLM context
- **Automated Literature Search**: Hybrid approach using PubMed API, Semantic Scholar, and web scraping
- **Intelligent Data Extraction**: Full-text PDF parsing with fallback to abstracts
- **GRADE-Based Critical Appraisal**: AI persona of Senior Spine Surgeon evaluates evidence quality
- **Dual Interface**: Dashboard for visualization + Chat for interactive analysis
- **Traffic Light Risk of Bias Plot**: Visual risk assessment framework

## 🛠 Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **LLM**: Google Gemini API (Free Tier - gemini-1.5-flash)
- **Literature APIs**: NCBI Entrez (PubMed), Semantic Scholar
- **PDF Processing**: PyMuPDF (fitz)
- **Data Processing**: Pandas, BeautifulSoup4
- **Database**: SQLite (lightweight, no dependencies)

### Frontend
- **UI Framework**: Streamlit (for rapid prototyping and AI integration)
- **Visualization**: Plotly, Streamlit Charts
- **State Management**: Streamlit Session State

## 📦 Project Structure

```
medical-literature-ai2/
├── backend/
│   ├── api/
│   │   ├── search_engine.py        # PubMed & Semantic Scholar integration
│   │   ├── deduplication.py        # Cross-database deduplication
│   │   └── extraction.py           # Full-text & abstract extraction
│   ├── ai/
│   │   ├── llm_interface.py        # Gemini API wrapper
│   │   ├── keyword_expansion.py    # Mind-map generation
│   │   └── appraisal.py            # GRADE framework & critical appraisal
│   ├── models/
│   │   └── data_models.py          # Pydantic schemas
│   ├── database/
│   │   └── db_manager.py           # SQLite operations
│   ├── utils/
│   │   ├── pdf_parser.py           # PyMuPDF integration
│   │   ├── logger.py               # Logging setup
│   │   └── constants.py            # Configuration
│   └── main.py                     # FastAPI entry point
├── frontend/
│   ├── streamlit_app.py            # Main Streamlit application
│   ├── pages/
│   │   ├── dashboard.py            # Dashboard interface
│   │   ├── chat.py                 # Chat interface
│   │   └── settings.py             # Configuration panel
│   └── components/
│       ├── mindmap_viz.py          # Interactive mind-map
│       ├── traffic_light.py        # Risk of bias visualization
│       └── data_tables.py          # Result tables
├── requirements.txt
├── .env.example
└── config.yaml
```

## 🚀 Quick Start

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Configure `.env` with your Google Gemini API key
6. Run backend: `python backend/main.py`
7. Run frontend: `streamlit run frontend/streamlit_app.py`

## 📖 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [API Documentation](docs/API.md)
- [LLM Prompt Engineering](docs/PROMPT_ENGINEERING.md)
- [Database Schema](docs/DATABASE.md)

## 🔐 Security & Compliance

- Free-tier optimized API calls (Gemini Flash)
- Secure credential management with environment variables
- Rate limiting for external APIs
- Local data storage (SQLite) for privacy

## 📄 License

MIT License - See LICENSE file for details

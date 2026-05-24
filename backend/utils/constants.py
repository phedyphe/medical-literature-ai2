"""Application-wide constants and configuration."""

from enum import Enum
from typing import Dict, List
from datetime import datetime

# ==================== EVIDENCE LEVELS ====================
class EvidenceLevel(str, Enum):
    """GRADE Framework Evidence Levels."""
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"
    VERY_LOW = "Very Low"

# ==================== RISK OF BIAS ====================
class RiskOfBias(str, Enum):
    """Risk of Bias Classification."""
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

# Traffic Light Mapping
TRAFFIC_LIGHT_MAP: Dict[RiskOfBias, str] = {
    RiskOfBias.LOW: "🟢",      # Green
    RiskOfBias.MODERATE: "🟡",  # Yellow
    RiskOfBias.HIGH: "🔴",      # Red
}

# ==================== DATA CATEGORIES ====================
class DataCategory(str, Enum):
    """Structured extraction categories."""
    DIAGNOSIS = "Diagnosis/Classification"
    SURGICAL_TECHNIQUE = "Surgical Technique"
    OUTCOME = "Outcome"

DATa_CATEGORY_DESCRIPTIONS: Dict[DataCategory, str] = {
    DataCategory.DIAGNOSIS: "Patient demographics, pathology grading, diagnostic criteria",
    DataCategory.SURGICAL_TECHNIQUE: "Robotic-assisted procedures, implant types, surgical approaches",
    DataCategory.OUTCOME: "Fusion rates, complication rates, blood loss, patient-reported measures",
}

# ==================== DATABASE SOURCES ====================
class DatabaseSource(str, Enum):
    """Literature database sources."""
    PUBMED = "PubMed"
    SEMANTIC_SCHOLAR = "Semantic Scholar"
    GOOGLE_SCHOLAR = "Google Scholar"

# ==================== STUDY TYPES ====================
STUDY_TYPES: List[str] = [
    "Randomized Controlled Trial (RCT)",
    "Cohort Study",
    "Case-Control Study",
    "Case Report",
    "Review",
    "Systematic Review",
    "Meta-Analysis",
]

# ==================== SPINE SURGERY KEYWORDS ====================
SPINE_SURGERY_BASE_KEYWORDS: Dict[str, List[str]] = {
    "spinal fusion": [
        "anterior cervical discectomy fusion",
        "posterolateral fusion",
        "posterior lumbar interbody fusion",
        "anterior lumbar interbody fusion",
        "cervical spine fusion",
    ],
    "robotic navigation": [
        "robotic-assisted spine surgery",
        "intraoperative CT navigation",
        "real-time imaging guidance",
        "robot-assisted pedicle screw placement",
    ],
    "implant techniques": [
        "pedicle screw fixation",
        "top-loading screws",
        "lateral mass screws",
        "expandable interbody devices",
        "anterior cervical plating",
    ],
    "minimally invasive": [
        "MIS spine surgery",
        "endoscopic spine surgery",
        "percutaneous fixation",
        "keyhole surgery",
    ],
}

# ==================== API CONFIGURATION ====================
PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SEMANTIC_SCHOLAR_BASE_URL = "https://api.semanticscholar.org/graph/v1"

PUBMED_TIMEOUT = 30
SEMANTIC_SCHOLAR_TIMEOUT = 30
PDF_FETCH_TIMEOUT = 30

# Max concurrent requests to avoid rate limiting
MAX_CONCURRENT_REQUESTS = 3
RATE_LIMIT_DELAY = 0.5  # seconds

# ==================== PDF PROCESSING ====================
MAX_PDF_SIZE_MB = 50
SUPPORTED_PDF_FORMATS = ["pdf", "html", "txt"]

# ==================== TEXT EXTRACTION ====================
MIN_ABSTRACT_LENGTH = 50  # characters
MIN_FULLTEXT_LENGTH = 500  # characters

# ==================== DEDUPLICATION ====================
DOI_WEIGHT = 1.0  # Exact match
TITLE_SIMILARITY_THRESHOLD = 0.95  # Fuzzy match
AUTHOR_SIMILARITY_THRESHOLD = 0.85

# ==================== DATE FORMATTING ====================
DATE_FORMAT = "%Y-%m-%d"
DEFAULT_SEARCH_YEARS = 5

# ==================== LOGGING ====================
LOG_FORMAT = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOG_FILE = "./logs/app.log"

# ==================== GEMINI AI SETTINGS ====================
GEMINI_MODEL = "gemini-1.5-flash"
GEMINI_TEMPERATURE = 0.7
GEMINI_MAX_TOKENS = 2000
GEMINI_TIMEOUT = 60

# Requests per minute limit for free tier
GEMINI_RPM_LIMIT = 10
GEMINI_RPD_LIMIT = 1500  # Requests per day

# ==================== ERROR MESSAGES ====================
ERROR_MESSAGES: Dict[str, str] = {
    "api_timeout": "API request timed out. Please try again.",
    "pdf_fetch_failed": "Failed to fetch PDF. Using abstract instead.",
    "extraction_failed": "Failed to extract data. Document may be corrupted.",
    "rate_limit": "Rate limit exceeded. Please wait before retrying.",
    "invalid_doi": "Invalid DOI format.",
    "gemini_error": "Error communicating with Gemini API.",
}

# ==================== SUCCESS MESSAGES ====================
SUCCESS_MESSAGES: Dict[str, str] = {
    "search_complete": "Literature search completed successfully.",
    "extraction_complete": "Data extraction completed.",
    "deduplication_complete": "Deduplication completed.",
    "appraisal_complete": "Critical appraisal generated.",
}

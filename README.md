# Anomaly-Based Threat Detection Dashboard

A machine learning and cybersecurity project that detects suspicious system activity using **unsupervised anomaly detection** and presents findings in an interactive **Streamlit dashboard**. The system uses **Isolation Forest** to identify unusual patterns in CPU usage, network traffic, login attempts, file access, and process behavior.

> Academic Project – Data Mining and Machine Learning (DMML) | Cybersecurity | Anomaly Detection | Threat Intelligence

---

## Overview

This project is designed to help identify potential security threats by analyzing system behavior and flagging anomalies that may indicate malicious activity, misuse, or abnormal operational events.

It combines:
- **Machine Learning for anomaly detection**
- **Retrieval-Augmented Generation (RAG)** for cybersecurity context
- **Threat intelligence references** from sources such as **MITRE ATT&CK** and **OWASP**
- **Interactive data visualization** using Streamlit and Plotly

---

## Key Features

- **Unsupervised anomaly detection** using Isolation Forest
- **Synthetic system log generation** for model testing and simulation
- **Real-time anomaly threshold adjustment**
- **Detection of unusual behavior** in:
  - CPU usage
  - Network outbound traffic
  - Login attempts
  - File access frequency
  - Process count
- **Anomaly score visualization**
- **Detected anomalies table** with export support
- **RAG-based explanation layer** for cybersecurity insights
- **Streamlit dashboard** for easy investigation and analysis

---

## Problem Statement

Traditional rule-based security systems often fail to detect:
- Unknown threats
- Zero-day attacks
- Low-and-slow anomalies
- Behavioral deviations that do not match static rules

This project addresses the problem by using machine learning to detect abnormal patterns in system activity and provide interpretable insights for security analysis.

---

## Project Workflow

1. **Generate synthetic activity data**
2. **Build vector database** for retrieval-based context
3. **Detect anomalies** using Isolation Forest
4. **Store and evaluate results**
5. **Visualize outputs** in the dashboard
6. **Use RAG to enrich anomaly explanations** with cybersecurity knowledge

---

## Tech Stack

- **Python**
- **Machine Learning**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Streamlit**
- **Plotly**
- **Hugging Face**
- **LangChain**
- **RAG (Retrieval-Augmented Generation)**
- **MITRE ATT&CK**
- **OWASP**
- **DigitalOcean VM** for development/deployment

---

## Repository Structure

```text
├── dashboard.py
├── detect_anamolies.py
├── generate_data.py
├── evaluate_results.py
├── build_vector_db.py
├── requirements.txt
├── anomaly_results.csv
├── anomaly_score_distribution.png
├── data/
├── knowledge_base/
├── rag/
├── results/
└── vector_db/
```

---

## File Descriptions

- **dashboard.py** – Streamlit dashboard for viewing anomaly scores and detections
- **generate_data.py** – Creates synthetic system activity data
- **detect_anamolies.py** – Runs anomaly detection using Isolation Forest
- **evaluate_results.py** – Evaluates detection output and results
- **build_vector_db.py** – Builds the vector database for RAG
- **knowledge_base/** – Stores cybersecurity knowledge sources
- **rag/** – Contains retrieval and explanation logic
- **results/** – Stores generated outputs and analysis artifacts
- **vector_db/** – Stores the embedded retrieval index

---

## ATS-Friendly Keywords

Cybersecurity, Threat Detection, Anomaly Detection, Machine Learning, Isolation Forest, Unsupervised Learning, Behavioral Analytics, Security Monitoring, Threat Intelligence, MITRE ATT&CK, OWASP, Retrieval-Augmented Generation, RAG, Streamlit Dashboard, Data Mining, Python, Scikit-learn, Pandas, Plotly, Log Analysis, Network Security, System Monitoring, AI for Cybersecurity, Security Analytics.

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Subash-1507/Data_Mining_and_MachineLearning_project_new.git
cd Data_Mining_and_MachineLearning_project_new
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
pip install huggingface-hub
pip install langchain-huggingface
```

### 3. Generate data and build the vector database
```bash
python generate_data.py
python build_vector_db.py
```

### 4. Run anomaly detection
```bash
python detect_anamolies.py
python evaluate_results.py
```

### 5. Launch the dashboard
```bash
streamlit run dashboard.py
```

---

## Use Cases

- Security operations monitoring
- L1 SOC analyst support
- Threat hunting
- Insider threat detection
- System behavior anomaly analysis
- Cybersecurity education and academic demonstration

---

## Future Improvements

- Add live log ingestion
- Improve anomaly explainability
- Integrate more threat intelligence sources
- Add authentication and role-based access
- Support real-time alerting and notifications
- Expand evaluation metrics for model performance

---

## License

N/A

---

## Author

**Subash-1507**
**SSV-07 Vaagai**

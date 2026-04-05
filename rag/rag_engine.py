from dotenv import load_dotenv
import os
from groq import Groq

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from rag.mitre_mapper import map_anomaly_to_mitre

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# --------------------------------------------------
# Initialize embeddings (same model used to build FAISS)
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# Load FAISS vector database
# --------------------------------------------------

vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})


# --------------------------------------------------
# Initialize Groq LLM client
# --------------------------------------------------

client = Groq()


# --------------------------------------------------
# RAG Explanation Function
# --------------------------------------------------

def explain_anomaly(cpu, network, login_attempts, process_count):

    # Map anomaly features → MITRE techniques
    threats = map_anomaly_to_mitre(
        cpu, network, login_attempts, process_count
    )

    threat_text = ""

    for t in threats:
        threat_text += f"""
Technique: {t['technique']} ({t['mitre_id']})
Reason: {t['reason']}
"""

    # Query describing the anomaly
    query = f"""
System anomaly detected.

CPU Usage: {cpu}
Network Traffic: {network}
Login Attempts: {login_attempts}
Process Count: {process_count}

Potential Threat Indicators:
{threat_text}
"""

    # Retrieve relevant cybersecurity knowledge
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])


    # SOC-style prompt
    prompt = f"""
You are a cybersecurity analyst working in a Security Operations Center.

Context Information:
{context}

Observed System Behavior:
CPU Usage: {cpu}
Network Traffic: {network}
Login Attempts: {login_attempts}
Process Count: {process_count}

Possible Threat Indicators:
{threat_text}

Provide a structured analysis including:

1. Threat Analysis
2. Possible Attack Technique
3. Indicators of Compromise
4. MITRE ATT&CK Mapping
5. Recommended Investigation Steps
6. Final Assessment
"""


    # Call Groq LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    return result

#RAG user questions
def ask_question_about_anomaly(question, cpu, network, login_attempts, process_count):

    query = f"""
User question: {question}

System behavior:
CPU Usage: {cpu}
Network Traffic: {network}
Login Attempts: {login_attempts}
Process Count: {process_count}
"""

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a cybersecurity analyst.

Context information:
{context}

System anomaly details:
CPU Usage: {cpu}
Network Traffic: {network}
Login Attempts: {login_attempts}
Process Count: {process_count}

User Question:
{question}

Provide a clear cybersecurity explanation.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
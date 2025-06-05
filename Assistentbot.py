import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from PyPDF2 import PdfReader
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0
)

Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True)
    filename = Column(String(255))
    content = Column(Text)

password = quote_plus("**********")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/dumy")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

st.title("🤵🏻HR Assistant")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for chats in st.session_state.chat_history:
    with st.chat_message(chats["role"]):
        st.markdown(chats['content'])

pdf_doc = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if pdf_doc:
    resume_text = get_pdf_text([pdf_doc])

    new_resume = Resume(
        filename=pdf_doc.name,
        content=resume_text
    )
    session.add(new_resume)
    session.commit()

    with st.chat_message("User"):
        st.markdown("Resume Uploaded & Stored in MySQL")
        st.session_state.chat_history.append({"role": "User", "content": "Resume Uploaded"})

    system_msg = {
        "role": "system",
        "content": """You are a helpful HR assistant who sorts candidate resumes.
        HR: You should compare the resume with the following job description.
        Your response should be only 'yes' or 'no' on whether to choose the candidate, along with a reason.
        Job Description: Requirement for software developer with 7 years of experience in both frontend and backend."""
    }

    human_msg = {
        "role": "user",
        "content": f"Candidate Resume:\n{resume_text}"
    }

    prompt = [system_msg, human_msg]
    llm_response = llm.invoke(prompt)

    with st.chat_message("Assistant"):
        st.markdown(llm_response.content)
        st.session_state.chat_history.append({"role": "Assistant", "content": llm_response.content})

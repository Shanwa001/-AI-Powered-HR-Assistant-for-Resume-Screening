# -AI-Powered-HR-Assistant-for-Resume-Screening
This project is an AI-driven HR assistant designed to automate the initial screening of resumes based on job requirements. Built using Python and Streamlit for a user-friendly interface, the system allows users to upload PDF resumes which are then parsed using the PyPDF2 library. The extracted text is stored in a MySQL database using SQLAlchemy ORM, ensuring persistent and structured data storage.

At the core of the application lies the Groq-hosted LLaMA 3 70B large language model, integrated via the LangChain framework. When a resume is uploaded, the system generates a prompt containing a predefined job description and the candidate’s resume text. The LLM then provides a "Yes" or "No" decision on whether the candidate matches the job requirements—specifically for a software developer with 7 years of full-stack experience—along with a concise explanation.

The solution maintains chat history and interacts with the user in a conversational format using Streamlit’s real-time components. This assistant significantly reduces manual HR effort, offering scalable and intelligent candidate filtering. It showcases practical integration of LLMs with database operations, PDF handling, and frontend display, making it ideal for recruitment automation and AI-powered enterprise solutions.
![Screenshot 2025-06-05 172509](https://github.com/user-attachments/assets/dd37139c-277a-42f8-b41d-1673506441ed)

![Screenshot 2025-06-05 172604](https://github.com/user-attachments/assets/5be499a1-9745-4dbd-a207-6df4e953835b)

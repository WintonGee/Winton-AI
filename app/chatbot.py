from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import json
import gradio as gr

# 1. Load first-person data
with open("data/processed/resume_chunks.json") as f:
    chunks = json.load(f)["chunks"]

# 2. Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3. FAISS index
vector_db = FAISS.from_texts(chunks, embeddings)

# 4. First-person prompt
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You ARE Winton Gee. Answer in first person using ONLY this context:
    {context}
    
    If unrelated, say: "I focus on my professional background."
    
    Question: {question}
    Answer:
    """
)

# 5. Configure LLM
llm = OllamaLLM(
    model="mistral:latest",
    base_url="http://localhost:11434",
    temperature=0.3
)

# 6. QA system
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever(),
    chain_type_kwargs={"prompt": prompt_template}
)

# 7. Gradio with validation
def respond(message, history):
    # Check relevance
    most_similar = vector_db.similarity_search_with_score(message, k=1)[0]
    if most_similar[1] < 0.25:  # Similarity threshold
        return "I focus on discussing my professional experience."
    
    # Get answer
    response = qa.invoke({"query": message})
    return response["result"]

gr.ChatInterface(respond).launch(share=True)
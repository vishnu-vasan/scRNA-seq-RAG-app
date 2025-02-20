import os
import warnings
import gradio as gr
import tempfile

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

warnings.filterwarnings("ignore", message=".*clean_up_tokenization_spaces.*")
# Global variables
index = None
query_engine = None

# Set up Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize Groq LLM and ensure it is used
# llm = Groq(model="llama-3.3-70b-versatile")
llm = Groq(model="deepseek-r1-distill-qwen-32b")
Settings.llm = llm  # Ensure Groq is the LLM being used

# Initialize our chosen embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
def load_documents(file_objs):
    global index, query_engine
    try:
        if not file_objs:
            return "Error: No files selected."

        documents = []
        document_names = [file_obj for file_obj in file_objs]  # file_objs are file paths

        # Load documents directly from file paths
        loaded_docs = SimpleDirectoryReader(input_files=document_names).load_data()
        documents.extend(loaded_docs)

        if not documents:
            return "No documents found in the selected files."

        # Create index
        index = VectorStoreIndex.from_documents(
            documents,
            llm=llm,
            embed_model=embed_model
        )

        # Create query engine
        query_engine = index.as_query_engine()

        return f"Successfully loaded {len(documents)} documents from: {', '.join(document_names)}"
    except Exception as e:
        return f"Error loading documents: {str(e)}"

# RAG query function
def perform_rag(query, history):
    global query_engine
    if query_engine is None:
        return history + [("Please load documents first.", None)]
    try:
        response = query_engine.query(query)  # Removed async
        return history + [(query, str(response))]
    except Exception as e:
        return history + [(query, f"Error processing query: {str(e)}")]
# Clear all
def clear_all():
    global index, query_engine
    index = None
    query_engine = None
    return None, "", [], ""
# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# RAG Multi-file Chat Application")

    with gr.Row():
        file_input = gr.File(label="Select files to load", file_count="multiple", type="filepath")

        load_btn = gr.Button("Load Documents")

    load_output = gr.Textbox(label="Load Status")

    msg = gr.Textbox(label="Enter your question", interactive=True)
    chatbot = gr.Chatbot()  
    clear = gr.Button("Clear")

    # Set up event handlers
    load_btn.click(load_documents, inputs=[file_input], outputs=[load_output])
    msg.submit(perform_rag, inputs=[msg, chatbot], outputs=[chatbot])
    clear.click(clear_all, outputs=[file_input, load_output, chatbot, msg])

# Run the app
if __name__ == "__main__":
    demo.launch()
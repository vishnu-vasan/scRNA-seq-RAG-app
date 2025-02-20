# RAG Multi-file Chat Application

This repository contains a Retrieval-Augmented Generation (RAG) application built using Gradio and LlamaIndex. The app allows users to upload multiple documents and perform queries on them using a Groq LLM-powered search engine.

## Features
- Upload multiple files and index them for querying.
- Uses Models from [Groq's playground](https://console.groq.com/playground) for LLM-based responses.
- Utilizes HuggingFace's `all-MiniLM-L6-v2` model for embedding.
- Interactive chatbot interface using Gradio.
- Supports clearing all indexed documents and resetting the chatbot.

## Specific Use Case: Pathway Analysis for scRNA-seq Data

This RAG application is specifically designed to assist in pathway analysis for Gene Ontology Biological Process (GOBP) pathways. It takes in upregulated and downregulated genes derived from single-cell RNA sequencing (scRNA-seq) analysis and provides insights into their biological context. The app enables researchers to:

- Upload and process DE Results.

- Retrieve relevant biological pathways associated with differentially expressed genes.

- Generate contextual information to aid in interpretation and hypothesis generation.

## Installation

Ensure you have Python 3.8+ installed. Then, install the required dependencies using:

```bash
pip install -r requirements.txt
```

If there are any issues with setting up the environment using `requirements.txt`, just type the below command:

```bash
pip install gradio llama-index-core llama-index-llms-groq llama-index-embeddings-huggingface sentence-transformers
```

## Environment Variables

Set up the required [API key for Groq](https://console.groq.com/keys) and paste that in the placeholder in the script:

## Usage

Run the application with:   

```bash
python rag_app.py
```

The Gradio interface will launch in your browser, allowing you to upload files and interact with the chatbot.

## Code Overview

- **`load_documents(file_objs)`**: Loads and indexes the selected documents for querying.
- **`perform_rag(query, history)`**: Queries the indexed documents and retrieves relevant responses.
- **`clear_all()`**: Resets the chatbot and clears all loaded documents.
- **Gradio UI**: Provides an interactive chatbot and file upload functionality.

## Example Workflow

1. Select files using the file input field.
2. Click the **Load Documents** button to index them.
3. Enter your question in the chatbot input field.
4. Receive LLM-powered responses based on the indexed documents.
5. Use the **Clear** button to reset the session.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to submit issues and pull requests to improve the project!

## Acknowledgments
- [Gradio](https://gradio.app/) for the UI.
- [LlamaIndex](https://gpt-index.readthedocs.io/) for indexing and querying.
- [Groq](https://groq.com/) for the LLM.
- [HuggingFace](https://huggingface.co/) for embeddings.

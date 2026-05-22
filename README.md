# LitRaG
RAG with Mistral + Chroma DB: Load PDF → chunk → embed → store → retrieve relevant context → LLM answers strictly from your the pdf's provided and a user-friendly GUI
# 📖 LitRaG – Ask Your PDF Anything

**LitRaG** is a Retrieval-Augmented Generation (RAG) application that lets you upload PDF books or documents, process them, and then ask natural language questions about their content. It uses **Mistral AI** for embeddings and LLM, **Chroma DB** for vector storage, and **Streamlit** for an interactive UI.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Mistral AI](https://img.shields.io/badge/Mistral%20AI-API-orange.svg)](https://mistral.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

- 📂 **Upload one or multiple PDFs** directly via the web interface
- ✂️ **Configurable chunking** (size & overlap) – control granularity
- 🧠 **Mistral AI embeddings** – high‑quality semantic representations
- 💾 **Persistent Chroma DB** – vector store saved on disk, reused across sessions
- 🔍 **MMR retrieval** – avoids redundant chunks, diversifies results
- 🤖 **Mistral LLM** – answers strictly from provided context (no hallucinations)
- 🔎 **Transparent** – shows retrieved text chunks alongside the answer
- 🎨 **Clean Streamlit UI** – no coding required to interact




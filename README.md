## **Michael Scott Joke Generator 🎭😂**
A **Retrieval-Augmented Generation (RAG) application** using **Qdrant** and **Google Gemini Pro API** to generate **Michael Scott-style jokes** based on dialogues from *The Office*. Built with **LangChain, Streamlit, and Hugging Face embeddings**.

![image](https://github.com/user-attachments/assets/6aef5740-db11-46b0-a857-1ba8dcc77d1b)


### **🚀 Features**
✅ **Retrieval-Augmented Generation (RAG):** Uses **Qdrant** to retrieve relevant dialogues from *The Office*  
✅ **Michael Scott-Style Jokes:** Generates jokes mimicking **Michael Scott’s humor**  
✅ **Google Gemini Pro API:** Uses **Gemini Pro** for joke generation  
✅ **Fast & Scalable Search:** Stores vector embeddings in **Qdrant** for fast retrieval  
✅ **Interactive UI:** Built using **Streamlit** for a simple user experience  

---

## **📌 How It Works**
1. **Preprocessing Stage**
   - Load dialogues from *The Office*.
   - Convert them into **vector embeddings** using **Hugging Face** models.
   - Store these embeddings in **Qdrant** for fast retrieval.

2. **Retrieval Step**
   - The user enters a **topic** (e.g., `"sales"`, `"Dunder Mifflin"`).
   - Qdrant performs **semantic search** to find **similar dialogues**.
   - The best-matching dialogues are retrieved.

3. **Joke Generation Step**
   - Retrieved dialogues and the **user’s topic** are sent to **Gemini Pro API**.
   - The model generates a **Michael Scott-style joke**.

4. **Displaying the Joke**
   - The joke is displayed in **Streamlit**.

---

## **🛠️ Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/michael-scott-joke-generator.git
cd michael-scott-joke-generator
```

### **2️⃣ Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**
Create a `.env` file and add the following:
```ini
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_HOST=your_qdrant_host_url
GOOGLE_API_KEY=your_google_gemini_pro_api_key
```

---

## **📌 Running the App**
```bash
streamlit run streamlit_app.py
```
📌 **Go to `http://localhost:8501/` in your browser to use the app.**

---

## **📂 Project Structure**
```
📦 michael-scott-joke-generator
│── 📄 .env                    # API keys (DO NOT SHARE)
│── 📄 requirements.txt         # Required dependencies
│── 📄 README.md                # Project documentation
│── 📄 streamlit_app.py         # Streamlit UI
│── 📄 retrieval.py             # Qdrant retrieval logic
│── 📄 joke_generator.py        # Joke generation logic
│── 📄 embeddings.py            # Embedding generation and Qdrant storage
│── 📁 data                     # Dialogues dataset
│── 📁 venv                     # Virtual environment (ignored in Git)
```

---


## **📌 Example Usage**
**User Input:**  
📝 `"Make a joke about sales."`

**Generated Joke:**  
🤣 `"Why did the salesman bring a ladder? Because he was trying to climb the corporate ladder, but ended up selling paper instead!"`

---

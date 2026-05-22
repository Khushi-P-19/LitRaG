from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

embedding_model=MistralAIEmbeddings()
vectorstore=Chroma(
    embedding_function=embedding_model,
    persist_directory="chroma-db"
)
retriever=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"fetch_k":10,"lambda_mult":0.5}
)
llm=ChatMistralAI(model="mistral-small-2603",temperature=0.9)
#promppt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","""You are a helpful assistant.
         USE ONLY THE PROVIDED CONTEXT TO ANSWER THE QUESTION. IF YOU DON'T KNOW THE ANSWER, SAY: I DON'T KNOW."""),
        ("human","""Context:
         {context}
         Question:
         {question}""")
         
         ]   
)
print("RAG system created")
print("press 0 to exit")
while True:
    query=input("Enter your question:")
    if query=="0":
        break
    docs=retriever.invoke(query)
    context="\n".join([d.page_content for d in docs])
    final_prompt=prompt.invoke({"context": context, "question": query})
    response=llm.invoke(final_prompt)
    print(f"\n AI is going to answer:{response.content}\n")
    
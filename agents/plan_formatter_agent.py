from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral",
    streaming=True,
    max_tokens=1000,
    callbacks=[StreamingStdOutCallbackHandler()]
)

template = """
Kullanıcının kişisel sağlık planını aşağıdaki bilgilere göre formatla:

📅 Günlük Zaman Planı:
{zamanlama}

🍽 Diyet Planı:
{diyet}

🏋 Egzersiz Planı:
{egzersiz}

💬 Haftalık Motivasyon Mesajları:
{motivasyon}

Planı şu formatta yaz:
===============================
FITMATE – KİŞİYE ÖZEL SAĞLIK PLANI
===============================

📅 Günlük Zaman Planı:
{zamanlama}

🍽 Diyet Planı:
{diyet}

🏋 Egzersiz Planı:
{egzersiz}

💬 Haftalık Motivasyon Mesajları:
{motivasyon}

🔁 Unutma, bu plan senin hedeflerine göre özelleştirildi. Sağlıklı günler!
"""

prompt = PromptTemplate(
    input_variables=["zamanlama", "diyet", "egzersiz", "motivasyon"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def format_plan(diyet, egzersiz, zamanlama, motivasyon):
    response = chain.invoke({
        "zamanlama": zamanlama,
        "diyet": diyet,
        "egzersiz": egzersiz,
        "motivasyon": motivasyon
    })
    return response["text"]
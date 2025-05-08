from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral",
    streaming=True,
    max_tokens=1250,
    callbacks=[StreamingStdOutCallbackHandler()]
)


template = """
Kullanıcının günlük öğün sayısı: {ogun_sayisi}
Uyku saatleri: {uyku_saatleri}
Spor saati: {spor_saati}

Bu bilgilere göre:
Çok özet bir şekilde:
1. Kahvaltı, öğle, akşam yemeği ve varsa ara öğünleri uygun saatlere yerleştir
2. Spor saatine göre önce veya sonra yemek öner
3. Zaman çizelgesi olarak sırayla yaz

Her bir madde tek bir satırda kısa ve net bir şekilde yazılmalı.
Kısa ve sade şekilde sadece planı listele.
"""

prompt = PromptTemplate(
    input_variables=["ogun_sayisi", "uyku_saatleri", "spor_saati"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def generate_schedule(ogun_sayisi, uyku_saatleri, spor_saati):
    return chain.invoke({
        "ogun_sayisi": ogun_sayisi,
        "uyku_saatleri": uyku_saatleri,
        "spor_saati": spor_saati
    })["text"]

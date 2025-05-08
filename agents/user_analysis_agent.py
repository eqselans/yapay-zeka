from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
import os
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
Kullanıcının bilgileri:

- Yaş: {yas}
- Boy: {boy} cm
- Kilo: {kilo} kg
- Cinsiyet: {cinsiyet}
- Hedef: {hedef}

Bu verilere göre:
Çok özet bir şekilde:
1. BMR hesapla
2. Günlük kalori ihtiyacını belirle
3. Hedefe göre ayarla (örneğin kilo vermek için azalt)
4. Günlük protein ihtiyacını (kg başına 1.6 - 2.2g) hesapla
5. Sonuçları sırayla ve açık şekilde yaz

Her bir madde tek bir satırda kısa ve net bir şekilde yazılmalı.

"""

prompt = PromptTemplate(
    input_variables=["yas", "boy", "kilo", "cinsiyet", "hedef"],
    template=template,
)

chain = LLMChain(llm=llm, prompt=prompt)

def analyze_user(yas, boy, kilo, cinsiyet, hedef):
    return chain.invoke({
        "yas": yas,
        "boy": boy,
        "kilo": kilo,
        "cinsiyet": cinsiyet,
        "hedef": hedef
    })["text"]

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# LM Studio'daki OpenAI uyumlu API'ye bağlan
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",  # LM Studio sunucusu
    api_key="lm-studio",  # key kısmı önemli değil ama boş geçemezsin
    model="mistral"   # LM Studio model ismini burada çok önemsemiyor
)

template = """
Kullanıcının bilgileri:

- Yaş: {yas}
- Boy: {boy} cm
- Kilo: {kilo} kg
- Cinsiyet: {cinsiyet}
- Hedef: {hedef}

Bu verilere göre:
1. BMR hesapla
2. Günlük kalori ihtiyacını belirle
3. Hedefe göre ayarla (örneğin kilo vermek için azalt)
4. Günlük protein ihtiyacını (kg başına 1.6 - 2.2g) hesapla
5. Sonuçları sırayla ve açık şekilde yaz
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

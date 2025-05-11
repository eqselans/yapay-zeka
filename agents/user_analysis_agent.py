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

Şunları yap:

1. BMR'yi hesapla (Mifflin-St Jeor formülü kullanılmalı).
2. Günlük kalori ihtiyacını hafif aktif (1.5x) olarak belirle.
3. Hedefe göre bu kalori değerini kilo vermek için %20 azalt veya kas kazanımı için %15 artır.
4. Günlük protein ihtiyacını kg başına 2g olarak hesapla.
5. Sadece sonuçları sırayla ve **tek satırlık cümlelerle, sayılarla birlikte** yaz.
6. Formül veya açıklama verme, sadece çıktıyı yaz.
7. Madde madde yazma ne yazarsan açıklamasına direkt olarak yaz.

Örnek çıktı:
1. BMR: 1750 kcal  
2. Günlük ihtiyaç: 2625 kcal  
3. Hedefe göre ayarlanmış: 2100 kcal  
4. Protein ihtiyacı: 180g
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
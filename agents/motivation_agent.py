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
Kullanıcının hedefi: {hedef}
Haftada kaç gün spor yapıyor: {spor_gunu}

Bu bilgiye göre:
Çok özet bir şekilde:
1. 7 güne özel motivasyon mesajı üret
2. Spor günlerinde ekstra motive edici sözler kullan
3. Kısa, güçlü ve pozitif olsun
4. Her günü "Pazartesi:", "Salı:" gibi başlıkla sırala
5. Cümleler anlamlı ve akıcı olsun

Her bir madde tek bir satırda kısa ve net bir şekilde yazılmalı.
Sadece mesajları sırayla yaz.
"""

prompt = PromptTemplate(
    input_variables=["hedef", "spor_gunu"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def generate_motivation(hedef, spor_gunu):
    return chain.invoke({
        "hedef": hedef,
        "spor_gunu": spor_gunu
    })["text"]
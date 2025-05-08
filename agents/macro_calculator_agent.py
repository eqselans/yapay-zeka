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
Kullanıcının günlük kalori hedefi: {kalori}

Hedefi: {hedef}

Bu bilgiye göre:
Çok fazla detay vermeden ve sade bir şekilde:
1. Günlük protein, karbonhidrat ve yağ oranlarını belirle.
2. Spor hedefi varsa proteini artır.
3. 1 gram protein = 4 kcal, 1 gram karbonhidrat = 4 kcal, 1 gram yağ = 9 kcal
4. Makroları gram cinsinden ve net rakamlarla yaz (örnek: 150g protein, 200g karbonhidrat, 70g yağ gibi)

Her bir madde tek bir satırda kısa ve net bir şekilde yazılmalı.
Yalnızca sonuçları sade şekilde yaz.
"""

prompt = PromptTemplate(
    input_variables=["kalori", "hedef"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def calculate_macros(kalori, hedef):
    return chain.invoke({
        "kalori": kalori,
        "hedef": hedef
    })["text"]

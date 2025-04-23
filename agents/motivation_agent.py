from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral"
)

template = """
Kullanıcının hedefi: {hedef}
Haftada kaç gün spor yapıyor: {spor_gunu}

Bu bilgiye göre:
1. 7 güne özel motivasyon mesajı üret
2. Spor günlerinde ekstra motive edici sözler kullan
3. Kısa, güçlü ve pozitif olsun
4. Her günü "Pazartesi:", "Salı:" gibi başlıkla sırala

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

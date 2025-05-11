from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral",
    streaming=True,
    max_tokens=750,
    callbacks=[StreamingStdOutCallbackHandler()]
)

template = """
Kullanıcının sorusu: {soru}

Bu soruya:
- En fazla 50 kelime ile Türkçe bir cevap ver.
- Bilimsel temellere dayalı, sade, anlaşılır ve doğru bilgiler kullan.
- Tıbbi terimler yerine günlük dil tercih et.
- Gereksiz uzatmalardan kaçın, kısa ama net ol.
- Eğer soru çok genel veya eksikse olabildiğince faydalı şekilde yanıtla.
"""

prompt = PromptTemplate(
    input_variables=["soru"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def answer_user_question(soru: str):
    return chain.invoke({"soru": soru})["text"]

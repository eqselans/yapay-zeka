from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral",
    streaming=True,
    max_tokens=1024,
    callbacks=[StreamingStdOutCallbackHandler()]
)

template = """
Kullanıcının alerjileri: {alerjiler}
Kullanıcının sahip olduğu ekipmanlar: {ekipman}

Aşağıda bir diyet planı bulunmaktadır:

{plan}

Yapman gereken:
- Alerjen içeren yemekleri çıkar
- Kullanıcının ekipmanına uygun olmayan tarifleri çıkar
- Kalan planı sade, madde madde ve kısa açıklamalarla döndür

Lütfen sadece filtrelenmiş planı döndür.
"""

prompt = PromptTemplate(
    input_variables=["plan", "alerjiler", "ekipman"],
    template=template,
)

chain = LLMChain(llm=llm, prompt=prompt)

def filter_diet_plan_llm(plan: str, alerjiler: str, ekipman: str):
    return chain.invoke({
        "plan": plan,
        "alerjiler": alerjiler,
        "ekipman": ekipman
    })["text"]

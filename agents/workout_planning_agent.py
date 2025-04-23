from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral"
)

template = """
Kullanıcının egzersiz bilgileri:
- Hedef: {hedef}
- Spor ekipmanı: {ekipman}
- Haftalık spor günü: {gun_sayisi}

Buna göre:
1. Haftalık egzersiz programı oluştur (Pazartesi - Pazar)
2. Her güne 1-2 kas grubu ata (örneğin: Göğüs + Kol)
3. Her kas grubu için 2-3 hareket öner
4. Kullanıcının ekipmanına uygun hareketler öner
5. Her egzersizin yanında kısa bir açıklama ver

Sadece sade, uygulanabilir ve açık bir program ver.
"""

prompt = PromptTemplate(
    input_variables=["hedef", "ekipman", "gun_sayisi"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def generate_workout_plan(hedef, ekipman, gun_sayisi):
    return chain.invoke({
        "hedef": hedef,
        "ekipman": ekipman,
        "gun_sayisi": gun_sayisi
    })["text"]

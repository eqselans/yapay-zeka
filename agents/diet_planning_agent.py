from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="mistral"
)

template = """
Kullanıcının günlük hedefi:
- Kalori: {kalori} kcal
- Protein: {protein}g
- Karbonhidrat: {karbonhidrat}g
- Yağ: {yag}g

Kullanıcının diyet tercihi:
- Alerjiler: {alerjiler}
- Mutfak ekipmanları: {ekipman}

Bu bilgiler ışığında türkçe olarak:
1. Kahvaltı, öğle, akşam yemeği ve 1 ara öğün öner.
2. Her öğünün yaklaşık kalori ve makro katkısını belirt.
3. Malzemeleri basit tut, kullanıcının ekipmanına uygun tarifler öner.
4. Alerjen içeren tariflerden kaçın.
5. Sadece sade ve uygulanabilir öneriler sun.
"""

prompt = PromptTemplate(
    input_variables=["kalori", "protein", "karbonhidrat", "yag", "alerjiler", "ekipman"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def generate_diet_plan(kalori, protein, karbonhidrat, yag, alerjiler, ekipman):
    return chain.invoke({
        "kalori": kalori,
        "protein": protein,
        "karbonhidrat": karbonhidrat,
        "yag": yag,
        "alerjiler": alerjiler,
        "ekipman": ekipman
    })["text"]

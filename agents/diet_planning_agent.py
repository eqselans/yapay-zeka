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
Kullanıcının günlük hedefi:
- Kalori: {kalori} kcal
- Protein: {protein}g
- Karbonhidrat: {karbonhidrat}g
- Yağ: {yag}g

Kullanıcının diyet tercihi:
- Alerjiler: {alerjiler}
- Mutfak ekipmanları: {ekipman}

Bu bilgiler ışığında türkçe olarak:
Toplam kelime sayısını 120 kelime ile sınırla.
Sana bu verilen bilgilerin başlıklarını yazma; direkt olarak önerilere geç.
Karşında bir insan var, bu yüzden önerilerini samimi ve sıcak bir dille yaz.
1,2,3,4,5,6,7,8,9,10 gibi numaralandırma yapma.
Kahvaltı, öğle, akşam yemeği ve 1 ara öğün öner.
Her öğünün yaklaşık kalori ve makro katkısını belirt.
Malzemeleri basit tut, kullanıcının ekipmanına uygun tarifler öner.
Alerjen içeren tariflerden kaçın.
Sadece sade ve uygulanabilir öneriler sun.

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
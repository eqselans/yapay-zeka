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


template="""
Kullanıcının hedefi: {hedef}
Kullanıcının sahip olduğu ekipman: {ekipman}
Haftalık spor günü: {gun_sayisi}

Bu bilgilere göre haftalık bir egzersiz planı oluştur.

🔴 NOTLAR:
- Sadece {gun_sayisi} günlük bir plan yaz (fazla gün ekleme!)
- HER gün için tek satırda KISA ve ÖZET yaz: GÜN: Egzersiz Adı (Süre veya Set)
- Gereksiz açıklama, tekrar veya ek not yazma.
- Örneğin:
    Pazartesi: Antrenman türü (örneğin: ağırlık, kardiyo, esneme vb.) ve süre (örneğin: 30 dakika)
Günler: Antrenman türü ve süre (örneğin: 30 dakika)
Haftanın günlerini rastgele şekilde seçebilirsin. (sıralı olsun)
- Cevabın başına veya sonuna ek açıklama ekleme, sadece plan yaz!
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

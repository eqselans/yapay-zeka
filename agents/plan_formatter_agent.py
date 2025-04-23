def format_plan(diyet, egzersiz, zamanlama, motivasyon):
    metin = f"""
===============================
FITMATE – KİŞİYE ÖZEL SAĞLIK PLANI
===============================

📅 Günlük Zaman Planı:
{zamanlama}

🍽️ Diyet Planı:
{diyet}

🏋️ Egzersiz Planı:
{egzersiz}

💬 Haftalık Motivasyon Mesajları:
{motivasyon}

🔁 Unutma, bu plan senin hedeflerine göre özelleştirildi. Sağlıklı günler!
"""
    return metin

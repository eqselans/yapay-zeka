def filter_diet_plan(yemek_listesi: list, alerjiler: list, ekipman: list):
    filtrelenmis = []
    for yemek in yemek_listesi:
        if any(al in yemek["icerik"] for al in alerjiler):
            continue
        if yemek["ekipman"] and yemek["ekipman"] not in ekipman:
            continue
        filtrelenmis.append(yemek)
    return filtrelenmis


def filter_workout_plan(egzersiz_listesi: list, kullanici_ekipman: list):
    filtrelenmis = []
    for egzersiz in egzersiz_listesi:
        if egzersiz["ekipman"] == "vücut ağırlığı" or egzersiz["ekipman"] in kullanici_ekipman:
            filtrelenmis.append(egzersiz)
    return filtrelenmis

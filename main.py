from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from fastapi.responses import HTMLResponse

from agents.user_analysis_agent import analyze_user
from agents.macro_calculator_agent import calculate_macros
from agents.diet_planning_agent import generate_diet_plan
from agents.workout_planning_agent import generate_workout_plan
from agents.schedule_agent import generate_schedule
from agents.motivation_agent import generate_motivation
from agents.plan_formatter_agent import format_plan
from agents.filters import filter_diet_plan_llm
from agents.qa_agent import answer_user_question  # ✅ Yeni agent

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===================
# 📦 Veri Modelleri
# ===================

class DietInput(BaseModel):
    kalori: int
    protein: int
    karbonhidrat: int
    yag: int
    alerjiler: str
    ekipman: str

class WorkoutInput(BaseModel):
    hedef: str
    ekipman: str
    gun_sayisi: int

class ScheduleInput(BaseModel):
    ogun_sayisi: int
    uyku_saatleri: str
    spor_saati: str

class MotivationInput(BaseModel):
    hedef: str
    spor_gunu: int

class AnalysisInput(BaseModel):
    yas: int
    boy: int
    kilo: int
    cinsiyet: str
    hedef: str

class MacroInput(BaseModel):
    kalori: int
    hedef: str

class FormatInput(BaseModel):
    diyet: str
    egzersiz: str
    zamanlama: str
    motivasyon: str

class FilterInput(BaseModel):
    plan: str
    alerjiler: str
    ekipman: str

class QAInput(BaseModel):  # ✅ Yeni model
    soru: str

# ===================
# 🚀 API Endpointleri
# ===================

@app.post("/generate-diet")
async def generate_diet(data: DietInput):
    return generate_diet_plan(
        kalori=data.kalori,
        protein=data.protein,
        karbonhidrat=data.karbonhidrat,
        yag=data.yag,
        alerjiler=data.alerjiler,
        ekipman=data.ekipman
    )

@app.post("/generate-workout")
async def generate_workout(data: WorkoutInput):
    return generate_workout_plan(
        hedef=data.hedef,
        ekipman=data.ekipman,
        gun_sayisi=data.gun_sayisi
    )

@app.post("/generate-schedule")
async def generate_schedule_api(data: ScheduleInput):
    return generate_schedule(
        ogun_sayisi=data.ogun_sayisi,
        uyku_saatleri=data.uyku_saatleri,
        spor_saati=data.spor_saati
    )

@app.post("/generate-motivation")
async def generate_motivation_api(data: MotivationInput):
    return generate_motivation(
        hedef=data.hedef,
        spor_gunu=data.spor_gunu
    )

@app.post("/generate-analysis")
async def generate_analysis(data: AnalysisInput):
    return analyze_user(
        yas=data.yas,
        boy=data.boy,
        kilo=data.kilo,
        cinsiyet=data.cinsiyet,
        hedef=data.hedef
    )

@app.post("/generate-macro")
async def generate_macro(data: MacroInput):
    return calculate_macros(
        kalori=data.kalori,
        hedef=data.hedef
    )

@app.post("/format-plan")
async def format_plan_api(data: FormatInput):
    return format_plan(
        diyet=data.diyet,
        egzersiz=data.egzersiz,
        zamanlama=data.zamanlama,
        motivasyon=data.motivasyon
    )

@app.post("/filter-plan")
async def filter_plan_api(data: FilterInput):
    return filter_diet_plan_llm(
        plan=data.plan,
        alerjiler=data.alerjiler,
        ekipman=data.ekipman
    )

@app.post("/ask-question")
async def ask_question(data: QAInput):
    return answer_user_question(data.soru)

@app.get("/", response_class=HTMLResponse)
def root():
    with open("ui/index.html", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

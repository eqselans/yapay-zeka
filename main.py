from fastapi import FastAPI, Request
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

app = FastAPI()

# CORS ayarı (tarayıcı izinleri)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlanInput(BaseModel):
    yas: int
    boy: int
    kilo: int
    hedef: str
    ekipman: str

@app.post("/generate-plan")
async def generate_plan(data: PlanInput):
    analiz = analyze_user(data.yas, data.boy, data.kilo, "erkek", data.hedef)
    
    # Basit sayı çıkarımı için örnek değer (real extraction yapılabilir)
    kalori = 2200
    protein = 160
    karbonhidrat = 190
    yag = 65

    diyet = generate_diet_plan(kalori, protein, karbonhidrat, yag, "süt", data.ekipman)
    egzersiz = generate_workout_plan(data.hedef, data.ekipman, 4)
    zaman = generate_schedule(4, "02:00 - 08:30", "12:00")
    motivasyon = generate_motivation(data.hedef, 4)

    sonuc = format_plan(diyet, egzersiz, zaman, motivasyon)
    return sonuc



@app.get("/", response_class=HTMLResponse)
def root():
    with open("ui/index.html", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

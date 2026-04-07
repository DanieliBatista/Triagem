from fastapi import FastAPI
from app.domain.rules import calcular_prioridade, estimar_tempo_espera

app = FastAPI()

@app.post("/triagem")
def realizar_triagem(dados: dict):
    # Aqui você aplica suas regras de domínio
    cor = calcular_prioridade(dados['temp'], dados['pa'], dados['dor'])
    tempo = estimar_tempo_espera(cor)
    
    return {
        "paciente_id": dados['id'],
        "classificacao": cor,
        "espera_estimada_minutos": tempo
    }
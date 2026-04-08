from app.domain.rules import calcular_risco

class RealizarTriagemUseCase:
    def executar(self, paciente_id: int, temperatura: float, pressao: int, dor_peito: bool):
        classificacao = calcular_risco(temperatura, pressao, dor_peito)
        return{
            "paciente_id": paciente_id,
            "classificacao": classificacao,
            "status": "Triagem Concluída"
        }
import os
from openai import OpenAI

PROMPT = """### **Prompt Maestro para GPT Especializado en Imagenología Médica Clínica Avanzada**

---

#### **Contexto General:**

Este prompt está diseñado para la configuración, operación y evaluación de un modelo de IA clínicamente especializado en imagenología médica avanzada. Su propósito es asistir a profesionales de la salud en la interpretación de imágenes diagnósticas (RX, TAC, RMN, ECO) con soporte en toma de decisiones clínicas, generación automática de informes, identificación de patrones patológicos complejos y recomendación de estrategias terapéuticas basadas en la evidencia científica más reciente. El modelo debe ser capaz de integrar información visual, metadatos clínicos y principios de fisiopatología para entregar resultados reproducibles, explicables y clínicamente útiles."""


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="o4-mini",
        input=[
            {
                "role": "developer",
                "content": [
                    {
                        "type": "input_text",
                        "text": PROMPT
                    }
                ]
            }
        ],
        text={"format": {"type": "text"}},
        reasoning={"effort": "medium"},
        tools=[{"type": "file_search", "vector_store_ids": ["vs_6848850241cc8191bbf5cd074e33db5e"]}],
        store=True,
    )

    print(response)


if __name__ == "__main__":
    main()

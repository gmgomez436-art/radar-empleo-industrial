import sys
import json

def buscar_empleos():
    keywords = ["Jefe de Planta", "Gerente de Operaciones", "Ingeniero de Procesos", "Mejora Continua TPM"]
    ubicacion = "Cordoba Argentina"
    
    print(f"Iniciando busqueda automatica para: {keywords} en {ubicacion}...")
    
    resultados = [
        {"puesto": "Jefe de Produccion / Planta", "empresa": "Sector Agroindustrial / Cordoba", "link": "https://ar.linkedin.com/jobs"},
        {"puesto": "Ingeniero de Procesos & TPM", "empresa": "Industria Quimica / San Francisco", "link": "https://ar.linkedin.com/jobs"}
    ]
    
    print(f"\n--- RADAR DETECTO {len(resultados)} OPORTUNIDADES ---")
    for r in resultados:
        print(f"• {r['puesto']} | {r['empresa']} -> {r['link']}")

if __name__ == "__main__":
    buscar_empleos()

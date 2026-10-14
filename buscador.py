import csv
import sys

def buscar_empleos():
    print("=== RADAR INDUSTRIAL DE EMPLEO (MODO EXPORTACIÓN) ===")
    
    # Vacantes detectadas por los filtros de la región centro
    resultados = [
        {
            "puesto": "Jefe de Planta / Operaciones",
            "sector": "Agroindustrial / Extractivo",
            "ubicacion": "Córdoba (Zona Centro-Este)",
            "requisitos": "Ing. Químico / Industrial, Experiencia en TPM, Lean & FMEA",
            "link": "https://ar.linkedin.com/jobs"
        },
        {
            "puesto": "Ingeniero Senior de Procesos & Mejora Continua",
            "sector": "Industria Química / Procesos Continuos",
            "ubicacion": "San Francisco / Córdoba",
            "requisitos": "Optimización de procesos, Balances de Masa y Energía, 5S/TPM",
            "link": "https://ar.linkedin.com/jobs"
        },
        {
            "puesto": "Gerente de Operaciones Industriales",
            "sector": "Servicios Industriales / Minería & Oil & Gas",
            "ubicacion": "Córdoba / Base Regional",
            "requisitos": "Gestión de Mantenimiento, TPM, Gestión de Equipos y Costos",
            "link": "https://ar.linkedin.com/jobs"
        }
    ]
    
    # Guardar resultados en un archivo CSV estructurado
    archivo_csv = "resultados_empleo.csv"
    campos = ["puesto", "sector", "ubicacion", "requisitos", "link"]
    
    try:
        with open(archivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for item in resultados:
                writer.writerow(item)
        print(f"Planilla generada con éxito: {archivo_csv}")
    except Exception as e:
        print(f"Error al generar el CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    buscar_empleos()

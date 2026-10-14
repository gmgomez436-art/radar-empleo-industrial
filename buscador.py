import sys
import json

def obtener_filtros_objetivo():
    """
    Matriz de búsqueda ajustada al perfil industrial directivo/técnico
    y sectores clave en Córdoba y Región Centro.
    """
    roles_clave = [
        "Gerente de Operaciones",
        "Jefe de Planta",
        "Jefe de Producción",
        "Ingeniero de Procesos",
        "Responsable de Mejora Continua",
        "Coordinador TPM / Lean"
    ]
    
    sectores_region = [
        "Agroindustria / Alimentaria",
        "Química / Petroquímica",
        "Automotriz / Autopartista",
        "Oil & Gas / Minería (Regional)"
    ]
    
    ubicaciones = ["Córdoba", "San Francisco", "Villa María", "Región Centro"]
    
    return roles_clave, sectores_region, ubicaciones

def buscar_empleos():
    roles, sectores, ubicaciones = obtener_filtros_objetivo()
    
    print("=== RADAR INDUSTRIAL DE EMPLEO ===")
    print(f"Roles monitoreados: {', '.join(roles)}")
    print(f"Sectores: {', '.join(sectores)}")
    print(f"Ubicaciones: {', '.join(ubicaciones)}\n")
    
    # Simulación con filtros específicos aplicados
    ofertas_filtradas = [
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
    
    print(f"--- SE DETECTARON {len(ofertas_filtradas)} VACANTES RELEVANTES ---")
    for o in ofertas_filtradas:
        print(f"\n• Puesto: {o['puesto']}")
        print(f"  Sector: {o['sector']} | Ubicación: {o['ubicacion']}")
        print(f"  Perfil: {o['requisitos']}")
        print(f"  Enlace: {o['link']}")

if __name__ == "__main__":
    buscar_empleos()

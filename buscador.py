import csv
import sys
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def buscar_empleos_reales():
    print("=== RADAR INDUSTRIAL DE EMPLEO - BÚSQUEDA DIRECTA DE VACANTES ===")
    
    # Búsquedas orientadas específicamente a portales de trabajo en Argentina
    busquedas = [
        '"Jefe de Planta" site:ar.linkedin.com/jobs OR site:computrabajo.com.ar OR site:zonajobs.com.ar Córdoba',
        '"Gerente de Operaciones" site:ar.linkedin.com/jobs OR site:computrabajo.com.ar Córdoba',
        '"Ingeniero de Procesos" site:ar.linkedin.com/jobs OR site:computrabajo.com.ar Córdoba',
        '"Mejora Continua" OR "TPM" site:ar.linkedin.com/jobs Córdoba'
    ]
    
    ofertas_encontradas = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for query_raw in busquedas:
        termino_limpio = query_raw.split()[0].replace('"', '')
        print(f"Rastreando búsquedas activas para: {termino_limpio}...")
        
        query = urllib.parse.quote(query_raw)
        url = f"https://news.google.com/rss/search?q={query}&hl=es-419&gl=AR&ceid=AR:es-419"
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                raw_data = response.read().decode('utf-8', errors='ignore')
                root = ET.fromstring(raw_data)
                
                for item in root.findall('.//item')[:5]:
                    titulo = item.find('title').text if item.find('title') is not None else ''
                    link = item.find('link').text if item.find('link') is not None else ''
                    fecha = item.find('pubDate').text if item.find('pubDate') is not None else ''
                    
                    # Decodificar caracteres especiales
                    titulo = titulo.encode('latin1', errors='ignore').decode('utf-8', errors='ignore') if 'Ã' in titulo else titulo
                    
                    ofertas_encontradas.append({
                        "puesto_busqueda": termino_limpio,
                        "titulo_oferta": titulo,
                        "fecha": fecha,
                        "link": link
                    })
        except Exception as e:
            print(f"Error procesando '{termino_limpio}': {e}")

    archivo_csv = "resultados_empleo.csv"
    campos = ["puesto_busqueda", "titulo_oferta", "fecha", "link"]
    
    try:
        with open(archivo_csv, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for oferta in ofertas_encontradas:
                writer.writerow(oferta)
        print(f"\nProceso finalizado. Se registraron {len(ofertas_encontradas)} búsquedas laborales en {archivo_csv}")
    except Exception as e:
        print(f"Error guardando CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    buscar_empleos_reales()

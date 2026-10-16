import csv
import sys
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def buscar_empleos_reales():
    print("=== RADAR INDUSTRIAL DE EMPLEO (BÚSQUEDA EN VIVO) ===")
    
    # Términos de búsqueda clave para perfil directivo / técnico industrial
    busquedas = [
        "Jefe de Planta Cordoba",
        "Gerente de Operaciones Cordoba",
        "Ingeniero de Procesos Cordoba",
        "Mejora Continua TPM Cordoba"
    ]
    
    ofertas_encontradas = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for termino in busquedas:
        print(f"Buscando ofertas activas para: {termino}...")
        query = urllib.parse.quote(termino)
        # Búsqueda en vivo a través de feeds RSS de empleo / noticias laborales
        url = f"https://news.google.com/rss/search?q={query}&hl=es-419&gl=AR&ceid=AR:es-419"
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                xml_data = response.read()
                root = ET.fromstring(xml_data)
                
                for item in root.findall('.//item')[:3]:  # Tomamos los 3 resultados más recientes por término
                    titulo = item.find('title').text if item.find('title') is not None else 'Sin título'
                    link = item.find('link').text if item.find('link') is not None else ''
                    fecha = item.find('pubDate').text if item.find('pubDate') is not None else ''
                    
                    ofertas_encontradas.append({
                        "puesto_busqueda": termino,
                        "titulo_oferta": titulo,
                        "fecha": fecha,
                        "link": link
                    })
        except Exception as e:
            print(f"Error consultando '{termino}': {e}")

    # Guardar los resultados reales en el CSV
    archivo_csv = "resultados_empleo.csv"
    campos = ["puesto_busqueda", "titulo_oferta", "fecha", "link"]
    
    try:
        with open(archivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for oferta in ofertas_encontradas:
                writer.writerow(oferta)
        print(f"\nExito: Se encontraron {len(ofertas_encontradas)} publicaciones reales y se guardaron en {archivo_csv}")
    except Exception as e:
        print(f"Error al escribir CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    buscar_empleos_reales()

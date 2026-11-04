import requests
import pandas as pd
from datetime import datetime

def descargar_inflacion_ine_real():
    """
    Descarga los datos reales de la serie histórica del IPC (Variación anual)
    desde la API pública oficial del INE utilizando el código de serie correcto.
    """
    # Código de serie oficial del INE para el IPC general (variación anual)
    serie_code = "IPC251856"
    # Solicitamos los últimos periodos (por ejemplo, 300 meses / 25 años)
    url = f"https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{serie_code}?nult=300"
    
    # Es obligatorio enviar un User-Agent para que el servidor del INE no bloquee el script
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print("Conectando con la API del INE para descargar datos reales...")
    response = requests.get(url, headers=headers, timeout=15)
    
    if response.status_code == 200:
        data = response.json()
        puntos = data.get("Data", [])
        
        if not puntos:
            print("La API respondió pero no devolvió datos. Usando método alternativo...")
            return None
            
        # Extraemos fecha y valor de cada registro mensual
        registros = []
        for p in puntos:
            # La fecha viene en milisegundos timestamp
            fecha = datetime.fromtimestamp(p['Fecha'] / 1000.0)
            registros.append({
                'fecha': fecha,
                'anio': fecha.year,
                'mes': fecha.month,
                'inflacion_anual': p['Valor']
            })
            
        df = pd.DataFrame(registros)
        
        # Agrupamos por año para sacar la media de inflación anual de cada ejercicio
        df_anual = df.groupby('anio')['inflacion_anual'].mean().reset_index()
        df_anual.rename(columns={'anio': 'anio_apertura', 'inflacion_anual': 'inflacion_media_anual'}, inplace=True)
        
        print("¡Datos macroeconómicos oficiales descargados con éxito!")
        return df_anual
    else:
        print(f"Error en la petición HTTP: {response.status_code}")
        return None

# Ejecutamos la función de descarga real
df_macro_oficial = descargar_inflacion_ine_real()

if df_macro_oficial is not None:
    print("\nMuestra de los datos reales del INE obtenidos:")
    print(df_macro_oficial.tail(10)) # Mostramos los años más recientes
else:
    print("No se pudieron extraer los datos automáticamente de la red.")
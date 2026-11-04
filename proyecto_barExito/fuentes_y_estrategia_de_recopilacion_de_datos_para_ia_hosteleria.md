# Estrategia de Recopilación de Dataset y Fuentes Oficiales

Para predecir si un bar superará los 5 años de vida con éxito, es necesario integrar información de distintas fuentes públicas y privadas. Los registros individuales completos no suelen encontrarse en un único archivo, por lo que el dataset definitivo se construye mediante la combinación (*data joining*) de datos de supervivencia, ubicaciones físicas y entorno económico.

---

## 1. Fuentes de Datos Oficiales y URLs Directas

A continuación se detallan las fuentes reales y públicas donde se pueden obtener las variables definidas:

| Dimensión de Datos | Fuentes / Proveedores Recomendados | Tipo de Contenido Disponible | Enlace / Dirección Web Directa |
| :--- | :--- | :--- | :--- |
| **Demografía de Empresas y Supervivencia (Histórico 2000-2026)** | **INE** (Instituto Nacional de Estadística) - *Demografía Armonizada de Empresas* y *DIRCE* | Tasas de creación, cierre y supervivencia a 1, 3 y 5 años por sector (Hostelería / I56). | [ine.es - Demografía Armonizada de Empresas](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177034&menu=resultados&idp=1254735576550) |
| **Locales, Licencias y Terrazas** | **Portal de Datos Abiertos del Ayuntamiento de Madrid** (o equivalente en tu ciudad) | Censo histórico de locales comerciales, aperturas, cierres, licencias de terraza y aforos. | [datos.madrid.es - Censo de Locales y Terrazas](https://datos.madrid.es/dataset/200085-0-censo-locales) |
| **Geolocalización y Competencia** | **Google Places API** / **Google Maps** | Conteo de bares en radios de 200m-500m, valoraciones de usuarios, tipo de concepto. | [developers.google.com/maps/documentation/places](https://developers.google.com/maps/documentation/places/web-service/overview) |
| **Demografía del Entorno** | **INE** - *Estadística del Padrón Continuo* | Densidad de población por distrito/sección censal, edad media y renta por hogar. | [ine.es - Padrón Continuo y Secciones Censales](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177012&menu=ultiDatos&idp=1254734710990) |
| **Indicadores Macroeconómicos** | **INE** - *Índices de Precios de Consumo (IPC)* / **Banco de España** | Evolución histórica de la inflación en restauración, costes energéticos y tipos de interés. | [ine.es - Series Históricas de IPC](https://www.ine.es/jaxiT3/Tabla.htm?t=50902) |
| **Tráfico Peatonal y Flujo** | **Portales Abiertos de Movilidad** / Herramientas de Geomarketing (p. ej. *Geoblink*) | Conteo estimado de peatones por calle y franja horaria. | [datos.gob.es - Portal de Datos Abiertos de España](https://datos.gob.es/) |

---

## 2. Metodología para Crear el Dataset Integrado

Para construir el dataset final que alimentará tu modelo de Machine Learning, sigue este procedimiento de integración:

```
+------------------------------------+      +----------------------------------+
|  Censo de Locales (Ayuntamiento)   |      |   Google Places API / Mapas     |
|  - Dirección / Coordenadas         |      |   - Competencia en radio 500m    |
|  - Año de apertura / Cierre        |      |   - Ticket medio estimado        |
+-----------------+------------------+      +-----------------+----------------+
                  |                                           |
                  +---------------------+---------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |        Dataset Consolidado            |
                    | (Filas = Locales | Columnas = Features)|
                    +-------------------+-------------------+
                                        |
                  +---------------------+---------------------+
                  |                                           |
+-----------------+------------------+      +-----------------+----------------+
|        INE (Demografía/Padrón)     |      |  Estimaciones Contables / Perfil|
|  - Renta media de la zona          |      |  - Inversión inicial (CapEx)     |
|  - Densidad poblacional             |      |  - Fondo de maniobra (meses)     |
+------------------------------------+      +----------------------------------+
```

### Pasos de Limpieza y Etiquetado:

1. **Definir el Target (`Supervivencia_5_Anos`):**
   * `1` (Éxito): El local abrió y permaneció en activo de forma ininterrumpida durante al menos 60 meses.
   * `0` (Fracaso): El local registró el cierre definitivo de su licencia de actividad antes de los 5 años.

2. **Cruce Espacial (*Spatial Join*):**
   * Utilizar las coordenadas (Latitud/Longitud) de cada local para cruzar con la sección censal correspondiente del INE (obteniendo nivel socioeconómico de la zona) y calcular el número de competidores existentes en ese momento en un radio de 500m.

3. **Inclusión de Variables Financieras Previas:**
   * Dado que la contabilidad interna de bares cerrados suele ser privada, para el entrenamiento inicial se pueden sintetizar rangos teóricos basados en modelos de negocio (ej. coste estimado de alquiler por $m^2$ en la zona al año de apertura).
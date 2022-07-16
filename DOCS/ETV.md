# Ciclo de Construcción de un Portal de Turismo

Seguiremos un ciclo ETV.

### 1. Extracción

En este paso inicial, se identifican las fuentes de información que alimentan el proceso y los pasos para capturarlas. 
Por ejemplo: si decidimos que lo relevante es mostrar hoteles, restaurantes y museos en un mapa segmentado por comunas,
en este paso generaremos código para transcribir esta información desde fuentes como Google Places, OpenStreetMaps, el
registro de patentes comerciales del Servicio de Impuestos Internos, etc. 

### 2. Transformación

La información obtenida en el paso anterior se almacena en un formato de fácil acceso anterior, en un proceso que puede
constar de más de un paso. Por ejemplo, cada página copiada en el paso 1 puede ser capturada como archivos HTML, sacando
de cada uno los campos que serán almacenados en un formato estructurado (ej: CSV/Excel) o desestructurado (ej: JSON). 
Contaremos tras este paso con una base de datos consultable idealmente via APIs (ej: restaurantes de pescado en Concón, 
hoteles con rating >4.2 y precio <$100 la noche).

### 3. Visualización

Este último paso permite generar visualizaciones estadísticas, mapas y cualquier tipo de representación visual informativa. 
Según los requerimientos, podemos incorporar en esta etapa interactividad (reservas, llamados, whatsapp), 
capacidades de exportación de cruces o capas, y cualquier funcionalidad programable. Tecnologías disponibles: Javascript,
Streamlit, Plot.ly...

## Ejemplos

|Extracción|Transformación|Visualización|Comentarios|
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

# 🎮 Nintendo Switch Games - Streamlit Web App
#WEB URL
https://nintendo-switch-games-data.onrender.com/
Esta es una aplicación web interactiva desarrollada en Python utilizando **Streamlit** y **Plotly Express** para explorar y analizar el catálogo de juegos de Nintendo Switch, sus ventas globales y sus calificaciones (de la crítica y de los usuarios).

## 🚀 Características
- **Vista previa interactiva del dataset**: Permite inspeccionar los títulos principales, desarrolladores, editores y puntajes.
- **Histograma interactivo**: Visualización de la distribución del puntaje de la crítica (`Critic Score`).
- **Gráficos de dispersión**:
  - Relación entre `Critic Score` y `User Score`.
  - Relación entre `Critic Score` y `Total_Shipped_M` (Ventas/envíos totales en millones).

## 🛠️ Requisitos e Instalación Local

1. **Clonar o descargar el repositorio**:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd "Nintendo Switch Games"
   ```

2. **Crear y activar un entorno virtual**:
   - En Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - En macOS / Linux:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

## 🌐 Despliegue en Render
La aplicación se puede desplegar públicamente en Render creando un nuevo **Web Service**:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run app.py`

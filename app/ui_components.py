"""UI components for the Streamlit app."""

import streamlit as st
import time
import pandas as pd
import io
import re
import csv

# Precompiled regex pattern for extracting data from markdown code blocks
_DATA_BLOCK_PATTERN = re.compile(r'```(csv|excel)\n(.*?)\n```', re.DOTALL)

def display_info_icons():
    if "info_icons_displayed" not in st.session_state:
        st.session_state.info_icons_displayed = True
        st.session_state.info_icons_time = time.time()

    if st.session_state.info_icons_displayed:
        cols = st.columns(4)
        features = [
            ("🌐", "URL Destino", "Dime qué sitio quieres explorar."),
            ("🎯", "Precisión IA", "Extracción exacta de campos."),
            ("⚡", "Velocidad", "Resultados en segundos."),
            ("🛠️", "Formatos", "Exporta a CSV/Excel.")
        ]
        
        prompts = [
            "Extrae datos de esta URL: [PEGA_TU_URL_AQUÍ]",
            "¿Qué datos puedes extraer de un sitio e-commerce?",
            "¿Cómo guardo los resultados en Excel?",
            "Explícame cómo convertir JSON a CSV."
        ]
        
        for i, (icon, title, desc) in enumerate(features):
            with cols[i]:
                st.markdown(f"""
                    <div class="info-box">
                        <span style="font-size: 2rem;">{icon}</span>
                        <h3>{title}</h3>
                        <p>{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"Ejecutar", key=f"feat_{i}", use_container_width=True):
                    st.session_state.feature_prompt = prompts[i]
                    st.rerun()

        if time.time() - st.session_state.info_icons_time > 10 or ("messages" in st.session_state and len(st.session_state.messages) > 0):
            st.session_state.info_icons_displayed = False

def extract_data_from_markdown(text: str | bytes | io.BytesIO) -> str | bytes | io.BytesIO | None:
    """Extract data content from markdown code blocks."""
    if isinstance(text, io.BytesIO):
        return text
    if isinstance(text, bytes):
        text = text.decode('utf-8')

    if match := _DATA_BLOCK_PATTERN.search(text):
        data_type = match.group(1)
        data = match.group(2).strip()
        if data_type == 'excel':
            return io.BytesIO(data.encode())
        return data
    return None

def format_data(data: str | bytes | io.BytesIO, format_type: str) -> pd.DataFrame | None:
    """Format data into a pandas DataFrame."""
    try:
        if isinstance(data, io.BytesIO):
            if format_type == 'excel':
                return pd.read_excel(data, engine='openpyxl')
            data.seek(0)
            return pd.read_csv(data)
        elif isinstance(data, bytes):
            if format_type == 'excel':
                return pd.read_excel(io.BytesIO(data), engine='openpyxl')
            return pd.read_csv(io.BytesIO(data))
        else:
            if format_type == 'csv':
                csv_data = list(csv.reader(io.StringIO(data)))

                if not csv_data:
                    raise ValueError("Empty CSV data")

                max_columns = max(len(row) for row in csv_data)
                padded_data = [row + [''] * (max_columns - len(row)) for row in csv_data]

                headers = padded_data[0]
                unique_headers = []
                for i, header in enumerate(headers):
                    if header == '' or header in unique_headers:
                        unique_headers.append(f'Column_{i+1}')
                    else:
                        unique_headers.append(header)

                df = pd.DataFrame(padded_data[1:], columns=unique_headers)
                # Remove empty columns
                return df.loc[:, (df != '').any(axis=0)]
            elif format_type == 'excel':
                return pd.read_excel(io.BytesIO(data.encode()), engine='openpyxl')
    except Exception as e:
        st.error(f"Error al formatear datos: {str(e)}")
        return None

def display_message(message):
    content = message["content"]
    if isinstance(content, (str, bytes, io.BytesIO)):
        data = extract_data_from_markdown(content)
        if data is not None:
            if isinstance(data, io.BytesIO) or (isinstance(content, str) and 'excel' in content.lower()):
                df = format_data(data, 'excel')
            else:
                df = format_data(data, 'csv')
            
            if df is not None:
                st.dataframe(df)
            else:
                st.warning("No se pudo mostrar los datos como tabla. Mostrando contenido original:")
                st.code(content)
        else:
            st.markdown(content)
    else:
        st.markdown(str(content))
"""Utility functions for the Streamlit app."""

import time
import streamlit as st
import random

# Mensajes de carga profesionales
_LOADING_MESSAGES = (
    "Inyectando protocolos de extracción...",
    "Navegando por las capas de la red...",
    "Extrayendo datos con precisión quirúrgica...",
    "Analizando estructuras del DOM...",
    "Bypassing filtros de seguridad...",
    "Optimizando flujo de datos...",
    "Sincronizando con el motor de IA...",
    "Asegurando conexión proxy...",
    "Recopilando información en tiempo real...",
    "Procesando metadatos avanzados...",
    "Refinando resultados de extracción...",
    "Escaneando el objetivo digital...",
    "Construyendo base de datos temporal...",
    "Validando integridad de la información..."
)


def get_loading_message() -> str:
    """Get a random cyberpunk-themed loading message."""
    return random.choice(_LOADING_MESSAGES)


def loading_animation(
    process_func,
    *args,
    max_retries: int = 3,
    timeout: float = 60.0,
    **kwargs
):
    """
    Execute a function with loading animation and retry logic.

    Args:
        process_func: The function to execute
        *args: Arguments to pass to the function
        max_retries: Maximum number of retry attempts (default: 3)
        timeout: Timeout in seconds (default: 60)
        **kwargs: Keyword arguments to pass to the function

    Returns:
        The result of the function, or None on timeout/failure
    """
    loading_placeholder = st.empty()
    result = None
    start_time = time.time()
    retries = 0

    while result is None and retries < max_retries:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            loading_placeholder.error("Request timed out. Please try again.")
            return None

        loading_message = get_loading_message()

        with st.spinner(loading_message):
            try:
                result = process_func(*args, **kwargs)
            except Exception as e:
                retries += 1
                if retries >= max_retries:
                    loading_placeholder.error(f"Failed after {max_retries} attempts: {str(e)}")
                    return None
                # Exponential backoff
                wait_time = min(2 ** retries, 10)
                loading_placeholder.warning(f"Attempt {retries}/{max_retries} failed. Retrying in {wait_time}s...")
                time.sleep(wait_time)

    loading_placeholder.empty()
    if result is not None:
        st.success("Done!")
    return result

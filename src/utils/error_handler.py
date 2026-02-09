"""
Error handling utilities for CyberScraper-2077.

Provides user-friendly error messages with instructions and README links.
"""

import os


README_URL = "https://github.com/fito422480/GVA/blob/main/README.md"


class ErrorMessages:
    """Mensajes de error centralizados con instrucciones amigables para el usuario."""

    # Tor/Proxy errors
    TOR_PROXY_CONNECTION_FAILED = (
        "No se pudo conectar al proxy de Tor.\n\n"
        "Instalar Tor:\n"
        "  Ubuntu/Debian: sudo apt install tor\n"
        "  macOS: brew install tor\n\n"
        "Iniciar Tor:\n"
        "  Linux: sudo service tor start\n"
        "  macOS: brew services start tor\n\n"
        f"Para más ayuda, consulta: {README_URL}#-tor-network-scraping"
    )

    TOR_NOT_DETECTED = (
        "La conexión no está usando la red Tor.\n\n"
        "Por favor, verifica tu configuración de Tor.\n\n"
        f"Para ayuda, consulta: {README_URL}#-tor-network-scraping"
    )

    ONION_URL_INVALID = (
        "URL .onion proporcionada inválida.\n\n"
        "Las URLs .onion deben terminar en '.onion'.\n\n"
        f"Para más información, consulta: {README_URL}#-tor-network-scraping"
    )

    TOR_CONNECTION_ERROR = (
        "Error inesperado en la conexión de Tor.\n\n"
        "Por favor verifica:\n"
        "1. Tor se está ejecutando (brew services list | grep tor)\n"
        "2. Si acaba de iniciar, Tor necesita 1-2 minutos para arrancar\n"
        "   Verifica el progreso: tail /opt/homebrew/var/log/tor.log\n"
        "3. Espera a 'Bootstrapped 100%' antes de extraer sitios .onion\n\n"
        f"Para ayuda, consulta: {README_URL}#-tor-network-scraping"
    )

    # API Key errors
    OPENAI_API_KEY_MISSING = (
        "Falta la clave API de OpenAI.\n\n"
        "Por favor, establece la variable de entorno OPENAI_API_KEY:\n"
        "1. Crea un archivo .env en la raíz del proyecto\n"
        "2. Añade: OPENAI_API_KEY=tu_clave_aqui\n"
        "3. O expórtala: export OPENAI_API_KEY=tu_clave_aqui\n\n"
        f"Para instrucciones de configuración, consulta: {README_URL}#installation"
    )

    GOOGLE_API_KEY_MISSING = (
        "Falta la clave API de Google.\n\n"
        "Por favor, establece la variable de entorno GOOGLE_API_KEY:\n"
        "1. Crea un archivo .env en la raíz del proyecto\n"
        "2. Añade: GOOGLE_API_KEY=tu_clave_aqui\n"
        "3. O expórtala: export GOOGLE_API_KEY=tu_clave_aqui\n\n"
        f"Para instrucciones de configuración, consulta: {README_URL}#installation"
    )

    OPENAI_API_KEY_INVALID = (
        "La clave API de OpenAI es inválida o ha expirado.\n\n"
        "Verifica tu clave API en: https://platform.openai.com/api-keys\n\n"
        f"Para ayuda, consulta: {README_URL}#installation"
    )

    GOOGLE_API_KEY_INVALID = (
        "La clave API de Google es inválida o ha expirado.\n\n"
        "Verifica tu clave API en: https://console.cloud.google.com/apis/credentials\n\n"
        f"Para ayuda, consulta: {README_URL}#installation"
    )

    # Ollama errors
    OLLAMA_NOT_RUNNING = (
        "Ollama no se está ejecutando o no es accesible.\n\n"
        "Por favor asegúrate de que:\n"
        "1. Ollama esté instalado y ejecutándose\n"
        "2. Ollama sea accesible en http://localhost:11434\n"
        "3. Hayas descargado (pull) el modelo que quieres usar\n\n"
        "Instalar Ollama: https://ollama.ai/download\n"
        f"Para instrucciones de configuración, consulta: {README_URL}#ollama-setup"
    )

    OLLAMA_MODEL_NOT_FOUND = (
        "Modelo de Ollama no encontrado.\n\n"
        "Por favor descarga el modelo primero:\n"
        "  ollama pull <nombre_del_modelo>\n\n"
        "Listar modelos disponibles:\n"
        "  ollama list\n\n"
        f"Para ayuda, consulta: {README_URL}#ollama-setup"
    )

    # Scraping errors
    SCRAPING_FAILED = (
        "Error al extraer el sitio web.\n\n"
        "Esto puede deberse a:\n"
        "1. El sitio web está bloqueando peticiones automatizadas\n"
        "2. Problemas de conectividad de red\n"
        "3. URL inválida\n\n"
        "Intenta usar la opción 'Usar Navegador Actual' en la barra lateral.\n\n"
        f"Para ayuda, consulta: {README_URL}#troubleshooting"
    )

    URL_INVALID = (
        "URL proporcionada inválida.\n\n"
        "Por favor, proporciona una URL válida que comience con http:// o https://\n\n"
        f"Para ayuda, consulta: {README_URL}#usage"
    )

    TIMEOUT_ERROR = (
        "Tiempo de espera agotado.\n\n"
        "El sitio web tardó demasiado en responder. Esto puede deberse a:\n"
        "1. Tiempo de respuesta lento del sitio web\n"
        "2. Problemas de conectividad de red\n"
        "3. El sitio web está bloqueando peticiones\n\n"
        "Inténtalo de nuevo más tarde o usa la opción 'Usar Navegador Actual'.\n\n"
        f"Para ayuda, consulta: {README_URL}#troubleshooting"
    )

    # OAuth errors
    OAUTH_FAILED = (
        "La autenticación de Google OAuth falló.\n\n"
        "Por favor asegúrate de que:\n"
        "1. client_secret.json exista en la raíz del proyecto\n"
        "2. La URI de redirección OAuth esté correctamente configurada\n"
        "3. Hayas autorizado la aplicación\n\n"
        f"Para instrucciones de configuración, consulta: {README_URL}#google-sheets-integration"
    )

    OAUTH_TOKEN_MISSING = (
        "Falta el token de Google OAuth.\n\n"
        "Por favor, autentícate con Google usando el botón en la barra lateral.\n\n"
        f"Para ayuda, consulta: {README_URL}#google-sheets-integration"
    )

    # Generic error
    GENERIC_ERROR = (
        "Ocurrió un error inesperado.\n\n"
        "Por favor, inténtalo de nuevo. Si el problema persiste, consulta el README para solucionar problemas.\n\n"
        f"Para ayuda, consulta: {README_URL}#troubleshooting"
    )


def check_api_keys() -> list[str]:
    """
    Check for missing API keys and return list of missing keys.

    Returns:
        List of error messages for missing API keys
    """
    errors = []

    openai_models = ["gpt-4.1-mini", "gpt-4o-mini", "gpt-4", "gpt-3.5-turbo", "text-"]
    gemini_models = ["gemini-1.5-flash", "gemini-pro", "gemini-"]

    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        errors.append(ErrorMessages.OPENAI_API_KEY_MISSING)

    # Check for Google API key
    if not os.getenv("GOOGLE_API_KEY"):
        errors.append(ErrorMessages.GOOGLE_API_KEY_MISSING)

    return errors


def check_model_api_key(model_name: str) -> str | None:
    """
    Check if the required API key for a model is present.

    Args:
        model_name: Name of the model to check

    Returns:
        Error message if API key is missing, None otherwise
    """
    if model_name.startswith(("gpt-", "text-")) and not os.getenv("OPENAI_API_KEY"):
        return ErrorMessages.OPENAI_API_KEY_MISSING

    if model_name.startswith("gemini-") and not os.getenv("GOOGLE_API_KEY"):
        return ErrorMessages.GOOGLE_API_KEY_MISSING

    return None

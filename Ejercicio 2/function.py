import openai

def initialize_openai(api_key: str):
    openai.api_key = api_key

def generate_post(context: str, tipo: str):
    """
    Genera un post para LinkedIn según el contexto y el tono.

    Parameters:
        context (str): Contexto del post (tema o situación).
        tipo (str): Tipo de post (ejemplo: Informativo, Contratación, Newsletter).

    Returns:
        str: Post generado.
    """
    try:
        prompt = (
            f"Por favor, genera un post para LinkedIn basado en el siguiente tema:\n"
            f"'{context}'\n"
            f"Usa un tipo de post como instrucción {tipo.lower()}."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en redacción de posts para LinkedIn."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=1.5,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error al generar el post: {str(e)}"
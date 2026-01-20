def generate_response(emotion: str) -> str:
    if emotion == "happy":
        return "You seem genuinely happy — that energy is beautiful."
    if emotion == "sad":
        return "You look a bit down. I'm here with you."
    if emotion == "angry":
        return "I sense tension. Slow breath — you're safe."
    if emotion == "surprise":
        return "Something unexpected caught your attention."
    if emotion == "neutral":
        return "You appear calm and present."

    return "I'm observing your emotional state."

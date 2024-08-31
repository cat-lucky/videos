import random

def animated_text(text):
    colors = ["#ff6347", "#ffa500", "#ffff00", "#32cd32", "#00ced1", "#1e90ff", "#9370db"]
    animated_text = "".join([f'<span style="color:{random.choice(colors)};">{char}</span>' for char in text])
    return animated_text

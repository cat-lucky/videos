import random

def randomColor():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        colors.append(hex_color)
    return colors

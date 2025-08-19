# YuEKral/structured_song_generator.py

def generate_intro():
    return "Intro part generated"

def generate_verse():
    return "Verse part generated"

def generate_chorus():
    return "Chorus part generated"

def generate_outro():
    return "Outro part generated"

def generate_song_structure():
    structure = [
        generate_intro(),
        generate_verse(),
        generate_chorus(),
        generate_verse(),
        generate_chorus(),
        generate_outro()
    ]
    return "\n".join(structure)

# Example usage
if __name__ == "__main__":
    print(generate_song_structure())


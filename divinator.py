import markovify
import json

# Function to generate a Markov chain from text
def generate_markov_chain(text):
    # Create a text model
    markov_text = markovify.Text(text)

    # Generate a sentence
    sentence = markov_text.make_sentence()

    return sentence

# Example text (you can replace this with your own text or use a file)
text = "The quick brown fox jumps over the lazy dog. The dog barked. The fox ran away."

# Generate a sentence from the text
generated_sentence = generate_markov_chain(text)
print("Generated sentence:", generated_sentence)

# Save the model to a file if you want to use it later
model = markovify.Text(text)
with open("markov_model.json", "w") as f:
    f.write(json.dumps(model.to_json()))

# Load the model from a file
with open("markov_model.json", "r") as f:
    model = markovify.Text.from_json(f.read())

# Generate another sentence from the loaded model
generated_sentence_from_file = model.make_sentence()
print("Generated sentence from file:", generated_sentence_from_file)


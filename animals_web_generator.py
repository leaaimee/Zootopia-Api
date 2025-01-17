import json
import os
import requests

print("Saving file to:", os.getcwd())


def load_data():
    """ Loads a JSON file """
    with open("animals_data.json", "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serialize a single animal object into an HTML list item"""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="animal-info">\n'
    output += f'      <li><strong>Scientific name:</strong> {animal_obj.get("characteristics", {}).get("scientific_name", "Unknown")}</li>\n'
    output += f'      <li><strong>Diet:</strong> {animal_obj.get("characteristics", {}).get("diet", "Unknown")}</li>\n'
    output += f'      <li><strong>Location:</strong> {", ".join(animal_obj.get("locations", ["Unknown"]))}</li>\n'
    output += f'      <li><strong>Type:</strong> {animal_obj.get("characteristics", {}).get("type", "Unknown")}</li>\n'
    output += f'      <li><strong>Name of young:</strong> {animal_obj.get("characteristics", {}).get("name_of_young", "Unknown")}</li>\n'
    output += f'      <li><strong>Lifestyle:</strong> {animal_obj.get("characteristics", {}).get("lifestyle", "Unknown")}</li>\n'
    output += f'      <li><strong>Skin type:</strong> {animal_obj.get("characteristics", {}).get("skin_type", "Unknown")}</li>\n'
    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animal_info(animals_data):
    """Generate HTML for all animals"""
    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)
    return animals_info


def generate_animal_html():
    """Generate HTML for all animals"""
    with open("animals_template.html", "r") as template_file:
        html_template = template_file.read()
    return html_template


def write_animal_html(animals_info):
    """Replaces placeholder in the template and writes to a file"""
    html_template = generate_animal_html()
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as output_file:
        output_file.write(html_output)
        print("File written successfully to animals.html")


def main():
    """Main function to load data, generate HTML, and write to a file"""
    animals_data = load_data()
    animals_info = generate_animal_info(animals_data)
    write_animal_html(animals_info)

if __name__ == "__main__":
    main()
import data_fetcher

def serialize_animal(animal_obj):
    """ serialize a single animal object into an HTML list item"""
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
    """ generate the list items HTML for all animals """
    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)
    return animals_info


def write_html_file(animals_info):
    """ read the template, replace placeholder, and write the final HTML file """
    with open("animals_template.html", "r") as template_file:
        html_template = template_file.read()

    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as output_file:
        output_file.write(html_output)

    print("HTML file 'animals.html' has been created successfully.")


def main():
    """ main function to fetch data and generate an HTML file """
    animal_name = input("Enter the name of an animal: ").strip()
    if not animal_name:
        print("Please enter a valid animal name.")
        return

    print(f"Fetching data for: {animal_name}")
    animals = data_fetcher.fetch_data(animal_name)

    if not animals:
        print(f"No data found for the animal: {animal_name}.")
        animals_info = f"<h2>No data found for the animal '{animal_name}'</h2>"
    else:
        animals_info = generate_animal_info(animals)

    write_html_file(animals_info)


if __name__ == "__main__":
    main()

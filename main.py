import requests

API_KEY = "HpCBmkrFEsFBD7aSkg3t/w==ReZb8BtppIw5Hrlc"
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_animal_data(animal_name):
    """
    Fetch animal data from the API based on the given animal name
    Returns a list of animals if the request is successful or an empty list otherwise
    """
    url = f"{BASE_URL}?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:  # Ensure data is not empty
                return data
            else:
                print(f"No data found for the animal: {animal_name}.")
                return []
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []


def generate_html_for_animals(animals, animal_name):
    """ Generate HTML for the animals or an error message if no animals are found """
    if not animals:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>No Data Found</title>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                h1 {{ text-align: center; }}
                h2 {{ color: red; text-align: center; }}
            </style>
        </head>
        <body>
            <h1>Results for '{animal_name}'</h1>
            <h2>
                Sorry, no data found for the animal '{animal_name}'. Please try another animal!
            </h2>
        </body>
        </html>
        """

    html_output = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Animal Information</title>
        <style>
            body { font-family: Arial, sans-serif; }
            ul { list-style-type: none; padding: 0; }
            .cards__item { margin: 20px; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
            .card__title { font-size: 1.5em; margin-bottom: 10px; }
            .animal-info { list-style-type: none; padding: 0; }
            .animal-info li { margin-bottom: 5px; }
        </style>
    </head>
    <body>
        <h1>Results for '{animal_name}'</h1>
        <ul>
    """
    for animal in animals:
        taxonomy = animal.get("taxonomy", {})
        characteristics = animal.get("characteristics", {})
        html_output += f"""
            <li class="cards__item">
                <div class="card__title">{animal.get("name", "Unknown")}</div>
                <ul class="animal-info">
                    <li><strong>Kingdom:</strong> {taxonomy.get('kingdom', 'Unknown')}</li>
                    <li><strong>Class:</strong> {taxonomy.get('class', 'Unknown')}</li>
                    <li><strong>Order:</strong> {taxonomy.get('order', 'Unknown')}</li>
                    <li><strong>Habitat:</strong> {characteristics.get('habitat', 'Unknown')}</li>
                    <li><strong>Diet:</strong> {characteristics.get('diet', 'Unknown')}</li>
                </ul>
            </li>
        """
    html_output += """
        </ul>
    </body>
    </html>
    """
    return html_output


def write_html_file(content, file_name="animals.html"):
    """ Write the HTML content to a file """
    with open(file_name, "w") as file:
        file.write(content)
    print(f"HTML file '{file_name}' has been created successfully.")


def main():
    """ Prompt user for an animal, fetch data, generate HTML, and save it to a file """
    animal_name = input("Enter the name of an animal: ").strip()
    if not animal_name:
        print("Please enter a valid animal name.")
        return

    animals = fetch_animal_data(animal_name)
    html_content = generate_html_for_animals(animals, animal_name)
    write_html_file(html_content)


if __name__ == "__main__":
    main()

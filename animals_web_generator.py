import data_fetcher

def generate_html_for_animals(animals, animal_name):
    """ generate HTML for the animals or an error message if no animal data is found """
    if not animals:
        print("Generating error HTML for missing animal.")
        return f"""
        <html>
        <head><title>Animals</title></head>
        <body>
            <h1>Results for '{animal_name}'</h1>
            <h2 style="color: red; text-align: center;">
                Sorry, no data found for the animal '{animal_name}'. Please try another animal!
            </h2>
        </body>
        </html>
        """
    print("Generating HTML for animals.")
    html_output = f"""
    <html>
    <head><title>Animals</title></head>
    <body>
        <h1>Results for '{animal_name}'</h1>
        <ul>
    """
    for animal in animals:
        taxonomy = animal.get("taxonomy", {})
        characteristics = animal.get("characteristics", {})
        html_output += f"""
            <li>
                <strong>Name:</strong> {animal.get("name", "Unknown")}<br>
                <strong>Taxonomy:</strong> {taxonomy.get('kingdom', 'Unknown')} > {taxonomy.get('class', 'Unknown')} > {taxonomy.get('order', 'Unknown')}<br>
                <strong>Habitat:</strong> {characteristics.get('habitat', 'Unknown')}<br>
                <strong>Diet:</strong> {characteristics.get('diet', 'Unknown')}<br>
            </li>
        """
    html_output += f"""
        </ul>
    </body>
    </html>
    """
    return html_output


def write_html_file(content):
    """ Write the HTML content to a file """
    with open("animals.html", "w") as file:
        file.write(content)
    print("HTML file 'animals.html' has been created successfully.")


def main():
    """ main function to fetch data & generate an HTML file """
    animal_name = input("Enter the name of an animal: ").strip()
    if not animal_name:
        print("Please enter a valid animal name.")
        return

    print(f"Fetching data for: {animal_name}")
    animals = data_fetcher.fetch_data(animal_name)

    if not animals:
        print(f"No data found for the animal: {animal_name}.")  # Add this print statement
    else:
        print(f"Data fetched for {animal_name}: {animals}")

    html_content = generate_html_for_animals(animals, animal_name)
    write_html_file(html_content)

if __name__ == "__main__":
    main()

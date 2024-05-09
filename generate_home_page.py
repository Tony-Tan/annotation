import jinja2
from code_comment_seg import parse_python_script
import json

def generate_home(algorithm_json_path, output_html_path):
    # Parse the Python script
    section = {'id': f'section-0', 'title': '', 'description': ''}
    section['title'] = 'HOME'
    with open(algorithm_json_path, 'r') as file:
        data = json.load(file)
        for algo in data["algorithms"]:
            algo_name = algo["name"]
            section['description'] += f'- [{algo_name}](./{algo_name}.html)\n\n'
    # Setup Jinja2 environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('home_temp.html')

    # Render the template with the sections data
    html_output = template.render(section=section)

    # Write the output to an HTML file
    with open(output_html_path, 'w') as file:
        file.write(html_output)

    print(output_html_path + " HOME page generated successfully!")


if __name__ == '__main__':
    generate_home('./examples/1.py', './output.html')
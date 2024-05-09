import jinja2
from code_comment_seg import parse_python_script


def generate_page(script_path, output_html_path):
    # Parse the Python script
    sections = parse_python_script(script_path)
    # Setup Jinja2 environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('page_temp.html')

    # Render the template with the sections data
    html_output = template.render(sections=sections)

    # Write the output to an HTML file
    with open(output_html_path, 'w') as file:
        file.write(html_output)

    print(script_path + " HTML page generated successfully!")


if __name__ == '__main__':
    generate_page('./examples/1.py', './output.html')
import jinja2

from code_comment_seg import parse_python_script
sections = parse_python_script('examples/1.py')
print(sections)

# Setup Jinja2 environment
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
template = env.get_template('template.html')

# Render the template with the sections data
html_output = template.render(sections=sections)

# Write the output to an HTML file
with open('output.html', 'w') as file:
    file.write(html_output)

print("HTML page generated successfully!")

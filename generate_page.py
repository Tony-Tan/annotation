import jinja2

# Data structure for the sections
sections = [
    {
        'id': 'section-0',
        'title': 'LLM.int() on GPT-NeoX',
        'description': '## test makdown \nThis implements a utility function to transform an nn.Linear layer\n to LLM.int8() linear layer.',
        'code': 'def transform_layer(layer):\npass  # Example code snippet'
    },
    {
        'id': 'section-1',
        'title': 'Import bitsandbytes',
        'description': '### test latex \n '+r'$\\frac{1}{1}$'+'\n\nImport the bitsandbytes package to enable specific functions.',
        'code': 'try:\n    from bitsandbytes import something\nexcept ImportError:\n    print("Install the package")'
    }
    # Add more sections as needed
]

# Setup Jinja2 environment
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
template = env.get_template('template.html')

# Render the template with the sections data
html_output = template.render(sections=sections)

# Write the output to an HTML file
with open('output.html', 'w') as file:
    file.write(html_output)

print("HTML page generated successfully!")

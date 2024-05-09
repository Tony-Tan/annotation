import jinja2

# Data structure for the sections
sections = [
    {
        'id': 'section-0',
        'title': 'LLM.int() on GPT-NeoX',
        'description': '## test makdown '+r'$\\delta$' +'\nThis implements a utility function to transform an nn.Linear layer\n to <code>LLM.int8()</code> linear layer.',
        'lang':'python',
        'code': [{'line_num': '1',
                  'content': 'def transform_layer(layer):'},
                 {'line_num': '2',
                  'content': '    pass  # Example code snippet'}
                 ]
    },
    {
        'id': 'section-1',
        'title': 'Import bitsandbytes',
        'description': '### test latex \n ' + r'$\\frac{1}{1}$' + '\n\nImport the bitsandbytes package to enable specific functions.',
        'lang':'python',
        'code':
            [{'line_num': '4', 'content': 'try:'},
             {'line_num': '5', 'content': '    from bitsandbytes import something'},
             {'line_num': '6', 'content': '    print("Package imported successfully")'},
             {'line_num': '7', 'content': 'except ImportError:'},
             {'line_num': '8', 'content': '    print("Install the package")'}]
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

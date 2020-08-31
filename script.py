from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

# Specify how you are going to load the file
template_env = Environment(loader=FileSystemLoader(searchpath='./env'))

with open('config.json', encoding="utf-8") as config_file:
    config = load(config_file)

######## INDEX
# tipo: portada, output:index
template = template_env.get_template('portada.html')

with open('index.html', 'w', encoding="utf-8") as output_file:
    output_file.write(
        template.render(
            config=config,
            page_name='index',
        )
    )

######## ARTICULOS
# tipo: lista, output:artículos
template = template_env.get_template('lista.html')

with open('articulos.html', 'w', encoding="utf-8") as output_file:
    output_file.write(
        template.render(
            config=config,
            page_name='articulos',
        )
    )


######## TUTORIALES
# tipo: lista, output:artículos
template = template_env.get_template('tutoriales.html')

with open('tutoriales.html', 'w', encoding="utf-8") as output_file:
    output_file.write(
        template.render(
            config=config,
            page_name='tutoriales',
        )
    )

######## TRADUCCIONES
# tipo: lista, output:artículos
template = template_env.get_template('traducciones.html')

with open('traducciones.html', 'w', encoding="utf-8") as output_file:
    output_file.write(
        template.render(
            config=config,
            page_name='traducciones',
        )
    )

######## OTROS
# tipo: lista, output:artículos
template = template_env.get_template('otros.html')

with open('otros.html', 'w', encoding="utf-8") as output_file:
    output_file.write(
        template.render(
            config=config,
            page_name='otros',
        )
    )

######## SOBREMI
# tipo: cuadro, output:sobremi
template = template_env.get_template('cuadro.html')

with open('sobremi.html', 'w', encoding="utf-8") as output_file:
    output_file.write(
        template.render(
            config=config,
            page_name='sobremi',
        )
    )
# with open('md/article.md') as markdown_file:
#     article = markdown(markdown_file.read(),
#     extras=['fenced-code-blocks', 'code-friendly'])
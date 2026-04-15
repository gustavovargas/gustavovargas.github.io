from datetime import date
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

# Specify how you are going to load the file
template_env = Environment(loader=FileSystemLoader(searchpath='./env'))

with open('config.json', encoding="utf-8") as config_file:
    config = load(config_file)

######## INDEX
template = template_env.get_template('portada.html')
with open('index.html', 'w', encoding="utf-8") as output_file:
    output_file.write(template.render(config=config, page_name='index'))

######## ARTICULOS (incluye tutoriales)
template = template_env.get_template('lista.html')
with open('articulos.html', 'w', encoding="utf-8") as output_file:
    output_file.write(template.render(config=config, page_name='articulos'))

######## TRADUCCIONES
template = template_env.get_template('traducciones.html')
with open('traducciones.html', 'w', encoding="utf-8") as output_file:
    output_file.write(template.render(config=config, page_name='traducciones'))

######## CHARLAS
template = template_env.get_template('charlas.html')
with open('charlas.html', 'w', encoding="utf-8") as output_file:
    output_file.write(template.render(config=config, page_name='charlas'))

######## SOBREMI
template = template_env.get_template('cuadro.html')
with open('sobremi.html', 'w', encoding="utf-8") as output_file:
    output_file.write(template.render(config=config, page_name='sobremi'))

######## REDIRECTS (mantener URLs antiguas vivas)
redirect_template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Redirigiendo…</title>
    <link rel="canonical" href="{target}">
    <meta http-equiv="refresh" content="0; url={target}">
    <meta name="robots" content="noindex">
</head>
<body>
    <p>Esta página se ha movido. Redirigiendo a <a href="{target}">{target}</a>…</p>
    <script>window.location.replace("{target}");</script>
</body>
</html>
'''
site_url = config['web_metadata']['url'].rstrip('/')
for old, new in [('otros', 'charlas'), ('tutoriales', 'articulos')]:
    with open(f'{old}.html', 'w', encoding='utf-8') as f:
        f.write(redirect_template.format(target=f'{site_url}/{new}.html'))

######## SITEMAP
today = date.today().isoformat()
sitemap_entries = [('index', 1.0, 'monthly')]
sitemap_entries += [(p, 0.8, 'monthly') for p in config['navbar']['pages'] if p != 'index']

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for page, priority, changefreq in sitemap_entries:
        loc = site_url + ('/' if page == 'index' else f'/{page}.html')
        f.write(f'  <url>\n')
        f.write(f'    <loc>{loc}</loc>\n')
        f.write(f'    <lastmod>{today}</lastmod>\n')
        f.write(f'    <changefreq>{changefreq}</changefreq>\n')
        f.write(f'    <priority>{priority}</priority>\n')
        f.write(f'  </url>\n')
    f.write('</urlset>\n')

######## ROBOTS
with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write('User-agent: *\n')
    f.write('Allow: /\n\n')
    f.write(f'Sitemap: {site_url}/sitemap.xml\n')

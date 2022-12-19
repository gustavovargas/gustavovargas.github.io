# gustavovargas.github.io
Página web personal. Podéis acceder a través de este [link](https://gustavovargas.github.io/).


[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)


Si quieres crear tu propia web a partir de estos datos, solo ten en cuenta los siguientes puntos:
- El archivo principal a partir del que se generan el resto es `script.py`. Crea el environment desde `environment.yml`, con ello podrás ejecutar el script. Cambia el prefix por la dirección donde se guardan tus entornos de conda. Esto lo puedes consultar haciendo `conda env list`
- Muchas modificaciones de contenido las puedes hacer cambiando el archivo `config.json`, a excepción del apartado `Sobre mí`
- Las plantillas a partir de las que se genera el resto de archivos están dentro de la carpeta `env`. Si necesitas modificarlas, modifícalas aquí. Ten en cuenta que aquí hemos usado simplemente Bootstrap, por su sencillez.
- Si quieres añadir o quitar páginas, hazlo desde `script.py`, usando las plantillas de `env`. Puedes indicar qué datos añadir desde el archivo `config.py`.
- He ido separando los archivos en dos carpetas: `files` e `images`. No es necesario que sigas ese orden, pero entiendo que viene bien.
- Usamos Github Pages, por lo que no se puede utilizar ningún backend. Es hosting gratuito.

Si tienes mejoras o quieres avisarme de alguna errata, escríbeme a ge.vargasn@gmail.com. Encantado de comentarlo :)

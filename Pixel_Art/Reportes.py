class Reporte:

    def __init__(self):
        self.lista_de_tokens = []
        self.lista_de_errores = []

    def reporte_tokens(self, tokens):
        self.lista_de_tokens = tokens

        with open('archivos_creados/tokens.html', mode='w') as HTML:  # -----> Crea un archivo.html en modo escritura
            HTML.write('<!DOCTYPE html>\n')
            HTML.write('<html>\n')
            HTML.write('    <head>\n')
            HTML.write('        <title>Reporte</title>\n')
            HTML.write('        <meta charset="utf-8">\n')
            HTML.write('        <link rel="stylesheet" type="text/css" href="../archivos/estilo.css">\n')
            HTML.write('        <link rel="icon" href="../archivos/icono 01.png">\n')
            HTML.write('    </head>\n')
            HTML.write('    <body>\n')
            HTML.write('        <header>\n')
            HTML.write('            <center><h2>Reporte de Tokens</h2></center>\n')
            HTML.write('        </header>\n')
            HTML.write('        <br>\n')
            HTML.write('        <section>\n')
            HTML.write('            <br>\n')

            for i in self.lista_de_tokens:
                token = i
                HTML.write('            <p style="text-align:center">' + token + '</p>\n')

            HTML.write('        </section>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <hr>\n')
            HTML.write('        <footer>LFP, Proyecto 1</footer>\n')
            HTML.write('    </body>\n')
            HTML.write('</html>')

    def reporte_errores(self, errores):
        self.lista_de_errores = errores

        with open('archivos_creados/errores.html', mode='w') as HTML:  # -----> Crea un archivo.html en modo escritura
            HTML.write('<!DOCTYPE html>\n')
            HTML.write('<html>\n')
            HTML.write('    <head>\n')
            HTML.write('        <title>Reporte</title>\n')
            HTML.write('        <meta charset="utf-8">\n')
            HTML.write('        <link rel="stylesheet" type="text/css" href="../archivos/estilo.css">\n')
            HTML.write('        <link rel="icon" href="../archivos/icono 01.png">\n')
            HTML.write('    </head>\n')
            HTML.write('    <body>\n')
            HTML.write('        <header>\n')
            HTML.write('            <center><h2>Reporte de Errores</h2></center>\n')
            HTML.write('        </header>\n')
            HTML.write('        <br>\n')
            HTML.write('        <section>\n')
            HTML.write('            <br>\n')

            for i in self.lista_de_errores:
                error = i
                HTML.write('            <p style="text-align:center">' + error + '</p>\n')

            HTML.write('        </section>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <hr>\n')
            HTML.write('        <footer>LFP, Proyecto 1</footer>\n')
            HTML.write('    </body>\n')
            HTML.write('</html>')

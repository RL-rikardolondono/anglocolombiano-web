# Contenido de www.anglocolombiano.com (Colegio Cristiano Anglocolombiano). Lo usa generador/build.py.
WA = '573011346868'
RAIZ = 'https://anglocolombiano.com'   # se queda en SiteGround solo para el campus virtual (Moodle), Dolibarr y la escuela musical
CAMPUS = f'{RAIZ}/campusvirtualanglo/login/index.php'
COLEGIO_IA = 'https://colegio-ia.skynetgenesis.com/'
WA_INFO = f'https://wa.me/{WA}?text=Hola%2C%20quiero%20informaci%C3%B3n%20sobre%20inscripciones%20en%20el%20Anglocolombiano'

SITIO = {
    'nombre': 'Colegio Cristiano Anglocolombiano', 'nombre_corto': 'Colegio Anglocolombiano', 'repo': 'anglocolombiano-web',
    'dominio': 'www.anglocolombiano.com', 'dominio_raiz': 'anglocolombiano.com', 'whatsapp': WA,
    'logo': 'leon.png', 'icono': 'leon.png', 'og': 'grupo.jpg',
    'marca_html': 'ANGLO<span>COLOMBIANO</span>', 'lema_corto': 'Colegio Cristiano · Santa Marta',
    'aviso_top': f'¡Inscripciones abiertas! Preescolar y Básica Primaria · WhatsApp <a href="{WA_INFO}">301 134 6868</a>',
    'nombre_noticias': 'Noticias del Anglo', 'nombre_galeria': 'Vida en el Anglo', 'ejemplo_clave': 'Anglo Santa Marta 2026',
    'colores': '--azul:#1A5C99;--azul-osc:#16263F;--celeste:#2BA3D8;--naranja:#C9A24A;--cta-txt:#16263F;--oro-osc:#8A6A1F;--oro-suave:#FBF5E6;--verde:#1F8A4C;--fondo:#F6FAFD;--fondo2:#E6F2FA;--sup:#fff;--texto:#1C2B39;--suave:#5D6B78;--borde:#D9E4EE',
    'css': '.marca span{color:#E6CF94}.marca img{border-radius:50%;background:#FBF5E6}.hero.foto>img.fondo{opacity:.28}',
    'imagenes': {
        'leon.png': '2024/09/cropped-cropped-Captura-de-pantalla-2024-04-04-024727-1.png',
        'leon-grande.png': '2024/09/Captura-de-pantalla-2024-04-04-024727.png',
        'logo-anglo.jpg': '2024/09/colegio-cristiano-anglocolombiano.jpg',
        'akademy.jpg': '2024/09/akad-scaled-2.jpg',
        'grupo.jpg': '2024/09/311133435_556089029857794_12075082162223296_n.jpg',
        'arte-collage.jpg': '2022/06/image-1.png', 'arte-1.jpg': '2022/06/image.png', 'arte-2.jpg': '2023/06/image.png',
        'cancha.jpg': '2024/09/images-1-1.jpeg', 'revista.jpg': '2024/09/images-2-1.jpeg', 'navidad.jpg': '2024/09/images-2.jpeg',
        'circo.jpg': '2024/09/images-3.jpeg', 'salida.jpg': '2024/09/images-4.jpeg', 'baile.jpg': '2024/09/images-5.jpeg',
        'mundo-marino.jpg': '2024/09/images-6.jpeg',
    },
    'carpetas_documentos': {'matriculas': 'Matrículas e inscripciones', 'circulares': 'Circulares a las familias', 'institucional': 'Documentos institucionales (PEI, manual de convivencia)'},
    'carpetas_en_siteground': ['campusvirtualanglo', 'dolibarr-20.0.2', 'escuelamusical'],
    'redirecciones': {'/our-clinic/': '/', '/home/': '/', '/category/sin-categoria/': '/noticias/', '/wp-admin/': '/admin/', '/wp-login.php': '/admin/'},
    'menu_derecha': 'Funcionarios',
    'menu': [
        ('Inicio', '/'),
        ('Aspirantes', '/aspirantes/'),
        ('Oferta académica', '/oferta-academica/'),
        ('Matrículas', '/matriculas/'),
        ('Proyectos y eventos', [('Arte para Soñar: Expresiones de la Infancia', '/arte-para-sonar-expresiones-de-la-infancia/'), ('Noticias y eventos', '/noticias/')]),
        ('Campus virtual', CAMPUS),
        ('Funcionarios', [('Agenda-IA', 'https://agenda-ia.skynetgenesis.com/', 'Agenda de trabajo y tareas'), ('Colegio-IA', COLEGIO_IA, 'Plataforma académica del colegio'),
                          ('Facturación SIIGO', 'https://siigonube.siigo.com/#/dashboard/1055'), ('Dolibarr', f'{RAIZ}/dolibarr-20.0.2/dolibarr-20.0.2/htdocs/index.php'),
                          ('Campus virtual (administración)', f'{RAIZ}/campusvirtualanglo/admin'), ('Ver todas las herramientas', '/funcionarios/')]),
    ],
    'pie': [
        ('Colegio Cristiano Anglocolombiano', 'Preescolar y Básica Primaria.<br>Educa al niño en Su Camino, cuando sea mayor no se apartará de Él.'),
        ('Contacto', f'Calle 11 D No. 22-90<br>Santa Marta, Magdalena<br>WhatsApp: <a href="https://wa.me/{WA}">301 134 6868</a><br>Correo: <a href="mailto:anglo@anglocolombiano.com">anglo@anglocolombiano.com</a>'),
        ('Enlaces', '<ul><li><a href="/aspirantes/">Aspirantes</a></li><li><a href="/oferta-academica/">Oferta académica</a></li><li><a href="/matriculas/">Matrículas</a></li><li><a href="/noticias/">Noticias y eventos</a></li><li><a href="/funcionarios/">Funcionarios</a></li></ul>'),
        ('Plataformas', f'<ul><li><a href="{CAMPUS}">Campus virtual</a></li><li><a href="{COLEGIO_IA}" target="_blank" rel="noopener">Colegio-IA</a></li></ul>'),
    ],
    'contenido_inicial': {
        'noticias': [{'id': 'arte-para-sonar', 'fecha': '2022-06-04', 'titulo': 'Arte para Soñar: Expresiones de la Infancia', 'texto': 'En 2022, la Fundación Reina Elizabeth ONG desarrolló una experiencia piloto de circulación artística para primeras infancias en alianza con el Colegio Anglocolombiano. La exposición reunió 48 obras creadas por niños y niñas entre 6 y 10 años.', 'foto': '/img/arte-collage.jpg', 'enlace': '/arte-para-sonar-expresiones-de-la-infancia/', 'textoEnlace': 'Ver el proyecto', 'video': ''}],
        'eventos': [], 'videos': [],
        'galeria': [{'foto': '/img/' + f, 'texto': t} for f, t in [('grupo.jpg', 'Nuestros estudiantes'), ('mundo-marino.jpg', 'Mundo Marino'), ('navidad.jpg', 'Celebración de Navidad'), ('baile.jpg', 'Presentaciones'), ('salida.jpg', 'Salidas pedagógicas'), ('circo.jpg', 'Día del circo'), ('cancha.jpg', 'Nuestra cancha'), ('arte-1.jpg', 'Arte para Soñar'), ('revista.jpg', 'Revista Colegios y Jardines')]],
    },
}

INICIO = f'''<div class="hero foto"><img class="fondo" src="/img/grupo.jpg" alt=""><div class="wrap">
<span class="etq">Santa Marta · Preescolar y Básica Primaria</span><h1>Colegio Cristiano Anglocolombiano</h1>
<p>Educa al niño en Su Camino, cuando sea mayor no se apartará de Él. Educación con valores cristianos para una sociedad más justa e incluyente.</p>
<div class="btns"><a class="btn b-ac" href="/aspirantes/">Inscripciones abiertas</a><a class="btn b-bl" href="{CAMPUS}">Ir al Campus Virtual</a></div></div></div>
<div class="wrap"><div class="cifras">
<div class="cifra"><b>Preescolar</b><span>El primer paso hacia un futuro brillante</span></div>
<div class="cifra"><b>Básica Primaria</b><span>El trampolín hacia el éxito académico y personal</span></div>
<div class="cifra"><b>Valores cristianos</b><span>¡La familia es primero!</span></div>
<div class="cifra"><b>Campus virtual</b><span>Aprendizaje también desde casa</span></div>
</div></div>
<section><div class="wrap"><div class="foto-texto"><div><span class="etq">¡Bienvenidos al Anglo!</span><h2>Educación con excelencia</h2>
<p>¡Bienvenidos al Colegio Cristiano Anglocolombiano! En nuestro entorno vibrante y acogedor en Santa Marta, cada día es una oportunidad para aprender, crecer y descubrir. Estamos emocionados de tenerte con nosotros y de acompañarte en este viaje educativo lleno de entusiasmo y excelencia.</p>
<div class="btns"><a class="btn b-az" href="/oferta-academica/">Conocer la oferta académica</a></div></div>
<img src="/img/akademy.jpg" alt="Colegio Cristiano Anglocolombiano Akademy" loading="lazy"></div></div></section>
<section class="alt"><div class="wrap"><h2>Nuestra oferta</h2><p class="sub-t">Preescolar y Básica Primaria en Santa Marta.</p><div class="grid">
<a class="card" href="/oferta-academica/#preescolar"><img src="/img/arte-2.jpg" alt="Preescolar" loading="lazy"><div class="cb"><span class="pill">Preescolar</span><h3>Preescolar</h3><p>Un entorno lleno de creatividad y aprendizaje, donde los más pequeños exploran, juegan y descubren su potencial.</p></div></a>
<a class="card" href="/oferta-academica/#primaria"><img src="/img/mundo-marino.jpg" alt="Básica Primaria" loading="lazy"><div class="cb"><span class="pill">Primaria</span><h3>Básica Primaria</h3><p>Formación académica sólida con desarrollo de habilidades sociales y emocionales.</p></div></a>
<a class="card" href="/arte-para-sonar-expresiones-de-la-infancia/"><img src="/img/arte-collage.jpg" alt="Arte para Soñar" loading="lazy"><div class="cb"><span class="pill n">Proyecto</span><h3>Arte para Soñar</h3><p>Exposición de 48 obras creadas por nuestros niños y niñas.</p></div></a>
</div></div></section>
<section><div class="wrap"><div class="dos"><div><h2>Noticias del Anglo</h2><div class="grid" data-bloque="noticias-inicio"></div>
<p style="margin-top:14px"><a class="mas" href="/noticias/">Ver todas las noticias →</a></p></div>
<aside><div class="box"><h2 style="font-size:1.4rem">Eventos</h2><div data-bloque="eventos"><p style="color:var(--suave)">Pronto anunciaremos nuevos eventos.</p></div></div></aside></div></div></section>
<section class="alt"><div class="wrap"><h2>Vida en el Anglo</h2><p class="sub-t">Nuestros niños y niñas aprendiendo, jugando y celebrando.</p><div class="galeria" data-bloque="galeria"></div></div></section>
<div class="franja"><div class="wrap"><div><h2>¡Inscripciones abiertas!</h2><p>Escríbanos y le contamos todo sobre el proceso de inscripción.</p></div><a class="btn b-ac" href="{WA_INFO}">WhatsApp 301 134 6868</a></div></div>
<section id="contacto"><div class="wrap"><h2>Contacto</h2><div class="contacto-grid">
<div class="box"><h3>Dirección</h3><p style="margin:0">Calle 11 D No. 22-90<br>Santa Marta, Magdalena</p><p style="margin:8px 0 0"><a class="mas" href="https://www.google.com/maps/search/?api=1&query=Calle+11D+22-90+Santa+Marta" target="_blank" rel="noopener">Ver en el mapa →</a></p></div>
<div class="box"><h3>Teléfono y WhatsApp</h3><p style="margin:0"><a href="tel:3011346868">301 134 6868</a></p></div>
<div class="box"><h3>Correo</h3><p style="margin:0"><a href="mailto:anglo@anglocolombiano.com">anglo@anglocolombiano.com</a></p></div>
</div></div></section>
'''

def hero(etq, titulo, texto=''):
    return f'<div class="hero"><div class="wrap"><span class="etq">{etq}</span><h1>{titulo}</h1>' + (f'<p>{texto}</p>' if texto else '') + '</div></div>'

ASPIRANTES = {'ruta': 'aspirantes/index.html', 'titulo': 'Aspirantes · Colegio Anglocolombiano', 'descripcion': 'Inscripciones abiertas en el Colegio Cristiano Anglocolombiano, Santa Marta: preescolar y básica primaria.', 'activo': '/aspirantes/', 'cuerpo': hero('Aspirantes', '¡Inscripciones abiertas!', 'Preescolar y Básica Primaria en Santa Marta.') + f'''
<section><div class="wrap"><div class="foto-texto"><div><h2>¿Cómo inscribirse?</h2>
<ol style="padding-left:20px"><li>Escríbanos por WhatsApp o al correo para recibir la información de costos y cupos.</li><li>Agende una visita para conocer el colegio.</li><li>Presente los documentos de inscripción.</li><li>¡Bienvenido a la familia Anglo!</li></ol>
<div class="btns"><a class="btn b-wa" href="{WA_INFO}">Escribir por WhatsApp</a><a class="btn b-az" href="mailto:anglo@anglocolombiano.com?subject=Inscripciones">Enviar correo</a></div></div>
<img src="/img/salida.jpg" alt="Estudiantes del Anglocolombiano" loading="lazy"></div></div></section>
<section class="alt"><div class="wrap"><h2>Documentos de inscripción y matrícula</h2><ul class="docs" data-carpeta="matriculas"></ul></div></section>'''}

OFERTA = {'ruta': 'oferta-academica/index.html', 'titulo': 'Oferta académica · Colegio Anglocolombiano', 'descripcion': 'Preescolar y Básica Primaria con valores cristianos en Santa Marta.', 'activo': '/oferta-academica/', 'cuerpo': hero('Oferta académica', 'Preescolar y Básica Primaria', 'Educa al niño en Su Camino, cuando sea mayor no se apartará de Él.') + '''
<section id="preescolar"><div class="wrap"><div class="foto-texto"><div><span class="etq">Preescolar</span><h2>El primer paso hacia un futuro brillante</h2>
<p>En el Colegio Cristiano Anglocolombiano, el preescolar es el primer paso hacia un futuro brillante. Ofrecemos un entorno lleno de creatividad y aprendizaje, donde los más pequeños exploran, juegan y descubren su potencial. Nuestro equipo de educadores dedicados utiliza metodologías innovadoras para fomentar el desarrollo integral, estimulando la curiosidad natural y el amor por el aprendizaje. Ven y únete a nuestra familia educativa en Santa Marta, donde cada niño es celebrado y preparado para un camino lleno de éxitos.</p></div>
<img src="/img/arte-2.jpg" alt="Niños de preescolar" loading="lazy"></div></div></section>
<section class="alt" id="primaria"><div class="wrap"><div class="foto-texto"><img src="/img/mundo-marino.jpg" alt="Estudiantes de primaria" loading="lazy"><div><span class="etq">Básica Primaria</span><h2>El trampolín hacia el éxito</h2>
<p>Nuestra básica primaria es el trampolín hacia el éxito académico y personal. Aquí, los estudiantes se embarcan en una emocionante aventura de aprendizaje, donde cada día está lleno de desafíos estimulantes y descubrimientos fascinantes. Nuestro enfoque integral combina una sólida formación académica con el desarrollo de habilidades sociales y emocionales, preparando a los niños para enfrentar el futuro con confianza y entusiasmo. Con un equipo de maestros apasionados y recursos educativos de vanguardia, garantizamos un ambiente en el que cada estudiante puede brillar y alcanzar su máximo potencial en Santa Marta.</p></div></div></div></section>
<div class="franja"><div class="wrap"><div><h2>¿Quiere un cupo?</h2><p>Inscripciones abiertas para preescolar y primaria.</p></div><a class="btn b-ac" href="/aspirantes/">Inscribirse</a></div></div>'''}

MATRICULAS = {'ruta': 'matriculas/index.html', 'titulo': 'Matrículas · Colegio Anglocolombiano', 'descripcion': 'Matrículas, documentos y plataforma de las familias del Colegio Anglocolombiano.', 'activo': '/matriculas/', 'cuerpo': hero('Matrículas', 'Matrículas', 'Información y documentos para las familias.') + f'''
<section><div class="wrap"><div class="dos"><div><h2>Documentos de matrícula</h2><ul class="docs" data-carpeta="matriculas"></ul>
<h3 style="margin-top:24px">Circulares a las familias</h3><ul class="docs" data-carpeta="circulares"></ul>
<h3 style="margin-top:24px">Documentos institucionales</h3><ul class="docs" data-carpeta="institucional"></ul></div>
<aside><div class="box"><h3>Plataforma de las familias</h3><p>Calificaciones, comunicados, estado de cuenta y más en la plataforma del colegio.</p><div class="btns"><a class="btn b-az" href="{COLEGIO_IA}" target="_blank" rel="noopener">Entrar a Colegio-IA</a></div></div>
<div class="box"><h3>¿Dudas?</h3><p>Escríbanos por WhatsApp.</p><div class="btns"><a class="btn b-wa" href="https://wa.me/{WA}">301 134 6868</a></div></div></aside></div></div></section>'''}

ARTE = {'ruta': 'arte-para-sonar-expresiones-de-la-infancia/index.html', 'titulo': 'Arte para Soñar: Expresiones de la Infancia · Colegio Anglocolombiano', 'descripcion': 'Exposición de 48 obras creadas por niños y niñas del Colegio Anglocolombiano, con la Fundación Reina Elizabeth ONG.', 'cuerpo': hero('Proyectos y eventos', 'Arte para Soñar: Expresiones de la Infancia') + '''
<section><div class="wrap"><div class="migas"><a href="/">Inicio</a> › <a href="/noticias/">Proyectos y eventos</a> › Arte para Soñar</div><div class="articulo">
<p>En 2022, la Fundación Reina Elizabeth ONG desarrolló una experiencia piloto de circulación artística para primeras infancias en alianza con el Colegio Anglocolombiano.</p>
<img src="/img/arte-2.jpg" alt="Niños pintando" loading="lazy" style="border-radius:12px;margin:8px 0 16px">
<p>El proyecto «Arte para Soñar: Expresiones de la Infancia» surgió de la convicción de que la formación de públicos culturales comienza en la niñez, y que los futuros profesionales dedicados al desarrollo infantil requieren competencias para valorar, documentar y potenciar la expresión creativa de los niños y niñas a su cargo.</p>
<img src="/img/arte-1.jpg" alt="Taller de exploración plástica" loading="lazy" style="border-radius:12px;margin:8px 0 16px">
<p>La exposición reunió 48 obras creadas por niños y niñas entre 6 y 10 años, estudiantes del Colegio Anglocolombiano, como resultado de los talleres de exploración plástica realizados durante el año escolar en las clases de educación artística. Las obras incluyeron dibujo, pintura, collage y técnicas mixtas, organizadas en torno a cuatro ejes temáticos diseñados en articulación con los estudiantes de Desarrollo Infantil: «Mi familia», «Mi lugar favorito», «Mis sueños» y «Los colores de mi alegría».</p>
<img src="/img/arte-collage.jpg" alt="Exposición Arte para Soñar" loading="lazy" style="border-radius:12px;margin:8px 0 16px">
<a class="volver" href="/">← Volver al inicio</a></div></div></section>'''}

NOTICIAS = {'ruta': 'noticias/index.html', 'titulo': 'Noticias y eventos · Colegio Anglocolombiano', 'descripcion': 'Noticias, eventos y videos del Colegio Anglocolombiano.', 'cuerpo': hero('Proyectos y eventos', 'Noticias y eventos', 'Lo que pasa en el Anglo.') + '''
<section><div class="wrap"><div class="dos"><div data-bloque="noticias-todas"></div><aside><div class="box"><h2 style="font-size:1.4rem">Eventos</h2><div data-bloque="eventos"><p style="color:var(--suave)">Pronto anunciaremos nuevos eventos.</p></div></div></aside></div></div></section>
<section id="videos" class="alt"><div class="wrap"><h2>Videos</h2><div class="videos" data-bloque="videos-todos"></div></div></section>'''}

HERR = [m for m in SITIO['menu'] if m[0] == 'Funcionarios'][0][1][:-1]
def funcionarios():
    t = ''
    for it in HERR:
        d = it[2] if len(it) > 2 else 'Herramienta de trabajo'
        cls = 'acceso destacado' if it[0] == 'Agenda-IA' else 'acceso'
        t += f'<a class="{cls}" href="{it[1]}" target="_blank" rel="noopener"><span class="ico">{it[0][:2].upper()}</span><span><b>{it[0]}</b><small>{d}</small></span></a>'
    return {'ruta': 'funcionarios/index.html', 'titulo': 'Funcionarios · Colegio Anglocolombiano', 'descripcion': 'Herramientas de trabajo del equipo del Colegio Anglocolombiano.',
            'cuerpo': hero('Equipo de trabajo', 'Funcionarios', 'Herramientas de trabajo del equipo del Anglo. La agenda de tareas es Agenda-IA.') + f'<section><div class="wrap"><div class="accesos">{t}</div></div></section>'}

PAGINAS = [
    {'ruta': 'index.html', 'titulo': 'Colegio Cristiano Anglocolombiano · Preescolar y Básica Primaria en Santa Marta', 'descripcion': 'Colegio Cristiano Anglocolombiano en Santa Marta: preescolar y básica primaria con valores cristianos. ¡Inscripciones abiertas!', 'cuerpo': INICIO, 'activo': '/'},
    ASPIRANTES, OFERTA, MATRICULAS, ARTE, NOTICIAS, funcionarios(),
]

import csv
import random
import string
from datetime import datetime, timedelta


def generate_contact_id(length: int = 20) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))


def random_phone_es() -> str:
    # E.164 Spain: +34 followed by 9 digits; start with 6/7 (mobile) or 8/9 (landline)
    starts = ["6", "7", "8", "9"]
    return "+34" + random.choice(starts) + ''.join(random.choice(string.digits) for _ in range(8))


def maybe(prob: float) -> bool:
    return random.random() < prob


def pick_weighted(options):
    # options: list of tuples (value, weight)
    values, weights = zip(*options)
    return random.choices(values, weights=weights, k=1)[0]


def generate_names():
    first_names = [
        "Juan", "María", "Lucía", "Pablo", "Laura", "Sergio", "Carmen", "Javier", "Sofía", "David",
        "Marta", "Andrés", "Paula", "Diego", "Elena", "Adriana", "Carlos", "Noelia", "Hugo", "Valeria",
        "Álvaro", "Nuria", "Raúl", "Irene", "Jorge", "Nicolás", "Ainhoa", "Clara", "Ismael", "Olga",
        "Gonzalo", "Beatriz", "Rubén", "Patricia", "Ariadna", "Víctor", "Alicia", "Daniel", "Natalia", "Eva",
    ]
    last_names = [
        "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín",
        "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez",
        "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina",
        "Morales", "Suárez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Iglesias",
    ]
    return random.choice(first_names), random.choice(last_names)


def generate_company(sector: str) -> str:
    bases = [
        "Solutions", "Consulting", "Studios", "Digital", "Group", "Innovations", "Global", "Partners",
        "Servicios", "Proyectos", "Talento", "Ventures", "Factory", "House", "Works", "Creative", "Labs"
    ]
    sector_to_hint = {
        "sector:tecnologia-y-software": "Tech",
        "sector:marketing-y-medios": "Marketing",
        "sector:educacion-y-formacion": "Edu",
        "sector:salud-y-bienestar": "Salud",
        "sector:servicios-profesionales": "Consult",
        "sector:finanzas-y-seguros": "Fin",
        "sector:comercio-y-ecommerce": "Retail",
        "sector:hosteleria-y-eventos": "Hostel",
        "sector:inmobiliario-y-construccion": "Inmo",
        "sector:administracion-publica-y-ong": "Cívico",
        "sector:industria-y-fabricacion": "Indus",
        "sector:creadores-y-artistas": "Creativo",
        "sector:otros": "Var"
    }
    hint = sector_to_hint.get(sector, "Biz")
    name_core = random.choice([
        "Nova", "Arco", "Tarraco", "Mediterrani", "Eixample", "Rambla", "Mar", "Horizon", "Alfa", "Omega",
        "Delta", "Orion", "Círculo", "Punta", "Faro", "Nexus", "Atlas", "Brisa", "Cobalto", "Tramuntana"
    ])
    suffix = random.choice(bases)
    company = f"{name_core} {hint} {suffix}"
    legal_suffix = random.choice(["S.L.", "S.A.", "S.L.U.", "S.C.", "S.Coop.", "S.L.P."])
    return f"{company} {legal_suffix}"


def email_from_name(first: str, last: str, domain: str = None) -> str:
    base = f"{first}.{last}".lower()
    base = base.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    base = base.replace(" ", "")
    domains = [
        "empresa.com", "negocio.es", "corp.es", "businessmail.com", "pro.es", "co.es", "startups.es",
        "consulting.es", "marketing.es", "finanzas.es"
    ]
    dom = domain if domain else random.choice(domains)
    return f"{base}@{dom}"


def additional_emails(first: str, last: str) -> str:
    count = random.choices([0, 1, 2, 3], weights=[0.6, 0.25, 0.1, 0.05])[0]
    if count == 0:
        return ""
    emails = []
    for i in range(count):
        if i == 0:
            emails.append(email_from_name(first, last, domain="corporate.net"))
        elif i == 1:
            emails.append(email_from_name(first, last, domain="office.es"))
        else:
            emails.append(email_from_name(first, last, domain="team.es"))
    return ", ".join(emails)


def additional_phones() -> str:
    count = random.choices([0, 1, 2], weights=[0.7, 0.25, 0.05])[0]
    if count == 0:
        return ""
    phones = []
    for _ in range(count):
        phones.append(random_phone_es())
    return ", ".join(phones)


def pick_sector_activity() -> tuple[str, str]:
    sector = pick_weighted([
        ("sector:tecnologia-y-software", 12),
        ("sector:marketing-y-medios", 10),
        ("sector:educacion-y-formacion", 8),
        ("sector:salud-y-bienestar", 8),
        ("sector:servicios-profesionales", 12),
        ("sector:finanzas-y-seguros", 6),
        ("sector:comercio-y-ecommerce", 9),
        ("sector:hosteleria-y-eventos", 8),
        ("sector:inmobiliario-y-construccion", 6),
        ("sector:administracion-publica-y-ong", 4),
        ("sector:industria-y-fabricacion", 7),
        ("sector:creadores-y-artistas", 6),
        ("sector:otros", 4),
    ])
    sector_to_activities = {
        "sector:tecnologia-y-software": ["actividad:software", "actividad:it"],
        "sector:marketing-y-medios": ["actividad:marketing", "actividad:medios"],
        "sector:educacion-y-formacion": ["actividad:formacion", "actividad:academia"],
        "sector:salud-y-bienestar": ["actividad:clinica", "actividad:estetica"],
        "sector:servicios-profesionales": ["actividad:consultoria", "actividad:legal"],
        "sector:finanzas-y-seguros": ["actividad:finanzas", "actividad:seguros"],
        "sector:comercio-y-ecommerce": ["actividad:retail", "actividad:ecommerce"],
        "sector:hosteleria-y-eventos": ["actividad:restauracion", "actividad:eventos"],
        "sector:inmobiliario-y-construccion": ["actividad:inmobiliaria", "actividad:construccion"],
        "sector:administracion-publica-y-ong": ["actividad:administracion", "actividad:ong"],
        "sector:industria-y-fabricacion": ["actividad:fabricacion", "actividad:logistica"],
        "sector:creadores-y-artistas": ["actividad:creacion", "actividad:arte"],
        "sector:otros": ["actividad:varios"],
    }
    activity = random.choice(sector_to_activities[sector])
    return sector, activity


def pick_source() -> str:
    return pick_weighted([
        ("source:web", 35),
        ("source:fb_ads", 30),
        ("source:ig_organico", 20),
        ("source:event_qr", 15),
    ])


def pick_service_and_reason() -> tuple[str, str]:
    service = pick_weighted([
        ("servicio:open-space", 20),
        ("servicio:sala-reuniones", 22),
        ("servicio:oficina-privada", 18),
        ("servicio:evento-networking", 12),
        ("servicio:curso-online-grabacion", 10),
        ("servicio:curso-online-directo", 8),
        ("servicio:estudio", 5),
        ("servicio:curso-presencial", 5),
    ])
    reason_templates = {
        "servicio:open-space": [
            "Necesito un puesto en open space para trabajar algunos días a la semana.",
            "Busco un entorno profesional para concentrarme en Tarragona.",
        ],
        "servicio:sala-reuniones": [
            "Quisiera reservar una sala de reuniones para un workshop.",
            "Necesitamos una sala para reuniones con clientes y presentaciones.",
        ],
        "servicio:oficina-privada": [
            "Estamos buscando un despacho privado para 2-4 personas.",
            "Nos interesa un despacho con acceso 24/7 y buena conectividad.",
        ],
        "servicio:evento-networking": [
            "Queremos organizar un evento de networking con ponencias breves.",
            "Estamos planificando un meetup para nuestra comunidad.",
        ],
        "servicio:curso-online-grabacion": [
            "Buscamos espacio y soporte para grabar un curso online.",
            "Necesitamos estudio para grabación con buena acústica.",
        ],
        "servicio:curso-online-directo": [
            "Queremos emitir un curso online en directo con soporte técnico.",
            "Necesitamos streaming estable para un webinar.",
        ],
        "servicio:estudio": [
            "Necesitamos el estudio para grabar contenido audiovisual.",
            "Buscamos un set con iluminación y sonido profesional.",
        ],
        "servicio:curso-presencial": [
            "Queremos impartir un curso presencial de fin de semana.",
            "Buscamos aula para formación con proyector.",
        ],
    }
    reason = random.choice(reason_templates[service])
    return service, reason


def proposal_from_service(service: str, company: str) -> str:
    templates = {
        "servicio:sala-reuniones": "En nuestro coworking de Tarragona, reserva salas equipadas con pantalla, videoconferencia y pizarra. Ideal para reuniones con clientes y workshops de {company}.",
        "servicio:oficina-privada": "Despachos privados llave en mano en Tarragona, con acceso 24/7, Internet simétrico y mobiliario ergonómico para el equipo de {company}.",
        "servicio:open-space": "Puestos flex y fijos en open space con luz natural, café de cortesía y comunidad activa. Perfecto para concentrarte y conectar en Tarragona.",
        "servicio:evento-networking": "Diseñamos y alojamos tu networking en Tarragona: catering opcional, apoyo de difusión y set-up para charlas. {company} proyectará una imagen profesional.",
        "servicio:curso-online-grabacion": "Estudio con acústica tratada, croma, cámaras 4K y soporte técnico para grabar el curso online de {company} con calidad profesional.",
        "servicio:curso-online-directo": "Streaming estable con redundancia de red, microfonía y realización en directo. Soporte técnico durante la emisión de {company}.",
        "servicio:estudio": "Estudio equipado con iluminación, fondo y audio profesional para las producciones de {company} en Tarragona.",
        "servicio:curso-presencial": "Aulas modulables con proyector y layout a medida para la formación presencial de {company}. Gestión de inscripciones si lo requieres.",
    }
    return templates.get(service, "Propuesta personalizada para tus necesidades en Tarragona.").format(company=company)


def random_datetime_2024_2025() -> datetime:
    start = datetime(2024, 10, 1, 8, 0, 0)
    end = datetime(2025, 8, 1, 20, 0, 0)
    delta = end - start
    seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=seconds)


def fmt_iso_with_offset(dt: datetime) -> str:
    # Append +02:00 explicitly (Tarragona summer time approximation)
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + "+02:00"


def generate_tags(base_existing: list[str], source: str, sector: str, activity: str, service: str) -> str:
    tags = list(base_existing)
    tags.extend([source, sector, activity, service])
    # Etiqueta fija para facilitar el borrado posterior en CRM
    if "Dummy" not in tags:
        tags.append("Dummy")
    return ", ".join(tags)


def pick_existing_style_tags() -> list[str]:
    pool = [
        "nuevo-lead", "interesado", "follow-up", "high priority", "warm lead"
    ]
    count = random.choices([0, 1, 2], weights=[0.4, 0.4, 0.2])[0]
    return random.sample(pool, k=count)


def main(output_path: str, n: int = 100, seed: int = 42) -> None:
    random.seed(seed)
    headers = [
        "First Name", "Last Name", "Business Name", "Company Name", "Phone", "Email",
        "Created", "Last Activity", "Tags", "Razón de Contacto", "Propuesta de Valor", "Additional Emails", "Additional Phones"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)

        for _ in range(n):
            first, last = generate_names()
            sector, activity = pick_sector_activity()
            company_name = generate_company(sector)
            business_name = company_name.replace(" S.L.", "").replace(" S.A.", "").replace(" S.L.U.", "").replace(" S.C.", "").replace(" S.Coop.", "").replace(" S.L.P.", "")
            phone = random_phone_es() if maybe(0.8) else ""
            email = email_from_name(first, last)
            source = pick_source()
            service, reason = pick_service_and_reason()
            proposal = proposal_from_service(service, business_name)

            created = random_datetime_2024_2025()
            last_activity = ""
            if maybe(0.7):
                last_activity_dt = created + timedelta(days=random.randint(0, 60), hours=random.randint(0, 10), minutes=random.randint(0, 59))
                last_activity = fmt_iso_with_offset(last_activity_dt)

            created_str = fmt_iso_with_offset(created)

            base_tags = pick_existing_style_tags()
            tags = generate_tags(base_tags, source, sector, activity, service)

            add_emails = additional_emails(first, last)
            add_phones = additional_phones()

            row = [
                first,
                last,
                business_name,
                company_name,
                phone,
                email,
                created_str,
                last_activity,
                tags,
                reason,
                proposal,
                add_emails,
                add_phones,
            ]
            writer.writerow(row)


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "synthetic_contacts_100.csv"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    main(out, n, seed)



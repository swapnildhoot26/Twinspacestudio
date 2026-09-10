"""Shared renderer for generated area and guide pages.

The scaffolding (head, nav, footer, FAQ script) is identical across pages on
purpose -- that is normal boilerplate. Everything inside <article> comes from
per-page content modules so no two pages share body copy.
"""

import html
import json
import os
import re

SITE = "https://twinspacestudios.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Real project photography. Every caption names the project it actually came
# from, so a photo is never implied to be work in a different neighbourhood.
PHOTOS = {
    # Baner -- 3 BHK duplex, Baner Road
    "e01": (1394, 1128, "Living room television wall in fluted teak with lit display niches", "Living room and television wall"),
    "e02": (1448, 1086, "Bedroom with a stone-panelled headboard wall and brass pendant lights", "Guest bedroom"),
    "e03": (1086, 1448, "Entrance foyer with a teak jaali screen and integrated planters", "Entry foyer and jaali screen"),
    "e04": (1122, 1402, "Master bedroom with a dark stone headboard wall and fluted side panelling", "Master bedroom"),
    "e05": (1212, 806, "Modular kitchen with a stone counter and a hob run under the window", "Modular kitchen"),
    "e06": (1448, 1086, "Study bedroom with a wardrobe, a built-in desk and a sofa", "Study bedroom"),
    "e07": (1024, 1536, "Backlit arched marble pooja unit with carved jaali doors", "Pooja unit"),
    "e08": (1448, 1086, "Bedroom with a built-in work desk beside the window", "Bedroom with work desk"),
    "e09": (1437, 1095, "Double-height living room with a built-in swing and the staircase beyond", "Living room and swing"),
    "e10": (1448, 1086, "Bedroom with a study desk and floor-length curtains", "Second bedroom"),
    "e11": (712, 832, "Tall kitchen unit with wicker basket pull-outs and glossy shutters", "Kitchen tall unit"),
    # Kothrud -- 3 BHK, Dahanukar Colony
    "a01": (1536, 1024, "Living room with a stone television panel against a blush art wall", "Living room"),
    "a02": (1402, 1122, "Living room with a pink sofa, a window seat and track lighting", "Living room and window seat"),
    "a03": (1086, 1448, "Child's bedroom with a window seat, a study desk and a patterned panel", "Child's bedroom"),
    "a04": (1086, 1448, "Bedroom with a day bed, black jaali screens and a study corner", "Day bed and study corner"),
    "a05": (1448, 1086, "Galley modular kitchen with a black counter and cream shutters", "Modular kitchen"),
    "a06": (1086, 1448, "Backlit pooja unit at the entry behind a black-framed glass partition", "Pooja unit at the entry"),
    "a07": (1122, 1402, "Wardrobe run in green shutters with a full-height mirror", "Wardrobe run"),
    "a08": (1402, 1122, "Twin-bed room with a green headboard panel and a window seat", "Twin bedroom"),
    "a09": (1402, 1122, "Master bedroom with a backlit mirror frame and a floral headboard wall", "Master bedroom"),
    # Kharadi -- 3 BHK
    "c01": (1086, 1448, "Entrance foyer with fluted panelling and a low shoe cabinet", "Entry foyer"),
    "c02": (1086, 1448, "Living room with a marble television wall opening to the balcony", "Living room"),
    "c03": (1182, 1331, "Modular kitchen with sage green base units and black wall cabinets", "Modular kitchen"),
    "c04": (1402, 1122, "Bedroom with an arched wardrobe detail and a slim wall ledge", "Bedroom wardrobe"),
    "c05": (1086, 1448, "Arched pooja niche with backlit lotus artwork and drawers below", "Pooja niche"),
    "c06": (1448, 1086, "Foyer with a black arched mirror above a wall-hung console", "Foyer console"),
    "c07": (1122, 1402, "Master bedroom with a blush wardrobe and access to the balcony", "Master bedroom"),
    "c08": (1086, 1448, "Bedroom with a sliding wardrobe and an arched mirror niche", "Second bedroom"),
    "c09": (1086, 1448, "Bedroom headboard in marble-look panelling with a pink upholstered bed", "Headboard detail"),
    # Kondhwa -- 4 BHK, Escon
    "b01": (1023, 1537, "Entry console with an arched niche above a fluted drawer unit", "Entry console"),
    "b02": (1023, 1537, "View from the passage into the living room with a blue sectional", "Passage to living room"),
    "b03": (1448, 1086, "Bedroom with a teal upholstered headboard and a glossy sliding wardrobe", "Bedroom"),
    "b04": (1537, 1023, "Dining set under a slatted timber ceiling beside a breakfast counter", "Dining and breakfast counter"),
    "b05": (1600, 900, "Living room with a blue sectional sofa and brass wall art", "Living room"),
    "b06": (1448, 1086, "Open-plan living and dining with a marble television wall", "Open-plan living and dining"),
    "b07": (1448, 1086, "L-shaped modular kitchen with a black counter and glass-fronted wall units", "Modular kitchen"),
    "b08": (1086, 1448, "Children's bedroom with twin beds and a scalloped headboard", "Children's bedroom"),
    # Balewadi -- 2 BHK
    "d01": (1536, 1024, "Living room with a television unit, a cane panel and a green sofa", "Living room"),
    "d02": (1086, 1448, "Kitchen opened into the living room across a breakfast counter", "Kitchen and breakfast counter"),
    "d03": (1536, 1024, "Open kitchen seen from the living room seating", "Open kitchen"),
    "d04": (1086, 1448, "Master bedroom with a glossy wardrobe and an upholstered headboard", "Master bedroom"),
    "d05": (1448, 1086, "Bedroom with an arched wardrobe in soft green", "Second bedroom"),
    "d06": (1086, 1448, "Dining area under a slatted ceiling with a pendant and a jaali screen", "Dining area"),
    "d07": (1086, 1448, "Guest bedroom with a study desk and open shelving", "Guest bedroom"),
    # Punawale -- 2 BHK
    "f01": (1448, 1086, "Living room with a fluted television wall and a teal sofa", "Living room"),
    "f02": (1402, 1122, "Master bedroom with an arched mirror and a botanical headboard panel", "Master bedroom"),
    "f03": (1086, 1448, "Bedroom with a fluted headboard and botanical wallpaper", "Bedroom"),
    "f04": (1448, 1086, "Daughter's bedroom in pink with a botanical mural and a storage bed", "Daughter's bedroom"),
    "f05": (1086, 1448, "Guest bedroom with a sofa-cum-bed below a framed gallery wall", "Guest bedroom"),
    "f06": (1122, 1402, "Study nook with a desk and overhead storage", "Study nook"),
    "f07": (1086, 1448, "Balcony with a hanging swing chair, a timber ceiling and planters", "Balcony"),
}

# Twelve of these photos already exist as SEO-named copies under /assets/areas/.
# Prefer those paths so the earlier filename work stays in use; the caption names the
# real project either way, so a "punawale" filename on the Wakad page is still accurate.
SEO_NAMES = {
    "e09": "interior-designers-baner-pune-living-room-swing",
    "e05": "interior-designers-baner-pune-modular-kitchen",
    "a02": "interior-designers-kothrud-pune-living-room",
    "a05": "interior-designers-kothrud-pune-modular-kitchen",
    "d06": "interior-designers-balewadi-pune-dining-pooja-unit",
    "d03": "interior-designers-balewadi-pune-open-kitchen",
    "c06": "interior-designers-kharadi-pune-foyer-arched-mirror",
    "c03": "interior-designers-kharadi-pune-modular-kitchen",
    "b04": "interior-designers-kondhwa-pune-dining-slatted-ceiling",
    "b06": "interior-designers-kondhwa-pune-tv-unit-breakfast-counter",
    "f01": "interior-designers-punawale-pune-living-dining",
    "f02": "interior-designers-punawale-pune-master-bedroom",
}


def img_paths(pid):
    """(jpg, webp) for a photo id, preferring the SEO-named copy."""
    if pid in SEO_NAMES:
        base = "/assets/areas/" + SEO_NAMES[pid]
        return base + ".jpg", base + ".webp"
    return "/assets/opt/%s.jpg" % pid, "/assets/opt/webp/%s.webp" % pid


PROJECTS = {
    "e": ("3 BHK duplex, Baner", "/projects/baner-duplex"),
    "a": ("3 BHK, Dahanukar Colony, Kothrud", "/projects/kothrud-3bhk"),
    "c": ("3 BHK, Kharadi", "/projects/kharadi-3bhk"),
    "b": ("4 BHK, Escon, Kondhwa", "/projects/kondhwa-4bhk"),
    "d": ("2 BHK, Balewadi", "/projects/balewadi-2bhk"),
    "f": ("2 BHK, Punawale", "/projects/punawale-2bhk"),
}

HEADER = """<header class="site-header">
  <a href="/" class="logo">
    <img src="/assets/images/logo-mark.png" alt="Twin Space Studio — interior design studio in Pune" width="200" height="121">
  </a>
  <nav>
    <a href="/#projects">Projects</a>
    <a href="/#services">Services</a>
    <a href="/#process">Process</a>
    <a href="/#founders">About</a>
    <a href="/#contact">Contact</a>
  </nav>
</header>"""

FOOTER = """<footer class="site-footer">
  <p>Full-service interior designers in Pune — residential and commercial interior design, turnkey execution and styling across Pune and PCMC.</p>
  <p>
    <a href="tel:+918208093011">Pooja Dhoot &middot; 82080 93011</a> &middot;
    <a href="tel:+918888177217">Dimple Marathe &middot; 88881 77217</a> &middot;
    <a href="mailto:info@twinspacestudios.com">info@twinspacestudios.com</a>
  </p>
  <p>A-1102, Phase 4, Puraniks Aldea Anexo, Mahalunge, Baner, Pune 411045</p>
  <p>&copy; 2026 Twin Space Studio, Pune. All rights reserved.</p>
</footer>"""

FAQ_SCRIPT = """<script>
// Browsers without <details name> support get the same one-at-a-time behaviour.
(function () {
  if ('name' in document.createElement('details')) return;
  var items = document.querySelectorAll('details.faq-item');
  items.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      items.forEach(function (o) { if (o !== d) o.open = false; });
    });
  });
})();
</script>"""


def esc(s):
    return html.escape(s, quote=False)


def gallery(ids, note=None):
    """Render a figure row from photo ids. Captions name the real project."""
    figs = []
    for pid in ids:
        w, h, alt, cap = PHOTOS[pid]
        proj, url = PROJECTS[pid[0]]
        jpg, webp = img_paths(pid)
        figs.append(
            '<figure class="project-shot">'
            f'<picture><source srcset="{webp}" type="image/webp"/>'
            f'<img src="{jpg}" alt="{esc(alt)} — {esc(proj)}, by Twin Space Studio" '
            f'width="{w}" height="{h}" loading="lazy"/></picture>'
            f'<figcaption>{esc(cap)} &mdash; <a href="{url}">{esc(proj)}</a></figcaption>'
            '</figure>'
        )
    out = '<div class="project-gallery">' + "".join(figs) + "</div>"
    if note:
        out += f'<p class="gallery-note">{note}</p>'
    return out


def faq_html(faqs):
    parts = ['<h2>Common questions</h2>']
    for q, a in faqs:
        parts.append(
            '<details class="faq-item" name="faq">'
            f'<summary class="faq-q">{esc(q)}<span aria-hidden="true" class="faq-icon"></span></summary>'
            f'<p class="faq-a">{a}</p></details>'
        )
    return "".join(parts)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def render(page):
    """page: dict describing one generated page."""
    url = SITE + page["path"]
    title = page["title"]
    desc = page["description"]
    lead_img = page.get("og_image")

    ld = []
    if page.get("service"):
        svc = {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Residential interior design and turnkey execution",
            "name": strip_tags(page["h1"]),
            "url": url,
            "provider": {"@id": SITE + "/#business"},
            "areaServed": {"@type": "Place", "name": page["service"]},
            "dateModified": page.get("modified", "2026-09-10"),
        }
        if lead_img:
            svc["image"] = [SITE + lead_img]
        ld.append(svc)
    if page.get("article"):
        ld.append({
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": strip_tags(page["h1"]),
            "description": strip_tags(desc),
            "url": url,
            "author": {"@id": SITE + "/#business"},
            "publisher": {"@id": SITE + "/#business"},
            "dateModified": page.get("modified", "2026-09-10"),
            "mainEntityOfPage": url,
        })
    ld.append({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": SITE + u if u else url}
            for i, (n, u) in enumerate(page["crumbs"])
        ],
    })
    if page.get("faqs"):
        ld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in page["faqs"]
            ],
        })

    ld_tags = "\n".join(
        '<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "</script>"
        for x in ld
    )

    crumb_nav = ['<nav class="crumbs" aria-label="Breadcrumb">']
    for i, (n, u) in enumerate(page["crumbs"]):
        last = i == len(page["crumbs"]) - 1
        crumb_nav.append(f"<span>{esc(n)}</span>" if last else f'<a href="{u}">{esc(n)}</a>')
        if not last:
            crumb_nav.append(" <span>/</span> ")
    crumb_nav.append("</nav>")

    og = f'<meta property="og:image" content="{SITE}{lead_img}">' if lead_img else ""

    body = page["body"]
    if page.get("faqs"):
        body += faq_html(page["faqs"])

    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Twin Space Studio">
{og}
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/54fef342-67e2-40d0-b750-f6f954aa3bd8.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/8be1dff1-74f1-417f-81c1-598d832e83d2.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/3811d17e-80cb-4332-bd35-dfa1f097b18c.woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/styles.css">
{ld_tags}
  <script src="https://analytics.ahrefs.com/analytics.js" data-key="Plb7nEibS4yHwbbbhQEpiw" async></script>
</head>
<body>
{HEADER}

<main>
<article class="project-page area-page">
{''.join(crumb_nav)}<h1>{page['h1']}</h1>
{body}
</article>
</main>

{FOOTER}
{FAQ_SCRIPT}
</body>
</html>
"""


def write(page):
    out = os.path.join(ROOT, page["path"].lstrip("/") + ".html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(page))
    words = len(re.sub(r"\s+", " ", strip_tags(page["body"])).split())
    return out, words

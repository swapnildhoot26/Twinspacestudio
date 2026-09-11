# -*- coding: utf-8 -*-
"""East Pune: Koregaon Park, Viman Nagar, Kalyani Nagar, Mundhwa, Hadapsar."""

from pagegen import gallery
from content_areas_a import CRUMBS
from content_areas_c import NOTE

PAGES = []

# ---------------------------------------------------------- KOREGAON PARK
PAGES.append(dict(
    path="/areas/koregaon-park",
    slug="koregaon-park",
    landing=True,
    area_name="Koregaon Park",
    hero_image="/assets/opt/b04.jpg",
    hero_subtitle="Low-rise buildings, independent houses and old bungalows. The work here is usually subtractive: restoring what is there rather than boxing it in.",
    title="Best Interior Designers in Koregaon Park, Pune | Twin Space Studio",
    description="Interior designers in Koregaon Park, Pune. Renovations and turnkey interiors for low-rise apartments and bungalows, with a transparent line-item quote.",
    h1="Best Interior Designers in Koregaon Park, Pune",
    service="Koregaon Park, Pune",
    og_image="/assets/opt/b05.jpg",
    crumbs=CRUMBS("Koregaon Park", "koregaon-park"),
    body=gallery(["b05", "c02", "b04"], NOTE) + """
<p>Koregaon Park is the one part of Pune where the neighbourhood itself sets the
brief. Numbered lanes, mature trees, low buildings and a lot of genuinely old
property mean the homes here have character that most Pune stock does not — and
constraints that most Pune stock does not either. This page covers both.</p>

<h2>What Koregaon Park homes are like</h2>
<p>The housing runs from 1970s and 1980s low-rise apartment blocks along the
numbered lanes, through a small number of surviving bungalows and their converted
outbuildings, to a thin layer of newer premium apartments and boutique developments.
Building heights are mostly modest by Pune standards, plot sizes are generous, and
tree cover is real.</p>
<p>Flats tend to be large, oddly shaped, and full of features that no builder would
produce today: deep verandahs, high ceilings, servant quarters, separate dining
rooms, and windows in places a modern plan would never put them. Owners are a mix of
long-settled Pune families, business owners, people in hospitality and creative work,
and a notable expatriate and long-stay international community.</p>

<h2>Designing with what is already there</h2>
<p>The instinct that ruins a Koregaon Park flat is treating it like a new one.
Boxing in a high ceiling to run a flat gypsum plane, replacing sound teak windows
with aluminium, or levelling out an irregular plan into rectangles removes precisely
what made the property worth buying.</p>
<p>Our starting position here is subtractive. We look first at what to restore —
mosaic or terrazzo flooring that only needs polishing, teak windows that need
reglazing rather than replacing, a ceiling height that should stay open. Then we add
services carefully around it: electrical runs in surface conduit where chasing a
1978 wall is unwise, lighting on track or pendant rather than a full false ceiling,
and joinery that stands as furniture rather than being built hard into an old wall.</p>
<p>Where a false ceiling is genuinely needed — usually to run air-conditioning — we
keep it partial and set it back so the original height still reads.</p>

<h2>Old-building constraints, honestly stated</h2>
<p>These buildings ask more questions than any new tower. Wiring is frequently
original and inadequate, sometimes still aluminium. Plumbing is cast iron or early
PVC, and where it runs is rarely documented. Waterproofing on terraces and in
bathrooms is at or past the end of its life. Walls may be load-bearing masonry rather
than framed, which changes what can be opened and what cannot.</p>
<p>Access is its own subject. Many Koregaon Park buildings have no lift at all, or a
small one that will not take sheet material. The lanes are narrow and heavily parked,
and several are one-way. A full-size delivery vehicle often cannot reach the
building, so material transfers or is carried.</p>
<p>We survey before quoting rather than after, including a look at the distribution
board and a check of what is behind at least one wet wall. It is the only way to give
a number that survives contact with the building.</p>
""" + gallery(["c06", "b06", "b01"], None) + """
<h2>Bungalows and independent houses</h2>
<p>Where the property is an independent house rather than a flat, the scope widens
beyond interiors: roof and terrace waterproofing, external joinery, compound-facing
elevations, and sometimes structural repair. We take on the interior scope and
coordinate with a structural consultant where the building needs one, rather than
pretending an interior contractor can carry that judgement.</p>
<p>Planning permission is also live in a way it never is in an apartment. Anything
that changes the building envelope needs checking against Pune Municipal Corporation
rules and, in some pockets, heritage-adjacent constraints. We flag it early rather
than building first.</p>

<h2>What a Koregaon Park interior costs</h2>
<p>A full 3 BHK apartment runs &#8377;16&ndash;21 lakh as a baseline, but Koregaon
Park projects sit above that band more often than not — not because of finish level
but because of what an old building requires before any interior work starts.
Rewiring, replumbing, waterproofing and making good frequently add
&#8377;2&ndash;5 lakh on a flat that has not been touched in three decades.</p>
<p>We separate that into a clearly labelled building-works section in the quote,
above the interior lines, so you can see exactly what is restoration and what is
design. Independent houses are quoted entirely on scope.</p>
<p>The honest guidance we give here: budget for the invisible work first. A beautiful
kitchen in a flat with failing wiring is a poor use of money, and we would rather say
that at quoting stage than build it.</p>

<h2>Working with us in Koregaon Park</h2>
<p>Koregaon Park is around forty-five minutes from our Mahalunge studio. On old
buildings we front-load the survey and keep a supervisor on site daily through the
opening-up phase, because that is when the decisions that move the budget get made.
Both founders stay on the project throughout.</p>
<p>We also work in <a href="/areas/kalyani-nagar">Kalyani Nagar</a>,
<a href="/areas/mundhwa">Mundhwa</a>, <a href="/areas/kharadi">Kharadi</a>,
<a href="/areas/viman-nagar">Viman Nagar</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/turnkey-interiors">turnkey interiors</a> and
<a href="/guides/renovation-vs-new-flat">renovating an older flat</a>.</p>

<p>To talk through a home in Koregaon Park, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Koregaon Park?",
         "A full 3 BHK apartment starts at the usual &#8377;16&ndash;21 lakh band, but old buildings frequently need &#8377;2&ndash;5 lakh of rewiring, replumbing and waterproofing before interior work begins. We quote that separately so you can see what is restoration and what is design."),
        ("Should I keep the original flooring and windows?",
         "Usually yes. Mosaic and terrazzo floors often need only polishing, and sound teak windows are better reglazed than replaced. Boxing in a high ceiling or squaring off an irregular plan removes exactly what made the property worth buying."),
        ("Can a delivery truck reach a Koregaon Park building?",
         "Often not. The numbered lanes are narrow, heavily parked and several are one-way, and many buildings have no lift or one too small for sheet material. Material transfers to a smaller vehicle or is carried, and we price that on the first visit."),
        ("Do you work on bungalows and independent houses?",
         "Yes, for the interior scope, and we coordinate with a structural consultant where the building needs one. Anything that changes the building envelope also needs checking against municipal rules, which we flag before work starts rather than after."),
        ("What should the budget priority be in an old flat?",
         "The invisible work first. A new kitchen in a flat with failing wiring is a poor use of money. We would rather say that at quoting stage than build it and have you discover it later."),
    ],
))

# ---------------------------------------------------------- VIMAN NAGAR
PAGES.append(dict(
    path="/areas/viman-nagar",
    slug="viman-nagar",
    landing=True,
    area_name="Viman Nagar",
    hero_image="/assets/opt/b03.jpg",
    hero_subtitle="Designing around aircraft noise and riverside humidity, and the specification difference between fitting out to live in and fitting out to let.",
    title="Best Interior Designers in Viman Nagar, Pune | Twin Space Studio",
    description="Interior designers in Viman Nagar, Pune. Turnkey 2 BHK and 3 BHK interiors in 10-12 weeks, with a transparent line-item quote before work begins.",
    h1="Best Interior Designers in Viman Nagar, Pune",
    service="Viman Nagar, Pune",
    og_image="/assets/opt/c07.jpg",
    crumbs=CRUMBS("Viman Nagar", "viman-nagar"),
    body=gallery(["c07", "b03", "c03"], NOTE) + """
<p>Viman Nagar is one of Pune's most established east-side neighbourhoods, built out
around the airport and now dense, walkable and largely finished. The flats here
range across three decades, and a fit-out is shaped less by the building than by two
local facts: aircraft noise and a resident population that moves in and out more than
most of Pune. This page covers both.</p>

<h2>What Viman Nagar homes are like</h2>
<p>The stock runs from 1990s and early-2000s societies through the large mid-period
developments around Nagar Road and Phoenix Marketcity, to a smaller layer of recent
high-rise. Flats are mostly 2 and 3 BHK, generally 700 to 1,200 square feet of carpet
area, with some considerably larger units in the older low-density societies.</p>
<p>The resident mix is unusually varied for Pune: airline and airport staff, hotel
and hospitality professionals, technology workers commuting to Kharadi and Magarpatta,
defence-linked families, and a long-standing expatriate community. A meaningful share
of flats are rented rather than owner-occupied.</p>

<h2>Designing around aircraft noise</h2>
<p>Viman Nagar sits close to the runway approach, and in the pockets nearest it,
aircraft noise is a genuine design input rather than a nuisance to be mentioned in
passing.</p>
<p>What actually helps is glazing and soft mass. Upgrading to a well-sealed double
or laminated glass unit in the bedrooms facing the approach does more than anything
else, and the sealing matters as much as the glass. Beyond that: heavy lined
curtains rather than thin ones, an upholstered headboard on the shared wall, a rug
with underlay rather than bare vitrified floor, and a solid-core bedroom door instead
of the hollow flush door most builders fit.</p>
<p>None of this eliminates noise and we do not claim it does. Together it takes a
bedroom from disruptive to liveable, and it is far cheaper decided at drawing stage
than retrofitted.</p>

<h2>Owner-occupied or let</h2>
<p>With a large rental share, we are frequently asked to specify a flat for letting
rather than living. It is a different brief and we quote it differently: finishes
that survive tenants, a neutral palette, storage that is generous but simple, and no
delicate detail that turns into a deposit argument in three years.</p>
<p>A letting specification typically runs twenty to thirty per cent below a
comparable owner-occupied one. We say so plainly rather than selling the same scope
to both.</p>
""" + gallery(["c04", "b08", "c08"], None) + """
<h2>Older societies versus newer towers</h2>
<p>In the 1990s and early-2000s societies the questions are the familiar ageing-flat
ones: electrical loads sized before universal air conditioning, plumbing that is not
where the drawing says, bathroom waterproofing at the end of its life, and ceiling
height already reduced once. Several of these buildings also have no service lift,
so sheet material is carried or cut down and assembled in the flat.</p>
<p>In the newer towers it is a straight bare-handover fit-out — square walls,
repeating plans, planned service cores, and the usual competition for lift slots
during possession waves.</p>
<p>We survey before quoting in either case, but in the older stock that survey is
what makes the first number resemble the last one.</p>

<h2>What a Viman Nagar interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh, itemised before anything is ordered. A specification aimed at letting typically
runs &#8377;8&ndash;12 lakh for a 2 BHK.</p>
<p>Two Viman Nagar lines worth budgeting deliberately. Acoustic glazing in the
bedrooms facing the approach path, typically &#8377;45,000 to &#8377;1.2 lakh
depending on the number of windows and the specification. And, in the older
societies, a demolition and rewiring allowance stated separately rather than absorbed
into a round figure.</p>

<h2>Working with us in Viman Nagar</h2>
<p>Viman Nagar is about forty minutes from our Mahalunge studio, so we schedule
fewer, longer site visits and keep a supervisor on site through the working day.
Both founders stay on the project from sketch to snag.</p>
<p>We also work in <a href="/areas/kalyani-nagar">Kalyani Nagar</a>,
<a href="/areas/kharadi">Kharadi</a>, <a href="/areas/koregaon-park">Koregaon Park</a>,
<a href="/areas/mundhwa">Mundhwa</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/wardrobes-storage">wardrobes and storage</a> and
<a href="/guides/interior-design-cost-pune">what a full interior costs in Pune</a>.</p>

<p>To talk through a home in Viman Nagar, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Viman Nagar?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh. A specification aimed at letting the flat typically runs &#8377;8&ndash;12 lakh for a 2 BHK."),
        ("Can anything be done about aircraft noise?",
         "A well-sealed double or laminated glass unit in the bedrooms facing the approach does most of the work, and the sealing matters as much as the glass. Heavy lined curtains, an upholstered headboard, a rug with underlay and a solid-core bedroom door do the rest. Budget roughly &#8377;45,000 to &#8377;1.2 lakh for the glazing."),
        ("Do you fit out flats that will be rented?",
         "Yes, as a separate brief. Letting specifications favour robust finishes, a neutral palette and simple generous storage, and typically run twenty to thirty per cent below an owner-occupied scope."),
        ("Are the older Viman Nagar societies harder to work in?",
         "They ask more questions — electrical loads, plumbing runs, bathroom waterproofing, remaining ceiling height — and several have no service lift. We survey before quoting so the first number accounts for it."),
        ("How long does a full interior take in Viman Nagar?",
         "Ten to twelve weeks from approved drawings for a straight fit-out. Renovation in an older society where the family stays in the flat runs about two weeks longer."),
    ],
))

# ---------------------------------------------------------- KALYANI NAGAR
PAGES.append(dict(
    path="/areas/kalyani-nagar",
    slug="kalyani-nagar",
    landing=True,
    area_name="Kalyani Nagar",
    hero_image="/assets/opt/b06.jpg",
    hero_subtitle="Compact premium flats by the river, where material choices have to survive the monsoon and quality matters more than covering every surface.",
    title="Best Interior Designers in Kalyani Nagar, Pune | Twin Space Studio",
    description="Interior designers in Kalyani Nagar, Pune. Turnkey and renovation interiors for riverside apartments, with a transparent line-item quote before work begins.",
    h1="Best Interior Designers in Kalyani Nagar, Pune",
    service="Kalyani Nagar, Pune",
    og_image="/assets/opt/c09.jpg",
    crumbs=CRUMBS("Kalyani Nagar", "kalyani-nagar"),
    body=gallery(["c09", "b06", "c05"], NOTE) + """
<p>Kalyani Nagar is compact, riverside and expensive, and the homes reflect all
three. Flats here are generally smaller than the price suggests, the buildings sit
close to the Mula-Mutha, and a high proportion are premium apartments from the
2000s now on their second interior. This page covers what that combination needs.</p>

<h2>What Kalyani Nagar homes are like</h2>
<p>The stock is mostly mid-rise premium apartments built between roughly 2000 and
2015, concentrated between the river and Nagar Road, with a smaller number of newer
high-end developments and a handful of older low-rise buildings. Flats are typically
2 and 3 BHK, often 800 to 1,400 square feet of carpet area, with generous room
proportions but modest total areas — you pay for the address and the position rather
than the footprint.</p>
<p>Owners skew toward business owners, senior professionals, hospitality and
restaurant operators, and a significant number of people who bought in Kalyani Nagar
specifically to be able to walk to things, which is rare in Pune.</p>

<h2>Compact premium, and what it demands</h2>
<p>A high budget in a modest floor area is a different design problem from a high
budget in a large one, and it is the defining Kalyani Nagar condition.</p>
<p>What works is spending on a small number of things properly rather than covering
every surface. A kitchen specified to a genuinely high standard because it is
compact enough to afford that. Joinery in materials that reward being seen closely,
since in a smaller room everything is seen closely. Fewer, better light fittings on
separate circuits. Stone used where it is touched rather than as wall cladding.</p>
<p>What does not work is the full-coverage approach that suits a larger flat. In
1,000 square feet, panelling every wall and dropping a ceiling throughout makes the
home smaller and more expensive at the same time.</p>

<h2>Living by the river</h2>
<p>Proximity to the Mula-Mutha has two practical effects worth planning for.</p>
<p>Humidity is higher and more persistent than in west Pune, particularly on lower
floors and river-facing sides. That argues for moisture-resistant carcass material in
the kitchen and any wardrobe on an external wall, marine-grade or BWP plywood in wet
zones rather than commercial ply, and hardware in stainless or properly coated finish
rather than the cheapest available. It also argues for ventilation that actually
works, including in bathrooms where a builder's token exhaust is often inadequate.</p>
<p>The second effect is monsoon. Lower floors in some riverside buildings have a
history of water ingress, and it is worth establishing that history honestly before
building fitted joinery against an affected wall. We ask, and we look.</p>
""" + gallery(["b01", "c08", "b03"], None) + """
<h2>Renovating a 2000s premium flat</h2>
<p>Most of our Kalyani Nagar work is second-round interiors: a flat that was well
finished fifteen years ago and now needs the kitchen, the bathrooms and the storage
brought up to date while the good bones stay.</p>
<p>The judgement calls are consistent. Stone flooring in good condition is almost
always worth keeping and polishing. Original hardwood joinery is usually worth
refinishing. A ceiling dropped in 2008 to hide air-conditioning ducting can often be
raised or partially removed to recover height. Bathrooms almost always need doing
completely, because the waterproofing is at the end of its life whatever the tiles
look like.</p>
<p>Roughly half these clients stay in the flat through the work. We phase it room by
room behind a sealed dust barrier, group the wet work into a single block, and keep
one bathroom and one bedroom usable throughout. It adds about two weeks.</p>

<h2>What a Kalyani Nagar interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh as a baseline, but Kalyani Nagar projects commonly sit above those bands because
the specification tends to be higher and because second-round renovation adds
demolition, debris and full bathroom replacement — typically &#8377;1.5 to
&#8377;3.5 lakh on a 3 BHK.</p>
<p>Every line is itemised before anything is ordered, and the building works are
listed separately from the interior scope so you can see which is which.</p>

<h2>Working with us in Kalyani Nagar</h2>
<p>Kalyani Nagar is around forty-five minutes from our Mahalunge studio. On
renovation work we front-load the survey and keep a supervisor on site through the
opening-up phase. Both founders stay on the project from sketch to snag.</p>
<p>We also work in <a href="/areas/koregaon-park">Koregaon Park</a>,
<a href="/areas/viman-nagar">Viman Nagar</a>, <a href="/areas/kharadi">Kharadi</a>,
<a href="/areas/mundhwa">Mundhwa</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/modular-kitchens">modular kitchens</a> and
<a href="/guides/plywood-and-materials">choosing plywood and materials</a>.</p>

<p>To talk through a home in Kalyani Nagar, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Kalyani Nagar?",
         "A full 2 BHK starts at &#8377;12&ndash;16 lakh and a 3 BHK at &#8377;16&ndash;21 lakh, though Kalyani Nagar projects commonly sit above those bands. Second-round renovation adds demolition, debris and full bathroom replacement, typically &#8377;1.5 to &#8377;3.5 lakh on a 3 BHK."),
        ("Does being near the river affect materials?",
         "Yes. Humidity is higher and more persistent, especially on lower floors and river-facing sides. We specify BWP or marine-grade plywood in wet zones, moisture-resistant carcass material for kitchens and external-wall wardrobes, and properly coated or stainless hardware."),
        ("How should a high budget be spent in a smaller flat?",
         "On fewer things done properly rather than on covering every surface. In 1,000 square feet, panelling every wall and dropping a ceiling throughout makes the home smaller and more expensive at once."),
        ("Is it worth keeping the existing stone flooring?",
         "Usually yes. Stone floors in good condition polish up well, and keeping them releases budget for the kitchen and bathrooms, which almost always need doing completely."),
        ("Can we live in the flat during a renovation?",
         "Yes, and about half our Kalyani Nagar clients do. We phase it room by room behind a dust barrier, group the wet work into one block and keep a bathroom and bedroom usable. It adds roughly two weeks."),
    ],
))

# ---------------------------------------------------------- MUNDHWA
PAGES.append(dict(
    path="/areas/mundhwa",
    slug="mundhwa",
    landing=True,
    area_name="Mundhwa",
    hero_image="/assets/opt/b07.jpg",
    hero_subtitle="Keshav Nagar high-rise, handed over in waves, in societies that are often still writing their fit-out rules. We get them in writing before drawings are final.",
    title="Best Interior Designers in Mundhwa, Pune | Twin Space Studio",
    description="Interior designers in Mundhwa and Keshav Nagar, Pune. Turnkey interiors for new-possession towers in 10-12 weeks, with a transparent line-item quote.",
    h1="Best Interior Designers in Mundhwa, Pune",
    service="Mundhwa, Pune",
    og_image="/assets/areas/interior-designers-kharadi-pune-modular-kitchen.jpg",
    crumbs=CRUMBS("Mundhwa", "mundhwa"),
    body=gallery(["c03", "b07", "c01"], NOTE) + """
<p>Mundhwa has changed faster than almost anywhere in Pune. A decade ago it was
industrial land and low-rise settlement; now the Keshav Nagar and riverside stretch
holds some of the city's largest new residential towers. Almost every project here is
a bare-handover fit-out in a society that is still forming. This page covers what
that means in practice.</p>

<h2>What Mundhwa homes are like</h2>
<p>The residential stock is overwhelmingly post-2016, concentrated in Keshav Nagar
and along the Mundhwa-Kharadi road, in large gated developments of fifteen floors and
upward. Flats are mostly 2 and 3 BHK between roughly 650 and 1,150 square feet of
carpet area, with a growing premium segment in the riverside towers.</p>
<p>Buyers are largely technology and services professionals working in Kharadi,
Magarpatta and Hadapsar, plus a significant investor share. Many bought off-plan and
see the flat for the first time on possession day, which shapes the brief: references
are already gathered, and the questions are about cost, sequence and accountability.</p>

<h2>Buying into a society that is still forming</h2>
<p>Mundhwa's defining condition is newness — not just of the buildings but of the
management around them. In a tower handing over its first phase, the fit-out rules
are frequently being written while you are working under them.</p>
<p>The practical consequences are real. Rules can change between your quote and your
start date. A deposit amount quoted verbally may not match the one demanded at the
gate. Service-lift booking systems are sometimes informal for the first few months,
which sounds convenient and in practice means whoever asks loudest gets the lift.</p>
<p>We get the rules in writing in week one, confirm the deposit and the working hours
with the facility management company rather than the security desk, and put the
lift-slot requirement in the schedule as a hard constraint. On a first-phase tower
that is worth more than any amount of design efficiency.</p>

<h2>Possession waves and the local trade queue</h2>
<p>When a Mundhwa tower hands over, it hands over in hundreds of flats. Everything
becomes scarce in the same fortnight: lift slots, electricians, painters, debris
trucks, and the few local hardware shops that serve the area.</p>
<p>Being ahead of that wave is the single largest lever on your timeline. Drawings
approved and material ordered before you collect the keys means carpentry starts in
week one while your neighbours are still arranging gate passes. Families who start
the conversation after possession routinely finish four to five weeks later for no
design reason at all.</p>
""" + gallery(["c04", "b02", "c05"], None) + """
<h2>Snagging before you start</h2>
<p>New does not mean finished, and in fast-built towers it means less than usual.
Before our work begins we walk the flat against a snag list and hand it to the
builder: floor level across each room, fall in the bathrooms and utility, window and
door alignment, seepage at external walls, and whether the promised electrical points
exist where the brochure said they would.</p>
<p>Riverside towers in particular are worth checking for damp at external walls
before joinery goes in. Once a wardrobe stands against an affected wall, the problem
stops being the builder's.</p>

<h2>What a Mundhwa interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh, itemised before anything is ordered. Mundhwa projects usually sit in the middle
to upper part of those bands, because bare handover means every line is new.</p>
<p>Two lines worth budgeting deliberately in these towers. Balcony treatment,
typically &#8377;70,000 to &#8377;1.6 lakh, which repays well given the height and
the river outlook in some blocks. And air-conditioning coordination, since outdoor
unit positions need society agreement and concealed pipe runs must be planned before
the false ceiling closes.</p>

<h2>Working with us in Mundhwa</h2>
<p>Mundhwa is around forty-five minutes from our Mahalunge studio, so we schedule
fewer, longer site visits and keep a supervisor on site through the working day. Both
founders stay on the project from first sketch to snag list, and carpentry is built in
your flat rather than shipped in.</p>
<p>We also work in <a href="/areas/kharadi">Kharadi</a>,
<a href="/areas/hadapsar">Hadapsar</a>,
<a href="/areas/magarpatta-city">Magarpatta City</a>,
<a href="/areas/koregaon-park">Koregaon Park</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/turnkey-interiors">turnkey interiors</a> and
<a href="/guides/new-flat-possession-checklist">what to check before you start</a>.</p>

<p>To talk through a home in Mundhwa or Keshav Nagar, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Mundhwa?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh, usually in the middle to upper part of those bands because bare handover means every line is new."),
        ("What is different about a society that has just formed?",
         "The fit-out rules are often still being written. Deposits, working hours and lift-booking systems can change between your quote and your start date. We confirm everything in writing with the facility management company in week one rather than relying on the security desk."),
        ("How do possession waves affect my timeline?",
         "When a Mundhwa tower hands over hundreds of flats at once, lift slots, electricians, painters and debris trucks all become scarce. Having drawings approved and material ordered before you collect the keys is what keeps the project at ten weeks."),
        ("Should I check the flat for damp before starting?",
         "Yes, especially in the riverside towers. Seepage at external walls needs resolving by the builder first, because once a wardrobe stands against an affected wall it becomes your problem rather than theirs."),
        ("How long does a full 3 BHK take in Mundhwa?",
         "Ten to twelve weeks from approved drawings. The variable is rarely the work itself; it is how much was arranged before possession."),
    ],
))

# ---------------------------------------------------------- HADAPSAR
PAGES.append(dict(
    path="/areas/hadapsar",
    slug="hadapsar",
    landing=True,
    area_name="Hadapsar",
    hero_image="/assets/opt/c06.jpg",
    hero_subtitle="Three different Hadapsars in one name — townships, mid-period societies and the old core — and township bye-laws that decide what a design can do.",
    title="Best Interior Designers in Hadapsar, Pune | Twin Space Studio",
    description="Interior designers in Hadapsar, Pune. Turnkey 2 BHK and 3 BHK interiors for townships and older societies, in 10-12 weeks with a line-item quote.",
    h1="Best Interior Designers in Hadapsar, Pune",
    service="Hadapsar, Pune",
    og_image="/assets/areas/interior-designers-kondhwa-pune-dining-slatted-ceiling.jpg",
    crumbs=CRUMBS("Hadapsar", "hadapsar"),
    body=gallery(["b04", "c06", "b08"], NOTE) + """
<p>Hadapsar covers more ground and more kinds of housing than almost any other name
on this list. It runs from old Hadapsar village and the Solapur Road corridor through
the large planned townships to the Amanora and Magarpatta edges, and a fit-out in one
part has very little in common with a fit-out in another. This page separates them.</p>

<h2>The three Hadapsars</h2>
<p><strong>The townships</strong> — Amanora and the developments around it — are
planned, walled and professionally managed. Flats are uniform, builder specification
is consistent, and the fit-out process is bureaucratic but predictable: registration
with the facility management company, deposit, worker records, defined hours, booked
lifts. This is the easiest part of Hadapsar to hold a fixed programme in.</p>
<p><strong>The mid-period societies</strong> along Solapur Road and toward Manjri are
2000s and early-2010s stock, mostly mid-rise, now on their first round of proper
interiors. Access is generally workable, and the questions are the ordinary
ageing-flat ones.</p>
<p><strong>Old Hadapsar and the village side</strong> holds lower, older buildings on
narrower lanes, where vehicle access and the absence of a service lift are the real
constraints rather than anything inside the flat.</p>

<h2>What Hadapsar homes are like</h2>
<p>Across all three, the dominant unit is a 2 or 3 BHK between roughly 650 and 1,200
square feet of carpet area, with larger units in the township premium segments.
Owners are largely people working in Magarpatta, Kharadi and the Hadapsar industrial
belt, with a broad income spread that is wider than in west Pune — which is why
Hadapsar budgets vary more than anywhere else we work.</p>

<h2>Township fit-out rules</h2>
<p>The walled townships run the tightest fit-out processes in Pune, and it is worth
knowing before you start. Contractor registration with the facility management
company is mandatory and takes days rather than hours. Worker identity records are
checked at the gate rather than filed and forgotten. Working hours are enforced, debris
removal is restricted to defined days, and material movement often has a window as
narrow as three hours.</p>
<p>Some townships also restrict what can be changed at all — external glazing,
balcony enclosure and anything affecting the facade are commonly prohibited outright,
regardless of what a contractor may tell you. We check the bye-laws before drawing
rather than after.</p>
""" + gallery(["b03", "c07", "b06"], None) + """
<h2>Budget range, honestly</h2>
<p>Hadapsar is the area where we most often quote two genuinely different scopes for
the same flat size, because the spread of what people want to spend here is wider
than anywhere else we work.</p>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh
at our standard specification. Below that, a considered, honest scope at
&#8377;8&ndash;11 lakh for a 2 BHK is achievable — it means fewer built-in elements,
false ceiling limited to the living room, simpler shutter materials and no
decorative panelling, while keeping kitchen internals, electrical work and wardrobe
carcass quality intact.</p>
<p>What we will not do is quote the lower number and deliver it by thinning the parts
you cannot see. If the budget is &#8377;9 lakh, we would rather show you a smaller
scope built properly than a full scope built badly, and say clearly which lines have
been left out so you can add them later.</p>

<h2>What Hadapsar briefs usually include</h2>
<p>A full kitchen rebuild, near-universally. Storage sized for a family that has
often moved from a smaller flat nearby. And, in the townships specifically, a living
room that works for entertaining, because township social life happens in flats more
than it does in west Pune.</p>
<p>Pooja spaces are requested more consistently in Hadapsar than in the newer western
areas, and are worth planning properly rather than fitting into a leftover corner —
given a wall, the right light and a door that closes, it stops being a compromise.</p>

<h2>Working with us in Hadapsar</h2>
<p>Hadapsar is around fifty minutes from our Mahalunge studio. We keep a supervisor on
site through the working day and schedule fewer, longer founder visits. Both founders
stay on the project from first sketch to snag list.</p>
<p>We also work in <a href="/areas/magarpatta-city">Magarpatta City</a>,
<a href="/areas/kondhwa">Kondhwa</a>, <a href="/areas/mundhwa">Mundhwa</a>,
<a href="/areas/kharadi">Kharadi</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/2-bhk-interior-design">2 BHK interior design</a> and
<a href="/guides/interior-design-cost-pune">what a full interior costs in Pune</a>.</p>

<p>To talk through a home in Hadapsar, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Hadapsar?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh at our standard specification. A considered lower scope at &#8377;8&ndash;11 lakh for a 2 BHK is achievable with fewer built-ins and simpler materials, while keeping kitchen internals, electrical work and carcass quality intact."),
        ("What are the township fit-out rules like?",
         "The tightest in Pune. Contractor registration with the facility management company takes days, worker identity is checked at the gate, working hours are enforced, debris removal is restricted to set days and material movement can have a three-hour window."),
        ("Can I enclose a balcony in an Amanora-type township?",
         "Usually not. Balcony enclosure, external glazing and anything affecting the facade are commonly prohibited outright by the bye-laws. We check them before drawing rather than after."),
        ("Will you build to a lower budget?",
         "Yes, with a smaller scope built properly rather than a full scope built badly. We state clearly which lines have been left out so you can add them later, and we do not thin the parts you cannot see."),
        ("How long does a full home interior take in Hadapsar?",
         "Ten to twelve weeks from approved drawings. Township registration adds a few days at the start, which is why we begin that paperwork before drawings are finalised."),
    ],
))

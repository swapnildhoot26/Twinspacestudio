# -*- coding: utf-8 -*-
"""Bavdhan, Pashan, Erandwane, Tathawade, Magarpatta City."""

from pagegen import gallery
from content_areas_a import CRUMBS
from content_areas_c import NOTE

PAGES = []

# ---------------------------------------------------------------- BAVDHAN
PAGES.append(dict(
    path="/areas/bavdhan",
    slug="bavdhan",
    landing=True,
    area_name="Bavdhan",
    hero_image="/assets/opt/a05.jpg",
    hero_subtitle="Larger flats on the hillside toward NDA Road, steep approaches that complicate delivery, and the risk of a big room that feels unfurnished rather than generous.",
    title="Best Interior Designers in Bavdhan, Pune | Twin Space Studio",
    description="Interior designers in Bavdhan, Pune. Turnkey 2 BHK, 3 BHK and larger interiors in 10-12 weeks, with a transparent line-item quote before work begins.",
    h1="Best Interior Designers in Bavdhan, Pune",
    service="Bavdhan, Pune",
    og_image="/assets/opt/a01.jpg",
    crumbs=CRUMBS("Bavdhan", "bavdhan"),
    body=gallery(["a01", "e04", "a05"], NOTE) + """
<p>Bavdhan sits on the hillside between Chandani Chowk and the NDA road, and it
attracts a particular kind of buyer: people who wanted more space and a green
outlook and were willing to accept a longer drive for it. The flats are generally
larger than the west Pune average and the sites are more awkward. This page covers
both sides of that trade.</p>

<h2>What Bavdhan homes are like</h2>
<p>The stock spans roughly twenty years, from early-2000s low-rise societies through
a large mid-period layer to newer developments on the higher ground toward NDA road
and the Bavdhan Khurd side. Flats tend toward 2 and 3 BHK with generous carpet areas,
frequently 900 to 1,400 square feet, and there is a meaningful supply of larger
units, duplexes and row houses that is rare at Bavdhan's price point.</p>
<p>Owners are largely families who prioritised space over commute, along with defence
and academic households, and a growing share of people working in Hinjawadi via the
Chandani Chowk route. Many are second-time buyers who know what they want and have
lived with what they did not.</p>

<h2>The hillside, and what it costs you</h2>
<p>Bavdhan's topography is the reason people buy here and the thing that complicates
building. Several developments sit up steep approach roads, some of them narrow and
awkward for a full-size delivery vehicle, and a few are still unmade in stretches.</p>
<p>The practical consequences belong in a quote rather than a conversation in week
three. Material sometimes transfers to a smaller vehicle for the last stretch.
Monsoon makes unmade approaches worse, and the monsoon here is heavier and longer
than in central Pune because of the hills. And the local trade network is thinner
than in Baner or Kothrud, so a forgotten item is a longer trip.</p>
<p>We check access on the first site visit, price the transfer honestly, stock
consumables on site rather than relying on nearby shops, and consolidate deliveries
into fewer, larger loads.</p>

<h2>Designing for a larger flat with a view</h2>
<p>Two things follow from Bavdhan's typical flat.</p>
<p>First, the extra area is usually in the living room and the bedrooms rather than
in an extra room, which means the risk is a large room that feels unfurnished rather
than a small one that feels cramped. The answer is zoning: a seating group that does
not hug the walls, a defined dining zone, and a reading or work corner that gives the
far end of the room a purpose.</p>
<p>Second, the outlook is genuinely worth designing around and regularly wasted.
Keep the window wall clear of tall joinery. Put seating where the view is rather than
where the television is convenient. Choose curtains that stack off the glass. And
layer the lighting on separate circuits, because a hillside outlook is at its best in
the evening and a single bright ceiling fixture turns the window into a black
mirror.</p>
""" + gallery(["a08", "e10", "a04"], None) + """
<h2>Older Bavdhan societies</h2>
<p>The early-2000s stock asks the familiar ageing-flat questions: electrical loads
sized before universal air conditioning, plumbing that is not always where the drawing
claims, bathroom waterproofing at the end of its life, and ceiling height already
reduced once by a previous false ceiling. Some of the lower buildings have no service
lift, so sheet material is carried or cut down and assembled in the flat.</p>
<p>Against that, these flats frequently have good bones — solid doors, sound flooring,
and room proportions that a modern builder would not give you at the same price. We
survey before quoting, and we say when something is worth keeping rather than
selling a strip-out.</p>

<h2>What a Bavdhan interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh. Bavdhan projects often sit at the upper end or slightly above, not because of
specification but because the flats are larger — more wardrobe runs, more ceiling
area, more electrical points and more painting.</p>
<p>Row houses and duplexes are quoted on scope. Two Bavdhan-specific lines we state
separately: access and material transfer where the approach requires it, and, in the
older societies, demolition and rewiring rather than an absorbed round figure.</p>

<h2>Working with us in Bavdhan</h2>
<p>Bavdhan is about twenty minutes from our Mahalunge studio, so a site decision does
not wait a week. Both founders stay on the project through execution, and carpentry
is built in your flat rather than shipped in as flat-pack.</p>
<p>We also work in <a href="/areas/kothrud">Kothrud</a>,
<a href="/areas/pashan">Pashan</a>, <a href="/areas/sus">Sus</a>,
<a href="/areas/baner">Baner</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/3-bhk-interior-design">3 BHK interior design</a> and
<a href="/services/false-ceilings-lighting">false ceilings and lighting</a>.</p>

<p>To talk through a home in Bavdhan, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Bavdhan?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh, often at the upper end because Bavdhan flats are larger. Row houses and duplexes are quoted on scope."),
        ("Do the hillside approach roads cause problems?",
         "They can. Some developments sit up steep or narrow approaches and a few stretches are unmade, which worsens in monsoon. Material sometimes transfers to a smaller vehicle for the last stretch, and we price that on the first visit rather than raising it later."),
        ("How do you design a large living room so it does not feel empty?",
         "By zoning it rather than filling it. A seating group that does not hug the walls, a defined dining zone, and a reading or work corner that gives the far end of the room a purpose."),
        ("How do you make the most of the view?",
         "Keep the window wall clear of tall joinery, place seating where the outlook is, use curtains that stack off the glass, and layer the lighting on separate circuits so the window does not become a black mirror after dark."),
        ("Are older Bavdhan flats worth renovating rather than stripping out?",
         "Frequently yes. Many have solid doors, sound flooring and room proportions a modern builder would not give you at the same price. We survey before quoting and say when something is worth keeping."),
    ],
))

# ---------------------------------------------------------------- PASHAN
PAGES.append(dict(
    path="/areas/pashan",
    slug="pashan",
    landing=True,
    area_name="Pashan",
    hero_image="/assets/opt/a09.jpg",
    hero_subtitle="Academic and research households near the university belt. Full-height library walls, studies that are actually studies, and finishes that stay quiet.",
    title="Best Interior Designers in Pashan, Pune | Twin Space Studio",
    description="Interior designers in Pashan, Pune. Renovations and turnkey interiors for established societies and newer towers, with a transparent line-item quote.",
    h1="Best Interior Designers in Pashan, Pune",
    service="Pashan, Pune",
    og_image="/assets/opt/e02.jpg",
    crumbs=CRUMBS("Pashan", "pashan"),
    body=gallery(["e02", "a09", "e06"], NOTE) + """
<p>Pashan is quieter and older than the areas that surround it. Between Pashan Lake,
the research institutions and the Sus Road side, it has held a settled, largely
academic and professional population for decades, and the housing reflects a
neighbourhood that grew steadily rather than in a boom. This page covers what that
means for a fit-out.</p>

<h2>What Pashan homes are like</h2>
<p>The stock is genuinely mixed. Older low-rise societies from the 1990s and 2000s
around Pashan-Sus Road and toward the lake. A layer of independent houses and
bungalows, some of them institutional or long-held family property. Mid-period
apartment buildings along the main roads. And newer towers on the Baner and Sus
edges, which behave like Baner rather than like Pashan.</p>
<p>Residents include a high concentration of scientists, academics and research
staff linked to the institutions nearby, along with defence households and
long-settled Pune families. It is one of the few areas where we regularly design
around a serious home library.</p>

<h2>Briefs that are quieter than most</h2>
<p>Pashan briefs tend to be restrained, and the requests that come up here are
different from the ones in Baner or Kharadi.</p>
<p>Books, first. A genuine library wall — not a decorative shelf with three
ornaments on it — needs depth of at least 250mm, adjustable shelving, and structural
support that a plasterboard partition will not give. It also needs light that does
not fade spines, which means keeping it off the direct-sun wall or accepting UV
filtering on the glazing.</p>
<p>Second, a study that is a real room rather than a corner. Pashan has a higher
proportion of people who work at home in a sustained, concentrated way than anywhere
else we build, and the specification follows: a door that closes, a solid-core one at
that, a desk sized for paper as well as a screen, and lighting that is even rather
than dramatic.</p>
<p>Third, restraint in the finish. We are asked for feature walls less often here
than anywhere in Pune, and asked for good joinery and good light more often. That is
a pleasant brief to work to and it changes where the budget goes.</p>
""" + gallery(["a03", "e08", "a07"], None) + """
<h2>Older societies and independent houses</h2>
<p>In the 1990s and 2000s societies the questions are the ordinary ageing-flat ones:
electrical loads, plumbing runs, bathroom waterproofing, and ceiling height already
reduced once. Several buildings are four to six floors with a single passenger lift
and no service lift, so sheet material is carried up the stairwell or cut down and
assembled in the flat.</p>
<p>Where the property is an independent house, the scope widens: terrace and roof
waterproofing, external joinery, and sometimes structural repair. We take the
interior scope and coordinate with a structural consultant where the building needs
one, rather than pretending an interior contractor carries that judgement.</p>
<p>Access on the interior lanes is the other recurring constraint. Several are narrow
and heavily parked, and a full-size vehicle often cannot reach the building. We check
it on the first visit and price it.</p>

<h2>What a Pashan interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh. Renovation in the older societies adds a demolition and debris line, typically
&#8377;70,000 to &#8377;1.3 lakh on a full 3 BHK strip-out, plus rewiring where the
existing load is inadequate. Independent houses are quoted entirely on scope.</p>
<p>A library wall built properly — full-height, adjustable, with real load capacity —
typically runs &#8377;90,000 to &#8377;2.2 lakh depending on length and material. It
is the line we are most often asked about here and the one people most often
underestimate.</p>

<h2>Working with us in Pashan</h2>
<p>Pashan is about fifteen minutes from our Mahalunge studio. On renovation work that
proximity matters most in the first fortnight, when walls are open and the decisions
that move a budget get made. Both founders stay on the project throughout.</p>
<p>We also work in <a href="/areas/baner">Baner</a>,
<a href="/areas/sus">Sus</a>, <a href="/areas/aundh">Aundh</a>,
<a href="/areas/bavdhan">Bavdhan</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/wardrobes-storage">wardrobes and storage</a> and
<a href="/guides/renovation-vs-new-flat">renovating an older flat</a>.</p>

<p>To talk through a home in Pashan, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Pashan?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh. Renovation in older societies adds &#8377;70,000 to &#8377;1.3 lakh for demolition and debris on a 3 BHK strip-out, plus rewiring where the load is inadequate."),
        ("What does a proper library wall cost?",
         "Typically &#8377;90,000 to &#8377;2.2 lakh depending on length and material. A real library needs at least 250mm depth, adjustable shelving and structural support a plasterboard partition will not give, which is why it costs more than a decorative shelf."),
        ("Do you work on independent houses in Pashan?",
         "Yes, for the interior scope, and we coordinate with a structural consultant where the building needs one. Terrace waterproofing and external joinery are quoted separately from interior lines."),
        ("Can a delivery vehicle reach buildings in the interior lanes?",
         "Often not. Several lanes are narrow and heavily parked. Material transfers to a smaller vehicle or is carried the last stretch, and we check and price that on the first site visit."),
        ("How do you plan a study that is actually usable?",
         "A door that closes — solid-core rather than the builder's hollow flush door — a desk sized for paper as well as a screen, even lighting rather than dramatic lighting, and a power point where the desk actually goes."),
    ],
))

# ---------------------------------------------------------------- ERANDWANE
PAGES.append(dict(
    path="/areas/erandwane",
    slug="erandwane",
    landing=True,
    area_name="Erandwane",
    hero_image="/assets/opt/d01.jpg",
    hero_subtitle="Core old Pune, where access is the defining constraint and most renovations happen with the family still in residence. We plan both before quoting.",
    title="Best Interior Designers in Erandwane, Pune | Twin Space Studio",
    description="Interior designers in Erandwane, Pune. Renovations and redevelopment fit-outs near Law College Road, with a transparent line-item quote before work begins.",
    h1="Best Interior Designers in Erandwane, Pune",
    service="Erandwane, Pune",
    og_image="/assets/areas/interior-designers-kothrud-pune-living-room.jpg",
    crumbs=CRUMBS("Erandwane", "erandwane"),
    body=gallery(["a02", "d01", "a06"], NOTE) + """
<p>Erandwane is core old Pune — Law College Road, Karve Road, the lanes around
Mehendale Garage and Nal Stop. Plots are small, buildings are close together, and
almost everything is either a decades-old society or a redevelopment tower built on
the footprint of one. Both are demanding in ways a new suburb is not. This page
covers them.</p>

<h2>What Erandwane homes are like</h2>
<p>The older stock is 1980s and 1990s low and mid-rise, on compact plots with limited
setbacks and minimal parking. Flats are conventionally planned, often with good
proportions and original teak joinery, and frequently occupied by the same family
since they were built.</p>
<p>The redevelopment layer is newer, taller and denser: the same plot rebuilt with
more floors, better lifts and modern services, but usually with tight site access
because the plot boundary has not moved. Owners are largely long-settled Pune
families, professionals, and increasingly the next generation taking over a family
flat.</p>

<h2>Access is the defining constraint</h2>
<p>More than anywhere else we work, Erandwane projects are shaped by getting things
into the building.</p>
<p>The lanes are narrow, parked on both sides, and several are one-way. A full-size
delivery vehicle frequently cannot reach the building at all, which means material
transfers to a tempo or a handcart for the last stretch. Many older buildings have a
single passenger lift too small for sheet material, so ply is carried up the
stairwell or cut down and assembled in the flat. Some have no lift above the fourth
floor at all.</p>
<p>None of this is unusual and none of it is a reason to avoid the area. It is a
reason to have it in the quote. This is the single most common line missing from a
cheaper Erandwane estimate, and the one most likely to become a conversation in week
three.</p>

<h2>Renovation with the family in residence</h2>
<p>A large share of our Erandwane work happens with the family still living in the
flat, often because moving out of a home held for thirty years is not a simple
proposition.</p>
<p>We phase it room by room behind a sealed dust barrier, keep one bedroom and one
bathroom usable at all times, and group all wet work into a single block so the water
goes off once rather than repeatedly. The kitchen goes last, after a temporary
arrangement is set up. It adds roughly two weeks to a ten-to-twelve week programme,
and we say so at quoting stage rather than in week eight.</p>
<p>Neighbours matter more here too. The buildings are close, the shared staircase is
everyone's route home, and noise carries. We agree working hours with the society in
writing, protect the common areas, and clear debris daily rather than weekly.</p>
""" + gallery(["a07", "d05", "a08"], None) + """
<h2>What to keep in an older Erandwane flat</h2>
<p>These flats often have things worth protecting. Solid teak doors and window
frames, which are better refinished than replaced. Flooring — sometimes mosaic,
sometimes good stone — that needs polishing rather than removal. Ceiling height that
a previous false ceiling has eaten and that can often be partly recovered.</p>
<p>We say when something is worth keeping even though a full strip-out would be the
larger project for us. Keeping sound flooring and doors regularly releases enough
budget to do the kitchen properly, which changes daily life far more.</p>

<h2>What an Erandwane interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh. Renovation adds demolition and debris removal, typically &#8377;70,000 to
&#8377;1.4 lakh on a full 3 BHK strip-out, and rewiring is usually a real line rather
than a nominal one in a 1980s building.</p>
<p>Access and material handling is stated separately in our Erandwane quotes. It is
a modest figure and an honest one, and it is why our first number sometimes looks
higher than an estimate that quietly assumed a truck could park at the gate.</p>

<h2>Working with us in Erandwane</h2>
<p>Erandwane is around thirty minutes from our Mahalunge studio. On renovation work
we front-load the survey — including opening a small section of the kitchen wall —
and keep a supervisor on site through the opening-up phase. Both founders stay on the
project from first sketch to snag list.</p>
<p>We also work in <a href="/areas/kothrud">Kothrud</a>,
<a href="/areas/bavdhan">Bavdhan</a>, <a href="/areas/pashan">Pashan</a>,
<a href="/areas/aundh">Aundh</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/modular-kitchens">modular kitchens</a> and
<a href="/guides/living-in-during-renovation">living in the flat during a renovation</a>.</p>

<p>To talk through a home in Erandwane, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Erandwane?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh. Renovation adds &#8377;70,000 to &#8377;1.4 lakh for demolition and debris on a 3 BHK strip-out, and rewiring is usually a real line in a 1980s building."),
        ("Why do Erandwane quotes include a material handling line?",
         "Because the lanes are narrow and heavily parked, a full-size vehicle often cannot reach the building, and many lifts are too small for sheet material. Transferring or carrying material is a real cost, and we state it rather than leaving it to surface in week three."),
        ("Can we stay in the flat during the work?",
         "Yes, and many Erandwane families do. We phase it room by room behind a dust barrier, keep one bedroom and one bathroom usable, group the wet work into a single block and leave the kitchen until last. It adds about two weeks."),
        ("What is worth keeping in an old Erandwane flat?",
         "Solid teak doors and window frames, and flooring in good condition. Refinishing rather than replacing both usually releases enough budget to do the kitchen properly, which matters far more day to day."),
        ("How do you manage noise and neighbours?",
         "We agree working hours with the society in writing, protect the shared staircase, and clear debris daily rather than weekly. In buildings this close together it matters more than the schedule does."),
    ],
))

# ---------------------------------------------------------------- TATHAWADE
PAGES.append(dict(
    path="/areas/tathawade",
    slug="tathawade",
    landing=True,
    area_name="Tathawade",
    hero_image="/assets/opt/f01.jpg",
    hero_subtitle="Compact PCMC two-bedroom flats from bare handover, where storage planning decides whether the home works — and PCMC society rules decide the programme.",
    title="Best Interior Designers in Tathawade, Pune | Twin Space Studio",
    description="Interior designers in Tathawade, PCMC. Complete 2 BHK and 3 BHK interiors from bare handover in 10-12 weeks, with a transparent line-item quote.",
    h1="Best Interior Designers in Tathawade, Pune",
    service="Tathawade, Pimpri-Chinchwad, Pune",
    og_image="/assets/areas/interior-designers-punawale-pune-master-bedroom.jpg",
    crumbs=CRUMBS("Tathawade", "tathawade"),
    body=gallery(["f02", "d04", "f01"], NOTE) + """
<p>Tathawade sits between Wakad, Punawale and the Mumbai-Bangalore highway, and it
has filled in fast. Most of the housing is recent, most of the buyers are furnishing
a first or second home, and the great majority of flats hand over bare. This page
covers what a complete fit-out here involves and what it costs.</p>

<h2>What Tathawade homes are like</h2>
<p>Almost all post-2015 construction, in mid and high-rise towers inside gated
developments, concentrated along the highway side and toward the Punawale and Ravet
boundaries. The dominant unit is a 2 BHK between roughly 600 and 850 square feet of
carpet area, with a solid supply of compact 3 BHKs.</p>
<p>Buyers are largely young families and dual-income couples working in Hinjawadi,
Wakad and the Chakan industrial belt, plus a student and rental segment linked to the
educational institutions nearby. Handover is genuinely bare: flooring, a kitchen
platform, basic electrical points, nothing else.</p>

<h2>Furnishing a first home properly</h2>
<p>Most Tathawade fit-outs have to produce a functioning household rather than an
upgrade to an existing one, and that changes how a budget should be built.</p>
<p>We split the quote into a move-in scope and a deferred scope. The move-in list is
joinery and services: kitchen, wardrobes, electrical work, lighting, and somewhere to
sit and eat. The deferred list is everything that can be added over a year without
construction — a second sofa, the balcony, the guest room furniture, the styling.</p>
<p>Splitting it that way means the flat is genuinely liveable at the end of week ten
and the rest of the budget goes on things you buy when you are ready rather than on
borrowed money.</p>

<h2>Compact-flat storage</h2>
<p>At 600 to 850 square feet, storage is planning rather than shopping. Wardrobes go
to the slab rather than stopping at a loft, which adds roughly a third more capacity
for a fraction more cost. Beds get storage below with hydraulic lifts rather than
hinged lids, because the hinged kind stops being used after a month. A full-height
utility unit beside the kitchen takes the appliances that otherwise live on the
counter. Deep window sills become seats with drawers underneath. And a shallow entry
unit, 250mm is enough, stops the foyer collecting shoes.</p>
<p>What we avoid is a wall of closed cabinetry in the living room. In a compact flat
it makes the room read smaller, and most of what goes in it belongs in a bedroom.</p>
""" + gallery(["f05", "d07", "f06"], None) + """
<h2>Letting versus living</h2>
<p>Tathawade has a real rental market, and a flat being fitted out to let is a
different brief. Robust finishes that survive tenants, a neutral palette, storage that
is generous but simple, and no delicate detail that becomes a deposit argument later.
A letting specification typically runs &#8377;8&ndash;11 lakh for a 2 BHK against
&#8377;12&ndash;16 lakh for one you will live in, and we quote them as different
scopes rather than selling the same one twice.</p>

<h2>What a Tathawade interior costs</h2>
<p>A complete 2 BHK fit-out runs &#8377;12&ndash;16 lakh, typically in the lower half
of that band because carpet areas are compact. A compact 3 BHK generally lands
between &#8377;15 lakh and &#8377;18 lakh. Every line is itemised before anything is
ordered.</p>
<p>We do not quote a rate per square foot here. On a compact flat it misleads: the
kitchen and the wardrobes cost what they cost regardless of the floor area around
them.</p>

<h2>PCMC rules and highway logistics</h2>
<p>Tathawade is under Pimpri-Chinchwad municipal jurisdiction, and the newer societies
run tight fit-out processes: registration with the facility management company, a
refundable deposit, worker identity records, working hours around 9am to 6pm, a
service-lift booking system, and debris removal on defined days.</p>
<p>Locally, many towers sit just off the Mumbai-Bangalore highway with service-road
access that congests badly at peak. We book material deliveries mid-morning rather
than early, which sounds trivial and saves real days across a project.</p>

<h2>Working with us in Tathawade</h2>
<p>Tathawade is around twenty-five minutes from our Mahalunge studio. Both founders
stay on the project through execution, and carpentry is built in your flat rather
than shipped in as flat-pack.</p>
<p>We also work in <a href="/areas/punawale">Punawale</a>,
<a href="/areas/wakad">Wakad</a>, <a href="/areas/hinjawadi">Hinjawadi</a>,
<a href="/areas/balewadi">Balewadi</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/2-bhk-interior-design">2 BHK interior design</a> and
<a href="/guides/interior-design-payment-schedule">how payments are staged</a>.</p>

<p>To talk through a home in Tathawade, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a 2 BHK interior cost in Tathawade?",
         "A complete fit-out runs &#8377;12&ndash;16 lakh, usually in the lower half of that band because carpet areas are compact. A compact 3 BHK generally lands between &#8377;15 lakh and &#8377;18 lakh."),
        ("What should I do first if this is my first home?",
         "Split the budget into a move-in scope and a deferred scope. Kitchen, wardrobes, electrical work and lighting have to exist before you move in; the second sofa, the balcony and the guest room can be added over a year without any construction."),
        ("How do I get more storage into a 650 square foot flat?",
         "Wardrobes to the slab rather than stopping at a loft, hydraulic storage beds rather than hinged ones, a full-height utility unit beside the kitchen, drawers under the window seat and a shallow entry unit. Avoid a wall of cabinetry in the living room."),
        ("Do you fit out flats for renting?",
         "Yes, as a separate scope. A letting specification typically runs &#8377;8&ndash;11 lakh for a 2 BHK against &#8377;12&ndash;16 lakh for an owner-occupied one."),
        ("How long does a full 2 BHK take in Tathawade?",
         "Ten to twelve weeks from approved drawings. Having drawings approved before you collect the keys is the single biggest thing that keeps it at ten."),
    ],
))

# ---------------------------------------------------------- MAGARPATTA CITY
PAGES.append(dict(
    path="/areas/magarpatta-city",
    slug="magarpatta-city",
    landing=True,
    area_name="Magarpatta City",
    hero_image="/assets/opt/b07.jpg",
    hero_subtitle="The strictest township rules in Pune. We confirm what the bye-laws allow before drawing, because a plan that assumes otherwise is a wasted plan.",
    title="Best Interior Designers in Magarpatta City, Pune | Twin Space Studio",
    description="Interior designers in Magarpatta City, Pune. Turnkey and renovation interiors within the township, with a transparent line-item quote before work begins.",
    h1="Best Interior Designers in Magarpatta City, Pune",
    service="Magarpatta City, Pune",
    og_image="/assets/opt/b05.jpg",
    crumbs=CRUMBS("Magarpatta City", "magarpatta-city"),
    body=gallery(["b05", "c02", "b07"], NOTE) + """
<p>Magarpatta City is a walled, planned township, and that single fact governs
almost everything about a fit-out inside it. The buildings are uniform, the
management is professional, and the rules are the strictest we work under anywhere
in Pune. This page explains what that means before you start.</p>

<h2>What Magarpatta homes are like</h2>
<p>The township was built out largely between 2000 and 2015 in distinct residential
clusters, and the housing is notably consistent: mid and high-rise apartment blocks
with standardised builder specification, 2 and 3 BHK flats generally between 700 and
1,300 square feet of carpet area, and a smaller premium and row-house segment.</p>
<p>Because the stock repeats, we usually know the layout before we arrive. That
makes Magarpatta quotes among the most predictable we produce — not cheaper, but
with a small gap between the first figure and the last one.</p>
<p>Residents are heavily weighted toward people working inside the township's own
commercial district and the wider Hadapsar and Kharadi IT belt, and many have lived
here long enough that the work is second-round renovation rather than first fit-out.</p>

<h2>Township rules, in detail</h2>
<p>This is the part worth reading before anything else.</p>
<p>Contractors generally must be registered with the township's facility management
before any gate pass is issued, and that process takes days rather than hours. Worker
identity records are checked at the gate rather than filed and forgotten. Working
hours are enforced, typically 9am to 6pm with no work on Sundays or public holidays.
Material movement is restricted to defined windows, and debris removal to defined
days. A refundable deposit and a written scope with a completion date are standard.</p>
<p>Structural and external changes are commonly prohibited outright: balcony
enclosure, external glazing changes, anything affecting the facade, and in many
clusters any alteration to a common wall. We check the bye-laws before drawing rather
than after, because a design that assumes a balcony can be enclosed is a wasted
drawing set here.</p>
<p>We start the registration paperwork before drawings are finalised. On a Magarpatta
project that alone usually saves a week.</p>
""" + gallery(["b08", "c03", "b06"], None) + """
<h2>Second-round renovation in a settled township</h2>
<p>Much of our Magarpatta work is a flat that was finished twelve or fifteen years
ago and now needs bringing up to date. The judgement calls are consistent.</p>
<p>Kitchens almost always need doing completely — the original modular units are at
the end of their service life even where the platform is sound. Bathrooms usually do
too, because waterproofing has a lifespan regardless of how the tiles look. Flooring
is frequently in good condition and worth keeping. A false ceiling dropped in 2010
can often be partly removed to recover height.</p>
<p>Around half these clients stay in the flat through the work. We phase it room by
room behind a sealed dust barrier, keep one bedroom and one bathroom usable, and
group the wet work into a single block. It adds roughly two weeks, and in a township
with fixed working hours that matters more than usual, because lost days cannot be
recovered by working late.</p>

<h2>What a Magarpatta interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh, itemised before anything is ordered. Second-round renovation adds demolition,
debris and full bathroom replacement, typically &#8377;1.2 to &#8377;3 lakh on a
3 BHK, stated as a separate section above the interior lines.</p>
<p>One township-specific note: because working hours are fixed and cannot be extended,
a Magarpatta project has less schedule flexibility than the same job elsewhere.
That does not change the price, but it does mean the programme is genuinely
ten to twelve weeks rather than ten to twelve weeks with evenings available.</p>

<h2>Working with us in Magarpatta City</h2>
<p>Magarpatta is around fifty minutes from our Mahalunge studio. We keep a supervisor
on site through the working day and schedule fewer, longer founder visits. Both
founders stay on the project from first sketch to snag list.</p>
<p>We also work in <a href="/areas/hadapsar">Hadapsar</a>,
<a href="/areas/kondhwa">Kondhwa</a>, <a href="/areas/mundhwa">Mundhwa</a>,
<a href="/areas/kharadi">Kharadi</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. See also
<a href="/services/modular-kitchens">modular kitchens</a> and
<a href="/guides/society-rules-interior-work-pune">society rules for interior work</a>.</p>

<p>To talk through a home in Magarpatta City, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Magarpatta City?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh. Second-round renovation adds demolition, debris and full bathroom replacement, typically &#8377;1.2 to &#8377;3 lakh on a 3 BHK."),
        ("What are the township's fit-out rules?",
         "Contractor registration with facility management before any gate pass, worker identity checked at the gate, enforced 9am to 6pm hours with no Sunday work, restricted material-movement windows, debris removal on defined days, a refundable deposit and a written scope with a completion date."),
        ("Can I enclose a balcony or change external glazing?",
         "Almost always no. Balcony enclosure, external glazing changes and anything affecting the facade are commonly prohibited, as is altering a common wall in many clusters. We check the bye-laws before drawing rather than after."),
        ("Are Magarpatta quotes predictable?",
         "More than most. The stock repeats across the township, so we usually know the layout before we arrive. That keeps the gap between the first figure and the final one small."),
        ("Does the fixed working-hours rule affect the timeline?",
         "It removes flexibility rather than adding time. The programme is genuinely ten to twelve weeks with no option to recover a lost day by working late, which is why we start the registration paperwork before drawings are finalised."),
    ],
))

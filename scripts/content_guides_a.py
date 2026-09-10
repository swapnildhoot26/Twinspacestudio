# -*- coding: utf-8 -*-
"""Cost guides: master cost page, 2 BHK, 3 BHK, kitchens, wardrobes."""

from pagegen import gallery

GC = lambda name, slug: [("Home", "/"), ("Guides", "/guides"), (name, f"/guides/{slug}")]

DISCLAIMER = """<p class="guide-note">The figures on this page are the ranges we
actually quote in Pune and PCMC in 2026. They are indicative, not a price list:
every project is measured on site and quoted line by line before anything is
ordered. Where a number depends on something specific to your flat, we say so.</p>"""

PAGES = []

# ------------------------------------------------- MASTER COST GUIDE
PAGES.append(dict(
    path="/guides/interior-design-cost-pune",
    title="Interior Design Cost in Pune (2026) | Twin Space Studio",
    description="What a full home interior actually costs in Pune in 2026 — 2 BHK &#8377;12-16 lakh, 3 BHK &#8377;16-21 lakh — and where every rupee of that budget goes.",
    h1="What Interior Design Costs in Pune",
    article=True,
    og_image="/assets/areas/interior-designers-baner-pune-living-room-swing.jpg",
    crumbs=GC("Interior design cost in Pune", "interior-design-cost-pune"),
    body=DISCLAIMER + gallery(["e09", "a05", "c07"]) + """
<p>Most interior design websites in Pune will not put a number on a page. We will,
because the first question everybody actually has is what this costs, and because a
studio that cannot answer it in public is unlikely to answer it clearly in private.</p>

<h2>The short answer</h2>
<p>A full 2 BHK interior in Pune runs <strong>&#8377;12&ndash;16 lakh</strong>.
A full 3 BHK runs <strong>&#8377;16&ndash;21 lakh</strong>. A 4 BHK or duplex is
quoted on scope and typically lands between <strong>&#8377;22 lakh and
&#8377;35 lakh</strong>.</p>
<p>"Full" means everything: modular kitchen, all wardrobes and bedroom joinery, the
living room television unit and storage, false ceilings and lighting, electrical
work, painting, and site supervision through to handover. It does not include loose
furniture beyond what is specified, or appliances.</p>

<h2>Where the money goes</h2>
<p>On a typical Pune 3 BHK, the split looks like this:</p>
<ul>
<li><strong>Joinery — roughly 50%.</strong> Kitchen, wardrobes, television unit,
entry storage, study and any bespoke furniture. The single largest line by a wide
margin.</li>
<li><strong>False ceilings and lighting — roughly 18%.</strong> Higher in new towers
that have the height for it, lower in older flats where the height is worth
protecting.</li>
<li><strong>Loose furniture, soft furnishing and styling — roughly 16%.</strong></li>
<li><strong>Electrical, plumbing, painting and hardware — roughly 12%.</strong></li>
<li><strong>Supervision and site management — roughly 4%.</strong></li>
</ul>
<p>That distribution is worth knowing because it tells you where a cheaper quote has
usually been cheapened. Two quotes can be twenty per cent apart on an identical
drawing set, and the difference sits almost entirely in the joinery: carcass
material, hinge and channel brands, edge banding, and whether the back of a wardrobe
is a proper panel or a sheet of hardboard.</p>

<h2>What moves the number up</h2>
<p><strong>Bare handover.</strong> A new flat with no existing kitchen, wardrobe or
ceiling means every line is new. New-possession projects in Kharadi, Mahalunge and
Mundhwa sit in the upper half of the bands for this reason alone.</p>
<p><strong>Floor area.</strong> More rooms means more wardrobe runs, more ceiling,
more electrical points and more site days. This is why a Kondhwa 4 BHK costs more in
total than a Baner 3 BHK while looking cheaper per square foot.</p>
<p><strong>Stone and specialist finishes.</strong> Natural stone, veneer and imported
hardware move a quote faster than anything else.</p>
<p><strong>Balcony and outdoor work.</strong> Decking, shade and lighting typically
add &#8377;70,000 to &#8377;1.6 lakh.</p>

<h2>What moves it down</h2>
<p><strong>Existing work worth keeping.</strong> Sound flooring and solid teak doors
in an older Kothrud, Aundh or Erandwane flat remove two significant lines. We say
when something is worth keeping, even though a full strip-out would be a larger
project for us.</p>
<p><strong>Deferring what can be added later.</strong> False ceilings beyond the
living room, decorative panelling, and built-ins in a room you will not use daily
can all wait without any construction later.</p>
<p><strong>Fewer, better decisions.</strong> In a compact flat, spending properly on
a small number of things beats covering every surface — and costs less.</p>

<h2>What renovation adds that new build does not</h2>
<p>Renovating an older flat carries lines a bare handover never sees. Demolition and
debris removal runs &#8377;60,000 to &#8377;1.4 lakh depending on the size of the
strip-out. Rewiring is frequently a real line rather than a nominal one, because a
1990s distribution board will not carry a modern kitchen. Bathroom waterproofing is
usually at the end of its life whatever the tiles look like.</p>
<p>Access can be a genuine cost too. In Erandwane, Koregaon Park, old Aundh and
parts of Pashan, a full-size delivery vehicle often cannot reach the building and
many lifts will not take sheet material. We state that as its own line rather than
absorbing it into a round figure — it is the item most often missing from a cheaper
estimate.</p>

<h2>Why we do not quote per square foot</h2>
<p>A rate per square foot is the most commonly advertised number in Indian interiors
and the least useful one. A kitchen and a set of wardrobes cost what they cost
regardless of how much floor surrounds them, so on a compact flat the rate looks
high and on a large one it looks low, while both quotes may be identical in scope.</p>
<p>The comparison that actually works is line by line: same carcass material, same
hardware brand, same shutter finish, same number of running feet. That is how our
quotes are written, and it is what makes two of them comparable.</p>

<h2>How payment is staged</h2>
<p>Payment runs against milestones rather than dates, so you are paying for work
that exists. The stages and the logic behind them are set out in our guide to
<a href="/guides/interior-design-payment-schedule">how payments are staged</a>.</p>
<p>The figure quoted on day one is the figure at handover. If scope changes because
you ask for something additional, that is quoted and approved before it is built —
never added to a final bill.</p>

<h2>Component costs</h2>
<p>For the individual elements, we have separate guides:
<a href="/guides/2-bhk-interior-cost-pune">what a 2 BHK costs</a>,
<a href="/guides/3-bhk-interior-cost-pune">what a 3 BHK costs</a>,
<a href="/guides/modular-kitchen-cost-pune">modular kitchen cost</a>,
<a href="/guides/wardrobe-cost-pune">wardrobe cost</a>,
<a href="/guides/false-ceiling-cost-pune">false ceiling and lighting cost</a>, and
<a href="/guides/hidden-costs-interior-design">the costs people forget to budget for</a>.</p>

<p>To talk through a specific flat, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a full home interior cost in Pune?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh, a full 3 BHK &#8377;16&ndash;21 lakh, and a 4 BHK or duplex &#8377;22&ndash;35 lakh quoted on scope. That covers kitchen, all joinery, ceilings and lighting, electrical work, painting and supervision through to handover."),
        ("Why do two quotes for the same drawing differ by twenty per cent?",
         "Almost always in the joinery you cannot see: carcass material, hinge and channel brands, edge banding, and whether a wardrobe back is a proper panel or hardboard. The visible finish is usually similar; the box behind it is not."),
        ("Do you quote a rate per square foot?",
         "No. A kitchen and a set of wardrobes cost what they cost regardless of floor area, so the rate looks high on a compact flat and low on a large one while the scope may be identical. We quote line by line instead."),
        ("What does renovation add to the cost?",
         "Demolition and debris removal of &#8377;60,000 to &#8377;1.4 lakh, rewiring where the existing load is inadequate, and bathroom waterproofing that is usually at the end of its life. In areas with narrow lanes we also state material handling as its own line."),
        ("Can the price change after work starts?",
         "Only if you ask for something additional, and then it is quoted and approved before it is built. The figure quoted on day one is the figure at handover."),
    ],
))

# ------------------------------------------------- 2 BHK COST
PAGES.append(dict(
    path="/guides/2-bhk-interior-cost-pune",
    title="2 BHK Interior Cost in Pune (2026) | Twin Space Studio",
    description="What a full 2 BHK interior costs in Pune in 2026: &#8377;12-16 lakh, broken down room by room, with what to protect and what to defer on a tight budget.",
    h1="2 BHK Interior Cost in Pune",
    article=True,
    og_image="/assets/areas/interior-designers-punawale-pune-living-dining.jpg",
    crumbs=GC("2 BHK interior cost", "2-bhk-interior-cost-pune"),
    body=DISCLAIMER + gallery(["f01", "d02", "f03"]) + """
<p>A full 2 BHK interior in Pune runs <strong>&#8377;12&ndash;16 lakh</strong>. This
page breaks that down room by room, explains what pushes a project to either end of
the band, and sets out what we recommend protecting when the budget is tight.</p>

<h2>The breakdown</h2>
<p>On a typical 650&ndash;850 square foot 2 BHK at our standard specification:</p>
<ul>
<li><strong>Modular kitchen — &#8377;2.5 to &#8377;4 lakh.</strong> Usually the
single largest line, because it is being built new rather than modified.</li>
<li><strong>Wardrobes and bedroom joinery — &#8377;2.5 to &#8377;3.5 lakh</strong>
across both bedrooms, including storage beds and any study.</li>
<li><strong>Living and dining — &#8377;2 to &#8377;3 lakh.</strong> Television unit,
entry storage, any partition or panelling, dining seating.</li>
<li><strong>False ceilings and lighting — &#8377;1.2 to &#8377;2 lakh.</strong></li>
<li><strong>Electrical, plumbing, painting and hardware — &#8377;1.5 to
&#8377;2.2 lakh.</strong></li>
<li><strong>Soft furnishing, styling and supervision — &#8377;1 to
&#8377;1.5 lakh.</strong></li>
</ul>

<h2>What puts a 2 BHK at the top of the band</h2>
<p>Bare handover, which means every line is new. Larger carpet area, particularly
where the living room is generous. Stone or veneer finishes rather than laminate.
A balcony treated properly. And a third sleeping or working space carved out of a
2 BHK plan, which is common now and adds real joinery.</p>

<h2>What puts it at the bottom</h2>
<p>Compact carpet area, which is why Punawale, Tathawade and Wakad projects usually
sit lower. An existing kitchen or wardrobes worth keeping. False ceiling limited to
the living room. And a decision to defer the second bedroom's built-ins until the
room is actually used daily.</p>

<h2>Building a first home from nothing</h2>
<p>Most 2 BHK projects we take on in PCMC are first homes, and the budget has to
produce a functioning household rather than an upgrade. We split those quotes into
two columns.</p>
<p><strong>Move-in scope</strong> is what must exist before you can live there:
kitchen, wardrobes, electrical work, lighting, and somewhere to sit and eat.
<strong>Deferred scope</strong> is everything that can be added over a year without
construction: the second sofa, the balcony, guest room furniture, styling.</p>
<p>Done that way the flat is genuinely liveable at the end of week ten and the rest
of the budget goes on things you buy when ready rather than on borrowed money.</p>

<h2>What to protect when money is tight</h2>
<p><strong>Kitchen internals and hardware.</strong> Used three times a day, and the
most disruptive thing in the flat to redo.</p>
<p><strong>Electrical work.</strong> Points, circuits and switch positions live
behind the wall. Adding them later means chasing a finished flat.</p>
<p><strong>Wardrobe carcass quality.</strong> Shutters can be changed in ten years;
the box behind them cannot.</p>

<h2>What can wait</h2>
<p>False ceilings beyond the living room — bedrooms rarely need them, and a good fan
with considered lighting does more. Decorative panelling, which photographs well and
changes nothing about how the home works. Built-ins in a bedroom that will not be
used daily for a year or two. And loose furniture beyond the essential pieces.</p>

<h2>Storage in a compact flat</h2>
<p>Five decisions do most of the work. Wardrobes to the slab rather than stopping at
a loft, which adds roughly a third more capacity for a fraction more cost. Storage
beds with hydraulic lifts rather than hinged lids. A full-height utility unit beside
the kitchen. Drawers under the window seat where the sill is deep. And a shallow
entry unit, 250mm is enough, so the foyer stops collecting shoes.</p>
<p>What we avoid is a wall of closed cabinetry in the living room. In a compact flat
it makes the room read smaller, and most of what goes in it belongs in a bedroom.</p>

<h2>Timeline</h2>
<p>Ten to twelve weeks from approved drawings for a full 2 BHK. See
<a href="/guides/interior-design-timeline">how the weeks are actually spent</a> and
<a href="/services/2-bhk-interior-design">our 2 BHK service page</a> for scope
detail.</p>

<p>To talk through a specific 2 BHK, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a 2 BHK interior cost in Pune?",
         "&#8377;12&ndash;16 lakh for a full interior: modular kitchen, all wardrobes and bedroom joinery, living room storage, false ceilings and lighting, electrical work, painting and supervision through to handover."),
        ("What does the kitchen alone cost in a 2 BHK?",
         "&#8377;2.5 to &#8377;4 lakh at our standard specification. It is usually the largest single line because it is being built new rather than modified."),
        ("Can a 2 BHK be done for under &#8377;10 lakh?",
         "Yes, with a smaller scope built properly rather than a full scope built badly — fewer built-in elements, false ceiling limited to the living room, simpler shutter materials, no decorative panelling. We state clearly which lines are left out so you can add them later."),
        ("What should I not cut?",
         "Kitchen internals and hardware, the electrical work, and the wardrobe carcass. All three are behind the wall or in daily use, and all three are expensive or disruptive to redo."),
        ("How long does a 2 BHK take?",
         "Ten to twelve weeks from approved drawings. Getting drawings approved before you collect the keys is what keeps it at ten."),
    ],
))

# ------------------------------------------------- 3 BHK COST
PAGES.append(dict(
    path="/guides/3-bhk-interior-cost-pune",
    title="3 BHK Interior Cost in Pune (2026) | Twin Space Studio",
    description="What a full 3 BHK interior costs in Pune in 2026: &#8377;16-21 lakh, broken down room by room, with guidance on planning the third bedroom.",
    h1="3 BHK Interior Cost in Pune",
    article=True,
    og_image="/assets/opt/c02.jpg",
    crumbs=GC("3 BHK interior cost", "3-bhk-interior-cost-pune"),
    body=DISCLAIMER + gallery(["c02", "a01", "e04"]) + """
<p>A full 3 BHK interior in Pune runs <strong>&#8377;16&ndash;21 lakh</strong>. This
page breaks that down, explains what moves a project within the band, and covers the
decision that matters most in a 3 BHK: what the third bedroom is actually for.</p>

<h2>The breakdown</h2>
<p>On a typical 900&ndash;1,250 square foot 3 BHK at our standard specification:</p>
<ul>
<li><strong>Modular kitchen — &#8377;3 to &#8377;5 lakh.</strong></li>
<li><strong>Wardrobes and bedroom joinery — &#8377;4 to &#8377;5.5 lakh</strong>
across three bedrooms, including storage beds, study units and dressers.</li>
<li><strong>Living and dining — &#8377;3 to &#8377;4 lakh.</strong> Television unit,
entry storage, panelling, partition work, dining.</li>
<li><strong>False ceilings and lighting — &#8377;2 to &#8377;3.2 lakh.</strong></li>
<li><strong>Electrical, plumbing, painting and hardware — &#8377;2 to
&#8377;2.8 lakh.</strong></li>
<li><strong>Soft furnishing, styling and supervision — &#8377;1.5 to
&#8377;2.2 lakh.</strong></li>
</ul>

<h2>The third bedroom decides the project</h2>
<p>In almost every 3 BHK we design, two bedrooms are obvious and the third is the
one that determines whether the home works. Left generic it becomes a store within
eighteen months. Given a purpose at drawing stage it earns its floor area.</p>
<p>The four briefs we see most often:</p>
<ul>
<li><strong>A real study.</strong> A door that closes, solid-core rather than the
builder's hollow flush door, a desk sized for paper as well as a screen, and a wall
behind you that reads well on a call.</li>
<li><strong>A guest room that is not empty for eleven months.</strong> A sofa-cum-bed
or a wall bed, with the room used as a study or sitting room the rest of the
year.</li>
<li><strong>A room for a parent.</strong> Bed height set for easy transfers, a lower
hanging rail, a grab point detailed so it does not look clinical, and layered
lighting that can be bright without glare.</li>
<li><strong>A child's room that will change.</strong> Built with the assumption that
the desk, the bed size and the storage all need to change twice, so the joinery is
adaptable rather than fixed to one age.</li>
</ul>
<p>Deciding which of these it is before drawings are frozen is worth more than any
material choice on the page.</p>

<h2>Two people working from home</h2>
<p>In a 3 BHK this is now the normal condition rather than the exception, and it is
an acoustic problem before it is a furniture one. The second desk goes in a bedroom
so a door can close. That door should be solid-core. The room needs soft surfaces —
a rug with underlay, lined curtains, an upholstered headboard — or it will echo. And
each desk needs a power point where the desk actually goes, which has to be settled
before the electrical layout is frozen.</p>

<h2>What moves a 3 BHK within the band</h2>
<p><strong>Upward:</strong> bare handover, larger carpet area, stone and veneer
rather than laminate, a fully treated balcony, and a fourth space carved out of the
plan.</p>
<p><strong>Downward:</strong> existing flooring and doors worth keeping, false
ceiling limited to the public rooms, and deferring built-ins in a bedroom that will
not be used daily yet.</p>

<h2>Above the band</h2>
<p>4 BHK homes and duplexes are quoted on scope and typically land between
&#8377;22 lakh and &#8377;35 lakh. The driver is joinery count rather than finish
level — more rooms means more wardrobes, more ceiling, more electrical points and
more site days. Duplexes add a staircase, which is the most expensive square metre
in the house and the hardest to change later.</p>

<h2>Timeline</h2>
<p>Ten to twelve weeks from approved drawings for a full 3 BHK; thirteen to fifteen
for a duplex. See <a href="/guides/interior-design-timeline">how the weeks are
spent</a>, <a href="/services/3-bhk-interior-design">our 3 BHK service page</a>, and
<a href="/guides/interior-design-cost-pune">the full Pune cost guide</a>.</p>

<p>To talk through a specific 3 BHK, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a 3 BHK interior cost in Pune?",
         "&#8377;16&ndash;21 lakh for a full interior, covering the modular kitchen, all wardrobes and bedroom joinery, living and dining, false ceilings and lighting, electrical work, painting and supervision through to handover."),
        ("What does a 4 BHK or duplex cost?",
         "&#8377;22&ndash;35 lakh, quoted on scope. The driver is joinery count rather than finish level, and a duplex adds a staircase, which is the most expensive square metre in the house."),
        ("What should the third bedroom be?",
         "Decide before drawings are frozen. A real study, a guest room that doubles as something else for eleven months of the year, a room for a parent, or a child's room built to be adapted twice. Left generic it becomes a store within eighteen months."),
        ("How do you plan for two people working from home?",
         "Put the second desk in a bedroom so a door can close, specify a solid-core door, add soft surfaces so the room does not echo, and put a power point where the desk will actually go — decided before the electrical layout is frozen."),
        ("How long does a 3 BHK take?",
         "Ten to twelve weeks from approved drawings. A duplex runs thirteen to fifteen weeks depending on the joinery count."),
    ],
))

# ------------------------------------------------- MODULAR KITCHEN COST
PAGES.append(dict(
    path="/guides/modular-kitchen-cost-pune",
    title="Modular Kitchen Cost in Pune (2026) | Twin Space Studio",
    description="What a modular kitchen costs in Pune in 2026, what drives the price, and which parts of the specification are worth protecting when the budget is tight.",
    h1="Modular Kitchen Cost in Pune",
    article=True,
    og_image="/assets/areas/interior-designers-kothrud-pune-modular-kitchen.jpg",
    crumbs=GC("Modular kitchen cost", "modular-kitchen-cost-pune"),
    body=DISCLAIMER + gallery(["a05", "c03", "b07"]) + """
<p>The kitchen is the largest single line in most Pune interior projects and the one
where the difference between a good quote and a cheap one is least visible. This page
covers what it costs, what drives that, and what actually matters in the
specification.</p>

<h2>What it costs</h2>
<p>In our projects, a full modular kitchen runs:</p>
<ul>
<li><strong>Compact straight or L-shape (8&ndash;10 running feet)</strong> —
&#8377;2 to &#8377;3 lakh</li>
<li><strong>Standard L-shape or U-shape (12&ndash;16 running feet)</strong> —
&#8377;3 to &#8377;4.5 lakh</li>
<li><strong>Large kitchen with island or breakfast counter</strong> —
&#8377;4.5 to &#8377;7 lakh</li>
</ul>
<p>That covers base and wall units, shutters, internal fittings, a stone counter,
the backsplash and installation. Appliances — hob, chimney, oven, dishwasher — are
separate, and we specify rather than supply them so you are not paying a margin on
a retail item.</p>

<h2>What actually drives the price</h2>
<p><strong>Running feet, not floor area.</strong> A kitchen is priced by the length
of its runs and the height of its units. Two kitchens in identically sized rooms can
differ by a lakh because one has a full-height tall unit and the other does not.</p>
<p><strong>Carcass material.</strong> The box behind the shutter is where quotes
diverge most. BWP or marine-grade plywood in the wet zones costs more than commercial
ply or particle board and is the difference between a kitchen that survives ten years
and one that swells at the sink within three.</p>
<p><strong>Hardware.</strong> Hinges, channels, lift-ups and baskets are used dozens
of times a day. Branded soft-close hardware adds meaningfully to a quote and is the
last thing we would remove.</p>
<p><strong>Shutter finish.</strong> Laminate, acrylic, lacquered glass and veneer sit
at increasing price points. This is the most visible choice and, honestly, the least
important to how the kitchen performs.</p>
<p><strong>Counter material.</strong> Granite, engineered quartz and natural stone
differ substantially. Quartz costs more than granite and tolerates staining better.</p>

<h2>Where to spend and where not to</h2>
<p>If the budget is tight, we recommend protecting the carcass, the hardware and the
chimney, and economising on the shutter finish and the backsplash.</p>
<p>The reasoning is simple. A laminate shutter on a marine-ply carcass with good
hinges is a kitchen that works for fifteen years and can be refaced later. An acrylic
shutter on a particle board carcass with cheap channels looks better in photographs
and fails at the point of use. The visible half is the replaceable half.</p>

<h2>Ventilation is not optional</h2>
<p>The most common specification failure we see in Pune kitchens is the chimney. A
recirculating unit with a charcoal filter does very little against Indian cooking; it
moves smell around rather than removing it. A properly ducted chimney with a real
outlet through an external wall is the only version worth fitting, and the duct run
needs planning before the false ceiling closes.</p>
<p>Suction should be matched to the hob and the room, and the chimney positioned at
the manufacturer's stated height rather than wherever the wall unit line suggests.</p>

<h2>Drawers beat shutters</h2>
<p>The change that most improves how a kitchen is used is replacing lower shutters
with deep drawers. A shutter with shelves behind it means kneeling and reaching into
a dark box. A drawer brings the contents out to you.</p>
<p>Drawers cost more per running foot, which is why they are the first thing cut from
a cheap quote. In our kitchens the base units are drawers as standard unless there is
a reason not to.</p>

<h2>Open or closed</h2>
<p>Whether to open the kitchen into the living room depends on how the home is
actually used, not on what is fashionable. In a compact
<a href="/areas/balewadi">Balewadi</a> or <a href="/areas/punawale">Punawale</a>
2 BHK, opening it transforms a dark living room and is usually the best money in the
project. In a <a href="/areas/kondhwa">Kondhwa</a> home with a large family cooking
from scratch daily, keeping it closed and spending the money on ventilation and
durability is the better answer.</p>
<p>Opening a kitchen wall runs &#8377;55,000 to &#8377;90,000 including the
electrical rerouting, and the wall must be confirmed non-structural first.</p>

<h2>Related</h2>
<p>See our <a href="/services/modular-kitchens">modular kitchen service page</a>,
<a href="/guides/plywood-and-materials">the guide to plywood and materials</a> and
<a href="/guides/interior-design-cost-pune">what a full interior costs in Pune</a>.</p>

<p>To talk through a kitchen, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a modular kitchen cost in Pune?",
         "&#8377;2&ndash;3 lakh for a compact 8&ndash;10 running foot kitchen, &#8377;3&ndash;4.5 lakh for a standard L or U-shape, and &#8377;4.5&ndash;7 lakh for a large kitchen with an island or breakfast counter. Appliances are separate and we specify rather than supply them."),
        ("What should I not economise on in a kitchen?",
         "The carcass material, the hardware and the chimney. A laminate shutter on a marine-ply carcass with good hinges lasts fifteen years and can be refaced. An acrylic shutter on particle board with cheap channels looks better in photographs and fails at the point of use."),
        ("Are recirculating chimneys worth fitting?",
         "No. A charcoal-filter recirculating unit moves smell around rather than removing it. A properly ducted chimney with a real outlet through an external wall is the only version worth fitting, and the duct run must be planned before the ceiling closes."),
        ("Should the base units be drawers or shutters?",
         "Drawers, unless there is a specific reason not to. A shutter with shelves behind it means kneeling and reaching into a dark box. Drawers cost more per running foot, which is why they are the first thing cut from a cheap quote."),
        ("How much does it cost to open the kitchen into the living room?",
         "&#8377;55,000 to &#8377;90,000 including electrical rerouting, once the wall is confirmed non-structural. In a compact 2 BHK it is usually the best money in the whole project."),
    ],
))

# ------------------------------------------------- WARDROBE COST
PAGES.append(dict(
    path="/guides/wardrobe-cost-pune",
    title="Wardrobe Cost in Pune (2026) | Twin Space Studio",
    description="What built-in wardrobes cost in Pune in 2026, sliding versus openable, and the internal decisions that determine whether storage actually gets used.",
    h1="Wardrobe Cost in Pune",
    article=True,
    og_image="/assets/opt/a07.jpg",
    crumbs=GC("Wardrobe cost", "wardrobe-cost-pune"),
    body=DISCLAIMER + gallery(["a07", "c08", "b03"]) + """
<p>Wardrobes are the second largest joinery line after the kitchen, and across three
bedrooms they often exceed it. This page covers what they cost, how sliding compares
with openable, and the internal decisions that decide whether the storage is actually
used.</p>

<h2>What it costs</h2>
<p>We price wardrobes by the elevation area — the height multiplied by the width of
the run — because that is what determines the material and labour.</p>
<ul>
<li><strong>Openable, laminate finish</strong> — &#8377;1,500 to &#8377;2,100 per
square foot of elevation</li>
<li><strong>Sliding, laminate or mirror</strong> — &#8377;1,900 to &#8377;2,600 per
square foot</li>
<li><strong>Acrylic, lacquered glass or veneer finish</strong> — &#8377;2,400 to
&#8377;3,600 per square foot</li>
</ul>
<p>A typical master bedroom wardrobe of 8 feet wide by 8 feet high is 64 square feet
of elevation, so &#8377;1 to &#8377;1.6 lakh at the common specifications. Across a
3 BHK, wardrobes and bedroom joinery together usually run
&#8377;4&ndash;5.5 lakh.</p>

<h2>Take it to the slab</h2>
<p>The single best-value decision in a wardrobe is running it to the ceiling rather
than stopping at a loft with a separate shutter above.</p>
<p>A full-height unit adds roughly a third more capacity for a small fraction more
cost, because the carcass and the run are already there. It also removes the dust
ledge that a loft creates, and it looks like joinery rather than like a cupboard with
a box on top. Where the ceiling is high, the top section becomes genuine long-term
storage with a proper shutter rather than an awkward gap.</p>

<h2>Sliding or openable</h2>
<p>Openable is cheaper, gives you the full opening at once, and lets you fit the
inside of the shutter with racks. It needs clear floor space in front, which a
compact bedroom may not have.</p>
<p>Sliding costs more and permanently loses you access to half the wardrobe at a
time, plus roughly 100mm of internal depth to the track. What it buys is that it
never obstructs a walkway, which in a tight
<a href="/areas/punawale">Punawale</a> or <a href="/areas/tathawade">Tathawade</a>
bedroom is often decisive.</p>
<p>Our default recommendation: openable where there is 900mm of clear floor in front,
sliding where there is not.</p>

<h2>The internals decide whether it gets used</h2>
<p>Most wardrobes are specified as a box with a rail and two shelves, and then people
wonder why the storage does not work. The internal layout should follow what actually
goes in it.</p>
<ul>
<li><strong>Full-height hanging</strong> for long garments, at least one section.</li>
<li><strong>Double hanging</strong> for shirts and folded-over trousers, which
doubles capacity in the same width.</li>
<li><strong>Drawers rather than shelves</strong> for anything small. Shelves at chest
height become a pile within a fortnight.</li>
<li><strong>A pull-out trouser or tie rack</strong> if that is what you own.</li>
<li><strong>A lower rail in at least one unit</strong> where an older family member
uses the room.</li>
</ul>
<p>Lighting inside a deep wardrobe is worth the small cost of a strip on a door
sensor. Without it the back of a wardrobe is unusable after dusk.</p>

<h2>Moisture and external walls</h2>
<p>Any wardrobe against an external wall needs a ventilation gap behind it and a
moisture-resistant carcass, particularly on lower floors and near the river in
<a href="/areas/kalyani-nagar">Kalyani Nagar</a> and
<a href="/areas/mundhwa">Mundhwa</a>. Building a sealed carcass hard against an
external wall is the most common cause of a wardrobe that smells damp in its second
monsoon.</p>

<h2>Storage beds</h2>
<p>In compact flats a storage bed adds significant capacity for
&#8377;35,000&ndash;70,000 depending on size and finish. Specify hydraulic lifts
rather than hinged lids — a hinged lid needs two people and stops being used after
the first month.</p>

<h2>Related</h2>
<p>See our <a href="/services/wardrobes-storage">wardrobes and storage service
page</a>, <a href="/guides/plywood-and-materials">the guide to plywood and
materials</a> and <a href="/guides/interior-design-cost-pune">what a full interior
costs in Pune</a>.</p>

<p>To talk through storage for a specific flat, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a built-in wardrobe cost in Pune?",
         "&#8377;1,500 to &#8377;2,100 per square foot of elevation for openable laminate, &#8377;1,900 to &#8377;2,600 for sliding, and &#8377;2,400 to &#8377;3,600 for acrylic, lacquered glass or veneer. A typical 8 by 8 foot master wardrobe is &#8377;1 to &#8377;1.6 lakh."),
        ("Should a wardrobe go all the way to the ceiling?",
         "Yes, in almost every case. A full-height unit adds roughly a third more capacity for a small fraction more cost, removes the dust ledge a loft creates, and looks like joinery rather than a cupboard with a box on top."),
        ("Sliding or openable doors?",
         "Openable where there is 900mm of clear floor in front — cheaper, full opening at once, and you can fit racks inside the shutter. Sliding where there is not, accepting the extra cost, the loss of about 100mm of depth and access to only half at a time."),
        ("Why does my wardrobe smell damp?",
         "Usually because a sealed carcass was built hard against an external wall with no ventilation gap. Any wardrobe on an external wall needs a gap behind it and a moisture-resistant carcass, especially on lower floors and near the river."),
        ("Are storage beds worth it?",
         "In compact flats, yes — &#8377;35,000 to &#8377;70,000 for significant extra capacity. Specify hydraulic lifts rather than hinged lids, because a hinged lid needs two people and stops being used after the first month."),
    ],
))

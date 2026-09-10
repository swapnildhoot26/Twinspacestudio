# -*- coding: utf-8 -*-
"""Practical guides: society rules, possession, materials, renovation."""

from pagegen import gallery
from content_guides_a import GC, DISCLAIMER

PAGES = []

# ------------------------------------------------- SOCIETY RULES
PAGES.append(dict(
    path="/guides/society-rules-interior-work-pune",
    title="Society Rules for Interior Work in Pune | Twin Space Studio",
    description="Working hours, service lift bookings, deposits and what most Pune societies will not let you change — everything to confirm before a fit-out starts.",
    h1="Society Rules for Interior Work in Pune",
    article=True,
    og_image="/assets/areas/interior-designers-balewadi-pune-open-kitchen.jpg",
    crumbs=GC("Society rules for interior work", "society-rules-interior-work-pune"),
    body=gallery(["d03", "b06", "e05"]) + """
<p>More Pune interior projects lose time to society rules than to anything a designer
does. None of it is difficult; all of it needs confirming before a schedule is built.
This is what to ask for and what to expect.</p>

<h2>Get it in writing, in week one</h2>
<p>Ask the society or the facility management company for the fit-out rules as a
written document before drawings are finalised. Not from the security desk, and not
from a neighbour who did their flat two years ago — the rules change, and committees
in newer buildings are often still writing them.</p>
<p>We do this as standard, and on a first-phase tower in
<a href="/areas/mundhwa">Mundhwa</a> or <a href="/areas/mahalunge">Mahalunge</a> it
is worth more than any amount of design efficiency.</p>

<h2>Working hours</h2>
<p>Commonly 9am to 6pm, with no work on Sundays and often none on public holidays.
Some societies restrict noisy work — drilling, cutting, breaking — to a narrower
window inside that, typically 10am to 5pm.</p>
<p>The practical consequence is that lost days cannot be recovered by working late.
In a township like <a href="/areas/magarpatta-city">Magarpatta City</a> where hours
are strictly enforced, a ten-to-twelve week programme is genuinely ten to twelve
weeks with no evening flexibility.</p>

<h2>Service lift booking</h2>
<p>This is the resource everything else queues behind. Most towers have one or two
service lifts shared across every flat under fit-out, and during a possession wave
that can be dozens of families at once.</p>
<p>Book slots as early as possible — in a new tower, the week you get the allotment
letter rather than the week you start. Then build the delivery schedule around the
slots you have, breaking joinery into loads that fit the window rather than sending
one truck that has to go away again.</p>

<h2>Material movement windows</h2>
<p>Separate from the lift booking, many societies restrict when material can enter
the premises at all — frequently a morning-only window, sometimes as narrow as three
hours.</p>
<p>In congested areas this interacts badly with traffic. In
<a href="/areas/wakad">Wakad</a> and <a href="/areas/hinjawadi">Hinjawadi</a>, a van
booked for 9am routinely loses two hours and then misses the window entirely. We
schedule deliveries for late morning and consolidate them.</p>

<h2>Deposits and paperwork</h2>
<p>Expect most or all of the following:</p>
<ul>
<li>A refundable fit-out deposit, commonly &#8377;15,000 to &#8377;50,000, higher in
townships</li>
<li>Sometimes a non-refundable administrative or debris charge</li>
<li>A written scope of work with a stated completion date</li>
<li>Photo identity and records for every worker on site</li>
<li>Contractor registration with the facility management company — this takes days
rather than hours, so start it before drawings are finalised</li>
<li>An undertaking on debris removal, sometimes required before a gate pass is
issued at all</li>
</ul>

<h2>What societies commonly will not allow</h2>
<p>This is the part that most often invalidates a design, so check before drawing:</p>
<p><strong>Balcony enclosure.</strong> Prohibited in most townships and many
societies, because it changes the facade.</p>
<p><strong>External glazing changes.</strong> Replacing windows with a different
frame colour or profile is frequently disallowed for the same reason.</p>
<p><strong>Anything affecting a common wall</strong> — and in some societies, any
alteration to a wall shared with a neighbouring flat, structural or not.</p>
<p><strong>Changes to plumbing risers</strong> or moving a bathroom's wet zone, which
many societies prohibit outright.</p>
<p><strong>Air-conditioning outdoor unit positions</strong> that differ from the
designated locations.</p>
<p>A drawing set that assumes a balcony can be enclosed in
<a href="/areas/magarpatta-city">Magarpatta</a> is a wasted drawing set. We check the
bye-laws first.</p>

<h2>Older buildings: no service lift</h2>
<p>In <a href="/areas/erandwane">Erandwane</a>,
<a href="/areas/koregaon-park">Koregaon Park</a>, older
<a href="/areas/kothrud">Kothrud</a> and <a href="/areas/aundh">Aundh</a>, many
buildings have a single passenger lift too small for sheet material, or no lift above
a certain floor.</p>
<p>Ply is then carried up the stairwell or cut smaller and assembled in the flat.
Both are routine and both belong in the quote. Societies here are also stricter about
the common staircase, since it is the neighbours' route to their own front doors — so
protect it, clear it daily, and agree a debris schedule before the first day rather
than after the first complaint.</p>

<h2>Neighbours</h2>
<p>Worth saying plainly: the people around you did not choose to have a building site
next door. Agreeing the working hours in writing, keeping the common areas clean,
clearing debris daily rather than letting it accumulate, and telling the immediate
neighbours when the noisy weeks will be, prevents most complaints — and a complaint
to the committee can stop a site faster than anything else on this page.</p>

<h2>Related</h2>
<p>See <a href="/guides/interior-design-timeline">how long a project takes</a> and
<a href="/guides/new-flat-possession-checklist">what to check before you start</a>.</p>

<p>To talk through a specific society's rules, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("What are typical society working hours for interior work in Pune?",
         "Commonly 9am to 6pm with no work on Sundays and often none on public holidays. Some societies restrict noisy work to a narrower window inside that, typically 10am to 5pm. Lost days cannot be recovered by working late."),
        ("When should I book the service lift?",
         "As early as possible — in a new tower, the week you get the allotment letter rather than the week you start. It is the resource everything else queues behind, especially during a possession wave."),
        ("What will a society usually not allow?",
         "Balcony enclosure, external glazing changes, alterations affecting a common wall, changes to plumbing risers or a bathroom's wet zone, and air-conditioning outdoor units in undesignated positions. Check the bye-laws before drawing, not after."),
        ("How much is a fit-out deposit?",
         "Commonly &#8377;15,000 to &#8377;50,000 refundable, higher in townships, sometimes with a non-refundable administrative or debris charge on top."),
        ("What if the building has no service lift?",
         "Sheet material is carried up the stairwell or cut smaller and assembled in the flat. Both are routine in older Pune buildings and both should appear in the quote, along with staircase protection and daily debris clearance."),
    ],
))

# ------------------------------------------------- POSSESSION CHECKLIST
PAGES.append(dict(
    path="/guides/new-flat-possession-checklist",
    title="New Flat Possession Checklist, Pune | Twin Space Studio",
    description="What to check and get the builder to fix before interior work starts in a new Pune flat — the snag list that saves money once joinery is in.",
    h1="What to Check Before Interior Work Starts",
    article=True,
    og_image="/assets/opt/c04.jpg",
    crumbs=GC("New flat possession checklist", "new-flat-possession-checklist"),
    body=gallery(["c04", "f05", "d05"]) + """
<p>New does not mean finished. In fast-built Pune towers it means less than usual,
and the difference between snagging a flat before interior work and after it is
several lakh rupees of someone else's problem becoming yours. This is what to check.</p>

<h2>Why the order matters</h2>
<p>Once a wardrobe stands against a wall, a damp patch behind it is your problem. Once
a false ceiling closes, a badly positioned electrical point is a chase through
finished plaster. Once flooring is protected and covered, a level problem is invisible
until the furniture rocks.</p>
<p>Everything on this list is the builder's responsibility to fix under the handover
snag process, and free — but only until you start building on top of it.</p>

<h2>Floors and levels</h2>
<p>Check level across each room with a spirit level or a long straight edge, not by
eye. Look particularly at the junction between rooms and at doorway thresholds.</p>
<p>Check the fall in every wet area — bathrooms, the utility, the balcony. Pour a
mug of water and watch where it goes. Water that pools or runs the wrong way is a
waterproofing and screed issue, and it is much easier to raise now.</p>
<p>Check tiles and flooring for hollowness by tapping. A hollow tile will crack.</p>

<h2>Walls and ceilings</h2>
<p>Look for seepage and damp at external walls, especially after rain and especially
on the weather-facing side. This is the single most important item on the list, and
it is why we do this walk before any joinery is fitted.</p>
<p>Check walls for plumb and for square at corners, because joinery has to fit
against them. Some deviation is normal and we scribe to it; a lot of deviation is
worth raising.</p>
<p>Check the slab and ceiling for cracks and for any sign of water ingress from the
flat above.</p>

<h2>Windows and doors</h2>
<p>Open and close everything. Look for alignment, smooth operation, and gaps at the
frame. Check that window drainage weep holes are clear, and that sliding tracks are
not full of construction debris.</p>
<p>Check the sealant around external window frames. Poor sealing here is a common
source of monsoon seepage and is far easier for the builder to redo than for anyone to
diagnose later.</p>

<h2>Electrical</h2>
<p>Count the points against the agreed layout, room by room. Builders routinely
provide fewer than the brochure implied, or provide them in positions that assume
furniture nobody would place there.</p>
<p>Test every socket and switch. Check the distribution board — the number of
circuits, the rating, and whether there is an RCD. Check that the earthing is
present and connected.</p>
<p>Note where you will actually need points once furniture is planned, because adding
them now costs far less than chasing a finished flat later.</p>

<h2>Plumbing</h2>
<p>Run every tap and flush every WC. Check pressure at the highest fitting. Look
under every sink and behind every WC for leaks and for whether the connections are
accessible.</p>
<p>Check the geyser point positions and the drainage in the utility. Confirm where
the water inlet and the shut-off valve are, because you will need them.</p>

<h2>Balcony and external</h2>
<p>Check railing fixing and height. Check the balcony fall and drain. Check for
seepage at the balcony-to-room threshold, which is a common weak point.</p>
<p>Confirm the designated air-conditioning outdoor unit positions with the society
before planning any concealed pipe runs.</p>

<h2>Get it in writing</h2>
<p>Submit the snag list to the builder in writing, dated, with photographs, and keep
a copy. Verbal reports at handover have a way of not existing later.</p>
<p>Get the resolution confirmed in writing too, and re-check the items yourself rather
than accepting that they were done.</p>

<h2>What we do</h2>
<p>We walk this list with clients before starting work, and we will not fit joinery
against a wall with unresolved seepage. Where the builder is slow, we sequence around
the affected room rather than building over the problem.</p>
<p>See also <a href="/guides/society-rules-interior-work-pune">society rules for
interior work</a> and <a href="/guides/interior-design-timeline">how long a project
takes</a>.</p>

<p>To have a new flat looked at before you start, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("What should I check before interior work starts in a new flat?",
         "Floor level and wet-area falls, seepage at external walls, window and door alignment and sealing, the electrical point count and distribution board, plumbing and pressure, and the balcony fall and railing. All of it is the builder's responsibility to fix, but only until you build on top of it."),
        ("Why does the order matter?",
         "Once a wardrobe stands against a wall, a damp patch behind it is your problem rather than the builder's. Once a ceiling closes, a badly positioned electrical point means chasing finished plaster."),
        ("What is the single most important item?",
         "Seepage and damp at external walls, checked after rain and on the weather-facing side. It is the reason we do this walk before any joinery is fitted."),
        ("How do I check the fall in a bathroom?",
         "Pour a mug of water and watch where it goes. Water that pools or runs away from the drain is a screed and waterproofing issue, and it is far easier to raise before you start than after."),
        ("Should the snag list be in writing?",
         "Yes — dated, with photographs, and keep a copy. Get the resolution confirmed in writing too, and re-check the items yourself rather than accepting that they were done."),
    ],
))

# ------------------------------------------------- PLYWOOD AND MATERIALS
PAGES.append(dict(
    path="/guides/plywood-and-materials",
    title="Plywood, Laminate and Materials Explained | Twin Space Studio",
    description="What BWP, MR and BWR plywood actually mean, where each belongs in a Pune home, and why the carcass matters more than the shutter you can see.",
    h1="Plywood, Laminate and What Actually Matters",
    article=True,
    og_image="/assets/opt/e11.jpg",
    crumbs=GC("Plywood and materials", "plywood-and-materials"),
    body=DISCLAIMER + gallery(["e11", "a03", "c09"]) + """
<p>Almost every disagreement about interior quotes comes down to materials you
cannot see once the job is done. This page explains what the terms mean, where each
material belongs, and what we specify.</p>

<h2>The carcass matters more than the shutter</h2>
<p>The box behind the door is what fails or does not. A laminate shutter on a
marine-ply carcass with good hinges is a unit that works for fifteen years and can be
refaced. An acrylic shutter on a particle-board carcass with cheap channels looks
better in photographs and fails at the point of use.</p>
<p>Two quotes twenty per cent apart on the same drawing set almost always differ
here. The visible half is the replaceable half.</p>

<h2>Plywood grades, plainly</h2>
<p><strong>MR (moisture resistant)</strong> — often called commercial ply. Bonded
with urea-formaldehyde resin. Fine for dry areas: bedroom wardrobes on internal
walls, television units, study furniture. Not for anything near water.</p>
<p><strong>BWR (boiling water resistant)</strong> — phenolic bonded, more moisture
tolerant than MR. A reasonable middle grade.</p>
<p><strong>BWP (boiling water proof) / marine grade</strong> — fully phenolic bonded.
This is what belongs in kitchens, bathroom vanities, utility units, and any wardrobe
against an external wall.</p>
<p>Grades are governed by Indian Standards — IS 303 for MR and BWR, IS 710 for
marine-grade BWP — and the stamp should be on the sheet. Ask to see it. "Marine ply"
without an IS 710 stamp is a description, not a specification.</p>

<h2>Where we specify what</h2>
<ul>
<li><strong>Kitchen base and tall units</strong> — BWP throughout. The area under the
sink is where every kitchen eventually gets wet.</li>
<li><strong>Kitchen wall units</strong> — BWP or good BWR.</li>
<li><strong>Wardrobes on internal walls</strong> — MR is adequate.</li>
<li><strong>Wardrobes on external walls</strong> — BWR or BWP, with a ventilation
gap behind. This matters especially on lower floors and near the river in
<a href="/areas/kalyani-nagar">Kalyani Nagar</a> and
<a href="/areas/mundhwa">Mundhwa</a>.</li>
<li><strong>Bathroom vanities and utility</strong> — BWP, without exception.</li>
<li><strong>Television units and study furniture</strong> — MR.</li>
</ul>
<p>Specifying BWP everywhere is a waste of your money. Specifying MR in a kitchen is
a waste of the kitchen.</p>

<h2>What about MDF and particle board</h2>
<p>MDF takes paint and routed profiles beautifully and is the right material for a
lacquered or painted shutter with a shaped profile. It is not a structural carcass
material and it does not tolerate water at all — a swollen MDF edge does not
recover.</p>
<p>Particle board is cheaper again and is what most flat-pack furniture is made from.
We do not use it for built-in joinery. In a climate with a real monsoon and a kitchen
that gets washed down, it does not last.</p>

<h2>Shutter finishes</h2>
<p><strong>Laminate</strong> — durable, enormous range, repairable in sections, the
most sensible default. A good 1mm laminate outlasts most alternatives.</p>
<p><strong>Acrylic</strong> — high gloss, seamless look, shows fingerprints and fine
scratches. Best away from the busiest surfaces.</p>
<p><strong>Lacquered glass</strong> — excellent in kitchens, easy to clean, heavier
and needs good hinges to match.</p>
<p><strong>Veneer</strong> — real wood, ages well, needs a polish coat and occasional
maintenance. The right choice where the joinery is meant to be furniture.</p>
<p><strong>PU / lacquer paint</strong> — best for shaped and profiled shutters, on
MDF. Repairable but not cheaply.</p>

<h2>Hardware</h2>
<p>Hinges, channels, lift-ups and baskets are operated dozens of times daily and are
where cheap quotes cut hardest. Branded soft-close hardware from a known manufacturer
is the last line we would remove from a specification. Ask which brand is quoted, not
just "soft-close" — the word is not a specification either.</p>
<p>For anything on an external wall or in a coastal or riverside microclimate,
specify a properly coated or stainless finish.</p>

<h2>Counters</h2>
<p><strong>Granite</strong> — hard, heat tolerant, economical, porous unless sealed
and needs resealing.</p>
<p><strong>Engineered quartz</strong> — non-porous, more stain resistant, more
expensive, less tolerant of direct heat.</p>
<p>For an Indian kitchen where turmeric and hot vessels are daily events, quartz is
usually worth the difference. Granite sealed properly is a perfectly good answer at a
lower price.</p>

<h2>Related</h2>
<p>See <a href="/guides/modular-kitchen-cost-pune">modular kitchen cost</a>,
<a href="/guides/wardrobe-cost-pune">wardrobe cost</a> and
<a href="/guides/interior-design-cost-pune">what a full interior costs in Pune</a>.</p>

<p>To talk through a specification, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("What is the difference between MR, BWR and BWP plywood?",
         "MR (moisture resistant, commercial ply) suits dry areas only. BWR (boiling water resistant) is a phenolic-bonded middle grade. BWP or marine grade is fully phenolic bonded and belongs in kitchens, bathroom vanities, utilities and wardrobes on external walls. Look for the IS 303 or IS 710 stamp on the sheet."),
        ("Does the whole house need marine plywood?",
         "No — that wastes money. MR is adequate for bedroom wardrobes on internal walls, television units and study furniture. BWP belongs where water reaches: kitchens, bathroom vanities, utility units and external-wall wardrobes."),
        ("Do you use MDF or particle board?",
         "MDF for lacquered or painted shutters with shaped profiles, where it is the right material. Not as a structural carcass, and never particle board for built-in joinery — it does not survive a real monsoon or a kitchen that gets washed down."),
        ("Which shutter finish is best?",
         "Laminate is the sensible default: durable, huge range, repairable in sections. Lacquered glass is excellent in kitchens, veneer where the joinery should read as furniture, acrylic where high gloss matters and traffic is low."),
        ("Granite or quartz for a kitchen counter?",
         "For an Indian kitchen with turmeric and hot vessels daily, engineered quartz is usually worth the extra. Granite sealed properly and resealed periodically is a perfectly good answer at a lower price."),
    ],
))

# ------------------------------------------------- RENOVATION VS NEW
PAGES.append(dict(
    path="/guides/renovation-vs-new-flat",
    title="Renovating an Older Flat in Pune | Twin Space Studio",
    description="How renovating an older Pune flat differs from fitting out a new one — what to survey, what to keep, what it adds to the cost, and what it adds to the time.",
    h1="Renovating an Older Flat",
    article=True,
    og_image="/assets/opt/a04.jpg",
    crumbs=GC("Renovating an older flat", "renovation-vs-new-flat"),
    body=DISCLAIMER + gallery(["a04", "e08", "f07"]) + """
<p>Roughly half our work is renovation rather than first fit-out, and it is a
genuinely different job. The design is the easy part; what makes a renovation succeed
or fail is what you find out before you quote it.</p>

<h2>Survey before quoting, not after</h2>
<p>A quote produced from a floor plan and a walk-through is a guess. In an older
<a href="/areas/kothrud">Kothrud</a>, <a href="/areas/aundh">Aundh</a> or
<a href="/areas/erandwane">Erandwane</a> flat we check, before pricing:</p>
<ul>
<li>Floor-to-slab height in more than one place, because a previous false ceiling has
often already taken 150mm</li>
<li>The distribution board — circuit count, rating, earthing, whether it will carry a
modern kitchen</li>
<li>Where the plumbing actually runs, which frequently means opening a small section
of the kitchen wall</li>
<li>Which walls are structural and which are not</li>
<li>Bathroom waterproofing condition and age</li>
<li>How material will physically get into the building</li>
</ul>
<p>This makes the first number slower to produce and much closer to the last one. It
is the whole reason we can say the figure quoted on day one is the figure at
handover.</p>

<h2>What renovation adds to the cost</h2>
<p><strong>Demolition and debris removal</strong> — &#8377;60,000 to &#8377;1.4 lakh
depending on the size of the strip-out.</p>
<p><strong>Rewiring</strong> — frequently a real line rather than a nominal one. A
1990s board sized for a fridge and two fans will not carry a hob, oven, chimney and
dishwasher.</p>
<p><strong>Bathrooms</strong> — &#8377;90,000 to &#8377;2.2 lakh each, and in a flat
over fifteen years old they usually cannot sensibly be skipped.</p>
<p><strong>Material handling</strong> where a truck cannot reach the building or the
lift will not take sheet material.</p>
<p>We list these as a separate building-works section above the interior lines, so
you can see what is restoration and what is design.</p>

<h2>What renovation saves</h2>
<p>Several new-build costs shrink or disappear entirely.</p>
<p><strong>Flooring</strong> is often sound and worth polishing rather than
replacing. <strong>Doors and window frames</strong> in solid teak are usually better
refinished than replaced — and what replaces them is rarely as good.
<strong>False ceilings</strong> are frequently partial rather than throughout, because
the remaining height is worth protecting. <strong>Room proportions</strong> in older
flats are often generous in a way a modern builder will not give you at the same
price.</p>
<p>We say when something is worth keeping, even though a full strip-out would be a
larger project for us. Keeping sound flooring and good doors regularly releases enough
budget to do the kitchen properly, which changes daily life far more than new
skirting.</p>

<h2>Where the budget lands differently</h2>
<p>A renovation quote at the same total as a new-build one is distributed differently.
More sits in work you will never see — rewiring, plumbing, waterproofing, making good
— and less in visible surfaces.</p>
<p>That is the correct distribution for a home meant to last another twenty years,
and it is worth understanding before comparing a renovation quote against a
new-flat one and concluding that one is poor value.</p>

<h2>Time</h2>
<p>Ten to twelve weeks from approved drawings, the same as a new flat, plus about two
weeks if the family stays in residence. The first fortnight is the risky one: walls
open, and whatever was hidden appears. That is when being able to reach the site
quickly matters most.</p>

<h2>The judgement calls</h2>
<p><strong>Kitchens</strong> — almost always replaced completely. The original is at
the end of its service life even where the platform is sound.</p>
<p><strong>Bathrooms</strong> — almost always redone, because waterproofing has a
lifespan whatever the tiles look like.</p>
<p><strong>Flooring</strong> — usually kept if it is sound. Mosaic, terrazzo and good
stone all polish up well.</p>
<p><strong>Ceiling height</strong> — an old false ceiling can often be partly removed
to recover height, which is worth more than most decorative additions.</p>
<p><strong>Joinery</strong> — original teak refinished; anything laminated in the
1990s replaced.</p>

<h2>Related</h2>
<p>See <a href="/guides/living-in-during-renovation">living in the flat during a
renovation</a>, <a href="/guides/hidden-costs-interior-design">the costs people forget
to budget for</a> and <a href="/guides/interior-design-cost-pune">what a full interior
costs in Pune</a>.</p>

<p>To have an older flat surveyed, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How is renovating an older flat different from fitting out a new one?",
         "The design is the easy part. What decides a renovation is the survey before quoting — ceiling height, the distribution board, where the plumbing actually runs, which walls are structural, bathroom waterproofing, and how material gets into the building."),
        ("What does renovation add to the cost?",
         "Demolition and debris of &#8377;60,000 to &#8377;1.4 lakh, rewiring where the load is inadequate, bathrooms at &#8377;90,000 to &#8377;2.2 lakh each, and material handling where access is restricted. We list these separately from the interior lines."),
        ("What is worth keeping in an older flat?",
         "Sound flooring, solid teak doors and window frames, and generous room proportions. Keeping flooring and doors regularly releases enough budget to do the kitchen properly, which matters far more day to day."),
        ("Do bathrooms always need redoing?",
         "In a flat over fifteen years old, usually yes. Waterproofing has a lifespan regardless of how the tiles look, and fixing it later means opening a finished flat."),
        ("How long does a renovation take?",
         "Ten to twelve weeks from approved drawings, plus about two weeks if the family stays in residence. The first fortnight carries the most risk, because that is when whatever was hidden appears."),
    ],
))

# ------------------------------------------------- LIVING IN DURING RENOVATION
PAGES.append(dict(
    path="/guides/living-in-during-renovation",
    title="Living in the Flat During a Renovation | Twin Space Studio",
    description="How we phase a Pune renovation so a family can stay in the home — dust control, which room goes last, and what it adds to the programme.",
    h1="Living in the Flat During a Renovation",
    article=True,
    og_image="/assets/opt/a08.jpg",
    crumbs=GC("Living in during a renovation", "living-in-during-renovation"),
    body=gallery(["a08", "d06", "e06"]) + """
<p>About half our renovation clients stay in the flat through the work, usually
because three months of rent costs more than the saving, and sometimes because moving
out of a home held for thirty years is not a simple proposition. It is entirely
workable. It changes the sequence, and it adds about two weeks.</p>

<h2>How we phase it</h2>
<p>The principle is that one bedroom and one bathroom stay usable at all times, and
the kitchen goes last.</p>
<p>We start with the rooms you can most easily do without — typically the second
bedroom and the living room — and complete them fully before opening the next. That
means dust and disruption move through the flat rather than filling it, and you always
have somewhere finished to retreat to.</p>
<p>The kitchen is deliberately last. A family can live without a spare bedroom for a
fortnight but not without somewhere to cook, so we set up a temporary arrangement —
usually an induction plate, a sink connection and a table in a finished room — before
the existing kitchen comes out.</p>

<h2>Dust control</h2>
<p>This is what actually determines whether living in is tolerable, and it is where
most contractors are casual.</p>
<p>We seal the working zone with a floor-to-ceiling barrier, not a hung sheet.
Doorways get zipped access panels. Air-conditioning and any ducted route between zones
is sealed off, because dust travels through it. Grinding and cutting happen outside
the flat wherever possible, and where it cannot, with extraction at the tool.</p>
<p>Floors in the finished zones stay protected throughout, and the site is cleaned at
the end of every working day rather than at the end of the week.</p>

<h2>Grouping the wet work</h2>
<p>The single most disruptive thing in a renovation is the water going off. Left
unplanned it goes off repeatedly — once for the kitchen, once per bathroom, once for
the utility.</p>
<p>We group all plumbing changes into a single block so the supply is interrupted once
rather than five or six times, and we tell you the dates in advance so you can plan
around them.</p>

<h2>Noise</h2>
<p>Demolition, chasing and core drilling are the loud phases, and they are
front-loaded — usually the first ten to fourteen working days. If anyone in the house
works from home or sleeps during the day, that is the window to be elsewhere if you
can.</p>
<p>Societies frequently restrict noisy work to a narrower window than general working
hours, commonly 10am to 5pm. See
<a href="/guides/society-rules-interior-work-pune">society rules for interior
work</a>.</p>

<h2>What it adds</h2>
<p>Roughly two weeks on a ten-to-twelve week programme. The time goes into sequencing
that would otherwise happen in parallel, setting up and moving dust barriers, and the
temporary kitchen arrangement.</p>
<p>We state this at quoting stage rather than discovering it in week eight. A
contractor who quotes the same duration whether you stay or move out has not thought
about the sequence.</p>

<h2>What we ask of you</h2>
<p>Pack and move what you can before we start — the fewer possessions in the working
zone, the faster and cleaner the work. Anything fragile or valuable should be out of
the flat entirely rather than covered.</p>
<p>Agree the noisy-work window with us so we can front-load it around your calendar,
and be reachable for decisions during working hours. Most site questions need an
answer within the hour.</p>

<h2>When we recommend moving out</h2>
<p>Honestly, there are cases. A full strip-out of a small flat where there is no room
that can be completed and sealed first. A household with a newborn, or someone with a
respiratory condition. And any project where the entire plumbing layout is changing,
which makes a single wet-work block impossible.</p>
<p>We say so when it applies rather than taking the work on terms that will make
everyone miserable.</p>

<h2>Related</h2>
<p>See <a href="/guides/renovation-vs-new-flat">renovating an older flat</a>,
<a href="/guides/interior-design-timeline">how long a project takes</a> and
<a href="/areas/kothrud">interior designers in Kothrud</a>, where most of this work
happens.</p>

<p>To talk through a renovation, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("Can we stay in the flat during a renovation?",
         "Usually yes, and about half our renovation clients do. We phase it room by room so one bedroom and one bathroom stay usable throughout, and the kitchen goes last after a temporary arrangement is set up."),
        ("How much longer does it take if we stay?",
         "About two weeks on a ten-to-twelve week programme. The time goes into sequencing that would otherwise run in parallel, moving dust barriers, and setting up the temporary kitchen."),
        ("How do you control dust?",
         "A sealed floor-to-ceiling barrier rather than a hung sheet, zipped access panels at doorways, air-conditioning and duct routes sealed off, cutting done outside the flat where possible with extraction at the tool, and a clean at the end of every working day."),
        ("How often will the water be off?",
         "Once, if it is planned properly. We group all plumbing changes into a single block rather than interrupting the supply separately for the kitchen, each bathroom and the utility, and we give you the dates in advance."),
        ("When would you advise moving out instead?",
         "A full strip-out of a small flat with no room that can be completed and sealed first, a household with a newborn or someone with a respiratory condition, or a project where the entire plumbing layout changes so a single wet-work block is impossible."),
    ],
))

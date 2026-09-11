# -*- coding: utf-8 -*-
"""Ceilings, hidden costs, process, timeline, payments."""

from pagegen import gallery
from content_guides_a import GC, DISCLAIMER

PAGES = []

# ------------------------------------------------- FALSE CEILING COST
PAGES.append(dict(
    path="/guides/false-ceiling-cost-pune",
    guide=True,
    eyebrow="Guide",
    title="False Ceiling and Lighting Cost in Pune (2026) | Twin Space Studio",
    description="What false ceilings and lighting cost in Pune in 2026, where a ceiling is worth doing, and where it quietly takes height you should have kept.",
    h1="False Ceiling and Lighting Cost in Pune",
    article=True,
    og_image="/assets/areas/interior-designers-kondhwa-pune-dining-slatted-ceiling.jpg",
    crumbs=GC("False ceiling and lighting cost", "false-ceiling-cost-pune"),
    body=DISCLAIMER + gallery(["b04", "d06", "e01"]) + """
<p>False ceilings are the line clients most often over-buy and the one where the real
cost is not money but ceiling height. This page covers what they cost, where they earn
their place, and where we recommend not having one at all.</p>

<h2>What it costs</h2>
<ul>
<li><strong>Peripheral gypsum ceiling with a cove</strong> — &#8377;95 to
&#8377;150 per square foot of ceiling area</li>
<li><strong>Full gypsum ceiling with profile lighting</strong> — &#8377;150 to
&#8377;240 per square foot</li>
<li><strong>Slatted timber or fluted feature ceiling</strong> — &#8377;320 to
&#8377;650 per square foot</li>
<li><strong>Plain POP with no lighting detail</strong> — &#8377;75 to &#8377;110 per
square foot</li>
</ul>
<p>Lighting is separate. Across a full home, fittings and their wiring typically run
&#8377;70,000 to &#8377;1.8 lakh depending on how many circuits and what quality of
fitting. In a 3 BHK, ceilings and lighting together usually come to
&#8377;2&ndash;3.2 lakh.</p>

<h2>The real cost is height</h2>
<p>A standard Pune flat has a floor-to-slab height of around 9 feet 6 inches to 10
feet. A peripheral ceiling takes 100&ndash;150mm at the edges only. A full ceiling
takes the same across the whole room.</p>
<p>In a new tower with generous height, that is fine. In an older
<a href="/areas/kothrud">Kothrud</a>, <a href="/areas/aundh">Aundh</a> or
<a href="/areas/erandwane">Erandwane</a> flat where a previous ceiling has already
taken 150mm, adding another is how a room ends up feeling low without anyone being
able to say why. We measure floor-to-slab in more than one place before recommending
anything.</p>

<h2>Where a ceiling earns its place</h2>
<p><strong>To conceal air-conditioning ducting and pipe runs.</strong> This is the
strongest reason and often the only necessary one.</p>
<p><strong>To make layered lighting possible.</strong> A cove that washes the ceiling,
plus spots on a separate circuit, plus a pendant over the dining, gives a room three
different characters. A single bright central fitting gives it one.</p>
<p><strong>To define a zone in an open plan.</strong> A dropped or slatted section
over the dining in an open-plan living room does more to separate the two than any
furniture arrangement.</p>
<p><strong>To hide genuinely bad slab condition</strong> in an older building.</p>

<h2>Where we recommend against one</h2>
<p><strong>Bedrooms, usually.</strong> A good fan, a well-placed pendant or wall
lights, and a cove only if there is ducting to hide. Most bedroom ceilings in Pune
exist because the quote included them, not because the room needed one.</p>
<p><strong>Small rooms with standard height.</strong> The height loss is
proportionally larger and the visual gain is smaller.</p>
<p><strong>Anywhere the original ceiling is worth seeing</strong> — high ceilings in
<a href="/areas/koregaon-park">Koregaon Park</a> and older Pune stock, which are the
reason to buy the flat and are routinely boxed in.</p>

<h2>Lighting matters more than the ceiling</h2>
<p>Most of what people credit to a beautiful ceiling is actually the lighting in it.
Three principles do the work.</p>
<p><strong>Separate circuits.</strong> The single most valuable lighting decision, and
close to free at wiring stage. Ambient, task and accent lighting on separate switches
means a room can be bright for cooking and low for the evening.</p>
<p><strong>Consistent colour temperature.</strong> Mixing warm and cool white in one
room reads as a mistake even when nobody can identify it. We specify one temperature
per space, usually 2700K to 3000K in living areas and bedrooms.</p>
<p><strong>Light the wall, not the floor.</strong> Downlights in a grid across the
ceiling light the floor and leave the walls dark, which makes a room feel smaller.
Wall-washing and cove light does the opposite.</p>

<h2>Related</h2>
<p>See our <a href="/services/false-ceilings-lighting">false ceilings and lighting
service page</a> and <a href="/guides/interior-design-cost-pune">what a full interior
costs in Pune</a>.</p>

<p>To talk through a ceiling and lighting plan, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a false ceiling cost in Pune?",
         "&#8377;95 to &#8377;150 per square foot for a peripheral gypsum ceiling with a cove, &#8377;150 to &#8377;240 for a full ceiling with profile lighting, and &#8377;320 to &#8377;650 for slatted timber. Lighting fittings and wiring are separate."),
        ("Do bedrooms need a false ceiling?",
         "Usually not. A good fan, a well-placed pendant or wall lights, and a cove only where there is ducting to hide. Most bedroom ceilings in Pune exist because the quote included them rather than because the room needed one."),
        ("How much height does a false ceiling take?",
         "100 to 150mm, at the edges for a peripheral ceiling and across the whole room for a full one. In an older flat where a previous ceiling already took 150mm, adding another is how a room ends up feeling low."),
        ("What is the most valuable lighting decision?",
         "Separate circuits for ambient, task and accent lighting. It costs almost nothing at wiring stage and it is the difference between a room that can be bright for cooking and low for the evening, and one that has a single setting."),
        ("Why does my room feel small despite good lighting?",
         "Probably because downlights in a ceiling grid light the floor and leave the walls dark. Washing the walls with light, or using cove lighting, does the opposite."),
    ],
))

# ------------------------------------------------- HIDDEN COSTS
PAGES.append(dict(
    path="/guides/hidden-costs-interior-design",
    guide=True,
    eyebrow="Guide",
    title="The Interior Costs People Forget to Budget For | Twin Space Studio",
    description="The lines that turn a &#8377;14 lakh interior quote into a &#8377;17 lakh bill in Pune — and how to get them into the number before you sign.",
    h1="The Costs People Forget to Budget For",
    article=True,
    og_image="/assets/opt/c01.jpg",
    crumbs=GC("Hidden interior design costs", "hidden-costs-interior-design"),
    body=DISCLAIMER + gallery(["c01", "f06", "d07"]) + """
<p>Almost every interior project that ends over budget does so for the same handful
of reasons, and design changes are rarely one of them. These are the lines that get
left out of a quote and arrive later, and what to ask before you sign anything.</p>

<h2>Society deposits and charges</h2>
<p>Most Pune societies require a refundable fit-out deposit, commonly
&#8377;15,000 to &#8377;50,000, and some add a non-refundable administrative or
debris charge on top. Townships and larger developments are at the higher end.
The deposit comes back; the charge does not.</p>
<p>Ask the society for the figure in writing before you finalise a budget, and check
whether it is payable by you or by the contractor.</p>

<h2>Material handling and access</h2>
<p>This is the biggest one and the most commonly omitted. If a full-size delivery
vehicle cannot reach your building, material transfers to a smaller vehicle or a
handcart. If the lift will not take sheet material, ply is carried up the stairwell
or cut down and assembled in the flat.</p>
<p>In <a href="/areas/erandwane">Erandwane</a>,
<a href="/areas/koregaon-park">Koregaon Park</a>, older
<a href="/areas/aundh">Aundh</a> and parts of <a href="/areas/pashan">Pashan</a>,
this is normal rather than exceptional. It is a real cost and it belongs in the
quote. A cheaper estimate that assumed a truck could park at the gate is not
cheaper; it is incomplete.</p>

<h2>Electrical work beyond the point count</h2>
<p>Builders provide a point count sized for a much simpler home than anyone actually
lives in. Additional points, dedicated circuits for a hob, oven, chimney or geyser,
and a distribution board upgrade in an older flat are frequently needed and
frequently quoted vaguely.</p>
<p>Ask for the point count and the circuit schedule as line items. "Electrical work"
as a single figure is not a quote.</p>

<h2>Bathrooms in a renovation</h2>
<p>In any flat over fifteen years old, bathroom waterproofing is at or near the end
of its life regardless of how the tiles look. Redoing a bathroom properly —
strip-out, waterproofing, plumbing, tiling, fittings — runs
&#8377;90,000 to &#8377;2.2 lakh each in Pune.</p>
<p>People routinely leave bathrooms out of an interior budget and then discover that
doing everything else while leaving a failing bathroom is a poor sequence, because
fixing it later means opening a finished flat.</p>

<h2>Appliances</h2>
<p>Hob, chimney, oven, dishwasher, geysers, fans and air conditioners are usually not
in an interior quote and can easily total &#8377;1.5 to &#8377;4 lakh. We specify
rather than supply them so you are not paying a margin, but that means the number
sits in your budget rather than ours, and it needs to be there.</p>

<h2>Loose furniture and soft furnishing</h2>
<p>Sofas, dining chairs, mattresses, curtains, rugs and lighting fittings beyond the
fixed ones. Depending on specification this is &#8377;1.5 to &#8377;5 lakh on a
3 BHK. Our quotes state clearly which of these are included and which are not.</p>

<h2>Living somewhere else</h2>
<p>If you cannot stay in the flat during the work, three months of rent is a real
project cost. It is also why roughly half our renovation clients stay in residence —
see <a href="/guides/living-in-during-renovation">living in the flat during a
renovation</a> for how that works and what it adds to the programme.</p>

<h2>The two questions that surface all of it</h2>
<p>Before signing any interior quote in Pune, ask these:</p>
<p><strong>"What is not included in this figure?"</strong> A studio that has thought
about your project can answer immediately and specifically. A vague answer is the
answer.</p>
<p><strong>"Under what circumstances would this number change?"</strong> The honest
answer is: only if you add scope, and then it is quoted and approved before it is
built. Anything else — market rates, material fluctuation, site conditions we will
assess later — is a quote that is not a quote.</p>

<h2>How we handle it</h2>
<p>Our quotes are itemised, and the items that commonly surprise people are stated
separately rather than absorbed: demolition and debris, material handling and access,
electrical points and circuits, and building works in an older flat listed above the
interior lines.</p>
<p>The figure quoted on day one is the figure at handover. That is only possible
because we survey before quoting rather than after.</p>

<p>To have a specific flat quoted properly, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("What costs are usually missing from an interior quote?",
         "Society deposits and charges, material handling where a truck cannot reach the building, electrical work beyond the builder's point count, bathrooms in a renovation, appliances, and loose furniture. Material handling is the most commonly omitted and the most likely to surprise you."),
        ("What should I ask before signing a quote?",
         "Two questions: what is not included in this figure, and under what circumstances would this number change. A studio that has thought about your project answers both immediately and specifically."),
        ("How much is a society fit-out deposit in Pune?",
         "Commonly &#8377;15,000 to &#8377;50,000 refundable, with townships at the higher end. Some societies add a non-refundable administrative or debris charge on top. Get the figure in writing before finalising a budget."),
        ("Does a bathroom need redoing during a renovation?",
         "In any flat over fifteen years old, usually yes — waterproofing has a lifespan regardless of how the tiles look. Budget &#8377;90,000 to &#8377;2.2 lakh per bathroom. Leaving it out means opening a finished flat later."),
        ("Are appliances included in an interior quote?",
         "Not in ours. We specify rather than supply them so you are not paying a margin on a retail item, which means &#8377;1.5 to &#8377;4 lakh sits in your budget rather than ours and needs to be planned for."),
    ],
))

# ------------------------------------------------- PROCESS
PAGES.append(dict(
    path="/guides/interior-design-process",
    guide=True,
    eyebrow="Guide",
    title="Our Interior Design Process, Step by Step | Twin Space Studio",
    description="The six stages of a Twin Space Studio project in Pune, what happens in each, what we need from you, and what you receive at the end of every stage.",
    h1="How an Interior Project Actually Runs",
    article=True,
    og_image="/assets/opt/e03.jpg",
    crumbs=GC("Interior design process", "interior-design-process"),
    body=gallery(["e03", "c06", "a06"]) + """
<p>Every studio publishes a process diagram. This is ours written out properly: what
happens at each stage, what we need from you, what you get, and where projects
usually go wrong.</p>

<h2>Stage 1 — Discover</h2>
<p><strong>What happens:</strong> We meet, at the flat where possible. We measure,
photograph and check the things that decide what is feasible — floor-to-slab height
in more than one place, where the plumbing runs, the distribution board, which walls
are structural, and how material will physically get into the building.</p>
<p><strong>What we need from you:</strong> How you actually live. Who cooks and how
often, who works from home and when, what you own that needs storing, and what
annoyed you about the last home.</p>
<p><strong>What you get:</strong> An honest first read on feasibility and budget
range, before any drawing exists.</p>

<h2>Stage 2 — Conceptualise</h2>
<p><strong>What happens:</strong> We develop the plan — zoning, circulation, where
storage goes and what each room is for. This is the stage that decides whether the
home works. Material and colour follow it rather than leading it.</p>
<p><strong>What we need from you:</strong> Decisions on room use, particularly the
third bedroom in a 3 BHK. Reference images are useful but the plan matters more.</p>
<p><strong>What you get:</strong> Layouts, a design direction and indicative
visuals.</p>

<h2>Stage 3 — Design and plan</h2>
<p><strong>What happens:</strong> Detailed drawings. Elevations for every joinery
run, the electrical layout, the ceiling and lighting plan, and the plumbing changes.
Every unit is drawn to actual dimensions taken on site.</p>
<p><strong>What we need from you:</strong> Sign-off on the electrical layout. This is
the single most schedule-critical approval in the project, because everything behind
the wall depends on it.</p>
<p><strong>What you get:</strong> A complete drawing set and the itemised quote. The
figure on that quote is the figure at handover.</p>

<h2>Stage 4 — Select and finalise</h2>
<p><strong>What happens:</strong> Materials, finishes, hardware and stone are
selected and confirmed. Long-lead items are identified and ordered first. Society
paperwork, registration and lift bookings are started.</p>
<p><strong>What we need from you:</strong> Timely selection, particularly of stone.
Late stone selection is the most common cause of a delayed Pune project, because it
blocks the kitchen and every counter behind it.</p>
<p><strong>What you get:</strong> A confirmed specification and a dated programme.</p>

<h2>Stage 5 — Execute</h2>
<p><strong>What happens:</strong> Site work, in sequence: demolition and civil
changes, electrical and plumbing, ceilings, carpentry, painting, then installation.
Our carpenters build in your flat rather than shipping in flat-pack, so every unit is
fitted to the actual wall.</p>
<p><strong>What we need from you:</strong> Availability for decisions. Most site
questions need an answer within hours, not days.</p>
<p><strong>What you get:</strong> A single point of contact, both founders on the
project, and progress you can see.</p>

<h2>Stage 6 — Deliver and stylise</h2>
<p><strong>What happens:</strong> Snagging, correction, deep cleaning, then styling —
soft furnishing, art placement, the final lighting settings.</p>
<p><strong>What you get:</strong> A finished home and a snag list that has already
been worked through rather than handed to you.</p>

<h2>Where projects actually go wrong</h2>
<p>Three things cause almost every delay, and none of them is design.</p>
<p><strong>Late client decisions</strong>, particularly stone and the electrical
layout, both of which block work behind them.</p>
<p><strong>Society access</strong> that was not confirmed in writing before the
schedule was built.</p>
<p><strong>Starting the conversation after possession</strong> rather than before,
which routinely costs four to five weeks for no design reason.</p>

<h2>Related</h2>
<p>See <a href="/guides/interior-design-timeline">how long each stage takes</a>,
<a href="/guides/interior-design-payment-schedule">how payments are staged</a> and
<a href="/guides/interior-design-cost-pune">what it costs</a>.</p>

<p>To start a project, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("What are the stages of an interior project?",
         "Six: Discover, Conceptualise, Design and plan, Select and finalise, Execute, and Deliver and stylise. Each has a defined output, and the itemised quote is issued at the end of stage three."),
        ("What is the most schedule-critical decision I have to make?",
         "Sign-off on the electrical layout, followed by stone selection. Everything behind the wall depends on the first, and the kitchen and every counter depend on the second."),
        ("Do I get a quote before detailed drawings?",
         "You get an honest budget range at stage one, before any drawing exists. The itemised quote comes with the complete drawing set at the end of stage three, and that figure is the figure at handover."),
        ("Who will I actually be dealing with?",
         "Both founders, from first sketch to snag list. You are not handed to a project manager you have never met once the drawings are signed."),
        ("What causes projects to run late?",
         "Late client decisions on stone and the electrical layout, society access that was not confirmed in writing, and starting the conversation after possession rather than before. Design changes are rarely the cause."),
    ],
))

# ------------------------------------------------- TIMELINE
PAGES.append(dict(
    path="/guides/interior-design-timeline",
    guide=True,
    eyebrow="Guide",
    title="How Long a Full Home Interior Takes in Pune | Twin Space Studio",
    description="Ten to twelve weeks, week by week — what happens when during a Pune home interior, and the three things that actually make a project run late.",
    h1="How Long a Home Interior Takes",
    article=True,
    og_image="/assets/opt/f04.jpg",
    crumbs=GC("Interior design timeline", "interior-design-timeline"),
    body=gallery(["f04", "b01", "d04"]) + """
<p>A full home interior in Pune takes <strong>ten to twelve weeks</strong>, measured
from approved drawings rather than from the first conversation. A duplex runs
thirteen to fifteen. A renovation with the family still living in the flat adds about
two weeks. This page sets out where those weeks actually go.</p>

<h2>Before the clock starts</h2>
<p>Design, drawings, material selection and society paperwork happen before week one,
and they typically take three to five weeks depending on how quickly decisions come
back. This is the part people forget when they say a project took four months.</p>
<p>If you have a possession date, all of it can happen before you collect the keys.
Drawings can be finalised off the builder's plan, material selected and ordered, and
society registration and lift bookings started as soon as the allotment letter
arrives. Families who do this start carpentry in week one. Families who start the
conversation after possession routinely finish four to five weeks later for no
design reason.</p>

<h2>Weeks 1&ndash;2: demolition, civil and services</h2>
<p>Any wall changes, then electrical and plumbing first fix. In a renovation this is
also when the surprises appear — plumbing that is not where the drawing said,
inadequate electrical load, a slab already chased. This is why we survey before
quoting rather than after.</p>
<p>Nothing looks like progress in these two weeks and everything depends on them.</p>

<h2>Weeks 3&ndash;4: ceilings and first carpentry</h2>
<p>False ceilings go in, with the air-conditioning and lighting runs concealed. Once
a ceiling closes, anything that should have been inside it is expensive to add, which
is why the lighting plan is signed before this point.</p>
<p>Carpentry starts in parallel — carcasses built on site and fitted to actual wall
dimensions.</p>

<h2>Weeks 5&ndash;7: the bulk of the joinery</h2>
<p>Kitchen, wardrobes, television unit, entry storage and any bespoke furniture.
This is the longest stretch and the one where being able to reach the flat quickly
matters, because a wall that is 20mm out needs a decision within the hour rather than
next week.</p>

<h2>Weeks 8&ndash;9: finishes</h2>
<p>Shutters, hardware, stone counters, backsplashes, painting. Stone arriving late is
the single most common cause of slippage here, which is why we identify long-lead
items in week one of the design stage rather than week six of the build.</p>

<h2>Weeks 10&ndash;11: installation and snagging</h2>
<p>Lighting fittings, sanitary fittings, appliance installation, and then our own snag
walk — we work through the list before handing it to you rather than after.</p>

<h2>Week 12: styling and handover</h2>
<p>Deep clean, soft furnishing, art placement, final lighting settings, handover.</p>

<h2>The three things that actually cause delay</h2>
<p><strong>Late client decisions.</strong> Stone selection and the electrical layout
block everything behind them. Nothing else you decide has the same effect.</p>
<p><strong>Society access.</strong> A schedule that assumed unrestricted access loses
a fortnight to a lift queue. We collect the rules in writing in week one and build
the sequence around lift slots — see
<a href="/guides/society-rules-interior-work-pune">society rules for interior
work</a>.</p>
<p><strong>Possession waves.</strong> When a tower hands over hundreds of flats at
once, lift slots, electricians, painters and debris trucks all become scarce in the
same fortnight. Being ahead of that wave is the largest single lever on your
timeline.</p>

<h2>What does not cause delay</h2>
<p>Design complexity, in our experience, rarely does. A detailed drawing set built by
carpenters on site runs to schedule more reliably than a simple one improvised in the
flat, because the decisions were made on paper where they are cheap.</p>

<h2>Related</h2>
<p>See <a href="/guides/interior-design-process">the six stages in detail</a>,
<a href="/guides/new-flat-possession-checklist">what to check before you start</a>
and <a href="/guides/interior-design-cost-pune">what it costs</a>.</p>

<p>To discuss a specific timeline, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How long does a full home interior take in Pune?",
         "Ten to twelve weeks from approved drawings. A duplex runs thirteen to fifteen weeks, and a renovation with the family still living in the flat adds about two weeks."),
        ("How long before the build starts?",
         "Design, drawings, material selection and society paperwork take three to five weeks depending on how quickly decisions come back. If you have a possession date, all of it can happen before you collect the keys."),
        ("What is the biggest cause of delay?",
         "Late client decisions on stone and the electrical layout, because both block everything behind them. After that, society access that was not confirmed in writing, and possession waves that make lift slots and trades scarce at once."),
        ("Does a more detailed design take longer to build?",
         "Usually the opposite. A detailed drawing set built by carpenters on site runs to schedule more reliably than a simple one improvised in the flat, because the decisions were made on paper where they are cheap."),
        ("When is the last point I can change the lighting plan?",
         "Before the false ceiling closes, in weeks three to four. After that, anything that should have been inside the ceiling is expensive to add."),
    ],
))

# ------------------------------------------------- PAYMENT SCHEDULE
PAGES.append(dict(
    path="/guides/interior-design-payment-schedule",
    guide=True,
    eyebrow="Guide",
    title="How Interior Design Payments Are Staged | Twin Space Studio",
    description="How we stage payments on a Pune interior project, why they run against milestones rather than dates, and what to watch for in any payment schedule.",
    h1="How Payments Are Staged",
    article=True,
    og_image="/assets/opt/c05.jpg",
    crumbs=GC("Payment schedule", "interior-design-payment-schedule"),
    body=gallery(["c05", "a09", "b02"]) + """
<p>Payment terms tell you more about a contractor than a portfolio does. This page
sets out how we stage payments, the reasoning behind each stage, and what to look for
in anyone else's schedule.</p>

<h2>Against milestones, not dates</h2>
<p>The principle we work to is that you should be paying for work that exists. Our
stages are tied to completed milestones rather than to calendar dates, so a payment
becomes due when something has actually been delivered.</p>
<p>A date-based schedule transfers the risk of delay onto you. If a payment is due in
week six regardless of whether week six's work happened, the incentive to keep the
site moving is weaker than it should be.</p>

<h2>Our stages</h2>
<p><strong>On design engagement.</strong> A design fee to begin drawings, measurement
and concept work. This is chargeable work in its own right, and if you decide not to
proceed to execution, the drawings are yours.</p>
<p><strong>On approval of the drawing set and quote.</strong> The first execution
instalment, which funds material procurement and long-lead ordering. Nothing is
ordered before this, and nothing is ordered without your approved specification.</p>
<p><strong>On completion of civil, electrical and plumbing first fix.</strong> The
unglamorous stage that everything else sits on.</p>
<p><strong>On completion of ceilings and carcass carpentry.</strong> By this point the
shape of the home is visible and verifiable.</p>
<p><strong>On completion of shutters, finishes and painting.</strong></p>
<p><strong>On handover, after snagging.</strong> The final instalment is due when the
snag list has been worked through, not when the site is declared finished.</p>
<p>Holding a meaningful final payment until after snagging matters. A schedule that
takes the last instalment on the day work stops removes the incentive to return for
the small corrections that decide how a home actually feels.</p>

<h2>The quote does not move</h2>
<p>The figure quoted on day one is the figure at handover. The only thing that
changes it is you asking for something additional, and that is quoted and approved in
writing before it is built — never added to a final bill.</p>
<p>This is only possible because we survey before quoting rather than after. A quote
produced without checking the distribution board, the plumbing runs and how material
gets into the building is a guess, and guesses get revised.</p>

<h2>What to watch for in any schedule</h2>
<p><strong>A large advance.</strong> Anything above a modest design fee plus first
material instalment, before drawings are approved, is money at risk against work that
does not yet have a specification.</p>
<p><strong>Date-based stages.</strong> As above: they shift delay risk to you.</p>
<p><strong>No retention against snagging.</strong> If the final payment falls due when
work stops rather than when snags are cleared, expect the snags not to clear.</p>
<p><strong>Vague milestone definitions.</strong> "On completion of carpentry" should
say which carpentry. Ambiguity in a payment trigger always resolves in the
contractor's favour.</p>
<p><strong>Cash-only or unbilled portions.</strong> An interior project is a
substantial purchase and should be documented as one. Ask for proper invoicing with
applicable tax stated.</p>

<h2>What our quote actually contains</h2>
<p>Every line itemised — kitchen against wardrobes against ceiling — so you can move
money between them or defer one. Demolition, debris and material handling stated
separately rather than absorbed. Electrical points and circuits listed rather than
summarised. Building works in an older flat listed above the interior lines so you can
see what is restoration and what is design.</p>
<p>What is <em>not</em> included is stated explicitly too. See
<a href="/guides/hidden-costs-interior-design">the costs people forget to budget
for</a>.</p>

<h2>Related</h2>
<p>See <a href="/guides/interior-design-cost-pune">what a full interior costs in
Pune</a> and <a href="/guides/interior-design-process">the six stages of a
project</a>.</p>

<p>To talk through terms for a specific project, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How are interior design payments staged?",
         "Against completed milestones rather than calendar dates: a design fee to begin, then instalments on approval of the drawing set, on first fix, on ceilings and carcass carpentry, on finishes, and a final instalment on handover after snagging."),
        ("Why milestones rather than dates?",
         "So you are paying for work that exists. A date-based schedule transfers the risk of delay onto you, and weakens the incentive to keep the site moving."),
        ("Should the final payment be held until snagging is done?",
         "Yes. If the last instalment falls due when work stops rather than when snags are cleared, expect the snags not to clear. It is the single most important term in any interior payment schedule."),
        ("Can the quoted price change during the project?",
         "Only if you ask for something additional, and then it is quoted and approved in writing before it is built. The figure quoted on day one is the figure at handover."),
        ("What should worry me in a payment schedule?",
         "A large advance before drawings are approved, date-based stages, no retention against snagging, vague milestone definitions, and any cash-only or unbilled portion. Ambiguity in a payment trigger always resolves in the contractor's favour."),
    ],
))

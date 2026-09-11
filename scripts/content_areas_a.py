# -*- coding: utf-8 -*-
"""Content for the six area pages that have a delivered project behind them."""

from pagegen import gallery

CRUMBS = lambda name, slug: [
    ("Home", "/"),
    ("Areas we serve", "/areas-we-serve"),
    (name, f"/areas/{slug}"),
]

COST_LINKS = (
    '<a href="/guides/interior-design-cost-pune">what a full interior costs in Pune</a>'
)

PAGES = []

# ---------------------------------------------------------------- BANER
PAGES.append(dict(
    path="/areas/baner",
    slug="baner",
    landing=True,
    area_name="Baner",
    hero_image="/assets/opt/e01.jpg",
    hero_subtitle="Our studio is ten minutes away in Mahalunge, and Baner is where we work most often. Full 3 BHK interiors from &#8377;16 lakh, quoted line by line before anything is ordered.",
    title="Best Interior Designers in Baner, Pune | Twin Space Studio",
    description="Interior designers in Baner, Pune. Turnkey 3 BHK, 4 BHK and duplex interiors in 10-12 weeks, with a transparent line-item quote before work begins.",
    h1="Best Interior Designers in Baner, Pune",
    service="Baner, Pune",
    og_image="/assets/areas/interior-designers-baner-pune-living-room-swing.jpg",
    crumbs=CRUMBS("Baner", "baner"),
    body="""
<p>We are a Pune interior design studio based in Mahalunge, about ten minutes
from Baner, and Baner is where we work most often. This page covers what homes
here are actually like, how the three sides of Baner differ, the society
constraints worth knowing before you start, what a full interior costs and where
that budget goes.</p>

<h2>What Baner homes are like</h2>
<p>Baner has become the address most people picture when they imagine a modern
Pune home. The housing runs from high-end 3 and 4 BHK apartments through
low-density towers to duplexes, spread between the Balewadi High Street side and
Pashan Road. Buyers here are mostly senior technology professionals, business
owners and returning NRIs, and they tend to arrive with a clear brief rather
than a blank page.</p>
<p>That changes the conversation. Most Baner clients are not asking what is
possible — they have seen it and want to know what it costs, how long it takes,
and who is accountable when something goes wrong on site. Our answers are a
line-item quote before work starts, ten to twelve weeks for a full home, and a
single point of contact throughout.</p>

<h2>The three sides of Baner, and why it matters</h2>
<p>People say "Baner" as though it were one place. For a fit-out it behaves as
three, and which one you are in changes the schedule more than the design does.</p>
<p><strong>Baner Road and the Balewadi side</strong> holds the newest towers and
most of the duplexes. Lifts are large, service access is planned, and the
societies are professionally managed. Work here is predictable, but the rules
are enforced to the letter.</p>
<p><strong>The Pashan Road and Sus Road edge</strong> is older and lower. Buildings
are four to seven floors, sometimes without a dedicated service lift, and material
has to be carried. That is not a problem if it is priced and scheduled from the
start; it is an expensive surprise if it is not.</p>
<p><strong>The interior lanes off Baner-Pashan Link Road</strong> are a mix of
early-2000s buildings now going through their second round of interiors. Here the
questions are about what is behind the wall rather than what goes on it — original
plumbing, undersized electrical loads, and slabs that have already been chased once.</p>

<h2>What a Baner interior costs</h2>
<p>A full 2 BHK interior runs &#8377;12&ndash;16 lakh and a full 3 BHK
&#8377;16&ndash;21 lakh. Duplex and 4 BHK projects are quoted on scope, since the
additional joinery, the staircase and the second level change the count materially.
A Baner duplex typically lands between &#8377;24 lakh and &#8377;35 lakh depending
on how much of the upper floor is fitted out.</p>
<p>Whatever the size, the quote is itemised before anything is ordered. You can see
what the kitchen costs against the wardrobes and the ceiling, and defer a line if
you would rather spend it elsewhere. The most common trade-off we discuss in Baner
is putting money into kitchen internals and wardrobe hardware — the parts you touch
daily — rather than into additional panelling.</p>

<h2>Working with us in Baner</h2>
<p>We also work in <a href="/areas/balewadi">Balewadi</a>, <a href="/areas/pashan">Pashan</a>, <a href="/areas/sus">Sus</a>, <a href="/areas/aundh">Aundh</a> and <a href="/areas-we-serve">across Pune and PCMC</a>. See also <a href="/services/3-bhk-interior-design">3 BHK interior design</a>, <a href="/services/modular-kitchens">modular kitchens</a> and <a href="/guides/interior-design-cost-pune">what a full interior costs in Pune</a>.</p>
<p>To talk through a home in Baner, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Baner, Pune?",
         "A full 2 BHK interior runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh. Duplex and 4 BHK projects are quoted on scope and typically land between &#8377;24 and &#8377;35 lakh. You receive a transparent line-item quote before any work begins."),
        ("How long does a full home interior take in Baner?",
         "Ten to twelve weeks from approved drawings to final styling, against a dated plan. Duplexes usually run thirteen to fifteen weeks depending on the joinery count."),
        ("Do you handle society permissions and working-hour restrictions?",
         "Yes. Baner societies typically enforce 9am to 6pm working hours, a service-lift booking system, a refundable deposit and worker identity records. We collect the society's rules in the first week and build the schedule around them rather than negotiating mid-project."),
        ("Do you work on duplexes and 4 BHK homes in Baner?",
         "Yes. Baner is where we most often design across two levels, and the approach is to carry one material language floor to floor so the home reads as a single residence rather than two stacked flats."),
        ("Can you work in older buildings near Pashan Road without a service lift?",
         "Yes, and we price it properly. Where material has to be carried, we break joinery into smaller loads and schedule around the society's material-movement window. The cost difference is stated in the quote rather than discovered on site."),
        ("Is the furniture built on site or brought in ready-made?",
         "Built on site. Our carpenters work in the flat so every unit is fitted to the actual wall, which matters in Baner's older buildings where walls are rarely square. Nothing is off the shelf."),
    ],
))

# ---------------------------------------------------------------- KOTHRUD
PAGES.append(dict(
    path="/areas/kothrud",
    slug="kothrud",
    landing=True,
    area_name="Kothrud",
    hero_image="/assets/opt/a01.jpg",
    hero_subtitle="Established societies, older buildings and renovation done with the family still living in the flat. We survey before we quote, and we say when something is worth keeping.",
    title="Best Interior Designers in Kothrud, Pune | Twin Space Studio",
    description="Interior designers in Kothrud, Pune. Renovations and turnkey interiors for established societies and redevelopment flats, in 10-12 weeks with a line-item quote.",
    h1="Best Interior Designers in Kothrud, Pune",
    service="Kothrud, Pune",
    og_image="/assets/areas/interior-designers-kothrud-pune-living-room.jpg",
    crumbs=CRUMBS("Kothrud", "kothrud"),
    body=gallery(["a02", "a01", "a05"]) + """
<p>Kothrud is one of the oldest planned parts of Pune and it behaves differently
from the new-build west. Most of the work here is renovation rather than first
fit-out, often in a home that has been lived in for twenty years, sometimes with
the family still in it. This page covers what that involves, what it costs, how we
work around a family in residence, and a 3 BHK we completed in Dahanukar Colony.</p>

<h2>What Kothrud homes are like</h2>
<p>The building stock runs from 1990s low-rise societies through the Dahanukar
Colony and Karve Road belt to newer redevelopment towers along Paud Road. Flats
tend to be generous in carpet area but conventional in plan — separate kitchen,
a passage, bedrooms off it. The layouts are sound; what dates them is the finish
and the storage.</p>
<p>Owners here are mostly long-settled Pune families, often second generation in
the same flat, and increasingly their adult children taking over the home. The
brief is rarely "make it look new". It is closer to: keep what works, fix what has
aged badly, and make the kitchen and storage behave like a modern home.</p>

<h2>Renovation, not fit-out</h2>
<p>A Kothrud project usually starts with removal rather than installation, and
that is where the surprises live. Twenty-year-old plumbing behind a kitchen wall
is rarely where the drawing says it is. Electrical loads sized for a fridge and two
fans do not carry a modern kitchen. Ceilings have often been dropped once already,
leaving less height than the measurement suggested.</p>
<p>We survey before quoting rather than after. That means opening a small section
of the kitchen wall, checking the distribution board, and measuring floor-to-slab
in three places rather than one. It makes the first quote slightly slower and the
final bill considerably more predictable.</p>
<p>The other renovation-specific question is what stays. Good teak windows,
sound flooring and solid doors are often worth keeping and refinishing, and doing so
frees budget for the kitchen. We say so when it is true, even though a full strip-out
would be a larger project for us.</p>

<h2>Working around a family still living there</h2>
<p>Roughly half our Kothrud clients stay in the flat through the work, usually
because a rented alternative for three months costs more than the saving. It is
workable, but it changes the sequence.</p>
<p>We phase it room by room, with a sealed dust barrier and one bedroom kept
habitable at all times. The kitchen goes last, after a temporary arrangement is set
up, because a family can live without a spare bedroom for a fortnight but not
without somewhere to cook. Wet work — plumbing changes and tiling — is grouped into
a single block so the water is off once rather than six times.</p>
<p>It adds roughly two weeks to a ten-to-twelve week programme. We say that at
quoting stage instead of discovering it in week eight.</p>

<h2>Redevelopment flats on Paud Road</h2>
<p>The newer redevelopment towers are a different job entirely: bare handover, square
walls, and no history to work around. What they bring instead is a compressed
timeline, because possession dates slip and then everyone in the building wants
their fit-out finished before Diwali at the same moment.</p>
<p>Two practical consequences. Book the service lift the week you get possession,
not the week you start. And expect the society's rules to be written by a committee
that has just been formed and is enforcing them with some enthusiasm.</p>

<h2>Inside a Kothrud 3 BHK</h2>
<p>In <a href="/projects/kothrud-3bhk">a 3 BHK in Dahanukar Colony</a> the family
wanted the home to carry art rather than pattern. We built the living room around a
soft blush wall treatment with a stone television panel set against it, kept the
palette warm and low-contrast, and put the storage where it would not be seen.</p>
<p>A pooja unit was set at the entry behind a black-framed glass partition so it
reads as part of the plan rather than an afterthought in a corner. The second
bedroom gained a window seat with drawers beneath it, which is the single most
useful thing you can do to a Kothrud bedroom with a deep sill. The kitchen was
rebuilt as a long galley with a black counter and cream shutters.</p>
""" + gallery(["a06", "a09", "a03", "a04", "a08", "a07"]) + """
<h2>What a Kothrud interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh, the same bands as the rest of Pune. Renovation work carries one additional
line that new-build fit-outs do not: demolition, debris removal and making good.
On a full 3 BHK strip-out in an older Kothrud society that is typically
&#8377;80,000 to &#8377;1.4 lakh, and it is stated separately rather than buried.</p>
<p>Against that, renovations often need less. If the flooring is sound and the doors
are good teak, two significant lines disappear. We have delivered Kothrud homes
below the band because the bones were worth keeping, and we would rather tell you
that than sell a strip-out.</p>

<h2>What Kothrud briefs usually include</h2>
<p>The kitchen is almost always first. A twenty-year-old Kothrud kitchen typically
has a granite platform in reasonable condition and everything around it failing —
shutters that no longer close flush, no drawers where drawers should be, a chimney
that was never adequate, and a dark corner that nobody can reach. Rebuilding it
with proper internals changes daily life more than any other line.</p>
<p>Second is a pooja space with a considered position. In older Kothrud plans it
has usually been squeezed into a passage corner or on top of a kitchen counter.
Given a wall of its own, with the right light and a door that closes, it stops
being a compromise.</p>
<p>Third is storage that matches how long the family has lived there. Twenty years
in one flat produces possessions that a builder-standard wardrobe was never sized
for. We plan for what is actually there — including the things that live in the
loft — rather than for a showroom.</p>
<p>Fourth, and increasingly, a room that works for a parent. Multi-generational
living is common here, and it changes specifications in practical ways: a bed at a
height that is easy to get out of, lever handles instead of knobs, a grab point in
the bathroom that does not look clinical, and lighting that can be bright without
being harsh.</p>

<h2>Where the budget goes on a renovation</h2>
<p>Renovation budgets split differently from new-build fit-outs. Joinery is still
the largest line at roughly half, but demolition, debris and making good take a
share that a new flat never pays. Electrical rewiring is frequently a real line
rather than a nominal one, because a 1990s distribution board will not carry a
modern kitchen with a hob, oven, chimney and dishwasher.</p>
<p>Against that, several new-build costs shrink or disappear. Flooring often stays.
Doors and frames in good teak are refinished rather than replaced. False ceilings
are frequently partial rather than throughout, because the original height is worth
protecting.</p>
<p>The practical consequence is that a Kothrud renovation quote looks different
from a Baner one at the same total. More of it sits in work you will never see, and
less of it in surfaces. That is the right distribution for a home that has to last
another twenty years.</p>

<h2>Getting materials up an older building</h2>
<p>Many Kothrud societies are four to six floors with a single passenger lift and
no service lift. Sheet material does not fit in a passenger lift, which means
either carrying it up the stairwell or cutting it smaller and assembling in the
flat. Both are normal; both need to be in the quote.</p>
<p>Societies here also tend to be strict about the common staircase — it is the
neighbours' route to their own front doors — so we protect it, clear it daily, and
agree a debris removal schedule before the first day rather than after the first
complaint.</p>

<h2>Working with us in Kothrud</h2>
<p>We are based in Mahalunge, about twenty-five minutes from Kothrud, and both
founders visit site through execution. On renovation work that matters more than
usual, because the decisions that cost money are made in the first fortnight when
walls are open and something unexpected has appeared.</p>
<p>We also work in <a href="/areas/erandwane">Erandwane</a>,
<a href="/areas/bavdhan">Bavdhan</a>, <a href="/areas/pashan">Pashan</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. Our service pages cover
<a href="/services/modular-kitchens">modular kitchens</a>,
<a href="/services/wardrobes-storage">wardrobes and storage</a> and
<a href="/services/turnkey-interiors">turnkey execution</a> in more detail.</p>

<p>To talk through a home in Kothrud, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does interior design cost in Kothrud, Pune?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21 lakh. Renovation work in older societies adds a separate demolition and debris line, typically &#8377;80,000 to &#8377;1.4 lakh on a full 3 BHK strip-out."),
        ("Can we keep living in the flat while the work happens?",
         "Yes, and about half our Kothrud clients do. We phase it room by room behind a sealed dust barrier, keep one bedroom habitable throughout and leave the kitchen until last. Expect roughly two additional weeks on the programme."),
        ("Do older Kothrud buildings cause problems for a fit-out?",
         "They raise questions rather than problems: where the plumbing actually runs, whether the electrical load is adequate, and how much ceiling height is left after an earlier false ceiling. We survey before quoting so those answers arrive before the price does."),
        ("Is it worth keeping the existing flooring and doors?",
         "Often, yes. Sound flooring and solid teak doors are worth refinishing rather than replacing, and doing so frees budget for the kitchen. We will tell you when that is the better call."),
        ("How do you get sheet material up a building with no service lift?",
         "Either carried up the stairwell or cut smaller and assembled in the flat. Both are routine in Kothrud and both are priced in the quote, along with staircase protection and a daily debris clearance."),
    ],
))

# ---------------------------------------------------------------- BALEWADI
PAGES.append(dict(
    path="/areas/balewadi",
    slug="balewadi",
    landing=True,
    area_name="Balewadi",
    hero_image="/assets/opt/d03.jpg",
    hero_subtitle="Gated townships around Balewadi High Street, and the question almost every owner asks first: can the kitchen wall come down. Usually yes, and here is what it costs.",
    title="Best Interior Designers in Balewadi, Pune | Twin Space Studio",
    description="Interior designers in Balewadi, Pune. Turnkey 2 BHK and 3 BHK interiors for gated townships near Balewadi High Street, in 10-12 weeks with a line-item quote.",
    h1="Best Interior Designers in Balewadi, Pune",
    service="Balewadi, Pune",
    og_image="/assets/opt/d01.jpg",
    crumbs=CRUMBS("Balewadi", "balewadi"),
    body=gallery(["d01", "d03", "d06"]) + """
<p>Balewadi is township country. Most homes here sit inside large gated
developments near Balewadi High Street and the sports complex, which makes the
flats fairly consistent and the society rules unusually organised. This page covers
what that means for a fit-out, what a 2 or 3 BHK costs, the one change that
transforms a standard Balewadi plan, and a 2 BHK we delivered here.</p>

<h2>What Balewadi homes are like</h2>
<p>The stock is dominated by mid and high-rise towers within planned townships,
mostly built after 2012, with 2 and 3 BHK flats between roughly 650 and 1,150
square feet of carpet area. Builder specification is decent and uniform: vitrified
flooring, a basic kitchen platform, and a granite counter that most owners replace
within the first year.</p>
<p>Buyers are largely dual-income couples working in Hinjawadi and the Baner
corridor, and a meaningful share are first-time owners moving out of rented flats
in Wakad and Pimple Saudagar. The brief is usually practical: make the small flat
work harder, and make it look like an adult home rather than a rental.</p>

<h2>The one change that transforms a Balewadi plan</h2>
<p>Almost every township 2 BHK here has the same weakness — a closed kitchen with a
solid wall between it and the living room, which leaves the living space dark and
the kitchen isolated. Opening that wall, fully or partly, is the single most
effective change available in a Balewadi flat.</p>
<p>It has to be done properly. The wall is usually non-structural, but it often
carries electrical conduit and sometimes a plumbing riser, both of which need
rerouting rather than cutting. Once it is open, a breakfast counter across the
opening gives you a serving edge, two or three seats, and storage on the kitchen
side — which is where the missing storage usually was.</p>
<p>The result is a living room that gets the kitchen window's light and a cook who
is not shut away from the room. In <a href="/projects/balewadi-2bhk">the 2 BHK we
delivered here</a>, that opening changed the flat more than any other line in the
quote.</p>

<h2>Township society rules</h2>
<p>Large Balewadi societies are well organised, which cuts both ways. The paperwork
is clear and predictable: written scope, refundable deposit, worker identity records,
and a defined completion date. The rules are also enforced, and there are a lot of
flats competing for the same two service lifts.</p>
<p>Expect working hours around 9am to 6pm, no Sunday work, and a material-movement
window that may be as narrow as three hours. Some townships restrict debris removal
to specific days. A few require the contractor to be registered with the facility
management company before any gate pass is issued, which takes a few days and is
worth starting early.</p>
<p>We collect all of this in week one. On a tower with two lifts and eighty flats,
the schedule is built around lift slots first and everything else second.</p>

<h2>Storage in a township 2 BHK</h2>
<p>Carpet area here is efficient rather than generous, so storage has to be planned
rather than added. Four decisions do most of the work: wardrobes taken to the
ceiling instead of stopping at a loft, a full-height utility unit beside the
kitchen, drawers built into the window seat, and a shallow entry unit that stops
the foyer accumulating.</p>
<p>Beds with storage below are close to standard in Balewadi, and worth specifying
with hydraulic lifts rather than the hinged type — the difference is whether anyone
actually uses it after the first month.</p>

<h2>Inside a Balewadi 2 BHK</h2>
<p>The <a href="/projects/balewadi-2bhk">2 BHK we completed in Balewadi</a> took the
open-kitchen route. The wall came down, a breakfast counter went across the opening
with storage below on the kitchen side, and the dining moved under a slatted timber
ceiling with a single pendant over it.</p>
<p>The living room got a television unit with a cane-textured panel beside it and a
green sofa that carries the palette. The master bedroom took a glossy wardrobe run
and an upholstered headboard; the second bedroom took an arched wardrobe in soft
green and a study that doubles as a dressing table.</p>
""" + gallery(["d02", "d04", "d05", "d07"]) + """
<h2>What a Balewadi interior costs</h2>
<p>A full 2 BHK runs &#8377;12&ndash;16 lakh and a full 3 BHK &#8377;16&ndash;21
lakh, quoted line by line before anything is ordered. Opening the kitchen wall and
building the counter across it typically adds &#8377;55,000 to &#8377;90,000
including the electrical rerouting, and it is the line we most often recommend
protecting when a budget needs trimming elsewhere.</p>
<p>Because township flats are consistent, our Balewadi quotes are unusually
predictable — we have measured enough of the same builder layouts to know what the
joinery count will be before we arrive. That does not make it cheaper, but it makes
the first number closer to the last one.</p>

<h2>Where the budget goes in a township flat</h2>
<p>In a Balewadi 2 BHK, the kitchen is usually the single largest item at roughly a
quarter of the project, because it is being replaced entirely rather than modified.
Wardrobes and bedroom joinery take another quarter. The living room — television
unit, panelling, any partition work — takes about a fifth. False ceilings and
lighting take a little over a tenth, and the remainder covers electrical work,
painting, soft furnishing and supervision.</p>
<p>Builder-standard flats have one advantage here: because the plan is known and
square, there is less on-site adjustment and less waste than in an older building.
That shows up as a tighter gap between the quoted figure and the final one, not as
a lower headline price.</p>
<p>The place we most often see money wasted in Balewadi is over-specified panelling
in the living room and under-specified hardware in the kitchen. Panelling is what
photographs; hinges, channels and a properly sized chimney are what you use every
day. When something has to give, we recommend it gives on the wall.</p>

<h2>How Balewadi compares with the areas around it</h2>
<p>People choosing Balewadi are usually also looking at Baner, Wakad and Sus, and
the fit-out implications differ more than the property listings suggest.</p>
<p>Against <a href="/areas/baner">Baner</a>, Balewadi flats are typically smaller
and more uniform, which means a lower total and a more predictable quote, but less
scope for the double-height and duplex work Baner allows. Against
<a href="/areas/wakad">Wakad</a>, the townships here are newer and better organised,
so society paperwork is smoother and lift access is better planned. Against
<a href="/areas/sus">Sus</a>, Balewadi is further along — the societies are
established, the rules are settled, and the surrounding infrastructure is finished
rather than promised.</p>
<p>The practical read: Balewadi is the most predictable place we work. If you want
a fixed programme and a quote that does not move, the township stock here is the
easiest in Pune to deliver against.</p>

<h2>Timing around possession</h2>
<p>Township possessions come in waves, and when a tower hands over, thirty families
start fit-outs in the same month. Lift slots, painters and even debris trucks get
scarce. If you have a possession date, the useful move is to have drawings approved
before you get the keys so work can start in week one rather than week five.</p>
<p>Ten to twelve weeks from approved drawings is the normal programme for a full
2 or 3 BHK here.</p>

<h2>Working with us in Balewadi</h2>
<p>Our studio is in Mahalunge, roughly fifteen minutes from Balewadi High Street, so
site visits are same-day rather than scheduled for next week. Both founders stay on
the project through execution.</p>
<p>We also work in <a href="/areas/baner">Baner</a>, <a href="/areas/wakad">Wakad</a>,
<a href="/areas/sus">Sus</a>, <a href="/areas/mahalunge">Mahalunge</a> and
<a href="/areas-we-serve">across Pune and PCMC</a>. For detail on individual
elements, see <a href="/services/modular-kitchens">modular kitchens</a>,
<a href="/services/wardrobes-storage">wardrobes and storage</a> and
<a href="/services/2-bhk-interior-design">2 BHK interior design</a>.</p>

<p>To talk through a home in Balewadi, call Pooja Dhoot on
<a href="tel:+918208093011">+91 82080 93011</a> or Dimple Marathe on
<a href="tel:+918888177217">+91 88881 77217</a>.</p>
""",
    faqs=[
        ("How much does a 2 BHK interior cost in Balewadi?",
         "A full 2 BHK runs &#8377;12&ndash;16 lakh, quoted line by line before anything is ordered. Opening the kitchen wall and building a breakfast counter across it typically adds &#8377;55,000 to &#8377;90,000 including electrical rerouting."),
        ("Can the kitchen wall be opened in a township flat?",
         "Usually yes — in most Balewadi townships that wall is non-structural. It often carries electrical conduit and sometimes a plumbing riser, both of which need rerouting rather than cutting. We confirm on site before it is quoted."),
        ("How do township society rules affect the schedule?",
         "Large Balewadi societies enforce working hours, service-lift booking and material-movement windows, and many require the contractor to be registered with the facility management company first. We collect the rules in week one and build the sequence around lift slots."),
        ("How long does a full 2 BHK take in Balewadi?",
         "Ten to twelve weeks from approved drawings. If you have a possession date, getting drawings approved before you collect the keys is what turns a fifteen-week project into a ten-week one."),
        ("Do you work in the townships near Balewadi High Street?",
         "Yes. Most of our Balewadi work sits inside the large gated developments around the High Street and the sports complex, so we already know how the common builder layouts behave."),
    ],
))

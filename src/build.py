"""Bygger index.html (norsk) og en/index.html (engelsk) fra template.html.

Kjør fra repo-roten:  python3 src/build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://geirlislebousnno.github.io/karusell/"
TEMPLATE = (ROOT / "src" / "template.html").read_text(encoding="utf-8")

NB = {
    "lang": "nb",
    "url": BASE,
    "ogLocale": "nb_NO",
    "docTitle": "Corioliseffekten – ballkast på karusellen (interaktiv simulering)",
    "title": "Ballkast på karusellen",
    "ogTitle": "Ballkast på karusellen – se corioliseffekten",
    "metaDesc": "Interaktiv simulering av corioliseffekten. En ball kastes fra kanten av en roterende karusell mot sentrum, og banen vises samtidig fra bakken (treghetssystem) og fra karusellen (roterende referansesystem).",
    "ogDesc": "Kast en ball på en roterende karusell og se banen fra bakken og fra karusellen side om side. Gratis simulering for fysikkundervisning.",
    "aboutJson": json.dumps(["Corioliseffekten", "Corioliskraft", "Roterende referansesystem", "Treghetssystem"], ensure_ascii=False),
    "redirect": "<script>try{if(new URLSearchParams(location.search).get('lang')==='en')location.replace('en/')}catch(e){}</script>",
    "langNav": '<span aria-current="page" lang="nb">NO</span><a href="en/" lang="en" hreflang="en">EN</a>',
    "lede": "En person står på kanten av en roterende karusell (radius 5 m) og triller en ball rett mot sentrum. Sett fra bakken går ballen i en rett linje. Sett fra karusellen bøyer banen av, fordi karusellen dreier seg under ballen mens den er underveis. Det er corioliseffekten.",
    "gTag": "Treghetssystem", "gTitle": "Sett fra bakken",
    "gAria": "Karusellen sett ovenfra fra bakken. Karusellen roterer, og ballen går i en rett linje.",
    "wTag": "Roterende referansesystem", "wTitle": "Sett fra karusellen",
    "wAria": "Karusellen sett fra en som står på den. Karusellen står stille, og ballens spor bøyer av.",
    "legPath": "Ballens bane over bakken", "legTraceRot": "Sporet på karusellen (roterer med)",
    "legTrace": "Sporet på karusellen", "legAim": "Siktelinje fra kasteren",
    "settings": "Innstillinger", "readings": "Måleverdier",
    "modeL": "Kasteretning", "modeIn": "Fra kanten mot sentrum", "modeOut": "Fra sentrum mot kanten",
    "omegaL": "Vinkelhastighet ω", "omegaH": "Positiv verdi betyr rotasjon mot klokka. Endringen gjelder fra neste kast.",
    "speedL": "Kastefart relativt til karusellen",
    "aimL": "Siktevinkel", "aimH": "0° er rett mot sentrum. Prøv å sikte slik at ballen treffer sentrum.",
    "slowL": "Avspillingsfart", "keep": "Behold tidligere spor",
    "throw": "Kast ballen", "pause": "Pause", "clear": "Fjern spor",
    "rT": "Tid siden kast", "rV": "Ballens fart over bakken", "rRim": "Kanthastighet ωR",
    "rCor": "Coriolisakselerasjon 2ωv", "rMiss": "Nærmeste avstand til sentrum",
    "explainOut": "I sentrum har karusellen ingen fart, så ballen går rett utover over bakken. Mens ballen er underveis, flytter mottakeren seg med kanten. Sett fra karusellen bøyer banen av i en spiral, fordi <b>corioliskraften</b> virker mot kasterens høyre side når karusellen roterer mot klokka. For å treffe må kasteren sikte <b>ωR/v</b> radianer foran mottakeren.",
    "explain": "Når ballen slippes, har den både kastefarten innover og kantens fart sidelengs (<b>ωR</b>). Over bakken går den derfor skrått og rett frem. Sett fra karusellen ser det ut som en sidekraft, <b>corioliskraften</b>, bøyer banen. Den virker mot kasterens høyre side når karusellen roterer mot klokka, slik som på den nordlige halvkule.",
    "article": """
    <section>
      <h2>Hva er corioliseffekten?</h2>
      <p>Corioliseffekten er den tilsynelatende avbøyningen av en bevegelse når den observeres fra et roterende referansesystem, for eksempel en karusell eller jorda. Ingen ekte kraft skyver ballen sidelengs. Avbøyningen oppstår fordi observatøren selv roterer.</p>
      <p>For å beskrive bevegelsen fra det roterende systemet innfører man en tenkt kraft, corioliskraften:</p>
      <p><span class="eq">F = −2m ω × v</span></p>
      <p>Når farten står vinkelrett på rotasjonsaksen, er størrelsen 2mωv. Kraften står alltid vinkelrett på farten, så den endrer retningen, men ikke farten.</p>
    </section>
    <section>
      <h2>Hvorfor bøyer banen av?</h2>
      <p>Når ballen slippes, har den kantens fart ωR sidelengs i tillegg til kastefarten. Over bakken går den deretter i en rett linje. Kasteren følger karusellen i en bue og dreier hele tiden mot venstre når karusellen roterer mot klokka. Sett fra kasteren ser det derfor ut som ballen glir mot høyre.</p>
      <p>Kaster man fra sentrum og ut, får ballen ingen sidefart, fordi karusellen står stille i sentrum. Over bakken går ballen rett ut langs en radius, mens mottakeren på kanten flytter seg. Sett fra karusellen blir banen en spiral. Her er avbøyningen ren corioliseffekt, uten bidrag fra kantens fart.</p>
      <p>Krumningsradien i det roterende systemet er omtrent v/(2ω). Lav kastefart eller rask rotasjon gir altså en krappere bue. På karusellen virker også sentrifugalkraften mω²r utover. Den får sporet til å drive utover, og derfor blir det en sløyfe og ikke en ren sirkel.</p>
    </section>
    <section>
      <h2>Corioliseffekten på jorda: vind, lavtrykk og havstrømmer</h2>
      <p>Sett ovenfra Nordpolen roterer jorda mot klokka, akkurat som karusellen med positiv ω. Derfor avbøyes vind, havstrømmer og prosjektiler mot høyre på den nordlige halvkule og mot venstre på den sørlige.</p>
      <p>Luft og vann som beveger seg fritt, går i sirkler med klokka på den nordlige halvkule. Det kalles treghetssvingninger, og det er samme dreieretning som ballen i simuleringen. Lavtrykk roterer likevel mot klokka. Trykkraften trekker lufta inn mot sentrum, corioliskraften bøyer den mot høyre, og lufta ender opp med å sirkle rundt lavtrykket med sentrum på venstre side. Rundt et høytrykk går lufta med klokka.</p>
      <p>Jordas vinkelhastighet er bare 7,29 · 10⁻⁵ rad/s. Effekten merkes derfor over store avstander og lang tid, men bestemmer ikke hvilken vei vannet virvler i en vask.</p>
    </section>
    <section>
      <h2>Prøv selv</h2>
      <ul>
        <li>Juster siktevinkelen slik at ballen treffer sentrum ved ω = 0,6 rad/s og v = 4 m/s. Regn ut vinkelen først og sjekk svaret i simuleringen. <span class="hint">Hint: Sidekomponenten av kastefarten må oppheve kantfarten ωR.</span></li>
        <li>Velg «Fra sentrum mot kanten». Hvor mange grader må du sikte foran mottakeren for å treffe ved ω = 0,6 rad/s og v = 4 m/s? <span class="hint">Hint: Ballen bruker tiden t = R/v ut til kanten. Hvor langt har mottakeren dreid på den tiden?</span></li>
        <li>Senk kastefarten til 1–2 m/s. Hvorfor danner sporet en sløyfe når du kaster fra kanten, men ikke fra sentrum?</li>
        <li>Sett ω til en negativ verdi. Banen bøyer nå mot venstre, som på den sørlige halvkule.</li>
        <li>Sett ω = 0. Banen blir rett i begge vinduene.</li>
        <li>Doble ω og se hvordan coriolisakselerasjonen og krumningen endrer seg.</li>
      </ul>
    </section>""",
    "by": "Laget av Geir Lislebo", "lic": "Lisens:",
    "licUrl": "https://creativecommons.org/licenses/by/4.0/deed.no",
    "source": "Kildekode på GitHub",
    "js": {"missIn": "Nærmeste avstand til sentrum", "missOut": "Bom ved kanten",
           "aimHIn": "0° er rett mot sentrum. Prøv å sikte slik at ballen treffer sentrum.",
           "aimHOut": "0° er rett mot mottakeren på kanten. Prøv å sikte slik at ballen treffer mottakeren.",
           "dec": ",", "ccw": "mot klokka", "cw": "med klokka", "still": "i ro",
           "left": "mot venstre", "right": "mot høyre", "straight": "rett frem",
           "pause": "Pause", "resume": "Fortsett"},
}

EN = {
    "lang": "en",
    "url": BASE + "en/",
    "ogLocale": "en_GB",
    "docTitle": "Coriolis effect – throwing a ball on a merry-go-round (interactive simulation)",
    "title": "Throwing a ball on a merry-go-round",
    "ogTitle": "Throwing a ball on a merry-go-round – see the Coriolis effect",
    "metaDesc": "Interactive Coriolis effect simulation. A ball is thrown from the edge of a rotating merry-go-round towards the centre, shown side by side from the ground (inertial frame) and from the merry-go-round (rotating reference frame).",
    "ogDesc": "Throw a ball on a rotating merry-go-round and compare its path from the ground and from the platform. Free simulation for physics teaching.",
    "aboutJson": json.dumps(["Coriolis effect", "Coriolis force", "Rotating reference frame", "Inertial frame"]),
    "redirect": "",
    "langNav": '<a href="../" lang="nb" hreflang="nb">NO</a><span aria-current="page" lang="en">EN</span>',
    "lede": "A person stands at the edge of a rotating merry-go-round (radius 5 m) and rolls a ball straight towards the centre. Seen from the ground, the ball moves in a straight line. Seen from the merry-go-round, the path curves, because the platform turns underneath the ball while it travels. This is the Coriolis effect.",
    "gTag": "Inertial frame", "gTitle": "Seen from the ground",
    "gAria": "The merry-go-round seen from above, from the ground. It rotates and the ball moves in a straight line.",
    "wTag": "Rotating reference frame", "wTitle": "Seen from the merry-go-round",
    "wAria": "The merry-go-round seen by someone standing on it. It is still and the ball’s trace curves.",
    "legPath": "Ball’s path over the ground", "legTraceRot": "Trace on the platform (rotates with it)",
    "legTrace": "Trace on the platform", "legAim": "Thrower’s line of aim",
    "settings": "Settings", "readings": "Readings",
    "modeL": "Throw direction", "modeIn": "From the edge inwards", "modeOut": "From the centre outwards",
    "omegaL": "Angular velocity ω", "omegaH": "Positive means anticlockwise. Changes apply from the next throw.",
    "speedL": "Throw speed relative to the platform",
    "aimL": "Aim angle", "aimH": "0° points straight at the centre. Try aiming so the ball hits the centre.",
    "slowL": "Playback speed", "keep": "Keep earlier traces",
    "throw": "Throw the ball", "pause": "Pause", "clear": "Clear traces",
    "rT": "Time since throw", "rV": "Ball’s speed over the ground", "rRim": "Rim speed ωR",
    "rCor": "Coriolis acceleration 2ωv", "rMiss": "Closest distance to centre",
    "explainOut": "At the centre the merry-go-round has no speed, so the ball moves straight outwards over the ground. While the ball travels, the catcher moves with the rim. Seen from the merry-go-round, the path bends into a spiral, because the <b>Coriolis force</b> acts towards the thrower’s right when the platform turns anticlockwise. To hit, the thrower must aim <b>ωR/v</b> radians ahead of the catcher.",
    "explain": "When the ball is released it carries both the inward throw speed and the sideways speed of the rim (<b>ωR</b>). Over the ground it therefore travels in a straight, slanted line. Seen from the merry-go-round, it looks as if a sideways force, the <b>Coriolis force</b>, bends the path. It acts towards the thrower’s right when the platform turns anticlockwise, as in the Northern Hemisphere.",
    "article": """
    <section>
      <h2>What is the Coriolis effect?</h2>
      <p>The Coriolis effect is the apparent deflection of a moving object when it is observed from a rotating reference frame, such as a merry-go-round or the Earth. No real force pushes the ball sideways. The deflection appears because the observer is rotating.</p>
      <p>To describe the motion from the rotating frame, we introduce a fictitious force, the Coriolis force:</p>
      <p><span class="eq">F = −2m ω × v</span></p>
      <p>When the velocity is perpendicular to the rotation axis, its magnitude is 2mωv. The force is always perpendicular to the velocity, so it changes the direction of motion but not the speed.</p>
    </section>
    <section>
      <h2>Why does the path curve?</h2>
      <p>When the ball is released it has the rim’s sideways speed ωR in addition to the throw speed. Over the ground it then moves in a straight line. The thrower follows the platform around a circle and keeps turning to the left when it rotates anticlockwise. From the thrower’s point of view, the ball therefore drifts to the right.</p>
      <p>When the ball is thrown from the centre outwards, it gets no sideways speed, because the platform is at rest at the centre. Over the ground the ball moves straight out along a radius while the catcher on the rim moves on. Seen from the merry-go-round, the path becomes a spiral. Here the deflection is a pure Coriolis effect, with no contribution from the rim speed.</p>
      <p>The radius of curvature in the rotating frame is roughly v/(2ω), so a slow throw or fast rotation gives a tighter curve. On the merry-go-round the centrifugal force mω²r also acts outwards. It makes the trace drift outwards, which is why it forms a loop rather than a clean circle.</p>
    </section>
    <section>
      <h2>The Coriolis effect on Earth: wind, low pressure and ocean currents</h2>
      <p>Seen from above the North Pole, the Earth rotates anticlockwise, just like the merry-go-round with positive ω. That is why winds, ocean currents and projectiles are deflected to the right in the Northern Hemisphere and to the left in the Southern Hemisphere.</p>
      <p>Air and water moving freely travel in clockwise circles in the Northern Hemisphere. These are called inertial oscillations, and they turn the same way as the ball in the simulation. Low-pressure systems still rotate anticlockwise. The pressure force pulls air towards the centre, the Coriolis force bends it to the right, and the air ends up circling the low with the centre on its left. Around a high, air circulates clockwise.</p>
      <p>The Earth’s angular velocity is only 7.29 × 10⁻⁵ rad/s. The effect matters over large distances and long times, but it does not decide which way water swirls in a sink.</p>
    </section>
    <section>
      <h2>Try it yourself</h2>
      <ul>
        <li>Adjust the aim angle so the ball hits the centre at ω = 0.6 rad/s and v = 4 m/s. Calculate the angle first, then check it in the simulation. <span class="hint">Hint: the sideways component of the throw must cancel the rim speed ωR.</span></li>
        <li>Choose “From the centre outwards”. How many degrees ahead of the catcher must you aim to hit at ω = 0.6 rad/s and v = 4 m/s? <span class="hint">Hint: the ball takes t = R/v to reach the rim. How far has the catcher turned in that time?</span></li>
        <li>Lower the throw speed to 1–2 m/s. Why does the trace form a loop when thrown from the edge, but not from the centre?</li>
        <li>Set ω to a negative value. The path now curves to the left, as in the Southern Hemisphere.</li>
        <li>Set ω = 0. The path is straight in both views.</li>
        <li>Double ω and watch how the Coriolis acceleration and the curvature change.</li>
      </ul>
    </section>""",
    "by": "Made by Geir Lislebo", "lic": "Licence:",
    "licUrl": "https://creativecommons.org/licenses/by/4.0/",
    "source": "Source code on GitHub",
    "js": {"missIn": "Closest distance to centre", "missOut": "Miss at the rim",
           "aimHIn": "0° points straight at the centre. Try aiming so the ball hits the centre.",
           "aimHOut": "0° points straight at the catcher on the rim. Try aiming so the ball hits the catcher.",
           "dec": ".", "ccw": "anticlockwise", "cw": "clockwise", "still": "at rest",
           "left": "left", "right": "right", "straight": "straight",
           "pause": "Pause", "resume": "Resume"},
}


def render(d):
    html = TEMPLATE
    d = dict(d)
    html = html.replace("{{jsStrings}}", json.dumps(d.pop("js"), ensure_ascii=False))
    for k, v in d.items():
        html = html.replace("{{" + k + "}}", v)
    assert "{{" not in html, "uerstattet plassholder"
    return html


(ROOT / "index.html").write_text(render(NB), encoding="utf-8")
(ROOT / "en").mkdir(exist_ok=True)
(ROOT / "en" / "index.html").write_text(render(EN), encoding="utf-8")
print("Bygget index.html og en/index.html")

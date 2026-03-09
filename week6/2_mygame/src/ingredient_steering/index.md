# Steering

Misschien is het leuker om een unit een richting te geven waarin het
beweegt zodat je kan sturen in plaats van alleen naar
links/recht/boven/onder te bewegen. Kijk dan naar de
[steering.py](steering.py) voorbeeldcode.

![steering.gif](steering.gif)

# Polar to Cartesian

In deze code wordt de
[pygame.Vector2.from_polar](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.from_polar)
method gebruikt voor het omzetten van een polar coordinaat naar een
cartesian coordinaat zoals uitgelegd in [Math is Fun, Polar and
Cartesian
Coordinates](https://www.mathsisfun.com/polar-cartesian-coordinates.html) wat je waarschijnlijk eerder bij een wiskunde vak gehad
hebt. Maar, omdat deze wiskunde is ingebouwd (encapsulated) in de
`pygame.Vector2` class kunnen we het gebruiken zonder over de details
na te hoeven denken (abstraction) wat het programmeren een stuk
makkelijker en de code een stuk leesbaarder maakt.

# Lineaire Algebra

In plaats van een polar coordinaat met een 'angle' kun je ook een matrix gebruiken (Lineaire Algebra met numpy) om de richting te representeren. Dit kan het makkelijker maken om complexere dingen te doen zoals ook de viewpoort roteren. Kijk hiervoor naar de [steering_linalg.py](steering_linalg.py) voorbeeldcode.

This module defines classes representing non-periodic and periodic sites. It provides two main classes: Site and PeriodicSite. The Site class represents a general non-periodic atomic site. It stores the atomic species, Cartesian coordinates, and optional properties such as magnetic moment or label. The PeriodicSite class extends Site by adding lattice information, enabling periodic boundary conditions and operations relevant to crystalline materials.

The module applies several object-oriented programming (OOP) concepts.
It defines classes (Site, PeriodicSite) and uses inheritance: PeriodicSite inherits from Site and adds new attributes (_lattice, _frac_coords) and methods related to periodicity.
It also demonstrates encapsulation, since many attributes are private (e.g. _species, _coords, _lattice) and accessed through properties like x, y, z, or frac_coords.
Method overriding is used — for example, both classes define their own versions of __repr__, __eq__, and distance() to handle different behaviors.
Polymorphism appears when both classes share the same interface (as_dict(), from_dict(), distance()), allowing them to be used interchangeably.
The code also uses properties (via @property) for controlled attribute access, and serialization through as_dict() and from_dict() methods using MontyEncoder and MontyDecoder.

Many dunder (magic) methods are implemented to integrate with Python’s data model.
__init__ initializes the object; __repr__ and __str__ provide readable text output; __eq__ compares two sites for equality, using coordinate tolerance; __hash__ allows objects to be stored in sets or used as dictionary keys; __getitem__ retrieves the occupancy of an element; __lt__ defines a sort order based on electronegativity; and __contains__ supports “in” operations for checking if an element is part of the species.
These methods make the classes behave naturally with Python syntax.

The difference between the two classes is that Site is non-periodic and stores Cartesian coordinates only, while PeriodicSite includes a lattice and fractional coordinates. The PeriodicSite class adds methods such as distance_and_image(), to_unit_cell(), and is_periodic_image() that compute distances under periodic boundary conditions and handle equivalent sites in crystals. In other words, Site is used for isolated or molecular systems, and PeriodicSite is used for periodic solids.
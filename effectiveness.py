n = "Normal"
f = "Fighting"
p = "Poison"
g = "Ground"
r = "Rock"
b = "Bug"
s = "Steel"
w = "Water"
e = "Electric"
i = "Ice"
d = "Dragon"
fa = "Fairy"
da = "Dark"
fl = "Flying"
gh = "Ghost"
fi = "Fire"
gr = "Grass"
ps = "Psychic"

super_eff = "Super Effective:"
not_very = "Not Very Effective:"
poke_type = "Type:"


def normal():
    super_effective = [""]
    not_very_effective = [gh, f]

    print(poke_type, n)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def fighting():
    super_effective = [i, s, r, n]
    not_very_effective = [da, fa, ps, gh, fl]

    print(poke_type, f)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def flying():
    super_effective = [gr, b, f]
    not_very_effective = [i, e, r]

    print(poke_type, fl)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def poison():
    super_effective = [fa, gr]
    not_very_effective = [ps, s, g]

    print(poke_type, p)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def ground():
    super_effective = [e, fi, s, r, p]
    not_very_effective = [fl, i, gr, w]

    print(poke_type, g)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def rock():
    super_effective = [i, fi, b, fl]
    not_very_effective = [gr, w, s, g, f]

    print(poke_type, r)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def bug():
    super_effective = [ps, gr]
    not_very_effective = [fi, r, fl]

    print(poke_type, b)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def ghost():
    super_effective = [ps, gh, f, n]
    not_very_effective = [da, gh, n]

    print(poke_type, gh)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def steel():
    super_effective = [fa, i, r]
    not_very_effective = [fi, g, f]

    print(poke_type, s)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def fire():
    super_effective = [i, gr, s, b]
    not_very_effective = [w, r, g]

    print(poke_type, fi)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def water():
    super_effective = [fi, r, g]
    not_very_effective = [e, gr]

    print(poke_type, w)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)


def grass():
    super_effective = [w, r, g]
    not_very_effective = [i, fi, b, p, fl]

    print(poke_type, gr)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)

def electric():
    super_effective = [w, fl]
    not_very_effective = [g]

    print(poke_type, e)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)

def psychic():
    super_effective = [p, f]
    not_very_effective = [gh, b]

    print(poke_type, ps)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)

def ice():
    super_effective = [d, gr, g, fl]
    not_very_effective = [fi, s, r, f]

    print(poke_type, i)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)

def dragon():
    super_effective = [d]
    not_very_effective = [fa, d, i]

    print(poke_type, d)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)

def fairy():
    super_effective = [d, f]
    not_very_effective = [da, s, p]

    print(poke_type, fa)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)

def dark():
    super_effective = [ps, gh]
    not_very_effective = [da, fa, f]

    print(poke_type, da)

    for x in super_effective:
        print(super_eff, x)

    for x in not_very_effective:
        print(not_very, x)
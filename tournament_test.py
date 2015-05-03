# Test cases for tournament.py


from tournament import *

def test_delete_matches():
    delete_matches()
    print "1. Old matches can be deleted."

def test_delete():
    delete_matches()
    delete_athletes()
    print "2. Athletes records can be deleted."

def test_count():
    delete_matches()
    delete_athletes()
    c = count_athletes()
    if c == '0':
        raise TypeError(
            "countAthletes() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countAthletes should return zero.")
    print "3. After deleting, countAthletes() returns zero."

def test_register():
    delete_matches()
    delete_athletes()
    register_athlete("Lizbeth Numbela")
    c = count_athletes()
    if c != 1:
        raise ValueError(
            "After one athlete registers, countAthletes() should be 1.")
    print "4. After registering an athlete, countAthletes() returns 1."

def test_register_count_delete():
    delete_matches()
    delete_athletes()
    register_athlete("Marcelo Espinoza")
    register_athlete("Jose Honor")
    register_athlete("Mauricio Arevalo")
    register_athlete("Abraham Espinoza")
    c = count_athletes()
    if c != 4:
        raise ValueError(
            "After registering four athletes, countAthletes should be 4.")
    delete_athletes()
    c = count_athletes()
    if c != 0:
        raise ValueError("After deleting, countAthletes should return zero.")
    print "5. Athletes can be registered and deleted."


def test_standings_before_matches():
    delete_matches()
    delete_athletes()
    register_athlete("Marcelo Avalos")
    register_athlete("Ricardo Arias")
    standings = athlete_standings()
    if len(standings) < 2:
        raise ValueError("Athletes should appear in athlete_standings even before they have fought any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered athletes should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each athlete_standings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered athletes should have no matches or wins.")
    if set([name1, name2]) != set(["Marcelo Avalos", "Ricardo Arias"]):
        raise ValueError("Registered athletes' names should appear in standings, even if they have no matches fought.")
    print "6. Newly registered athletes appear in the standings with no matches."


def test_report_matches():
    delete_matches()
    delete_athletes()
    register_athlete("Marcelo Vargas")
    register_athlete("Javier Torrico")
    register_athlete("Marco Grageda")
    register_athlete("Juan Escobar")
    standings = athlete_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_match(id1, id2)
    report_match(id3, id4)
    standings = athlete_standings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each athlete should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, athletes have updated standings."


def test_pairings():
    delete_matches()
    delete_athletes()
    register_athlete("Claudia Mayorga")
    register_athlete("Wendy Riss")
    register_athlete("Marcela Soria")
    register_athlete("Kelly guzman")
    standings = athlete_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_match(id1, id2)
    report_match(id3, id4)
    pairings = swiss_pairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four athletes, swissPairings should return two pairs.")
    [(aid1, aname1, aid2, aname2), (aid3, aname3, aid4, aname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([aid1, aid2]), frozenset([aid3, aid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, athletes with one win should be paired.")
    print "8. After one match, athletes with one win are paired."


if __name__ == '__main__':
    test_delete_matches()
    test_delete()
    test_count()
    test_register()
    test_register_count_delete()
    test_standings_before_matches()
    test_report_matches()
    test_pairings()
    print "Success!  All tests pass!"

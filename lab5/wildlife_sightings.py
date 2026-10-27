"""Wildlife sanctuary sightings logging and analysis."""
import hashlib
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE sightings "
    "(id INTEGER PRIMARY KEY, species TEXT, zone TEXT, count INTEGER)"
)


def log_sighting(connection, species, zone, count, extras=None):
    """Record a wildlife sighting and update species totals."""
    if extras is None:
        extras = {}
    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count)
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Generate a short identifier for an observer."""
    return hashlib.sha256(observer.encode()).hexdigest()[:6]


def zone_summary(connection, zone):
    """Return the total number of sightings in a zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()
    if row[0] is None:
        return 0
    return row[0]


def rarest(connection):
    """Return the species with the lowest total sightings."""
    rows = connection.execute(
        "SELECT species, SUM(count) FROM sightings GROUP BY species"
    ).fetchall()
    rarest_species = min(rows, key=lambda row: row[1])
    return rarest_species[0]


def main():
    """Run the wildlife sightings demonstration."""
    totals = log_sighting(conn, "Leopard", "North", 1)
    log_sighting(conn, "Chital", "North", 24, totals)
    log_sighting(conn, "Hornbill", "East", 3, totals)
    if len(totals) != 3:
        raise ValueError("Expected three species in totals")
    print(observer_id("Arun"), zone_summary(conn, "North"), rarest(conn))


main()

SCHEMA_CONTEXT = """
The database is Chinook, a SQLite relational database for a digital music store.

All ID columns are INTEGER PRIMARY KEY.
Foreign keys are INTEGER and reference the corresponding primary keys.
Text fields are stored as NVARCHAR or TEXT.
Prices and totals are NUMERIC.
Dates are stored as DATETIME (TEXT in SQLite).

Tables and columns:

Artists(
  ArtistId INTEGER PRIMARY KEY,
  Name NVARCHAR
)

Albums(
  AlbumId INTEGER PRIMARY KEY,
  Title NVARCHAR,
  ArtistId INTEGER NOT NULL REFERENCES Artist(ArtistId)
)

Tracks(
  TrackId INTEGER PRIMARY KEY,
  Name NVARCHAR NOT NULL,
  AlbumId INTEGER REFERENCES Album(AlbumId),
  MediaTypeId INTEGER NOT NULL REFERENCES MediaType(MediaTypeId),
  GenreId INTEGER REFERENCES Genre(GenreId),
  Composer NVARCHAR,
  Milliseconds INTEGER NOT NULL,
  Bytes INTEGER,
  UnitPrice NUMERIC NOT NULL
)

Genres(
  GenreId INTEGER PRIMARY KEY,
  Name NVARCHAR
)

Media_Types(
  MediaTypeId INTEGER PRIMARY KEY,
  Name NVARCHAR
)

Customers(
  CustomerId INTEGER PRIMARY KEY,
  FirstName NVARCHAR NOT NULL,
  LastName NVARCHAR NOT NULL,
  Company NVARCHAR,
  Address NVARCHAR,
  City NVARCHAR,
  State NVARCHAR,
  Country NVARCHAR,
  PostalCode NVARCHAR,
  Phone NVARCHAR,
  Fax NVARCHAR,
  Email NVARCHAR NOT NULL,
  SupportRepId INTEGER REFERENCES Employee(EmployeeId)
)

Employees(
  EmployeeId INTEGER PRIMARY KEY,
  LastName NVARCHAR NOT NULL,
  FirstName NVARCHAR NOT NULL,
  Title NVARCHAR,
  ReportsTo INTEGER REFERENCES Employee(EmployeeId),
  BirthDate DATETIME,
  HireDate DATETIME,
  Address NVARCHAR,
  City NVARCHAR,
  State NVARCHAR,
  Country NVARCHAR,
  PostalCode NVARCHAR,
  Phone NVARCHAR,
  Fax NVARCHAR,
  Email NVARCHAR
)

Invoices(
  InvoiceId INTEGER PRIMARY KEY,
  CustomerId INTEGER NOT NULL REFERENCES Customer(CustomerId),
  InvoiceDate DATETIME NOT NULL,
  BillingAddress NVARCHAR,
  BillingCity NVARCHAR,
  BillingState NVARCHAR,
  BillingCountry NVARCHAR,
  BillingPostalCode NVARCHAR,
  Total NUMERIC NOT NULL
)

Invoice_Items(
  InvoiceLineId INTEGER PRIMARY KEY,
  InvoiceId INTEGER NOT NULL REFERENCES Invoice(InvoiceId),
  TrackId INTEGER NOT NULL REFERENCES Track(TrackId),
  UnitPrice NUMERIC NOT NULL,
  Quantity INTEGER NOT NULL
)

Playlists(
  PlaylistId INTEGER PRIMARY KEY,
  Name NVARCHAR
)

Playlist_Track(
  PlaylistId INTEGER NOT NULL REFERENCES Playlist(PlaylistId),
  TrackId INTEGER NOT NULL REFERENCES Track(TrackId),
  PRIMARY KEY (PlaylistId, TrackId)
)

Relationships:
- One Artist → Many Albums
- One Album → Many Tracks
- One Track → One Genre, One MediaType
- One Genre → Many Tracks
- One MediaType → Many Tracks
- One Customer → Many Invoices
- One Invoice → Many InvoiceItems
- One InvoiceItem → One Track
- One Employee → Many Customers (SupportRepId)
- Employees can report to other Employees (ReportsTo)
- Playlists and Tracks have a many-to-many relationship via PlaylistTrack
"""
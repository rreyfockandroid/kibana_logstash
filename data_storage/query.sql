 desc books;
┌──────────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│     column_name      │ column_type │  null   │   key   │ default │  extra  │
│       varchar        │   varchar   │ varchar │ varchar │ varchar │ varchar │
├──────────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ author_key           │ VARCHAR[]   │ YES     │ NULL    │ NULL    │ NULL    │
│ author_name          │ VARCHAR[]   │ YES     │ NULL    │ NULL    │ NULL    │
│ cover_edition_key    │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ cover_i              │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ edition_count        │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ first_publish_year   │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ has_fulltext         │ BOOLEAN     │ YES     │ NULL    │ NULL    │ NULL    │
│ key                  │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ language             │ VARCHAR[]   │ YES     │ NULL    │ NULL    │ NULL    │
│ public_scan_b        │ BOOLEAN     │ YES     │ NULL    │ NULL    │ NULL    │
│ title                │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ ia                   │ VARCHAR[]   │ YES     │ NULL    │ NULL    │ NULL    │
│ ia_collection_s      │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ lending_edition_s    │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ lending_identifier_s │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ subtitle             │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
├──────────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┤
│ 16 rows                                                          6 columns │
└────────────────────────────────────────────────────────────────────────────┘


create table books as select * from read_json_auto('books_openlib.json');

select author_name from books where array_contains(author_name, 'Django Wexler');

select unnest(author_name) as name, list_aggregate(author_name, 'count') as count from books order by count;

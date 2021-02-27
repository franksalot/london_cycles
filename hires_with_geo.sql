SELECT 
h.duration, 
h.duration / 60 as duration_minutes, 
h.start_date,
h.end_date,
f.latitude as start_lat, 
f.longitude as start_long, 
ST_GEOGPOINT(f.longitude, f.latitude) as from_p,
t.latitude as end_lat, 
t.longitude as end_long,
ST_GEOGPOINT(t.longitude, t.latitude) as to_p
FROM `bigquery-public-data.london_bicycles.cycle_hire` h 
INNER JOIN  `bigquery-public-data.london_bicycles.cycle_stations` f 
    ON f.id = h.start_station_id
INNER JOIN  `bigquery-public-data.london_bicycles.cycle_stations` t 
    ON t.id = h.end_station_id



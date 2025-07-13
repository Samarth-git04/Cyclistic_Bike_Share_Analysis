CREATE VIEW trip_analysis AS WITH trip_analysis_CTE AS (
	SELECT ride_id,
		rideable_type,
		started_at::date AS start_date,
		started_at::time AS start_time,
		start_station_id,
		start_station_name,
		ended_at::date AS end_date,
		CASE
			EXTRACT(
				DOW
				FROM started_at::date
			)
			WHEN 0 THEN 'SUNDAY'
			WHEN 1 THEN 'MONDAY'
			WHEN 2 THEN 'TUESDAY'
			WHEN 3 THEN 'WEDNESDAY'
			WHEN 4 THEN 'THURSDAY'
			WHEN 5 THEN 'FRIDAY'
			WHEN 6 THEN 'SATURDAY'
		END AS day_of_week,
		CASE
			EXTRACT(
				MONTH
				FROM started_at::date
			)
			WHEN 1 THEN 'January'
			WHEN 2 THEN 'February'
			WHEN 3 THEN 'March'
			WHEN 4 THEN 'April'
			WHEN 5 THEN 'May'
			WHEN 6 THEN 'June'
			WHEN 7 THEN 'July'
			WHEN 8 THEN 'August'
			WHEN 9 THEN 'September'
			WHEN 10 THEN 'October'
			WHEN 11 THEN 'November'
			WHEN 12 THEN 'December'
		END AS month,
		ended_at::time AS end_time,
		end_station_id,
		end_station_name,
		ROUND(
			EXTRACT(
				EPOCH
				FROM (ended_at - started_at)
			) / 60,
			2
		) AS trip_duration_minutes,
		member_casual
	FROM cyclistic_trips
)
SELECT *
FROM trip_analysis_CTE;
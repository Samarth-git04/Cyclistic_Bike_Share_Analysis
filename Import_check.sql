SELECT
  TO_CHAR(started_at, 'YYYY-MM') AS month,
  COUNT(*) AS num_trips
FROM
  cyclistic_trips
GROUP BY
  month
HAVING TO_CHAR(started_at, 'YYYY-MM') = '2024-06'
ORDER BY
  month;
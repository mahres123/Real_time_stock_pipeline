SELECT
  predicted_last_price,
  *
FROM
  ML.PREDICT(
    MODEL `your_project.stock_dataset.price_regressor`,
    (
      SELECT
        volume,
        average_price,
        open,
        high,
        low,
        close,
        EXTRACT(HOUR FROM TIMESTAMP(timestamp)) AS hour
      FROM
        `your_project.stock_dataset.external_table`
      WHERE last_price IS NOT NULL
      LIMIT 10
    )
  );
-- Étape 1 : Entraînement du modèle multivarié par instrument_token
CREATE OR REPLACE MODEL `your_project.stock_dataset.price_forecast_multi`
OPTIONS (
  model_type = 'ARIMA_PLUS',
  time_series_timestamp_col = 'timestamp',
  time_series_data_col = 'last_price',
  time_series_id_col = 'instrument_token',
  horizon = 10,
  auto_arima = TRUE
) AS
SELECT
  TIMESTAMP(timestamp) AS timestamp,
  CAST(instrument_token AS STRING) AS instrument_token,
  last_price
FROM
  `your_project.stock_dataset.external_table`
WHERE
  last_price IS NOT NULL
ORDER BY
  instrument_token, timestamp;


-- Étape 2 : Prédictions pour les 10 prochaines valeurs de chaque instrument_token
SELECT
  *
FROM
  ML.FORECAST(
    MODEL `your_project.stock_dataset.price_forecast_multi`,
    STRUCT(10 AS horizon)
  );
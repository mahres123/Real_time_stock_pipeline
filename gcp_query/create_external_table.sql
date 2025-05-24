CREATE OR REPLACE EXTERNAL TABLE `your_project.stock_dataset.external_table`
OPTIONS (
  format = 'JSON',
  uris = ['gs://your-bucket-name/data/stock_data_sample.json']
);

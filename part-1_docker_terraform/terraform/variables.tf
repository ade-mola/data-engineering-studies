locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
  description = "GCP Project ID"
}

variable "region" {
  description = "Region for GCP resorces"
  default = "europe-west6"
  type = string
}

variable "storage_class" {
    description = "Storage class for bucket"
    default = "STANDARD"  
}

variable "BQ_DATASET" {
  description = "BigQuery dataset that data will be written to"
  type = string
  default = "trips_data_all"
}
variable "credentials" {
  description = "Service Account Credentials"
  default     = "../../keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "terraform-demo-413314"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage bucket name"
  default     = "terraform-demo-413314-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}
resource "random_id" "test" {
  byte_length = "8"
}
output "randoutputs" {
  description = "Random id"
  value = "${random_id.test}"
}


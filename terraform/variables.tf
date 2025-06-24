variable "aws_region" {
  default = "us-east-1"
}

variable "services" {
  default = ["auth", "product", "cart", "order", "payment", "review"]
}

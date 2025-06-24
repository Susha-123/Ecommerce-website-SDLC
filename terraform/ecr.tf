resource "aws_ecr_repository" "repos" {
  for_each = toset(var.services)
  name     = each.key
}

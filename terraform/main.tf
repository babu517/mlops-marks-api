terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "mlops" {
  name         = "mlops-marks-api:latest"
  keep_locally = true
}

resource "docker_container" "mlops" {
  image = docker_image.mlops.image_id
  name  = "mlops-terraform"
  ports {
    internal = 8000
    external = 8001
  }
}

output "url" {
  value = "http://localhost:8001/predict?marks=80"
}

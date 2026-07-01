
resource "aws_instance" "devops_server" {

  ami = "ami-01a00762f46d584a1"

  instance_type = "m7i-flex.large"

  key_name = "mohankeyindia"


  tags = {

    Name = "Devops-2tier-server"
  }
}

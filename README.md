# AWS DEPLOY ALMOST FREE

For explanation on the repo see this video: <br>
https://youtu.be/xxjtPHSPA9w  <br>

A minimal FastAPI todo API backed by Postgres, with Alembic migrations and Docker Compose. <br>


```sh
# Build image locally
docker compose up -d
```

## Create EC2 Intance
download PEM and save as repository secrect

### install docker and git
```sh
sudo yum update -y
sudo yum install -y docker git
sudo service docker start
sudo usermod -aG docker ec2-user

sudo mkdir -p /usr/local/lib/docker/cli-plugins

sudo curl -SL https://github.com/docker/compose/releases/download/v5.1.0/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
docker compose version

sudo curl -SL https://github.com/docker/buildx/releases/download/v0.32.1/buildx-v0.32.1.linux-amd64 -o /usr/local/lib/docker/cli-plugins/docker-buildx
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-buildx
docker buildx version
```

### clone YOUR repo
```sh
sudo git clone https://github.com/nivitzhaky/cicd.git
```

### add inbound rule 
TCP port 8000  mask 0.0.0.0/0

```sh
cd cicd
sudo docker compose up -d
```
### test
test machineip:8000

### change H1 title 
commit and push and test again

### buy a xyz domain on godaddy
do not take any protection <br>
choose one year <br>
goto: https://account.godaddy.com/myrenewals <br>
choose cancel plan
### create hosted zone in AWS
https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=us-east-1#
### copy records to godaddy
https://account.godaddy.com/products <br>
DNS <br>
update nameservers from aws
### ACM request AWS
ask for domain.name and *.domain.name <br>
click create records in Route53 <br>
wait for verification (can take long time) 
### Cloudfront
origin type -> public DNS of your Ec2 <br>
edit origin change to http only and put port 8000 <br>
in behaviours -> cache policy -> CachingDisabled <br>
### Route53
Hosted zoned -> your domain -> create record <br>
A record -> alias to cloudfront -> choose the cloudfront <br>
CMANE -> www -> no alias -> put your cloudfront url <br>





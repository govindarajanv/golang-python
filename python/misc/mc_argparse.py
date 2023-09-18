import argparse

managed_services = {
    "aws": "rds, ecs, eks",
    "azure": "aks, cosmosdb",
    "gcp": "cloudrun, gke",
}

parser = argparse.ArgumentParser(prog='mcms',description="multi-cloud managed services.",epilog='Please refer the documentation for more details')
parser.add_argument("cloud", type=str,help="choose one from aws,azure,gcp")
parser.add_argument('--color', choices=['red', 'green', 'blue'])
parser.add_argument("-r", "--region", help="aws region")
args = parser.parse_args()

ms = managed_services.get(args.cloud, "")
print(ms)

if args.region:
    print(f"region chosen: {args.region}")

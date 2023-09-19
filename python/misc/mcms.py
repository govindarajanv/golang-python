import argparse
def is_positive(n):
    n = int(n)
    if n <= 0:
        raise argparse.ArgumentTypeError("Must be a positive integer")
    return n
    
managed_services = {
    "aws": "rds, ecs, eks",
    "azure": "aks, cosmosdb",
    "gcp": "cloudrun, gke",
}

parser = argparse.ArgumentParser(prog='mc',description="multi-cloud managed services.",epilog='Please refer the documentation for more details')
mcms_group = parser.add_argument_group('ms', 'Multi-Cloud Managed Services')
mcms_group.add_argument("-v", "--verbose", action="store_true", help="Verbosity")
mcms_group.add_argument('--cloud', choices=['aws', 'azure', 'gcp'],type=str,help="choose one from aws,azure,gcp",required=True)
mcms_group.add_argument("-r", "--region", help="aws region", default="global")
mcms_group.add_argument("-q", "--quantity", type=is_positive, help="A positive integer")
 

# Create an argument group for cost-related options
#parser = argparse.ArgumentParser(description="A program to demonstrate argument grouping.")
finops_group = parser.add_argument_group('finops', 'Multi-Cloud Cost Management')

finops_group.add_argument("-n", "--notify", help="cost related notifications")
finops_group.add_argument("-b", "--budget", help="set budgets")


args = parser.parse_args()
ms = managed_services.get(args.cloud, "")
print(f"Managed services in {args.cloud} are {ms}")

if args.region:
    print(f"region chosen: {args.region}")

if args.verbose:
    print("verbosity:", args)  
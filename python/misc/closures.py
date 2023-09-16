# Closures needs nested functions

def get_instances(cloud_account,ondemand=True):
    def on_demand():
        return (f"returning list of on-demand instances for account {cloud_account}")
        
    def reserved():
        return (f"returning list of reserved instances for account {cloud_account}")
    if ondemand:
        return on_demand
    else:
        return reserved
        
if __name__ == "__main__":
    instances = get_instances("12345")
    print (instances())
    instances = get_instances("12345",False)
    print (instances())
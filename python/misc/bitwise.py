from enum import IntFlag

class Role(IntFlag):
    REPO_READ = 8
    REPO_WRITE = 4 
    REPO_MODIFY = 2 
    REPO_ADMIN = REPO_READ | REPO_WRITE | REPO_MODIFY
    WORKSPACE_MODIFY = 1
    WORKSPACE_ADMIN = REPO_ADMIN | WORKSPACE_MODIFY


developer = Role.REPO_READ | Role.REPO_WRITE
#print ("Developer has",developer)
dev_lead = Role.REPO_ADMIN 
release_manager = Role.REPO_READ
org_admin = Role.WORKSPACE_ADMIN


print ("Common accesses between developer and dev_lead are", developer & dev_lead)
print ("Extra accesses that lead has when compared with the developer are", developer ^ dev_lead)
print ("Accesses that a team consisting of a release manager and a developer have are",developer | release_manager)
print ("Accesses that a team consisting of a release manager and a developer will not have are",~(developer | release_manager))

# wallet is available at 50% discount while belt is at no discount, ring's price is up by 50%
class ItemPrice(IntFlag):
    WALLET = 200
    BELT = 500
    RING = 25000
    

print ("final price of the selected wallet",ItemPrice.WALLET >> 1)
print ("final price of the selected belt",ItemPrice.BELT)
print ("final price of the selected ring",ItemPrice.RING << 1)

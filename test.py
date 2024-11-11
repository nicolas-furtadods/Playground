import boto3
import json
import os
from os import path
import getopt,sys

#### SCRIPT PARAMETERS
options = "r:"
run_options = ["network", "ipam", "resolved_rules","hosted_zones","all"]
long_options = ["run_option="]
chosen_option = "all"

#### MAIN IDENTIFIER
irt = "a2742"
trigram = "sbx"
env = "hml"
main_identifier = irt.upper() + "_" + trigram.upper() + "_" + env.upper


##### - NETWORK STATIC VARIABLES
vpc_name = main_identifier + "VPC"
##### - IPAM STATIC VARIABLES
##### - RESOLVER RULES STATIC VARIABLES
##### - HOSTED_ZONES STATIC VARIABLES

def import_network_resources():
    # This function will list import network resources
    print("--- Function import_network_resources ----")
    # This list will contain resources to be imported
    import_map = {}
    # This list will contain errors
    resources_not_found_list = []

    # Open the necessary resources
    print("Loading resources S3")
    s3 = boto3.resource('s3')
    print("Loading resources EC2")
    ec2 = boto3.resource('ec2')

    # S3 Bucket
    for bucket in s3.buckets.all():
        if(bucket.name == "nicolasfdslogs"):
            print("Bucket matching naming convention found...")
            import_map["module.infra.bucket"] = bucket.name
            break
    if("module.infra.bucket" not in import_map):
        resources_not_found_list.append("No resource found - - module.infra.bucket ")

    ## Print the list of resources to be imported
    print("--- Resources found that will be imported ----")
    keys = import_map.keys()
    for key in keys:
        print("terraform import",key, import_map[key])

    # Print the error 
    print("ERROR : RESOURCES NOT FOUND FOR FUNCTION import_network_resources")
    for x in resources_not_found_list:
        print(x)

def import_ipam_cidrs():
    print("")
def import_resolver_rules():
    print("")

def import_hosted_zones():
    print()

### MAIN 
def main(argv):
    print ("--- Script INIT -- Checking Arguments ---")
    # ----- Argument Parsing --- BEGINS
    try:
        arguments, values = getopt.getopt(argv, options, long_options)
    except getopt.GetoptError:
        print("usage: test.py -r <run_option>")
        print("Do not specify aguments -r | --run_option to perform the full script")
        print("<run_option> : ipam, network, resolver_rules, hosted_zones")
        sys.exit(2)
    for currentArgument,currentValue in arguments:
        if(currentArgument == '-h'):
            print("usage: test.py -r <run_option>")
            print("Do not specify aguments -r | --run_option to perform the full script")
            print("<run_option> : ipam, network, resolver_rules, hosted_zones")
            sys.exit() 
        elif currentArgument in ("-r", "--run_option"):
            chosen_option = currentValue
    # ----- Argument Parsing --- ENDS

    ## 
    print ("--- Script RUN START ---")

    ## Choose profile

    ## Choose Coretech

    ## Load Functions based on INPUTS
    if(chosen_option == "all"):
        print("No run_option provider, the script will impact all resources")
    else:
        print("Chosen option for script:", chosen_option)
        
    match chosen_option:
        case "network":
            import_network_resources()
        case "ipam":
            import_ipam_cidrs()
        case "resolver_rules":
            import_resolver_rules()
        case "hosted_zones":
            import_hosted_zones()
        case _:
            import_network_resources()
            import_ipam_cidrs()
            import_resolver_rules()
            import_hosted_zones()

    print("--- Script RUN FINISHED ---")

if __name__ == "__main__":
   main(sys.argv[1:])
    #import_network_resources()
# https://docs.python.org/3/library/subprocess.html
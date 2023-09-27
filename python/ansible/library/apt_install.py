#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def perform_action(module, package_name):
    cmd = "apt install -y " + package_name
    rc, stdout, stderr = module.run_command(cmd, check_rc=True)
    return stdout

def main():
    module = AnsibleModule(
        argument_spec=dict(
            package_name=dict(required=True, type='str'),
        )
    )

    package_name = module.params['package_name']

    if package_name is None:
       module.fail_json(msg='Please provide package name')
       
    result = perform_action(module, package_name)

    module.exit_json(changed=True, msg=result)
if __name__ == '__main__':
    main()
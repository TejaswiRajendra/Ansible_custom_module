#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module_args = dict(
        name=dict(type='str', required=False, default='World')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    name = module.params['name']

    message = "This is Tejaswi R."

    result = dict(
        changed=False,
        original_message=message,
        generated_message=message
    )
    
    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()
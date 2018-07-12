[![Build Status](https://travis-ci.org/slated/ansible-rabbitmq-role.svg?branch=master)](https://travis-ci.org/slated/ansible-rabbitmq-role)

Rabbitmq
========

Add repos and packages for RabbitMQ. Configure listen addresses,
plugins, users, and vhosts.

Requirements
------------

An installed Ubuntu server. 

Role Variables
--------------

Ubuntu distro, e.g., 'xenial'

    rabbitmq_distribution: '{{ ansible_distribution_release }}'

Apt packages for rabbitmq server install

    rabbitmq_packages:
      - erlang
      - rabbitmq-server

Rabbitmq plugins

    rabbitmq_plugins:
      - rabbitmq_management
      - rabbitmq_tracing
      - rabbitmq_federation

An admin user with access to all vhosts

    rabbitmq_admin_user:
      username: admin
      password: admin

Users with policymaker access to their vhost

    rabbitmq_users:
      - username: user
        password: user
        vhost: user

Listen address and port
    rabbitmq_listen_address: 127.0.0.1
    rabbitmq_listen_port: 5672

Max memory to access; can be as high as .9 for beefy dedicated rabbit server

    rabbitmq_memory_high_watermark: .25

Vars for rabbitmq-env.conf

    rabbitmq_conf_env:
      RABBITMQ_NODE_IP_ADDRESS: '{{ rabbitmq_listen_address }}'

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: taskbrokers
      tasks:
        - import_role:
            name: rabbitmq
          vars:
            rabbitmq_admin_user:
              username: myadmin
              password: mypassword
            rabbitmq_users:
              - username: me
                password: mepassword
                vhost: mehost
              - username: my
                password: mypassword
                vhost: myhost

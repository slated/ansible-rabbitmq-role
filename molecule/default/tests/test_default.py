import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rabbitmq_server_is_installed(host):
    rabbitmq_server = host.package('rabbitmq_server')

    assert rabbitmq_server.is_installed


def test_rabbitmq_server_is_running(host):
    rabbitmq_server = host.service('rabbitmq-server')

    assert rabbitmq_server.is_running
    assert rabbitmq_server.is_enabled


def test_rabbitmq_server_config_is_existed(host):
    rabbitmq_server = host.file("/etc/rabbitmq/rabbitmq.config")
    assert rabbitmq_server.exists

# Test application

There is a dockerized web application with ansible playbook for automated deploying.

Web application was written on Python+Flask. Nginx is a web server.

The database is Mysql. There was used the test dump from there https://github.com/datacharmer/test_db

## Installation

1. Install Ansible.

```
    sudo apt-get -y install software-properties-common
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get -y update
    sudo apt-get -y install ansible git
    sudo ansible-galaxy install angstwad.docker_ubuntu
```

2. Create rsa keys to use key-based authentication.

```
    ssh-keygen -t rsa
```

3. Open the home directory and check out git repository with the test application.

```
    cd ~ && git clone https://github.com/sybertuk/test_app.git
```

4. Go to the project directory and create the inventory file "hosts" from the default template.

```
    cd test_app && cp hosts.default hosts
```

5. Edit hosts file and add your hosts for provisioning.

    Each host should be specified according to following template:

    {Host IP/domain name} ansible_ssh_user='%username%' ansible_ssh_pass='%ssh_password%' ansible_sudo_pass='%sudo_password%'

    For example:
```
    192.168.0.1 ansible_ssh_user='user' ansible_ssh_pass='mypass123' ansible_sudo_pass='mypass123'
```

6. Set do not check hosts for ssh connections.

```
    export ANSIBLE_HOST_KEY_CHECKING=False
```

7. Run ansible playbook for provisioning the servers from inventory file 'hosts'

```
    ansible-playbook -i hosts web_app_docker.yml
```

## Testing the installation

    Ater installing, you can find the web application running on 80 port on each provisioned host. 
    URL for host 192.168.0.1 will be: http://192.168.0.1

## Tips
Once the playbook 'web_app_docker.yml' was run one time for the host at least you can delete ssh and sudo password from hosts file since rsa key was installed to remote host. For example:

```
    192.168.0.1 ansible_ssh_user='user'
```
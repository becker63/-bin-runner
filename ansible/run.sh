yay -S ansible && yay -S sshpass && export ANSIBLE_HOST_KEY_CHECKING=False && ansible-playbook -i hosts playbook.yml -e ansible_password='jidw'

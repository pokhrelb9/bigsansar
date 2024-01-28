



def call_ssh(user):

    ssh_config ="" \
                "\n" \
                "Protocol 2" \
                "\n" \
                "Match User *,!{0}" \
                "\n" \
                "   ChrootDirectory %h" \
                "\n" .format(user)
    
    return ssh_config



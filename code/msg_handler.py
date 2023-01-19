
def handle_user_msg(message) -> str:
    p_message = message.lower()
    if p_message == '!help':
        return "Work in progress"
    else: 
        return 'I don\'t know what that means. Try typing "!help".'

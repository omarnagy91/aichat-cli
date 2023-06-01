import os
import pyperclip

ascii_art = '''
    __     _                        ______ __            __ 
   / /    (_)____ ___   ___        / ____// /_   ____ _ / /_
  / /    / // __ `__ \ / _ \      / /    / __ \ / __ `// __/
 / /___ / // / / / / //  __/     / /___ / / / // /_/ // /_  
/_____//_//_/ /_/ /_/ \___/______\____//_/ /_/ \__,_/ \__/  
                          /_____/                           
'''


def store_conversation(user_input, bot_response, bot_name, conversation):
    conversation.append((user_input, bot_response, bot_name))


def insert_clipboard_message(conversation, chatbot, current_bot, dir):
    clipboard_text = pyperclip.paste()
    if clipboard_text:
        print("\nClipboard contents:\n")
        print(clipboard_text)
        print("\n")
        option = clipboard_text.strip()
        response = chatbot(option.replace('\n', ' '), current_bot, dir)
        store_conversation(option, response, current_bot, conversation)


def export_conversation(conversation, ascii_art):
    filename = input("Enter the file name: ")
    filename += ".txt"
    directory = "conv"  # default name, you can change it
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        file.write(ascii_art)
        for user_input, bot_response, bot_name in conversation:
            file.write("#######################\n")
            file.write(f"**USER**: {user_input}\n")
            file.write(f"**BOT**: {bot_response}\n")
        file.write("\n***conversation exported by limebot_cli***")
        file.close()
    print(f"Conversation exported to {filepath}.")


def print_menu():
    print("-" * 50)
    print("[1] - Change the bot (somtimes buggy)")
    print("[2] - Insert clipboard contents as message")
    print("[3] - Export conversation to .txt file")
    print("[0] - Close the program")
    print("\nType your message or choose an option:\n")


def change_bot():
    bot_input = input(
        "[1] - Sage (tweaked 3.5gpt_turbo) 4096 token\n[2] - ChatGPT (default) 4096 token\n[3] - GPT4(slower,more accurate) 8192 token \n[4] - Claude (default, FAST) 4500 token\n[5] - Claude+ (more creative, FASTER) 9000 token\n[6] - Claude_100K (BETA, very long messages) 100000 token\n\nChoose your bot: ")
    if bot_input == "1":
        bot = "sage"
    elif bot_input == "2":
        bot = "chatgpt"
    elif bot_input == "3":
        bot = "beaver"
    elif bot_input == "4":
        bot = "claude"
    elif bot_input == "5":
        bot = "claudeplus"
    elif bot_input == "6":
        bot = "claudehunk"
    else:
        print("Invalid input, please try again.")
    return bot


def close_program():
    pass

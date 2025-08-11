from instagrapi import Client

cl = Client()
cl.login("first_experimant_", "gaja gaja")
member_file = "members.txt"

def get_members():
    try:
        with open(member_file, "r") as f:
            members = f.read().splitlines()
    except FileNotFoundError:
        members = []
    return members

def add_member(username):
    members = get_members()
    if username not in members:
        members.append(username)
        with open(member_file, "w") as f:
            f.write("\n".join(members))
        return len(members)
    else:
        return None

def send_welcome_message(user_id, serial_number, username):
    message = f"স্বাগতম @{username}! আপনি আমাদের গ্রুপের {serial_number} নম্বর সদস্য।"
    cl.direct_send(message, [user_id])

def main():
    new_members = ["new_user1", "new_user2"]

    for username in new_members:
        serial = add_member(username)
        if serial:
            user_id = cl.user_id_from_username(username)
            send_welcome_message(user_id, serial, username)
            print(f"Message sent to {username} with serial {serial}")

if __name__ == "__main__":
    main()

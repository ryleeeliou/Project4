class User:
    def __init__(self,username):
        self.username = username 
        self.music_collection = {}
#methods for the class (manipulates songs and artist info)
    def add_song(self, title, artist):
        self.music_collection[title] = artist 
        print(f"Added song: {title} by {artist}")

    def get_song(self,title):
        artist = self.music_collection.get(title)
        if artist:
            print(f"Song: {title} by {artist}")
        else:
            print(f"Song '{title}' not found in current collection.")

    def update_song(self, title, new_artist):
        if title in self.music_collection: 
            self.music_collection[title] = new_artist
            print(f"Updated song: {title} to new artist: {new_artist}.")
        else:
            print(f"Song '{title}' not found in current collection.")

    def delete_song(self, title):
        if title in self.music_collection:
            del self.music_collection[title]
            print(f"Deleted song: {title}")
        else:
            print(f"Song '{title}' not found in currect collection.")

    def display_all_songs(self):
        if self.music_collection:
            print("Music Collection (All Songs):")
            for title, artist in self.music_collection.items():
                print(f"Title: {title} by {artist}.")
        else:
            print("No songs in current collection.")

#adds and changes users
class music_collection_organizer:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            print(f"User '{username}' added successfully!")
        else:
            print(f"User '{username}' is already in the system.")


    def change_user(self, username):
        if username in self.users:
            self.current_user = self.users[username]
            print(f"Switched to user '{username}'.")
        else:
            print(f"User '{username}' does not exist. Please add user to the system first. ")
#main program
    def program(self): 
        while True:
            print("\nOptions: add_user, change_user, add_song, get_song, update_song, delete_song, display_all_songs, exit")#visual list of prompts
            option = input("Please enter an option: ").strip().lower()

            if option == "add_user":
                username = input("Please enter username: ").strip()
                self.add_user(username)

            elif option == "change_user":
                username = input("Please enter username: ").strip()
                self.change_user(username)

            elif option == "add_song":
                if self.current_user:
                    title = input("Please enter song title: ").strip()
                    artist = input("Please enter artist: ").strip()
                    self.current_user.add_song(title, artist)
                else:
                    print("No user has been selected. Please change or add a new user first.")

            elif option == "get_song":
                if self.current_user:
                    title = input("Please enter song title: ").strip()
                    self.current_user.retrieve_song(title)
                else:
                    print("No user selected. Please change or add a new user first.")

            elif option == "update_song":
                if self.current_user:
                    title = input("Please enter song title: ").strip()
                    new_artist = input("Please enter new artist: ").strip()
                    self.current_user.update_song(title, new_artist)
                else:
                    print("No user selected. Please change or add a new user first.")

            elif option == "delete_song":
                if self.current_user:
                    title = input("Please enter song title: ").strip()
                    self.current_user.delete_song(title)
                else:
                    print("No user selected. Please change or add a new user first.")

            elif option == "display_all_songs":
                if self.current_user:
                    self.current_user.display_all_songs()
                else:
                    print("No user selected. Please change or add a new user first.")

            elif option == "exit":
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    organizer = music_collection_organizer()
    organizer.program()
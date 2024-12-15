import sys
import json
from db.users import create_user, get_user_by_username
from db.usersFollowingList import add_following

def process_user_data(json_data):
    """
    Process the JSON data to insert the main user and their following list into the database.
    """
    try:
        # Step 1: Insert the main user (from ProfileMap)
        profile_map = json_data.get("Profile", {}).get("Profile Information", {}).get("ProfileMap", {})
        if not profile_map:
            print("Error: Could not find 'Profile -> Profile Information -> ProfileMap' in the input JSON.")
            return

        # Extract the required fields for the user
        photo_url = profile_map.get("profilePhoto")
        username = profile_map.get("userName")
        bio = profile_map.get("bioDescription")

        if not username:
            print("Error: 'userName' is required for the main user. Skipping this entry.")
            return

        # Insert into the users table
        create_user(username=username, bio=bio, photo_url=photo_url)
        print(f"User '{username}' successfully inserted into the database.")

        # Retrieve the created user's ID
        created_user = get_user_by_username(username)
        if not created_user:
            print(f"Error: Unable to retrieve the created user '{username}' from the database.")
            return

        created_user_id = created_user["id"]

        # Step 2: Insert following list (from Following array)
        following_list = json_data.get("Activity", {}).get("Following List", {}).get("Following", [])
        if not following_list:
            print(f"Note: No following data found for user '{username}'.")
            return

        # Prepare batch data for insertion
        batch_data = []

        for follower in following_list:
            follower_username = follower.get("UserName")
            followed_date = follower.get("Date")

            if not follower_username:
                print("Error: Skipping entry in following list due to missing 'UserName'.")
                continue

            # Append tuple to batch data
            batch_data.append((created_user_id, follower_username, followed_date))

        if batch_data:
            # Perform batch insert
            add_following_batch(batch_data)
            print(f"Batch added {len(batch_data)} followings for user '{username}'.")
        else:
            print(f"No valid followings to add for user '{username}'.")


    except Exception as e:
        print(f"Error processing user data: {e}")

def main():
    """
    Main function to handle JSON input from stdin and process it.
    """
    print("Please provide the TikTok JSON data (end input with Ctrl+D):")
    try:
        # Read JSON data from standard input
        input_data = sys.stdin.read()
        json_data = json.loads(input_data)

        # Process the data
        process_user_data(json_data)

    except json.JSONDecodeError:
        print("Error: Invalid JSON input.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

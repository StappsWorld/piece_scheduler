from time import sleep
import json
import requests

FAIL_AMT = 10


def get_episode_list(start_page=1):
    delay = 0.25
    page = start_page
    episodes = []
    errors = []
    while True:
        try:
            print(f"[+] Getting page {page}...")
            response = requests.get(
                f"https://api.jikan.moe/v4/anime/21/episodes?page={page}"
            )
            if response.status_code == 200:
                print(f"[+] Successfully got page {page}!")
                episode_lesser_data = response.json()

                # No more episodes
                if "data" in episode_lesser_data and episode_lesser_data["data"] == []:
                    print("[+] No more episodes!")
                    break
                elif "data" not in episode_lesser_data:
                    print("[-] Data list not found in json response! Exitting...")
                    break

                for episode in episode_lesser_data["data"]:
                    trial = 1
                    while trial < FAIL_AMT:
                        print(
                            f"[+] Getting episode {episode['mal_id']}'s data...")
                        episode_data = requests.get(
                            f"https://api.jikan.moe/v4/anime/21/episodes/{episode['mal_id']}")
                        if episode_data.status_code == 200:
                            print(
                                f"[+] Successfully got episode {episode['mal_id']}'s data!")
                            episode_data = episode_data.json()
                            if "data" in episode_data:
                                episodes.append(episode_data["data"])
                                break
                            else:
                                print(
                                    f"[-] Data not found in json response! Trying again... (trial {trial} of {FAIL_AMT})")
                                trial += 1
                                sleep(delay)
                        elif episode_data.status_code == 429:
                            delay += 0.2
                            print(
                                f"[-] 429 error! Sleeping for {delay} seconds...")
                            sleep(delay)
                        else:
                            print(
                                f"[-] Error: Failed to get episode {episode['mal_id']} {episode_data.status_code}. Trying again... (trial {trial} of {FAIL_AMT})")
                            sleep(delay)
                    if trial >= FAIL_AMT:
                        print(
                            f"[-] Failed to get episode {episode['mal_id']}'s data! Adding to errors list.")
                        errors.append(episode["mal_id"])
                    sleep(delay)
            elif response.status_code == 429:
                delay += 0.2
                print(f"[-] 429 error! Sleeping for {delay} seconds...")
            else:
                print(
                    f"[-] Error: Failed to get page {page} {response.status_code}")
            page += 1
            sleep(delay)
        except Exception as e:
            print(f"[-] Error: {e}")
            break
    return episodes, errors


def get_episode_data(episode_id):
    print(f"[+] Getting episode {episode_id}'s data...")
    response = requests.get(
        f"https://api.jikan.moe/v4/anime/21/episodes/{episode_id}")
    if response.status_code == 200:
        print(f"[+] Successfully got episode {episode_id}'s data!")
        return response.json()
    elif response.status_code == 429:
        print("[-] 429 error!")
        return None
    else:
        print(
            f"[-] Error: Failed to get episode {episode_id} {response.status_code}")
        return None


def main():
    print("[+] Getting episode list...")
    episode_list, errors = get_episode_list()
    print(f"[+] Done! There were {len(errors)} errors!")
    if errors:
        print("[+] Errors:")
        for error in errors:
            print(f"    {error}")
    print("[+] Writing to file...")
    with open('data.json', 'w') as f:
        json.dump(episode_list, f)
    print("[+] Done!")

    # failed = [962, 931, 856]
    # episodes = []

    # for episode_id in failed:
    #     episodes.append(get_episode_data(episode_id))
    #     sleep(0.25)

    # with open('data2.json', 'w') as f:
    #     json.dump(episodes, f)


if __name__ == "__main__":
    main()

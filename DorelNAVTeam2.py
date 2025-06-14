from DorelNavOfficial import *

# Define your riddles here. Each riddle has a description, the correct answer,
# a Google Maps link for the next point, and optional images to display.
team_riddles = {
    543: { # Mizpe Modiin -> Random location 2
        "description": "**Location 1:** Solve this riddle to find the first clue in the heart of Ben-Shemen forest...",  # longer description
        "answer": "5",
        "link": "https://www.google.com/maps/place/31%C2%B056'52.4%22N+34%C2%B057'33.0%22E",
        "images": ["dorelNavPhoto/514_1.jpeg", "dorelNavPhoto/514_2.jpeg", "dorelNavPhoto/514_3.jpeg"]  # add up to 3 image URLs or file paths here
    },
    572: { # Random location 2 -> Mahzeba
        "description": "**Location 2:** A second challenge awaits you among the pine trees...",
        "answer": "5",
        "link": "https://www.google.com/maps/place/31%C2%B056'41.1%22N+34%C2%B057'34.7%22E",
        "images": []
    },
    528: { # Mahzeba -> HaPagoda
        "description": "**Location 3:** The third puzzle is hidden near the old grove...",
        "answer": "5",
        "link": "https://www.google.com/maps/place/31%C2%B056'49.0%22N+34%C2%B057'24.6%22E",
        "images": []
    },
    514: { # HaPagoda
        "description": "**Location 4:** Almost there—figure this out to proceed to the clearing...",
        "answer": "5",
        "link": None,
        "images": []
    }
    # ,
    # 560: { # Gathering point
    #     "description": "**Location 5:** Final riddle before the gathering point under the big oak...",
    #     "answer": "5",
    #     "link": None,  # No next link, this is the last one
    #     "images": []
    # }
}

main(team='Team2', alt_riddles=team_riddles)
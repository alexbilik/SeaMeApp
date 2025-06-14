from DorelNavOfficial import *

# Define your riddles here. Each riddle has a description, the correct answer,
# a Google Maps link for the next point, and optional images to display.
team_riddles = {
    543: { # Mizpe Modiin - > HaPagoda
        "description": "**Location 1:** Solve this riddle to find the first clue in the heart of Ben-Shemen forest...",  # longer description
        "answer": "5",
        "link": "https://www.google.com/maps/place/31%C2%B056'49.0%22N+34%C2%B057'24.6%22E",
        "images": ["dorelNavPhoto/514_1.jpeg", "dorelNavPhoto/514_2.jpeg", "dorelNavPhoto/514_3.jpeg"]  # add up to 3 image URLs or file paths here
    },
    514: { # HaPagoda -> Random location 1
        "description": "**Location 2:** A second challenge awaits you among the pine trees...",
        "answer": "5",
        "link": "https://www.google.com/maps/place/31%C2%B056'46.2%22N+34%C2%B057'34.6%22E",
        "images": []
    },
    559: { # Random location 1 -> The partisans
        "description": "**Location 3:** The third puzzle is hidden near the old grove...",
        "answer": "5",
        "link": "https://www.google.com/maps/place/31%C2%B056'48.1%22N+34%C2%B057'20.6%22E",
        "images": []
    },
    531: { # The partisans
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

main(team='Team1', alt_riddles=team_riddles)
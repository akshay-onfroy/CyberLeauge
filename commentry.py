import random

def commentary(event):
    lines = {
        "six": "What a shot! Straight over the boundary.",
        "wicket": "Bowled him! The crowd erupts.",
        "dot": "Defended solidly. No run."
    }
    return lines.get(event, "The match continues...")

if __name__ == "__main__":
    print(commentary("six"))

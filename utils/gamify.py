# utils/gamify.py

from database.db import users_collection

def update_xp(username, xp, quiz_level):

    user = users_collection.find_one({"username": username})
    if not user:
        return None, []

    current_xp = user.get("xp", 0)
    new_xp = current_xp + xp
    level = new_xp // 100
    badges = user.get("badges", [])

    #  Badge logic
    new_badges = []
    if quiz_level == 1 and "Quiz Beginner" not in badges:
        new_badges.append("Quiz Beginner")
    if xp == 150 and "Quiz Master" not in badges:  # scored 10/10
        new_badges.append("Quiz Master")

    users_collection.update_one(
        {"username": username},
        {
            "$set": {"xp": new_xp, "level": level},
            "$addToSet": {"badges": {"$each": new_badges}}
        }
    )

    return level, new_badges

# database/seed_quiz_levels.py
from pymongo import MongoClient

client = MongoClient(" ") # mongdb url
db = client["Agri_db"]
quizzes = db["quizzes"]

quizzes.delete_many({})
print("🧹 Existing quizzes cleared!")

#  insert quiz levels with correct answers
quiz_levels = [
    {
        "title": "Agri Quiz - Level 1",
        "level": 1,
        "questions": [
            {"q": "What is the ideal pH for most crops?", "options": ["4.5", "6.5", "7.0", "8.5"], "answer": "6.5"},
            {"q": "Which fertilizer is rich in nitrogen?", "options": ["DAP", "Urea", "MOP", "Potash"], "answer": "Urea"},
            {"q": "Which crop is known as a cereal?", "options": ["Cotton", "Wheat", "Mustard", "Potato"], "answer": "Wheat"},
            {"q": "Which irrigation method is most efficient?", "options": ["Flood", "Sprinkler", "Drip", "Canal"], "answer": "Drip"},
            {"q": "Best time to sow wheat in India?", "options": ["May", "June", "October", "December"], "answer": "October"},
            {"q": "What is MSP?", "options": ["Minimum Support Price", "Market Supply Price", "Maximum Selling Price", "Monthly Subsidy Plan"], "answer": "Minimum Support Price"},
            {"q": "What is used in organic farming?", "options": ["Urea", "Compost", "Pesticides", "Fungicides"], "answer": "Compost"},
            {"q": "Which is a Rabi crop?", "options": ["Paddy", "Maize", "Wheat", "Jowar"], "answer": "Wheat"},
            {"q": "Main nutrient for leaf growth?", "options": ["Nitrogen", "Potassium", "Phosphorus", "Zinc"], "answer": "Nitrogen"},
            {"q": "Which soil is best for cotton?", "options": ["Black", "Red", "Alluvial", "Sandy"], "answer": "Black"}
        ]
    },
    {
        "title": "Agri Quiz - Level 2",
        "level": 2,
        "questions": [
            {"q": "Which hormone helps in fruit ripening?", "options": ["Auxin", "Gibberellin", "Ethylene", "Cytokinin"], "answer": "Ethylene"},
            {"q": "Which nutrient helps flowering?", "options": ["Nitrogen", "Phosphorus", "Potassium", "Calcium"], "answer": "Potassium"},
            {"q": "Name the pest for cotton?", "options": ["Thrips", "Aphids", "Bollworm", "Whitefly"], "answer": "Bollworm"},
            {"q": "Which gas is used in ripening chamber?", "options": ["CO2", "O2", "Ethylene", "Nitrogen"], "answer": "Ethylene"},
            {"q": "Which vitamin is in carrot?", "options": ["A", "C", "D", "B12"], "answer": "A"},
            {"q": "Function of stomata?", "options": ["Photosynthesis", "Water transport", "Gas exchange", "Food storage"], "answer": "Gas exchange"},
            {"q": "What is intercropping?", "options": ["Single crop", "Same crop rotation", "Two crops at once", "Mono farming"], "answer": "Two crops at once"},
            {"q": "Milch animal example?", "options": ["Goat", "Buffalo", "Ox", "Hen"], "answer": "Buffalo"},
            {"q": "Which is a cash crop?", "options": ["Paddy", "Cotton", "Wheat", "Barley"], "answer": "Cotton"},
            {"q": "Which fruit is citrus?", "options": ["Banana", "Apple", "Orange", "Papaya"], "answer": "Orange"}
        ]
    },
    {
        "title": "Agri Quiz - Level 3",
        "level": 3,
        "questions": [
            {"q": "What is the cause of soil salinity?", "options": ["Fertilizer", "Irrigation", "Rainfall", "Pesticide"], "answer": "Irrigation"},
            {"q": "Which pest affects paddy?", "options": ["Stem borer", "Fruit borer", "Aphid", "Thrips"], "answer": "Stem borer"},
            {"q": "Seed dormancy means?", "options": ["No germination", "Slow growth", "Rapid growth", "Weak root"], "answer": "No germination"},
            {"q": "Which machine sows seeds?", "options": ["Plough", "Seeder", "Tractor", "Harvester"], "answer": "Seeder"},
            {"q": "Crop rotation helps in?", "options": ["Yield", "Pest control", "Fertility", "All"], "answer": "All"},
            {"q": "Which is a pulse crop?", "options": ["Wheat", "Gram", "Rice", "Sugarcane"], "answer": "Gram"},
            {"q": "Function of potassium?", "options": ["Photosynthesis", "Fruit development", "Seed growth", "Leaf color"], "answer": "Fruit development"},
            {"q": "Tea needs what soil?", "options": ["Alkaline", "Saline", "Acidic", "Neutral"], "answer": "Acidic"},
            {"q": "Which animal is used for ploughing?", "options": ["Dog", "Buffalo", "Goat", "Hen"], "answer": "Buffalo"},
            {"q": "Source of green manure?", "options": ["Cow dung", "Urea", "Legumes", "Pesticides"], "answer": "Legumes"}
        ]
    },
    {
        "title": "Agri Quiz - Level 4",
        "level": 4,
        "questions": [
            {"q": "Which mineral helps in chlorophyll?", "options": ["Zinc", "Iron", "Manganese", "Copper"], "answer": "Iron"},
            {"q": "Which crop is known as 'Golden Fibre'?", "options": ["Cotton", "Jute", "Wheat", "Sugarcane"], "answer": "Jute"},
            {"q": "Wheat affected by?", "options": ["Rust", "Blight", "Wilt", "Smut"], "answer": "Rust"},
            {"q": "Which scheme gives soil health cards?", "options": ["PMFBY", "SHC", "MIDH", "PMKSY"], "answer": "SHC"},
            {"q": "What is IPM?", "options": ["Pest system", "Disease model", "Agri model", "Integrated Pest Management"], "answer": "Integrated Pest Management"},
            {"q": "Photosynthesis occurs in?", "options": ["Roots", "Stems", "Leaves", "Flowers"], "answer": "Leaves"},
            {"q": "Citrus is rich in?", "options": ["Iron", "Calcium", "Vitamin C", "Vitamin A"], "answer": "Vitamin C"},
            {"q": "Which crop improves soil nitrogen?", "options": ["Sugarcane", "Maize", "Groundnut", "Paddy"], "answer": "Groundnut"},
            {"q": "Which farming uses cow dung?", "options": ["Chemical", "Organic", "Precision", "Integrated"], "answer": "Organic"},
            {"q": "Main pest in tomato?", "options": ["Borer", "Aphid", "Whitefly", "Nematode"], "answer": "Borer"}
        ]
    },
    {
        "title": "Agri Quiz - Level 5",
        "level": 5,
        "questions": [
            {"q": "Vermicompost is made by?", "options": ["Worms", "Bacteria", "Mushrooms", "Fungi"], "answer": "Worms"},
            {"q": "Sugarcane propagated by?", "options": ["Setts", "Seeds", "Stem", "Cuttings"], "answer": "Setts"},
            {"q": "CACP recommends what?", "options": ["Seeds", "MSP", "Irrigation", "Machines"], "answer": "MSP"},
            {"q": "Which soil is best for pulses?", "options": ["Clay", "Sandy", "Loamy", "Black"], "answer": "Loamy"},
            {"q": "Which fertilizer is potassium-based?", "options": ["Urea", "MOP", "DAP", "Ammonium Sulphate"], "answer": "MOP"},
            {"q": "What is the full form of NPK?", "options": ["Nitrogen-Phosphorus-K", "Nitrate-Phosphite-Kalium", "Nutrient-Potash-Kelp", "None"], "answer": "Nitrogen-Phosphorus-K"},
            {"q": "Which disease affects maize?", "options": ["Rust", "Smut", "Wilt", "Blight"], "answer": "Smut"},
            {"q": "Agriculture census is done every?", "options": ["2 years", "5 years", "10 years", "Annually"], "answer": "5 years"},
            {"q": "Which scheme supports crop insurance?", "options": ["PMFBY", "SHC", "PMGSY", "NFSM"], "answer": "PMFBY"},
            {"q": "Pollination is done by?", "options": ["Birds", "Wind", "Insects", "All"], "answer": "All"}
        ]
    }
]

quizzes.insert_many(quiz_levels)
print(" All 5 quiz levels inserted successfully with correct answers!")

# database/seed_blogs.py

from datetime import datetime
from db import blogs_collection

#blogs_collection.delete_many({})

blogs = [
    {
        "title": "Organic Pest Control",
        "content": """🌿 Organic Pest Control Techniques

Organic pest control is all about protecting your crops using natural, eco-friendly methods — without relying on synthetic chemicals that can harm the soil, water, and ecosystem.

🚫 Why avoid chemical pesticides?
Chemical-based pest control may be effective in the short term, but over time it can:
- Damage soil microbes
- Harm beneficial insects like bees 🐝
- Lead to pesticide-resistant pests
- Affect human and animal health

✅ Best Organic Techniques:

1. Neem Oil Spray:
   Neem oil is a powerful natural pesticide that deters over 200 insect species. Mix 5 ml neem oil with 1 liter of water and spray on affected crops weekly.

2. Garlic & Chili Spray:
   Blend garlic and red chili with water. Strain and spray. This pungent mix repels most soft-bodied insects.

3. Companion Planting:
   Plant marigolds with tomatoes, or basil near peppers. These plants repel insects naturally.

4. Handpicking:
   For larger pests like beetles and caterpillars, manual removal during early morning hours is effective.

5. Beneficial Insects:
   Ladybugs 🐞, lacewings, and praying mantises naturally feed on aphids, mites, and other harmful bugs.

🌾 Conclusion:
Going organic doesn't mean compromising yield. It means smarter, sustainable farming — protecting both your crop and the planet 🌍. Start small, and experiment with combinations that work best for your soil and climate.

Happy Farming! 🌱""",
        "author": "admin",
        "timestamp": datetime(2025, 4, 21, 10, 0),
        "tags": ["organic", "pest"],
        "likes": 0,
        "comments": []
    },
    {
        "title": "Smart Water Usage Techniques",
        "content": """💧 Smart Water Usage Techniques in Agriculture

Efficient water use is one of the pillars of sustainable farming. With growing water scarcity and unpredictable rainfall patterns, farmers need to adopt techniques that maximize yield while conserving every drop.

🌍 Why it matters:
- Agriculture uses over 70% of freshwater globally.
- Over-irrigation leads to soil salinity, waterlogging, and wastage.
- Smart irrigation improves plant health and reduces cost.

✅ Best Techniques:

1. Drip Irrigation:
   Water is delivered directly to the plant root zone, minimizing evaporation. It's ideal for vegetables, fruits, and row crops.

2. Sprinkler Systems:
   Useful for fields with uneven topography. Sprinklers distribute water evenly and reduce runoff.

3. Mulching:
   Organic mulch (like straw or dried leaves) covers the soil, preventing evaporation and maintaining soil moisture for longer.

4. Irrigation Scheduling:
   Water early in the morning or late evening to reduce evaporation loss. Avoid watering during windy afternoons.

5. Rainwater Harvesting:
   Collect and store rainwater during monsoons for off-season irrigation. You can use small farm ponds, tanks, or roof-based catchment systems.

6. Moisture Sensors:
   Soil moisture sensors help determine when to irrigate, avoiding over-watering and under-watering.

💡 Pro Tip:
Group crops with similar water requirements together — it reduces water waste and makes irrigation easier.

💧 Final Thought:
Water is precious. Managing it wisely isn't just smart farming — it’s future-proof farming 🌱💦
""",
        "author": "admin",
        "timestamp": datetime(2025, 4, 19, 8, 30),
        "tags": ["water", "irrigation"],
        "likes": 0,
        "comments": []
    },
    {
        "title": "Choosing the Right Fertilizer",
        "content": """🌾 Choosing the Right Fertilizer for Healthy Crops

Fertilizers play a crucial role in modern agriculture by replenishing soil nutrients and enhancing crop growth. However, choosing the wrong type or applying the wrong quantity can damage plants, soil, and the environment.

🧪 Types of Fertilizers:

1. Organic Fertilizers:
   - Examples: Compost, manure, bone meal, vermicompost
   - Benefits: Improve soil structure, increase microbial activity, and release nutrients slowly
   - Ideal For: Sustainable and long-term soil health

2.  Inorganic (Chemical) Fertilizers:
   - Examples: Urea, DAP (Diammonium Phosphate), MOP (Muriate of Potash)
   - Benefits: Immediate nutrient availability, precise control
   - Ideal For: Quick corrections of nutrient deficiencies

📊 Understanding the NPK Ratio:

- N = Nitrogen (Leaf growth)
- P = Phosphorus (Root & flower development)
- K = Potassium (Overall health & disease resistance)

🧠 Example:  
A fertilizer labeled 20-10-10 has:
- 20% Nitrogen  
- 10% Phosphorus  
- 10% Potassium  

📍 Choosing Based on Crop:
- Leafy vegetables (e.g. spinach, lettuce): High Nitrogen
- Root crops (e.g. carrot, beetroot): More Phosphorus
- Fruiting crops (e.g. tomato, brinjal): Balanced NPK

💡 Pro Tips:
- Always do a soil test before applying fertilizer.
- Apply during cooler hours (morning/evening).
- Avoid over-fertilization — it can burn crops 🌿

 Sustainable Tip:
Combine organic and inorganic fertilizers (Integrated Nutrient Management) to get the best of both worlds.

Healthy soil = Healthy crops = Healthy humans 🌱
""",
        "author": "admin",
        "timestamp": datetime(2025, 4, 17, 14, 45),
        "tags": ["fertilizer", "soil"],
        "likes": 0,
        "comments": []
    },
    {
        "title": "Sustainable Farming Practices",
        "content": """🌱 Sustainable Farming Practices for Long-Term Agricultural Success

Sustainable farming focuses on producing food in a way that preserves natural resources, supports biodiversity, and maintains soil fertility — ensuring that future generations can farm the same land.

🌍 Why Go Sustainable?
- Reduces environmental impact
- Increases long-term productivity
- Improves soil and water quality
- Builds resilience against climate change

✅ Core Sustainable Techniques:

1. Crop Rotation:
   Changing crop types every season improves soil structure and disrupts pest life cycles. For example, follow rice with legumes to naturally fix nitrogen.

2. Cover Cropping:
   Planting crops like clover or mustard during off-seasons prevents soil erosion, adds organic matter, and suppresses weeds.

3. Integrated Pest Management (IPM):
   Combines natural predators, crop monitoring, and minimal pesticide use to manage pests without harming the ecosystem.

4. Reduced/No Tillage:
   Tilling less or not at all helps retain soil moisture, improves carbon sequestration, and reduces erosion.

5. Agroforestry:
   Integrating trees with crops or livestock systems improves biodiversity, provides shade, and protects soil from wind/water erosion.

6. Organic Composting:
   Recycling crop residues, animal dung, and kitchen waste into compost enriches the soil naturally — reducing dependence on synthetic fertilizers.

💧 Water Conservation:
- Drip irrigation
- Rainwater harvesting
- Mulching to prevent evaporation

🐝 Bonus Tip:
Encourage biodiversity — plant native flowers around your farm to attract pollinators like bees, which boost crop yields.

📈 Final Thought:
Sustainable farming is not just a trend — it's a necessity. By nurturing the soil and working in harmony with nature, farmers can secure both their livelihood and the planet’s future 🌎

Grow smart. Grow green 🌾🌿
""",
        "author": "admin",
        "timestamp": datetime(2025, 4, 15, 12, 0),
        "tags": ["sustainable", "farming"],
        "likes": 0,
        "comments": []
    }
]

blogs_collection.insert_many(blogs)

print(" Blog data seeded successfully.")


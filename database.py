products = [
    {
        "name": "BudgetBook 14",
        "category": "Laptop",
        "features": ["8GB RAM", "256GB SSD", "14-inch Display", "Lightweight", "Student Friendly"],
        "price": 450
    },
    {
        "name": "ZoomMate Pro",
        "category": "Camera",
        "features": ["Good Zoom", "Image Stabilization", "Compact"],
        "price": 295
    },
    {
        "name": "Speedster X",
        "category": "Laptop",
        "features": ["16GB RAM", "512GB SSD", "Gaming Ready"],
        "price": 850
    },
    {
        "name": "LightSnap 200",
        "category": "Camera",
        "features": ["Basic Zoom", "HD Video"],
        "price": 200
    },
     {
        "name": "StudyMate 13",
        "category": "Laptop",
        "features": ["8GB RAM", "128GB SSD", "Lightweight", "Student Friendly"],
        "price": 399
    },
    {
        "name": "ProZoom 400X",
        "category": "Camera",
        "features": ["Optical Zoom", "Image Stabilization", "HD Recording"],
        "price": 320
    },
    {
        "name": "WorkLite Flex",
        "category": "Laptop",
        "features": ["16GB RAM", "512GB SSD", "Backlit Keyboard", "Lightweight"],
        "price": 780
    },
    {
        "name": "ClickSnap Mini",
        "category": "Camera",
        "features": ["Compact Design", "4K Recording", "Beginner Friendly"],
        "price": 280
    },
    {
        "name": "UltraView Pro",
        "category": "Camera",
        "features": ["Zoom Lens", "Tripod Mount", "Wireless Transfer"],
        "price": 450
    },
    {
        "name": "EduBook X1",
        "category": "Laptop",
        "features": ["8GB RAM", "256GB SSD", "Touchscreen", "Long Battery Life"],
        "price": 499
    },
    {
        "name": "CamTech Vibe",
        "category": "Camera",
        "features": ["AI Scene Detection", "Stabilizer", "USB-C Charging"],
        "price": 390
    },
    {
        "name": "ThinkLite 15",
        "category": "Laptop",
        "features": ["12GB RAM", "256GB SSD", "Full HD Display", "Slim Body"],
        "price": 620
    },
    {
        "name": "SnapJet 5",
        "category": "Camera",
        "features": ["Zoom", "Night Mode", "Bluetooth Sharing"],
        "price": 310
    },
    {
        "name": "CodeMate Air",
        "category": "Laptop",
        "features": ["8GB RAM", "Fanless Design", "Silent Keyboard", "Student Friendly"],
        "price": 450
    }
]


def search_products(query: str) -> str:
    import re

    budget = 9999
    category = ""
    features = []

    budget_match = re.search(r'under \$?(\d+)', query.lower())
    if budget_match:
        budget = int(budget_match.group(1))

    if "laptop" in query.lower():
        category = "Laptop"
    elif "camera" in query.lower():
        category = "Camera"

    if "8gb" in query.lower():
        features.append("8GB RAM")
    if "zoom" in query.lower():
        features.append("Zoom")
    if "student" in query.lower():
        features.append("Student Friendly")
    if "stabilization" in query.lower():
        features.append("Image Stabilization")

    matches = []
    for product in products:
        if category and product['category'] != category:
            continue
        if product['price'] > budget:
            continue
        if not all(any(f.lower() in feature.lower() for feature in product['features']) for f in features):
            continue
        matches.append(product)

    if not matches:
        return "No matching products found."

    return "\n".join([f"{p['name']} - ${p['price']} - Features: {', '.join(p['features'])}" for p in matches])

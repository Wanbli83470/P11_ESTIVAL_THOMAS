"""constantes connection"""

HOST='127.0.0.1'
USER='root'
PASSWORD='azerty'
DB='P11'
PORT = 3306

CATEGORIES = "`CATEGORIES`"
PRODUITS = "`PRODUITS`"
SUBSTITUTS = "`SUBSTITUTS`"

TABLES = [SUBSTITUTS, PRODUITS, CATEGORIES]

PRODUCTS = {"Boisson" :["Coca Cola", "Ice tea", "Fanta", "Orangina"], 
			"Gâteaux/Sucrerie":["Kinder Pingouin", "Oréo", "Nutella", "Petit Prince", "Cookie"], 
			"Apérétifs":["Chips", "Cacahuètes", "Crackers", "Kiri"], 
			"Dessert":["Lait nestlé", "Fondant Chocolat", 'Flamby'], 
			"Poisson":["Batonnet de surémi", "poisson pané"]}

CATEGORIES_TO_ENGLISH = {"Boisson":"carbonated-drinks", "Gâteaux/Sucrerie": "sweet-snacks", "Apérétifs":"salty-snacks", "Dessert" : "desserts", "Poisson" : "seafood"}
meals_data = [
    {
    'name': "Mediterranean Chicken Bowls with Whole-Wheat Couscous",
    'description': "This colorful and flavorful bowl combines protein-rich chicken, complex carbs from couscous, fiber-rich vegetables, and heart-healthy fats from olives and avocado."
    },
    {
        'name': "Salmon with Roasted Sweet Potato and Broccoli",
        'description': "This omega-3-packed salmon dish with fiber-rich vegetables and vitamin-rich sweet potato provides a well-balanced and nutritious meal",
    },
    {
        'name': "Lentil Soup with Whole-Wheat Bread",
        'description': "This hearty soup is loaded with protein and fiber from lentils, making it a filling and satisfying choice. Whole-wheat bread provides additional complex carbs and dietary fiber. ",
    },
    {
        'name': "Vegetarian Chili with Kidney Beans and Quinoa",
        'description': "This plant-based chili is packed with protein and fiber from kidney beans and quinoa, while vegetables like tomatoes, peppers, and onions add vitamins and antioxidants. ",
    },
    {
        'name': "Baked Cod with Lemon and Herbs",
        'description': "This simple and healthy dish features flaky cod coated in a light and flavorful lemon herb sauce. Served with roasted vegetables for added vitamins and fiber.",
    },
    {
        'name': "Turkey Meatloaf with Mashed Sweet Potatoes",
        'description': "This lean and flavorful meatloaf is made with ground turkey and topped with a sweet and healthy mashed sweet potato topping. A complete and satisfying meal. ",
    },
    {
        'name': "Chicken Stir-Fry with Brown Rice and Broccoli",
        'description': "This classic stir-fry combines lean protein, complex carbs, and fiber-rich broccoli for a healthy and balanced meal. Easy to customize with different vegetables.",
    },
    {
        'name': "Greek Yogurt Parfait with Berries and Granola",
        'description': "This layered parfait is a healthy and delicious breakfast or snack option. Greek yogurt provides protein and probiotics, berries are rich in antioxidants, and granola adds fiber and texture. ",
    },
    {
        'name': "Whole-Wheat Toast with Avocado and Egg",
        'description': "This simple and nutritious breakfast or snack option provides protein from the egg, healthy fats from the avocado, and complex carbs from the whole-wheat toast. ",
    },
    {
        'name': "Tuna Salad Lettuce Wraps",
        'description': "A lighter take on tuna salad, served in lettuce wraps for a low-carb option. Packed with protein and healthy fats from tuna, and fiber from the lettuce. ",
    },
    {
        'name': "Black Bean Burgers on Whole-Wheat Buns",
        'description': "This plant-based burger satisfies cravings while providing protein and fiber from black beans. Whole-wheat buns add complex carbs and dietary fiber",
    },
    {
        'name': "Roasted Butternut Squash with Quinoa and Cranberries",
        'description': "This vibrant and flavorful dish features roasted butternut squash, protein-rich quinoa, and tart cranberries for a satisfying and nutritious meal. ",
    },
    {
        'name': "Chicken Curry with Chickpeas and Naan",
        'description': "This flavorful and filling curry is packed with protein from chicken and chickpeas, while vegetables add vitamins and fiber. Serve with warm naan for a complete meal. ",
    },
    {
        'name': "Quinoa Tabouli with Fresh Herbs and Cucumber",
        'description': "This light and refreshing salad combines protein-rich quinoa with fresh herbs, cucumber, and tomatoes for a healthy and flavorful lunch or side dish. ",
    },
    {
        'name': "Turkey Burger with Avocado, Sprouts, and Chipotle Mayo",
        'description': "This flavorful burger combines lean turkey, creamy avocado, crunchy sprouts, and a smoky chipotle mayo for a satisfying and healthy meal. ",
    },
    {
        'name': "Shrimp and Vegetable Spring Rolls with Sweet and Sour Dipping Sauce",
        'description': "These delicate spring rolls are packed with flavorful shrimp and fresh vegetables, making them a healthy and delicious appetizer or light meal. ",
    },    {
        'name': "Cream of Tomato Soup with Whole-Wheat Grilled Cheese",
        'description': "This classic comfort food can be made healthy with homemade tomato soup and whole-wheat grilled cheese. A satisfying and nutritious meal. ",
    },
    {
        'name': "Baked Tofu with Roasted Brussels Sprouts and Tahini Sauce",
        'description': "This plant-based dish features protein-rich tofu, fiber-rich Brussels sprouts, and a creamy tahini sauce for a flavorful and satisfying meal.",
    },
    {
        'name': "Poached Salmon with Lemon Dill Sauce and Quinoa Pilaf",
        'description': "This light and delicate dish features omega-3 rich salmon cooked in a fragrant lemon dill sauce, served over a flavorful quinoa pilaf for a complete and protein-packed meal. (Suitable for heart health, digestive health, and diabetes management) ",
    },
    {
        'name': "Roasted Chicken Breast with Sweet Potato Mash and Green Beans",
        'description': "This classic combination provides lean protein from chicken, complex carbs and vitamin A from sweet potatoes, and fiber and essential vitamins from green beans. (Supports muscle health, blood sugar control, and bone health)",
    },
    {
        'name': "Lentil and Vegetable Stew with Whole-Wheat Roll",
        'description': "This hearty and flavorful stew is rich in protein and fiber from lentils, vitamins and antioxidants from vegetables, and complex carbs from whole-wheat bread. (Promotes gut health, heart health, and weight management) ",
    },
    {
        'name': "Turkey Chili with Kidney Beans and Brown Rice",
        'description': "A protein-packed chili using lean ground turkey and kidney beans, with additional fiber and nutrients from brown rice and vegetables. (Ideal for managing cholesterol, blood pressure, and weight) ",
    },
    {
        'name': "Baked Cod with Herbs and Crushed Tomatoes",
        'description': "This simple and nutritious dish features flaky cod seasoned with fresh herbs and topped with a light tomato sauce, making it a great low-calorie option. (Supports immune function, bone health, and cognitive function) ",
    },
    {
        'name': "Tofu Scramble with Spinach and Turmeric",
        'description': "This plant-based scramble provides protein and iron from tofu, antioxidants and vitamins from spinach, and anti-inflammatory benefits from turmeric. (Suitable for vegetarian and vegan diets, gluten-free)",
    },
    {
        'name': "Chicken Stir-Fry with Broccoli and Brown Rice Noodles",
        'description': "Lean protein from chicken combines with fiber-rich broccoli and complex carbs from brown rice noodles for a balanced and satisfying stir-fry. (Promotes muscle building, gut health, and blood sugar control)",
    },    {
        'name': "Greek Yogurt Parfait with Berries and Chia Seeds",
        'description': "This nutrient-rich parfait combines protein and probiotics from Greek yogurt, antioxidants from berries, and omega-3s and fiber from chia seeds. (Supports bone health, immune function, and digestion)",
    },
    {
        'name': "Whole-Wheat Toast with Nut Butter and Sliced Fruits",
        'description': "A simple and healthy breakfast or snack option providing protein and healthy fats from nut butter, vitamins and fiber from fruits, and complex carbs from whole-wheat toast. (Good for heart health, weight management, and energy levels)",
    },

]
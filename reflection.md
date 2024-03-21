# Reflection

## Inheritance Simplified
In our game, we have a "family" of characters. Think of `Character` as the parent in the family. It has basic information like a name and health. Now, from this parent, we create two "children" in our game family: `Hero` and `Enemy`. These children inherit (or get) the traits of their parent, like having a name and health, but they also add their own special touches. For example, our `Hero` can carry a weapon, showing how kids can have both shared traits from their parents and their unique features.

## Association Simplified
In our game, our characters (like our `Hero` and `Enemy`) can hold weapons. This is like saying, "Hey, you can use this item, but it doesn't mean it's a part of you." This relationship is like a friendship; our characters "know" a weapon and can use it, but if the weapon goes away, our characters are still there. It shows how our game characters and their weapons are connected but still live their lives independently.

## Encapsulation Simplified
Imagine our game characters have their personal diaries (their internal states and information), and they don't want anyone just flipping through them. Instead, if someone wants to know something or change something, they have to ask the character directly. For example, if we want our `Hero` to pick up a weapon, we don't just glue the weapon to their hand. Instead, we tell the `Hero`, "Please, pick up this weapon." This way, the `Hero` controls what happens to them, keeping their diary safe while still letting the outside world interact with them in a controlled way.


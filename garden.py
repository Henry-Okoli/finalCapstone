import spacy

# Load the SpaCy English model
nlp = spacy.load('en_core_web_sm')

# List of sentences
sentences = [
    "The man saw the mountain climbers using binoculars.", 
    "The old man the boats to the harbor.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never her hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition for each sentence
for sentence in sentences:
    doc = nlp(sentence)
    
    # Print the categorized entities in the sentence
    for entity in doc.ents:
        print(entity.text, entity.label_)

    tokens = [token.text for token in doc]

    # Perform named entity recognition
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    print("Tokens:", tokens)
    
    print("Entities:", entities)

    # Print the explanation of entities that you don't understand
    unclassified_entities = set([ent.label_ for ent in doc.ents if ent.label_ not in spacy.explain(ent.label_)])
    for label in unclassified_entities:
        print(spacy.explain(label))

    print()

# Explanation for each entity:

# "The man" - PERSON: Represents a person.
# "mountain climbers" - PERSON: Represents a person.
# "binoculars" - PRODUCT: Represents a product.
# "The old man" - PERSON: Represents a person.
# "the boats" - PRODUCT: Represents a product.
# "the harbor" - LOCATION: Represents a location.
# "Mary" - PERSON: Represents a person.
# "the child" - PERSON: Represents a person.
# "Band-Aid" - PRODUCT: Represents a product.
# "That Jill" - PERSON: Represents a person.
# "her hurts" - PERSON: Represents a person.
# "The cotton clothing" - PRODUCT: Represents a product.
# "Mississippi" - GPE: Represents a geopolitical entity (in this case, a state in the United States)

# Based on the code provided, the entities are identified based on their labels, 
# such as PERSON, PRODUCT, LOCATION, and GPE. The labels themselves are predefined 
# categories that represent different types of entities. These labels are associated
# with specific patterns and characteristics that help the named entity recognition 
# system classify the entities.
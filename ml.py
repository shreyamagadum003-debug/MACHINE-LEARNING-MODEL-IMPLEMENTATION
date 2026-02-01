print("Program started")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# Dataset (1 = Spam, 0 = Not Spam)
# -------------------------------
emails = [
    "Win money now",
    "Limited time offer",
    "Claim your free prize",
    "Congratulations you won",
    "Free entry win cash",
    "Hey are we meeting today",
    "Let's have lunch tomorrow",
    "Can you send me the notes",
    "See you in class",
    "How are you doing today"
]

labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# -------------------------------
# Convert text data to numbers
# -------------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# -------------------------------
# Split dataset
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=42
)

# -------------------------------
# Train the model
# -------------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

print("Model training completed")

# -------------------------------
# Evaluate model
# -------------------------------
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# -------------------------------
# Predict new email
# -------------------------------
new_email = ["You have won a free lottery"]
new_email_vector = vectorizer.transform(new_email)

prediction = model.predict(new_email_vector)

print("\nNew Email:", new_email[0])
if prediction[0] == 1:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")
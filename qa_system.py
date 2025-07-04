from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_loader import extract_question_and_answer

class MedicalQASystem:
     def __init__(self, qa_list):
        self.qa_list = [item for item in qa_list if item["question"].strip() != ""]
        self.questions = [item["question"] for item in self.qa_list]
        self.answers = [item["answer"] for item in self.qa_list]

        # Check if we have any valid questions
        if not self.questions:
            raise ValueError("No valid questions found. Please check your dataset.")

        # Vectorize questions using TF-IDF
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

     def fetch_relevant_answer(self, user_query, top_n=1):
        query_vec = self.vectorizer.transform([user_query])
        similarity = cosine_similarity(query_vec, self.question_vectors)
        top_match_index = similarity[0].argsort()[::-1][:top_n]

        # Return top matching answer(s)
        result = []
        for idx in top_match_index:
            result.append({
                "matched_question": self.questions[idx],
                "answer": self.answers[idx],
                "score": similarity[0][idx]
            })
        return result

# Test script
if __name__ == "__main__":
    folder_path = r"C:/Users/rosaa/Downloads/MedQuAD-master/MedQuAD-master/"
    qa_data = extract_question_and_answer(folder_path)

    qa_bot = MedicalQASystem(qa_data)

    while True:
        user_input = input("\nAsk a medical question (or type 'exit'): ")
        if user_input.lower() == 'exit':
            break
        matched_results = qa_bot.fetch_relevant_answer(user_input)
        if matched_results:
            print("\n🔍 Closest Question:", matched_results[0]['matched_question'])
            print("💬 Answer:", matched_results[0]['answer'])
        else:
            print("No matching answer found.")

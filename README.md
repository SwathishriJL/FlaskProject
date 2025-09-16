In today’s world, we’re surrounded by a vast pool of financial products and services – from loans and insurance plans to investment opportunities and health benefits. With so many options available, it becomes extremely difficult for users to find the right product at the right time.

That’s where our problem statement comes in. Our goal was to design a Gen-AI based solution that can not only generate personalized recommendations for users but also provide actionable insights for businesses to improve customer engagement.

Our approach to personalization is built on a simple but powerful mantra:

Data + Interactions = Recommendations + Actionable Insights.

We developed a Gen-AI powered system that analyzes user data, interactions, and preferences to provide contextually relevant recommendations. Unlike traditional approaches that suggest products randomly, our system uses OpenAI’s reasoning capabilities to deliver personalized choices while also addressing a key challenge in financial services — explainability. For every recommendation, the system clearly explains why it was suggested, ensuring transparency, building user trust, and solving the long-standing issue of explainability in AI-driven personalization.

Finally, the scope of our project extends to multiple dimensions – analyzing user profiles, relationships, social activity, health records, fitness, income, and existing financial products. By integrating all these aspects, our personalization engine ensures that customers receive smarter, more relevant, and explainable recommendations.”

	1.	Introduction:
“This slide represents the dataset we designed for our system. To make the recommendations realistic, we needed to simulate both the financial products and the user profiles.”
	2.	Financial Products:
“On the left, we have financial products across different categories — from deposit accounts, credit and loan products, investment and wealth management, to insurance protection plans and different types of cards. Each of these product categories was populated with synthetic details so that the model has a wide spectrum to recommend from.”
	3.	User Profile:
“On the right, we built a rich user profile dataset. This goes beyond just basic user details like name, DOB, or occupation. We also added relationships, social activity, income and spending patterns, as well as medical and fitness data. The idea was to create a 360-degree profile of the user so recommendations are not only financial but also contextual — for example, linking spending behavior, lifestyle, and health with financial product suitability.”
	4.	Note on Vector Embeddings:
“As shown at the bottom, everything is ultimately converted into vector embeddings so the Gen-AI system can compute similarities and provide relevant recommendations.”

2.	Recommendations for You:
“The first engine is personalized financial recommendations for the user. It looks at spending habits, transactions, and overall financial profile to suggest the most suitable products for investment, credit, or savings.”
	3.	For the People You Love:
“The second engine focuses on relationship-based recommendations. Using connections like spouse, parents, or children, it generates curated suggestions tailored for your family, built on advanced graph-based models.”
	4.	Healthcare Services:
“The third engine expands into healthcare and insurance. It recommends the best healthcare services and financial plans based on a user’s medical and wellness data, supporting informed health and insurance decisions.”
	5.	Conversational Search Engine (Chatbot):
“Finally, all of these come together in our chatbot interface. Instead of browsing manually, a user can simply ask questions in natural language — and the system instantly provides smart, contextual recommendations in a conversational way.”

For personalized recommendations, the first step is to fetch the embedding vector of the user from our database
We then use MongoDB Atlas Vector Search to find the top 5 most similar users. By analyzing the financial products those users own, we can identify the most relevant offerings for our target user.
Finally, an LLM generates explanations, so the recommendation is not just shown but also justified in natural language.”

For family oriented recommendations,
We build a relationship graph, extract the products owned by these related users, and convert them into embeddings. Then, using cosine similarity, we rank the most relevant financial products for each family member.

We determine the user segment using the rule based mapping. Based on the segmentation, we apply conditional logic to filter out the right set of services

Rule 1 – Age-based mapping:
If the user is above 60, the system recommends a Senior Citizen Health Insurance Plan.

Rule 2 – Spending and transaction behavior:
If a user has frequent hospital payments or sudden high medical expenses, we recommend an Emergency Medical Loan to help them manage short-term liquidity

•	Rule 3 – Lifestyle and fitness data:
If the system sees the user logging daily steps and wellness activity from wearables, we recommend Wellness Programs such as discounted gym memberships or preventive health checkups.

Finally, Conversation chat engine - the interface that ties everything together 
Here, any input from the user first goes through intent detection using an LLM. Based on the intent, the system decides whether to fetch product recommendations, healthcare services, or family-related suggestions in a conversation way along with reason

1. Data Generation and Preparation

“We started by organizing our data across different dimensions.
	•	User Data: This includes user profiles (demographics and bank interactions), user health profiles, and user embeddings. For embeddings, we picked key fields, concatenated them, and used sentence transformers to generate contextual embeddings.
	•	Service Plans: These cover both financial services (like loans, insurance, refinancing) and healthcare services. We also created embeddings for these using vector stores.

Since real user data can’t always be used, we needed synthetic data. 


“To generate synthetic data, we used two approaches:
	1.	Faker Library – This was used to generate user data such as names, demographics, health-related fields, and banking interactions. Faker allowed us to create a realistic but completely synthetic set of users without exposing any real personal information.
	2.	LLM Models – For the financial services and products, we needed rich textual descriptions and details. Here, we used LLMs in a few-shot style. We gave the model a handful of well-structured examples of product descriptions, and then it generated diverse and natural-sounding descriptions for other products. This ensured our dataset was both realistic and scalable.”

“On the home page, we implemented multiple recommendation modules:
	•	Recommended for You: This is based on user-based collaborative filtering. Traditional filtering uses TF encodings like one-hot vectors, but that fails to capture context. We improved it by using embeddings from sentence transformers, which capture deeper relationships. That way, we can recommend products that actually align with user intent.
	•	For the People You Love: Here, we leveraged relationships from graph-based modeling. For example, if there’s an education loan for children, it makes sense to recommend it to the parents. This builds personalization based on family or social context.
	•	Health Services: Based on the health profile, we used a rule-based engine to recommend relevant healthcare benefits.”

⸻

3. Conversational Search Engine

“We also built a conversational search engine.

The pipeline is:
	•	Identify the intent of the query,
	•	Route it to the right logic,
	•	Fetch relevant data from user and catalog,
	•	And finally use an LLM to reason and respond.

The best part is: for every recommendation, we also generate the reason behind it. This addresses explainability – which is a big challenge in AI-driven banking.”

⸻

4. Slave Server for Campaigns

“Alongside real-time recommendations, we added a slave server for background processing of campaign data.

When campaigns are run (say on social media), we capture interaction data. The slave server processes this into linguistic constructs – short summaries of user needs and preferences. These constructs are embedded and searched against our database to generate personalized recommendations.

This boosts outbound sales and helps in customer outreach beyond WellsPro’s ecosystem.”

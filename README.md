

🌱 Eco Page: Empowering Sustainability through Technology 🌍

I am thrilled to introduce "Eco Page," a collaborative web application developed by our dedicated team to promote environmental sustainability and community engagement. 🌿

Project Highlights:

🌎 Environmental Impact: Eco Page encourages responsible waste disposal by allowing users to submit their waste items and earn credits for every kilogram recycled. It's a small step toward a greener planet.

💡 Technology Stack: Leveraging Flask, HTML, CSS, Bootstrap, JavaScript, and MySQL, Eco Page offers a seamless and user-friendly experience.

♻️ Credit System: Users are rewarded with credits for their eco-conscious efforts. This gamification element not only motivates users but also raises awareness about waste reduction.

📊 Database Management: MySQL ensures efficient data storage and retrieval, enabling us to keep track of waste submissions and user credits.

🌐 Web Development: The project showcases our collective skills in front-end (HTML, CSS, Bootstrap, and JavaScript) and back-end (Flask and MySQL) development.


🙌 Contributors: A special shout-out to my dedicated team of contributors:

S. Ashok Kumar Reddy
PRANAV CHIMPANNA
Aashrith Sriramadas
Pravar Pera

📢 Community Engagement: By fostering a sense of responsibility and reward, Eco Page brings people together for a common cause: protecting our environment.

We're passionate about using technology to make a positive impact, and Eco Page is a testament to our collective commitment. I invite you to explore the project and share your thoughts. Let's work together to create a more sustainable future! 🌟


Thank you for joining us on this eco-friendly journey! 🌎🌿

#EcoPage #Sustainability #WebDevelopment #EnvironmentalAwareness #TechForGood




Database structure:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE wastesubmit1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    location VARCHAR(255),
    bnb VARCHAR(255),
    type VARCHAR(255),
    amount FLOAT,
    coins INT DEFAULT 0,
    FOREIGN KEY (username) REFERENCES users(username)
);


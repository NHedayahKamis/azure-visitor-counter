# azure-visitor-counter

A full-stack serverless application that tracks and displays website visitor counts using a cloud-native architecture. This project demonstrates the integration of Python Flask, NoSQL databases, and automated CI/CD pipelines.

Tech Stack:
-Frontend/Backend: Python (Flask)
-Database: Azure Cosmos DB (NoSQL)
-Hosting: Azure App Service
-CI/CD: GitHub Actions

Architecture:
1. Code: A Python Flask app handles web requests and database logic.
2. Deployment: GitHub Actions automatically builds and deploys the code to Azure upon every push to the main branch.
3. Data: Azure Cosmos DB stores visitor count as a JSON document, ensuring persistance and scalability.

Key Learning and Challenges:
This project provided hands-on experience with real-world cloud deployment hurdles:
-Automated Pipeline: Configure GitHub Actions to sync local code with cloud resources.
-Security and Identity: Managed authentication via Azure Environment Variables and secured database access using Primary Keys.
-Debugging: Troubleshoot 403 Forbidden errors and session timeout within the Azure Portal by analyzing Log Stream.


 

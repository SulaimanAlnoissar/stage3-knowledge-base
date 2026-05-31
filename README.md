# Stage 3 - Knowledge Base

This project contains a small and focused Knowledge Base for the M2 Smart Bot.

## Project Idea

The goal of this stage is to collect and organize useful club information so the chatbot can use it later in a RAG pipeline.

The Knowledge Base includes confirmed information about GDG KSU, its committees, activities, educational snippets, and frequently asked questions.

## Why the Knowledge Base is Small

The available sources are limited, so the Knowledge Base was designed to be focused and reliable.

Instead of adding large amounts of unverified information, the content only includes useful and confirmed information from available club materials and social media posts.

## Files

- `knowledge_base_plan.md`: Explains the plan and structure of the Knowledge Base.
- `club_info.md`: Contains general information about GDG KSU.
- `committees.md`: Contains information about the club committees.
- `activities.md`: Contains information about visits, workshops, sessions, and initiatives.
- `knowledge_snippets.md`: Contains short educational technical snippets from social media content.
- `faq.md`: Contains frequently asked questions and answers.
- `metadata.json`: Describes each document using metadata such as title, category, source, tags, and description.

## How This Supports RAG

When a user asks a question, the chatbot can search the Knowledge Base, retrieve the most relevant document or section, and send it with the user question to Gemini.

This helps the chatbot generate answers based on organized club information instead of relying only on general AI knowledge.

## Concepts Covered

- Knowledge Base organization
- Markdown documents
- Metadata
- RAG support
- Information cleaning and structuring
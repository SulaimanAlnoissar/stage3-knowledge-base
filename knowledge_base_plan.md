# Stage 3 - Knowledge Base Plan

## Purpose

The purpose of this stage is to design a small and focused Knowledge Base for the M2 Smart Bot. Since the available sources are limited, the Knowledge Base will only include confirmed and useful information instead of adding large amounts of general or unverified content.

This helps keep the chatbot answers more accurate and reduces the chance of giving wrong or unsupported information.

## Knowledge Base Scope

The Knowledge Base will focus on the most important information needed by the chatbot, including:

- General information about GDSC KSU
- Basic information about the Technical Committee
- Information about the M2 Smart Bot project
- Frequently asked questions related to the club and the chatbot

## File Structure

The Knowledge Base will be organized into a small number of clear files:

- `club_info.md`: General information about the club.
- `m2_smart_bot.md`: Information about the chatbot project.
- `faq.md`: Common questions and answers.
- `metadata.json`: Metadata that describes each document.

This structure keeps the Knowledge Base simple, readable, and easy to update.

## Metadata

Each document will have metadata to describe its purpose and make it easier to retrieve during the RAG process.

The metadata will include:

- title
- category
- source
- tags
- file_name
- last_updated

## How It Supports RAG

When the user asks a question, the chatbot can search the Knowledge Base and retrieve the most relevant file or section. Then the retrieved information is added to the prompt and sent to Gemini.

This allows Gemini to generate answers based on the available club information instead of depending only on general knowledge.

## Final Goal

The final goal is to build a clean and reliable mini Knowledge Base that can support the M2 Smart Bot in answering student questions using organized and trusted information.
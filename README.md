# Agentic Orchestration Systems Comparison

Welcome to the **Agentic Orchestration Systems Comparison** repository! This repository is designed to help you compare and understand different agentic orchestration systems such as **LangGraph**, **Llama Workflows**, and **OpenAI Swarm**. Whether you're new to these frameworks or looking for a deeper comparison, this repo provides insights and examples to get you started quickly.

## Overview

Agentic orchestration systems allow for the coordination and management of intelligent agents, enabling them to collaborate and perform complex tasks autonomously. As AI systems become more advanced, choosing the right orchestration framework can significantly impact how efficiently and effectively tasks are executed. This repository compares the following three popular orchestration systems:

1. **LangGraph**: A graph-based framework for building complex AI systems where agents are connected through graph structures.
2. **Llama Workflows**: A workflow-driven orchestration system that focuses on chaining AI agent tasks into cohesive workflows.
3. **OpenAI Swarm**: TODO

## Goals of the Comparison

The purpose of this repository is to provide:

- **Detailed comparisons** of the architecture, features, and use cases of LangGraph, Llama Workflows, and OpenAI Swarm.
- **Benchmarks** on performance, scalability, and flexibility.
- A **hands-on guide** with simple example projects to implement in any of these frameworks.

By the end of this comparison, you’ll have a solid understanding of which framework best fits your project needs..

## Why Compare These Frameworks?

These frameworks all tackle the challenge of orchestrating intelligent agents but have different approaches in how they do it. Understanding their differences will help you:

- **Select the right orchestration system** for your needs, whether you’re focused on simple workflows, complex decision trees, or distributed task management.
- **Optimize your development process** by choosing a framework that integrates well with your tools and goals.
- **Enhance agent collaboration** by understanding how these systems manage and coordinate multiple AI agents.

# Test Project: Automated Travel Planning Assistant

### Task:
The system will help plan a weekend trip by:
- Selecting a **destination** based on user preferences (e.g., nature, city) and weather conditions.
- Booking **transportation** options (e.g., flight, train, bus, car rental) within the user’s budget.
- Finding **accommodation** (hotel, Airbnb, etc.) near the destination that fits the budget and location preferences.
- Recommending **activities** to do during the trip, tailored to the user’s interests.

### Agents Involved:
1. **Destination Selector Agent**: Chooses the destination based on distance, weather, and user preferences.
2. **Transportation Agent**: Finds the best transportation option within the user’s budget.
3. **Accommodation Finder Agent**: Suggests accommodations near the destination based on price and proximity to attractions.
4. **Activity Planner Agent**: Generates an itinerary of activities (e.g., tours, local attractions) that align with user interests.

### Tools Used:
- **Weather API**: To check weather conditions for potential destinations.
- **Price Comparison API**: For comparing prices of transportation and accommodation options.

### Example Workflow:
1. The user specifies their preferences (e.g., nature getaway within a $600 budget).
2. The **Destination Selector Agent** suggests a location with good weather and fits the budget.
3. The **Transportation Agent** finds the most convenient and affordable travel option.
4. The **Accommodation Finder Agent** recommends a hotel or Airbnb close to attractions.
5. The **Activity Planner Agent** creates a list of activities based on the user’s interests (e.g., hiking, city tours).

This project demonstrates how multiple agents can collaborate to simplify a real-world task like travel planning, making decisions based on user inputs and external data.

### APIs used

To help our agents by finding hotel and flight deals we need APIs that can help us provide this information.

For this example I used API endpoints from [amadeus for developers](https://developers.amadeus.com/).
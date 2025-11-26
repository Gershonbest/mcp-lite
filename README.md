# ArxivExplorer MCP Server

A lightweight Model Context Protocol (MCP) server that enables AI assistants to search and explore ArXiv research papers using Tavily search.

## Description

ArxivExplorer is an MCP server built with FastMCP that provides tools and resources for discovering academic papers on ArXiv. It uses Tavily's search API to query ArXiv and returns paper titles and URLs, making it easy for AI assistants to help users find relevant research papers.

## Features

- **Search ArXiv**: Query ArXiv for recent papers on any topic
- **Suggested Topics Resource**: Provides curated AI research topics for exploration
- **Topic Exploration Prompt**: Helper prompt template for exploring research topics systematically

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set up your Tavily API key in a `.env` file:
   ```
   TAVILY_API_KEY=your_api_key_here
   ```

3. Run the server:
   ```bash
   python main.py
   ```

## Usage

The server exposes:
- **Tool**: `search_arxiv(query, max_results=5)` - Search ArXiv for papers matching a query
- **Resource**: `resource://ai/arxiv_topics` - List of suggested AI research topics
- **Prompt**: `explore_topic_prompt(topic)` - Template for exploring a research topic


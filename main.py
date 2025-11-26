import os
from typing import Dict, List
from fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv


load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


tavily = TavilyClient(api_key=TAVILY_API_KEY)
mcp = FastMCP(name="ArxivExplorer")

@mcp.resource("resource://ai/arxiv_topics")
def arxiv_topics() -> List[str]:    
    return ["Transformer interpretability", "Efficient large-scale model training","Federated learning privacy", "Neural network pruning"]

@mcp.tool(annotations={"title": "Search Arxiv"})
def search_arxiv(query: str, max_results: int = 5) -> List[Dict]:    

    """Queries ArXiv via Tavily, returning title + link for each paper, and *only* ArXiv results."""    
    resp = tavily.search(query=f"site:arxiv.org {query}",max_results=max_results)
    return [{"title": r["title"].strip(), "url": r["url"]} for r in resp.get("results", [])]


@mcp.prompt
def explore_topic_prompt(topic: str) -> str:
    return (
        f"I want to explore recent work on '{topic}'.\n"
        f"1. Call the 'Search Arxiv' tool to find the 5 most recent papers.\n"
        f"2. For each paper URL, call 'Summarize Paper' to extract its key contributions.\n"
        f"3. Combine all summaries into an overview report."
    )

if __name__ == "__main__":
    print("\n🚀 Starting ArxivExplorer Server...")
    mcp.run(transport="http")

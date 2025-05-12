"""
Disney Jokes MCP Server

A simple Model Context Protocol server that returns jokes related to Disney animation movies.
"""
import random
from typing import Optional, Dict, List, Any
import sys
from mcp.server.fastmcp import FastMCP

# Create MCP server with enhanced configuration
mcp = FastMCP(
    name="Disney-Jokes-Generator",
    description="An MCP server that provides jokes about Disney animation movies and characters",
    version="1.0.0",
    dependencies=["mcp>=1.8.0"]
)

# Disney jokes database
# Format: {character/movie: [list of jokes]}
DISNEY_JOKES = {
    "mickey": [
        "Why did Mickey Mouse go to outer space? To find Pluto!",
        "What's Mickey Mouse's favorite type of car? A Minnie-van!",
        "How does Mickey Mouse feel when Minnie is angry? Mouserable!",
        "What did Mickey say to Minnie when she asked if her outfit looked good? 'You look Minnie-malistic!'"
    ],
    "frozen": [
        "What's Elsa's favorite place to shop? The Frozen food section!",
        "What did Olaf say during summer? 'I'm a puddle of emotion!'",
        "Why didn't Elsa have a balloon? Because she always 'Let It Go!'",
        "Why was Elsa banned from the swimming pool? She kept freezing the water!"
    ],
    "lion_king": [
        "What's Simba's favorite type of car? A Roaring Royce!",
        "Why couldn't the lion eat the clown? Because he tasted funny!",
        "What do you call Simba when he's standing in a circle? The Lion Ring!",
        "How does Mufasa like his steak? Rare with a little son on the side!"
    ],
    "toy_story": [
        "Why was Woody worried when Andy started playing chess? He was afraid of being a pawn!",
        "What did Buzz Lightyear say to his investment banker? 'To infinity and a bond!'",
        "How do the toys from Toy Story stay cool? With a Buzz-ing fan!",
        "Why did Mr. Potato Head get a job at the bank? He wanted to keep his eyes on the cash!"
    ],
    "aladdin": [
        "What did Aladdin say when discounts were introduced at the marketplace? 'A whole new sale!'",
        "Why does Genie make a terrible comedian? Because his jokes are always rubbing people the wrong way!",
        "What's Jasmine's favorite music? Arabian raps!",
        "How many wishes did it take for Aladdin to get rich? Just one, the rest was carpet overhead!"
    ],
    "moana": [
        "Why doesn't Moana use a GPS? She knows the way!",
        "What's Maui's favorite type of cookie? Shape shifters!",
        "What did the ocean say to Moana? Nothing, it just waved!",
        "Why did Heihei cross the ocean? Because someone put a boat under him!"
    ],
    "mulan": [
        "What did Mushu say when Mulan asked if her disguise was working? 'You're dragon it off!'",
        "How did Mulan cut her food? With Shan-Yu!",
        "Why was Mulan such a good student? She always got down to business!",
        "What's Mulan's favorite game? Dress-up!"
    ],
    "finding_nemo": [
        "What did the fish say when he swam into a wall? 'Dam!'",
        "Why are fish so smart? Because they live in schools!",
        "What did Dory say when she was lost? 'Have you seen my son? He's orange with a white stripe. Wait, who are you?'",
        "What's Nemo's favorite subject in school? Current events!"
    ]
}

# General Disney jokes
GENERAL_DISNEY_JOKES = [
    "Why don't Disney characters use dating apps? They always want their Happily Ever After right away!",
    "What do you call a Disney princess who can't carry a tune? Tone-deaf-erella!",
    "Why are Disney movies so unrealistic? No one has parents!",
    "How do Disney characters shop online? With one-click and a wish!",
    "What do you call a Disney villain's autobiography? 'My Side of the Story'",
    "Why did the Disney animator go to the doctor? Because they couldn't stop drawing conclusions!",
    "What's a Disney princess's favorite exercise? The royal-thigh workout!",
    "How many Disney princesses does it take to change a lightbulb? None, they just sing and animals do it for them!"
]

@mcp.tool(
    description="Get a joke related to Disney animation movies and characters"
)
def get_disney_joke(character: Optional[str] = None, movie: Optional[str] = None) -> str:
    """Get a joke related to Disney animation movies.
    
    This tool returns jokes about Disney characters and movies. You can request jokes
    about specific characters like Mickey, Elsa, Simba, or specific movies like Frozen,
    Lion King, or Toy Story. If no parameters are provided, a random Disney joke will be returned.
    
    Args:
        character: The Disney character to get a joke about (e.g., "mickey", "elsa")
        movie: The Disney movie to get a joke about (e.g., "frozen", "lion_king")
        
    Returns:
        A joke related to the specified Disney character or movie, or a random Disney joke if no parameters provided.
    """
    # Convert parameters to lowercase for case-insensitive matching
    if character:
        character = character.lower().replace(" ", "_")
    if movie:
        movie = movie.lower().replace(" ", "_")
    
    # Search for jokes based on character
    if character and character in DISNEY_JOKES:
        return random.choice(DISNEY_JOKES[character])
    
    # Search for jokes based on movie
    if movie and movie in DISNEY_JOKES:
        return random.choice(DISNEY_JOKES[movie])
    
    # Try to find a close match if exact match not found
    if character or movie:
        search_term = character or movie
        for key in DISNEY_JOKES.keys():
            if search_term in key or key in search_term:
                return random.choice(DISNEY_JOKES[key])
    
    # Return a general Disney joke if no match found or no parameters provided
    return random.choice(GENERAL_DISNEY_JOKES)

@mcp.tool(
    description="Get a list of all available Disney joke categories"
)
def list_available_joke_categories() -> Dict[str, List[str]]:
    """Get a list of available Disney joke categories.
    
    This tool returns a dictionary containing all the available characters and movies
    that can be used with the get_disney_joke tool. Use this to discover what joke categories
    are available.
    
    Returns:
        Dictionary with available characters and movies for jokes.
    """
    return {
        "characters_and_movies": list(DISNEY_JOKES.keys())
    }

if __name__ == "__main__":
    print("Starting Disney Jokes MCP Server...")
    print("Server provides jokes about Disney animation movies and characters")
    print("Use with an MCP client like Claude Desktop")
    print("-" * 50)
    
    # Run the MCP server with stdio transport for easy integration with MCP clients
    mcp.run(transport="stdio")

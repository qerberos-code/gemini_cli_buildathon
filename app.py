#!/usr/bin/env python3
"""
Gemini CLI Buildathon Demo Script

This script demonstrates a Local File Wrangler pattern:
- Parse local files (PDFs/markdown)
- Extract key facts using Gemini
- Produce structured JSON summaries
- Save intermediate and final outputs for debugging
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

import google.generativeai as genai
from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler

# Load environment variables
load_dotenv()

# Initialize rich console for beautiful output
console = Console()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)]
)
logger = logging.getLogger("gemini-demo")


class GeminiFileWrangler:
    """Local File Wrangler using Gemini for document processing."""
    
    def __init__(self):
        """Initialize the Gemini client."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Set up directories
        self.data_dir = Path("data")
        self.demo_dir = Path("demo")
        self.demo_dir.mkdir(exist_ok=True)
        
        logger.info("✅ Gemini File Wrangler initialized")
    
    def read_file(self, file_path: Path) -> str:
        """Read file content based on file type."""
        if file_path.suffix.lower() == '.md':
            return file_path.read_text(encoding='utf-8')
        elif file_path.suffix.lower() == '.txt':
            return file_path.read_text(encoding='utf-8')
        else:
            # For other file types, read as text
            return file_path.read_text(encoding='utf-8', errors='ignore')
    
    def extract_key_facts(self, content: str, file_name: str) -> Dict[str, Any]:
        """Extract key facts from document content using Gemini."""
        
        prompt = f"""
        Analyze the following document and extract key facts in a structured format.
        
        Document: {file_name}
        Content:
        {content}
        
        Please provide a JSON response with the following structure:
        {{
            "summary": "Brief 2-3 sentence summary of the document",
            "key_facts": [
                "Fact 1",
                "Fact 2",
                "Fact 3"
            ],
            "topics": ["topic1", "topic2", "topic3"],
            "entities": {{
                "people": ["person1", "person2"],
                "organizations": ["org1", "org2"],
                "locations": ["location1", "location2"]
            }},
            "sentiment": "positive/negative/neutral",
            "provenance": {{
                "source_file": "{file_name}",
                "processed_at": "{datetime.now().isoformat()}",
                "model_used": "gemini-1.5-flash"
            }}
        }}
        
        Be concise but comprehensive. Focus on the most important information.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Try to parse as JSON, fallback to text if needed
            try:
                result = json.loads(response.text)
            except json.JSONDecodeError:
                # If JSON parsing fails, create a structured response
                result = {
                    "summary": response.text[:200] + "..." if len(response.text) > 200 else response.text,
                    "key_facts": ["Unable to parse structured response"],
                    "topics": ["unknown"],
                    "entities": {"people": [], "organizations": [], "locations": []},
                    "sentiment": "neutral",
                    "provenance": {
                        "source_file": file_name,
                        "processed_at": datetime.now().isoformat(),
                        "model_used": "gemini-1.5-flash",
                        "raw_response": response.text
                    }
                }
            
            return result
            
        except Exception as e:
            logger.error(f"Error processing {file_name}: {e}")
            return {
                "summary": f"Error processing file: {str(e)}",
                "key_facts": [],
                "topics": [],
                "entities": {"people": [], "organizations": [], "locations": []},
                "sentiment": "neutral",
                "provenance": {
                    "source_file": file_name,
                    "processed_at": datetime.now().isoformat(),
                    "model_used": "gemini-1.5-flash",
                    "error": str(e)
                }
            }
    
    def process_files(self) -> List[Dict[str, Any]]:
        """Process all files in the data directory."""
        results = []
        
        # Find all supported files
        supported_extensions = ['.md', '.txt', '.json']
        files = []
        for ext in supported_extensions:
            files.extend(self.data_dir.glob(f"*{ext}"))
        
        if not files:
            logger.warning("No files found in data directory")
            return results
        
        logger.info(f"Found {len(files)} files to process")
        
        for file_path in files:
            logger.info(f"Processing: {file_path.name}")
            
            # Read file content
            content = self.read_file(file_path)
            
            # Extract key facts
            facts = self.extract_key_facts(content, file_path.name)
            
            # Add file info
            facts["file_info"] = {
                "path": str(file_path),
                "size_bytes": file_path.stat().st_size,
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            }
            
            results.append(facts)
            
            # Save individual result
            output_file = self.demo_dir / f"{file_path.stem}_analysis.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(facts, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Saved analysis to {output_file}")
        
        return results
    
    def generate_summary_report(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate a comprehensive summary report."""
        
        # Collect all key facts
        all_facts = []
        all_topics = []
        all_entities = {"people": [], "organizations": [], "locations": []}
        
        for result in results:
            all_facts.extend(result.get("key_facts", []))
            all_topics.extend(result.get("topics", []))
            
            entities = result.get("entities", {})
            for key in all_entities:
                all_entities[key].extend(entities.get(key, []))
        
        # Create summary report
        summary_report = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "total_files_processed": len(results),
                "total_facts_extracted": len(all_facts),
                "unique_topics": list(set(all_topics)),
                "model_used": "gemini-1.5-flash"
            },
            "consolidated_facts": all_facts[:20],  # Top 20 facts
            "consolidated_entities": {
                key: list(set(values))[:10]  # Top 10 unique entities per category
                for key, values in all_entities.items()
            },
            "file_summaries": [
                {
                    "file": result["provenance"]["source_file"],
                    "summary": result["summary"],
                    "fact_count": len(result.get("key_facts", [])),
                    "topics": result.get("topics", [])
                }
                for result in results
            ]
        }
        
        return summary_report


def run_demo():
    """Run the complete demo workflow."""
    console.print("\n🚀 [bold blue]Gemini CLI Buildathon Demo[/bold blue]")
    console.print("=" * 50)
    
    try:
        # Initialize the wrangler
        wrangler = GeminiFileWrangler()
        
        # Process files
        console.print("\n📁 [bold]Processing files...[/bold]")
        results = wrangler.process_files()
        
        if not results:
            console.print("❌ No files processed. Please add files to the /data directory.")
            return
        
        # Generate summary report
        console.print("\n📊 [bold]Generating summary report...[/bold]")
        summary_report = wrangler.generate_summary_report(results)
        
        # Save summary report
        summary_file = wrangler.demo_dir / "summary_report.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_report, f, indent=2, ensure_ascii=False)
        
        # Display results
        console.print(f"\n✅ [bold green]Demo completed successfully![/bold green]")
        console.print(f"📄 Processed {len(results)} files")
        console.print(f"📊 Generated {len(results)} individual analyses")
        console.print(f"📋 Created summary report: {summary_file}")
        
        # Show sample results
        console.print("\n🔍 [bold]Sample Results:[/bold]")
        for i, result in enumerate(results[:2]):  # Show first 2 results
            console.print(f"\n[bold cyan]File {i+1}:[/bold cyan] {result['provenance']['source_file']}")
            console.print(f"[bold]Summary:[/bold] {result['summary']}")
            console.print(f"[bold]Key Facts:[/bold] {len(result.get('key_facts', []))} facts extracted")
            console.print(f"[bold]Topics:[/bold] {', '.join(result.get('topics', [])[:3])}")
        
        console.print(f"\n📁 [bold]Output files saved to:[/bold] {wrangler.demo_dir}")
        
    except Exception as e:
        console.print(f"\n❌ [bold red]Demo failed:[/bold red] {e}")
        logger.exception("Demo execution failed")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        run_demo()
    else:
        console.print("Usage: python app.py demo")
        console.print("\nThis script demonstrates the Gemini CLI integration.")
        console.print("Make sure to:")
        console.print("1. Set GEMINI_API_KEY in your .env file")
        console.print("2. Add sample files to the /data directory")
        console.print("3. Run: python app.py demo")

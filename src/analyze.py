#!/usr/bin/env python3
"""
X12 EDI Mapping Analyzer
Analyzes uploaded X12 files, maps, and schemas
"""

import argparse
import json
import os
from pathlib import Path
from datetime import datetime


class X12Analyzer:
    """Analyzes X12 EDI files and maps"""
    
    def __init__(self, input_dir, output_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def analyze(self):
        """Run analysis on uploaded files"""
        results = {
            "timestamp": datetime.now().isoformat(),
            "files_processed": 0,
            "analysis_results": []
        }
        
        # Look for uploaded files
        if not self.input_dir.exists():
            print(f"Input directory {self.input_dir} does not exist")
            return results
        
        # Process EDI files
        for edi_file in self.input_dir.glob("*.edi"):
            result = self._analyze_edi_file(edi_file)
            results["analysis_results"].append(result)
            results["files_processed"] += 1
        
        # Process map files
        for map_file in self.input_dir.glob("*.map"):
            result = self._analyze_map_file(map_file)
            results["analysis_results"].append(result)
            results["files_processed"] += 1
        
        # Process XML maps
        for xml_file in self.input_dir.glob("*.xml"):
            result = self._analyze_xml_file(xml_file)
            results["analysis_results"].append(result)
            results["files_processed"] += 1
        
        # Save results
        self._save_results(results)
        return results
    
    def _analyze_edi_file(self, file_path):
        """Analyze an EDI file"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Basic EDI parsing
            segments = content.split('\n')
            standard = self._detect_standard(segments)
            
            return {
                "file": file_path.name,
                "type": "EDI",
                "standard": standard,
                "segment_count": len([s for s in segments if s.strip()]),
                "status": "analyzed"
            }
        except Exception as e:
            return {
                "file": file_path.name,
                "type": "EDI",
                "error": str(e),
                "status": "failed"
            }
    
    def _analyze_map_file(self, file_path):
        """Analyze a Seeburger map file"""
        return {
            "file": file_path.name,
            "type": "Map",
            "format": "binary",
            "status": "detected"
        }
    
    def _analyze_xml_file(self, file_path):
        """Analyze an XML map file"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            is_map = "map" in content.lower() or "mapping" in content.lower()
            
            return {
                "file": file_path.name,
                "type": "XML Map" if is_map else "XML",
                "size_bytes": file_path.stat().st_size,
                "status": "analyzed"
            }
        except Exception as e:
            return {
                "file": file_path.name,
                "type": "XML",
                "error": str(e),
                "status": "failed"
            }
    
    def _detect_standard(self, segments):
        """Detect X12 standard from segments"""
        for segment in segments:
            if segment.startswith("ST*"):
                parts = segment.split("*")
                if len(parts) >= 2:
                    return f"X12-{parts[1]}"
        return "Unknown"
    
    def _save_results(self, results):
        """Save analysis results to file"""
        output_file = self.output_dir / "analysis_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"✅ Results saved to {output_file}")
        print(f"   Files processed: {results['files_processed']}")


def main():
    parser = argparse.ArgumentParser(description="X12 EDI Mapping Analyzer")
    parser.add_argument("--input-dir", default="uploads", help="Input directory with uploaded files")
    parser.add_argument("--output-dir", default="results", help="Output directory for results")
    
    args = parser.parse_args()
    
    analyzer = X12Analyzer(args.input_dir, args.output_dir)
    results = analyzer.analyze()
    
    if results["files_processed"] == 0:
        print("⚠️  No files found to process")
    else:
        print(f"✅ Analysis complete: {results['files_processed']} files processed")


if __name__ == "__main__":
    main()

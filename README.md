PDF Compression Tool User Guide ====================

Function Description --------
This tool can compress PDF files to a specified size (default 5MB), automatically optimizing the file size.  
It supports compressing multiple PDF files at once and running silently in the background. 
Install dependencies --------
1. Open Command Prompt (CMD) or Terminal  
2. Navigate to the current directory: cd pdf-compression  
3. Install dependencies: pip install -r requirements.txt 
Usage Instructions --------
Method 1: Command line (supports multiple files)  
python pdf_compressor.py <PDF file 1> <PDF file 2> ... 
Example: python pdf_compressor.py document1.pdf document2.pdf report.pdf

Method 2: Drag-and-Drop (Recommended, no CMD window)  
Drag one or more PDF files directly onto the compress.vbs file. 
Output file --------
The compressed file will be saved in the same directory as the original file, with the filename format: original_filename_compressed.pdf 
Example: document.pdf -> document_compressed.pdf

Precautions
--------
1. Ensure that the Python environment is installed  
2. Dependencies need to be installed for first-time use  
3. Compression quality will automatically adjust based on target size  
4. If the original file is already smaller than 5MB, it will be saved directly  
5. The CMD window will not appear when running via VBS script drag-and-drop  
6. A pop-up notification will appear after compression completes 
File List --------
- pdf_compressor.py    - Main program file  
- compress.vbs         - Background running script (drag-and-drop usage)  
- requirements.txt     - Dependency configuration file  
- Usage_instructions.txt - This documentation

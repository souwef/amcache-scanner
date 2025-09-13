# Cheat CSV Scanner

A Python tool for scanning CSV files for a set of SHA1 hashes and returning corresponding file paths. !! Specifically made for Eric Zimmerman's amcacheparser !!

## Features
- Fast CSV parsing and scanning
- Colored output using [rich](https://github.com/Textualize/rich)
- Easy to add new cheats by updating the `SHA1_CHEATS` dictionary in `main.py`

## Usage
1. Install dependencies:
   ```bash
   pip install rich
   ```
2. Add your SHA1:CheatName pairs to the `SHA1_CHEATS` dictionary in `main.py`.
3. Run the tool:
   ```bash
   python main.py <your_csv_file.csv>
   ```
4. View detected cheats and their file paths in the terminal.

## Example
```
python main.py sample.csv
```

## Output
- Detected cheats are shown in a colorized table with SHA1 (cyan), cheat name (green), and file path (yellow).
- If no cheats are found, a green message is displayed.

import csv
from typing import Dict, List, Tuple
from rich.console import Console
from rich.table import Table

SHA1_CHEATS = {
    "bbdf0e0176017b6d950d262671b874b50cce3b37": "Tuke1.1.1",
    "3689b44d42583008d5d158968bf7e81c3c0ccf3c": "Krypton Client",
    "986a82f96ae5d3a5ef13f077d04696ccd532bca3": "Koid v1.3",
    "369673654fc3b2883af6246433547b924458a5af": "Itami Ghost V6",
    "d7e5d3c3bbcf42d9ea40ccd3214cf85d25de77cb": "Itami Ghost V5",
    "8c69b2322c23c68d325689542378c394531a6cd2": "Itami Ghost V4",
    "05e0ca45f7d7260f607a8aa6045a5e31ba4f2c35": "Itami Ghost V3",
    "cb05534ee976606e61ecc255a0e31c7b809b80b4": "Itami Ghost V2",
    "b03680bbd404ea604227715c1ec3135d7c691560": "Itami Ghost V1",
    "fac81f6c1f1bd668b66f2d1d84c6fe2a4e6b0c98": "IceTea Client",
    "362aa869faa961e8192567035eb54e187f625726": "Sylph Clicker",
    "c04b108edbb95b75dc1496bed342b937f37fa17a": "Slinky",
    "4857f30e4aec8071a97716db38b6b2e374578e5f": "Chione Clicker"

    # Add more cheats in the same format
}

console = Console()

def parse_csv_and_find_cheats(csv_path: str, sha1_cheats: Dict[str, str] = SHA1_CHEATS) -> List[Tuple[str, str, str]]:
    results = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = {col.strip(): col for col in reader.fieldnames}
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)
        sha1_col = columns.get('SHA1')
        path_col = columns.get('Full Path') or columns.get('FullPath')
        if not path_col:
            for key in columns:
                if 'full' in key.lower() and 'path' in key.lower():
                    path_col = columns[key]
                    break
        for row in reader:
            sha1 = row.get(sha1_col, '').strip() if sha1_col else ''
            full_path = row.get(path_col, '').strip() if path_col else ''
            if sha1 in sha1_cheats:
                cheat_name = sha1_cheats[sha1]
                results.append((sha1, cheat_name, full_path if full_path else '(No path found)'))
    return results

def print_cheat_report(results: List[Tuple[str, str, str]]):
    if not results:
        console.print("[bold green]No cheats detected.[/bold green]")
        return
    table = Table(title="", show_lines=True)
    table.add_column("SHA1", style="cyan", no_wrap=True)
    table.add_column("Cheat Name", style="green")
    table.add_column("Path", style="yellow")
    for sha1, cheat_name, full_path in results:
        table.add_row(sha1, cheat_name, full_path)
    console.print(table)
    console.print(f"[bold red]{len(results)} cheat(s) detected.[/bold red]")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        console.print("[bold yellow]Usage:[/bold yellow] python main.py <csv_file_path>")
        sys.exit(1)
    csv_file = sys.argv[1]
    found_cheats = parse_csv_and_find_cheats(csv_file)
    print_cheat_report(found_cheats)

import tkinter as tk
from tkinter import ttk
import csv
import requests
from bs4 import BeautifulSoup

def scrape_ranking_data():
    url = "https://www.transfermarkt.com/premier-league/tabelle/wettbewerb/GB1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'items'})
    ranking_data = []

    for row in table.tbody.find_all('tr'):
        rank = row.find('td', {'class': 'rechts'}).text.strip()
        team = row.find('td', {'class': 'no-border-links'}).text.strip()
        points = row.find_all('td', {'class': 'zentriert'})[-1].text.strip()
        ranking_data.append([rank, team, points])

    return ranking_data

def create_table(parent, data):
    table = ttk.Treeview(parent, columns=('Rank', 'Team', 'Points'), show='headings')
    table.heading('Rank', text='Rank')
    table.heading('Team', text='Team')
    table.heading('Points', text='Points')

    for row in data:
        table.insert('', 'end', values=row)

    return table

def main():
    ranking_data = scrape_ranking_data()

    root = tk.Tk()
    root.title('Premier League Ranking')

    table = create_table(root, ranking_data)
    table.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()

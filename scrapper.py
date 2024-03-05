import requests
from bs4 import BeautifulSoup


URL = "https://fbref.com/en/comps/8/stats/Champions-League-Stats"

def scrape_stats():
    response = requests.get(URL)
    
    # Check if the response was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        
        # Finding table with the stats
        # results = soup.find(id="div_stats_standard")
        resultados = soup.find(id='all_stats_standard')
        
        
        if resultados:
            print(resultados.prettify())
        else:
            print("Error: Element with id 'stats_standard' not found.")
    else:
        print("Error: Response not successful")
        
        
    
    
    

    
    

scrape_stats()
    